# scripts/

## `filter_variants.py`

Reproducible implementation of the filtering pipeline described in the main README, Section 2.2.

### Requirements

```bash
pip install pandas openpyxl
```

### Usage

```bash
# single annotated table
python filter_variants.py -i annotated.xlsx -o ../data

# table split across several files (e.g. for file-size reasons)
python filter_variants.py -i part1.xlsx part2.xlsx part3.xlsx -o ../data

# tab-separated input
python filter_variants.py -i annotated.tsv --sep $'\t' -o ../data
```

### Outputs

- `filtered_candidate_variants.csv` — variants surviving all filters
- `filtering_summary.csv` — variant/gene counts at each step

### Two implementation details that matter

**1. Locale-tolerant number parsing.** When an annotated table is exported through a spreadsheet under certain locale settings, decimal values can be written with `/` instead of `.` (e.g. `0/0005`). A naive `float()` call fails on these, which can silently drop real variants from the output. `to_float()` normalises the separator before conversion.

**2. Recovery of VCF fields from unnamed columns.** ANNOVAR appends the original VCF record (`QUAL`, `FILTER`, `INFO`, `FORMAT`, sample genotype) after the annotation columns. In a spreadsheet export these arrive as `Unnamed: N` columns, so `FILTER` is present in the data but not addressable by name — and the quality filter would pass every row without warning. `recover_vcf_columns()` locates the FILTER column by its content and restores the surrounding field names.

Both behaviours are reported in the script's console output so that a skipped filter is visible rather than silent.

### Privacy

Per-sample genotype, allelic depth, and VCF `INFO`/`FORMAT` fields are deliberately excluded from the exported CSV (see `EXPORT_COLS`).
