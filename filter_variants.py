#!/usr/bin/env python3
"""
filter_variants.py
------------------
Reproducible variant-filtering pipeline for the WES analysis described in README.md.

Applies a stepwise filter to an ANNOVAR-annotated variant table and writes:
  - filtered_candidate_variants.csv : variants surviving all filters
  - filtering_summary.csv           : variant/gene counts remaining at each step

Filtering steps
---------------
  1. Quality                : VCF FILTER == "PASS"
  2. ClinVar (CLINSIG)      : Pathogenic / Likely pathogenic / Uncertain significance /
                              Other / Not provided   (i.e. benign calls removed)
  3. InterVar (ACMG)        : Pathogenic / Likely pathogenic / Uncertain significance
  4. Location               : Func.refGene == "exonic"
  5. Consequence            : ExonicFunc.refGene in {nonsynonymous SNV, stopgain, stoploss}
  6. Population frequency   : ExAC_ALL < 0.001 (variants absent from ExAC are retained)

Usage
-----
    python filter_variants.py --input annotated.xlsx  --outdir ../data
    python filter_variants.py --input part1.xlsx part2.xlsx --outdir ../data
    python filter_variants.py --input annotated.tsv --sep '\t' --outdir ../data

Notes
-----
* Accepts .xlsx, .csv or .tsv input. Multiple files (e.g. a large table split for
  file-size reasons) can be passed and will be concatenated and de-duplicated.
* Numeric parsing is locale-independent: values such as "0/0005" (produced when a
  spreadsheet is saved under a locale that uses a non-standard decimal separator)
  are normalised before conversion. This prevents rows being silently dropped.
* Raw sequencing data and per-sample genotypes are NOT written to the output;
  only de-identified variant-level annotation is exported.

Author: Zahra Gholami
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

# --------------------------------------------------------------------------- #
# Configuration
# --------------------------------------------------------------------------- #

CLINSIG_KEEP = {
    ".", "Uncertain significance", "not provided", "Other", "other",
}

INTERVAR_KEEP = {
    "Pathogenic", "Likely pathogenic", "Uncertain significance",
}

EXONICFUNC_KEEP = {
    "nonsynonymous SNV", "stopgain", "stoploss",
}

MAX_AF = 0.001

# Columns exported (per-sample genotype / INFO fields are deliberately excluded)
EXPORT_COLS = [
    "Chr", "Start", "End", "Ref", "Alt",
    "Func.refGene", "Gene.refGene", "ExonicFunc.refGene",
    "ExAC_ALL", "CLINSIG", "InterVar", "QUAL", "DP", "rsID", "FILTER",
]


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def to_float(value):
    """Locale-tolerant float conversion.

    Returns None for '.', empty values, or anything unparseable.
    Handles '0/0005'-style values produced by some spreadsheet locales.
    """
    if value is None:
        return None
    text = str(value).strip()
    if text in {"", ".", "NA", "nan", "None"}:
        return None
    text = text.replace("/", ".").replace(",", ".")
    try:
        return float(text)
    except ValueError:
        return None


def load_table(path: Path, sep: str | None) -> pd.DataFrame:
    """Read one annotated variant table (.xlsx, .csv or .tsv)."""
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    if sep is None:
        sep = "\t" if path.suffix.lower() in {".tsv", ".txt"} else ","
    return pd.read_csv(path, sep=sep, low_memory=False)


def require_columns(df: pd.DataFrame) -> None:
    """Fail loudly if the expected annotation columns are missing."""
    required = [
        "Chr", "Start", "End", "Ref", "Alt",
        "Func.refGene", "Gene.refGene", "ExonicFunc.refGene",
        "ExAC_ALL", "CLINSIG",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        sys.exit(
            "ERROR: input is missing required column(s): "
            + ", ".join(missing)
            + "\nFound columns: "
            + ", ".join(map(str, df.columns[:40]))
        )


def normalise_intervar(df: pd.DataFrame) -> pd.DataFrame:
    """Accept either 'InterVar' or 'InterVar(automated)' as the column name."""
    if "InterVar" in df.columns:
        return df
    for candidate in df.columns:
        if str(candidate).lower().startswith("intervar"):
            return df.rename(columns={candidate: "InterVar"})
    sys.exit("ERROR: no InterVar column found in the input table.")


def recover_vcf_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Recover VCF fields that ANNOVAR packs into trailing 'Otherinfo' columns.

    ANNOVAR appends the original VCF record after the annotation columns. When the
    table is exported to a spreadsheet these arrive as 'Unnamed: N' columns, so
    FILTER/QUAL/DP are present in the data but unusable by name. Without this
    recovery the quality filter silently passes every row.

    The trailing block is identified by locating the column holding the VCF FILTER
    values (PASS / LowQual / caller-specific filter names).
    """
    if "FILTER" in df.columns:
        return df

    unnamed = [c for c in df.columns if str(c).startswith("Unnamed:")]
    if not unnamed:
        print("NOTE: no FILTER column found; quality filtering will be skipped.")
        return df

    filter_col = None
    for col in unnamed:
        values = df[col].astype(str)
        if values.eq("PASS").mean() > 0.05:  # column dominated by VCF FILTER values
            filter_col = col
            break

    if filter_col is None:
        print("NOTE: no FILTER column found; quality filtering will be skipped.")
        return df

    renamed = {filter_col: "FILTER"}

    # Fields at fixed offsets relative to FILTER in a standard VCF record:
    #   ... ID  REF  ALT  QUAL  FILTER  INFO  FORMAT  SAMPLE
    cols = list(df.columns)
    idx = cols.index(filter_col)
    offsets = {-4: "rsID", -1: "QUAL_vcf", 1: "INFO", 2: "FORMAT", 3: "SAMPLE"}
    for offset, name in offsets.items():
        pos = idx + offset
        if 0 <= pos < len(cols) and str(cols[pos]).startswith("Unnamed:"):
            renamed[cols[pos]] = name

    print(f"Recovered VCF fields from unnamed columns: {', '.join(renamed.values())}")
    return df.rename(columns=renamed)


# --------------------------------------------------------------------------- #
# Pipeline
# --------------------------------------------------------------------------- #

def run_pipeline(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Apply the six filtering steps; return (filtered_variants, summary)."""
    df = df.copy()
    df["_af"] = df["ExAC_ALL"].apply(to_float)

    summary = []

    def record(label: str, frame: pd.DataFrame) -> None:
        summary.append(
            {
                "Filtering step": label,
                "Variants remaining": len(frame),
                "Unique genes": frame["Gene.refGene"].nunique(),
            }
        )

    record("0. Raw annotated positions (deduplicated)", df)

    # Step 1 - quality
    if "FILTER" in df.columns:
        df = df[df["FILTER"] == "PASS"]
    record("1. Quality filter (FILTER = PASS)", df)

    # Step 2 - ClinVar
    clinsig = df["CLINSIG"].astype(str)
    df = df[clinsig.isin(CLINSIG_KEEP) | clinsig.str.contains("Uncertain", na=False)
            | clinsig.str.contains("athogenic", na=False)]
    record("2. ClinVar significance filter", df)

    # Step 3 - InterVar / ACMG
    df = df[df["InterVar"].astype(str).isin(INTERVAR_KEEP)]
    record("3. InterVar ACMG classification filter", df)

    # Step 4 - exonic
    df = df[df["Func.refGene"] == "exonic"]
    record("4. Exonic only (Func.refGene)", df)

    # Step 5 - protein-altering consequence
    df = df[df["ExonicFunc.refGene"].astype(str).isin(EXONICFUNC_KEEP)]
    record("5. Protein-altering consequence", df)

    # Step 6 - rare in ExAC (absent variants retained)
    df = df[df["_af"].isna() | (df["_af"] < MAX_AF)]
    record(f"6. Rare in ExAC (AF < {MAX_AF})", df)

    return df.drop(columns=["_af"]), pd.DataFrame(summary)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Stepwise WES variant filtering (see README.md, Section 2.2)."
    )
    parser.add_argument(
        "--input", "-i", nargs="+", required=True,
        help="One or more annotated variant tables (.xlsx/.csv/.tsv).",
    )
    parser.add_argument(
        "--outdir", "-o", default="../data",
        help="Directory for output files (default: ../data).",
    )
    parser.add_argument(
        "--sep", default=None,
        help="Field separator for text input (default: inferred from extension).",
    )
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    frames = []
    for raw_path in args.input:
        path = Path(raw_path)
        if not path.exists():
            sys.exit(f"ERROR: input file not found: {path}")
        frame = load_table(path, args.sep)
        print(f"Loaded {path.name}: {len(frame):,} rows")
        frames.append(frame)

    df = pd.concat(frames, ignore_index=True)
    df = normalise_intervar(df)
    df = recover_vcf_columns(df)
    require_columns(df)

    before = len(df)
    df = df.drop_duplicates(subset=["Chr", "Start", "End", "Ref", "Alt"]).reset_index(drop=True)
    if before != len(df):
        print(f"Removed {before - len(df):,} duplicate positions across input files")
    print(f"Combined dataset: {len(df):,} unique annotated positions\n")

    filtered, summary = run_pipeline(df)

    print(summary.to_string(index=False))
    print()

    export_cols = [c for c in EXPORT_COLS if c in filtered.columns]
    variants_path = outdir / "filtered_candidate_variants.csv"
    summary_path = outdir / "filtering_summary.csv"

    filtered[export_cols].sort_values("Gene.refGene").to_csv(variants_path, index=False)
    summary.to_csv(summary_path, index=False)

    print(f"Wrote {len(filtered):,} candidate variants -> {variants_path}")
    print(f"Wrote filtering summary               -> {summary_path}")


if __name__ == "__main__":
    main()
