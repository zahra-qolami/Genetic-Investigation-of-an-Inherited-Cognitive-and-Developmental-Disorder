# ACMG/AMP Classification Worksheet — *KMT5B* Candidate Variant

**Variant:** chr11:67957408 C>T (GRCh37/hg19), rs138431226
**Gene:** *KMT5B* (lysine methyltransferase 5B; previously *SUV420H1*)
**Consequence:** nonsynonymous SNV (missense)
**Zygosity:** heterozygous
**Read depth (DP):** 65 | **VCF FILTER:** PASS
**ExAC_ALL:** 0.0005
**Automated classification (InterVar):** Uncertain significance
**ClinVar:** no submitted interpretation at time of analysis

Classification framework: Richards et al., *Genet Med* 2015 (ACMG/AMP) [ref. 2 in README].

---

## 1. Status

> **Working classification: Variant of Uncertain Significance (VUS).**
>
> This worksheet documents the evidence considered and, critically, **which criteria cannot yet be applied** because the required data have not been generated. It is a working document for a fellowship coursework exercise, **not a clinical report**, and should not be used for diagnostic or reproductive decision-making.

---

## 2. Criteria assessment

### Criteria that can be assessed from current data

| Code | Description | Applied? | Justification |
|---|---|---|---|
| **PM2** | Absent/at extremely low frequency in population databases | **Assessed — supporting at most** | ExAC_ALL = 0.0005. This is rare but **not absent**. For a highly penetrant dominant neurodevelopmental disorder, a frequency of 5×10⁻⁴ is arguably higher than expected. Current ClinGen SVI guidance recommends PM2 be downgraded to *supporting* strength. Recommend re-checking against gnomAD v4 (larger, better-powered than ExAC) before finalising. |
| **PP2** | Missense variant in a gene with a low rate of benign missense variation and where missense is a common mechanism of disease | **Not applied — requires verification** | *KMT5B* pathogenic variants reported to date are predominantly protein-truncating; pathogenic missense variants exist but are fewer. The gene-specific missense constraint (e.g. gnomAD Z-score / o/e) should be checked before applying PP2. |
| **BP4 / PP3** | Computational evidence against / supporting deleterious effect | **Not applied — not yet evaluated** | *In-silico* predictions (REVEL, CADD, SIFT, PolyPhen-2, conservation via PhyloP/PhastCons) were not systematically extracted for this variant. These are available in the ANNOVAR annotation and in UCSC/Ensembl conservation tracks and should be tabulated. Note ACMG guidance: computational evidence is *supporting* strength only and must not be double-counted. |

### Criteria that cannot currently be applied (data not available)

| Code | Description | Blocker |
|---|---|---|
| **PS2 / PM6** | *De novo* occurrence (confirmed / assumed) | **Parental samples not sequenced.** Cannot be assessed. Note: in this pedigree the phenotype appears *inherited* through the paternal line, so a *de novo* origin is unlikely and these criteria would probably not apply even with parental data. |
| **PP1** | Co-segregation with disease in multiple affected family members | **Only one family member sequenced.** This is the single most valuable missing piece of evidence. Testing the second affected brother, the unaffected brother, and (ideally) the affected paternal uncle, paternal cousin, and paternal aunt's daughter could allow PP1 to be applied at supporting → strong strength depending on the number of informative meioses. |
| **BS4** | Lack of segregation in affected family members | Same blocker as PP1 — segregation testing would also be capable of **refuting** this candidate. This possibility must be stated explicitly. |
| **PS3 / BS3** | Well-established functional studies | No variant-specific functional assay has been performed. Published functional work concerns *KMT5B* haploinsufficiency in general, **not this specific missense change**, and therefore cannot be transferred to this variant. |
| **PS4** | Increased prevalence in affected individuals vs controls | This specific variant has not been reported in affected cohorts. |
| **PM1** | Located in a mutational hot spot / critical functional domain | Requires mapping the residue against the SET domain and the distribution of known pathogenic variants. Not yet performed. |
| **PM5 / PS1** | Novel missense at a residue where a different pathogenic missense has been seen / same amino acid change as a known pathogenic variant | Requires a systematic ClinVar/literature search at this specific codon. Not yet performed. |
| **PVS1** | Null variant in a gene where loss of function is a known mechanism | **Not applicable** — this is a missense variant, not a predicted null. |

---

## 3. Provisional classification

**Uncertain Significance (VUS).**

With PM2 at supporting strength as effectively the only currently applicable criterion, the evidence does not meet the ACMG/AMP combining rules for Likely Pathogenic. The gene-level argument for *KMT5B* presented in the README (phenotypic match to macrocephaly + mild-to-moderate ID, documented autosomal dominant inheritance with variable expressivity) is **evidence about the gene, not about this variant**, and is not itself an ACMG criterion.

---

## 4. Required next steps to resolve the classification

Listed in descending order of expected value:

1. **Segregation analysis.** Sanger-sequence this position in the second affected brother, the unaffected brother, and available affected paternal relatives. This is the only step that can meaningfully move the classification in either direction (PP1 or BS4), and it is inexpensive because only one genomic position needs testing.
2. **Independent variant confirmation.** Sanger-confirm the variant in the index case, and finalise HGVS cDNA/protein nomenclature against a defined RefSeq transcript (e.g. NM_017635) with Ensembl/UCSC cross-checking.
3. **Re-check population frequency in gnomAD v4** (and in a population-matched subset, if available) rather than relying on ExAC alone.
4. **Tabulate computational evidence** (REVEL, CADD, conservation) and apply PP3/BP4 at supporting strength only.
5. **Codon- and domain-level review** in ClinVar and the primary literature to determine whether PM1 or PM5 can be applied.

---

## 5. Honest limitations of this worksheet

- Classification is based on a **single sequenced individual**; no segregation data exist.
- Several criteria above are marked "not yet evaluated" rather than "absent". They may change the classification once assessed, in either direction.
- The variant's HGVS nomenclature has not yet been independently verified against a specified reference transcript.
- Automated tools (InterVar) classify this variant as VUS; no manual expert-panel curation has been applied.
- **This is a coursework exercise using real data, not a validated clinical interpretation.**
