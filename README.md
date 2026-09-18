# Genetic Investigation of an Inherited Cognitive and Developmental Disorder

**Zahra Gholami¹**

¹ MSc in Midwifery, Genomics Laboratory, Iran ([genomicslaboratory.ir](https://www.genomicslaboratory.ir/)); Helix Institute of Medical and Biological Sciences, USA ([helixinstitute.us](https://www.helixinstitute.us/))

---

## Abstract

We report a whole‑exome sequencing (WES)‑based investigation of a family segregating a cognitive and developmental disorder across multiple generations. Two affected brothers with mild developmental delay, borderline‑to‑educable intellectual functioning, and macrocephaly were identified within a pedigree showing additional affected relatives on the paternal side (a paternal uncle, a father's paternal cousin, and the father's paternal aunt's daughter), consistent with autosomal dominant transmission with variable expressivity. A stepwise variant‑filtering pipeline (quality → ClinVar significance → InterVar/ACMG automated classification → exonic/functional consequence → population frequency) was applied to the complete annotated WES call set (532,973 annotated positions) from one affected individual, yielding 387 rare, functionally plausible variants of uncertain significance across 271 genes. Phenotype‑driven review of this candidate list, cross‑referenced against the primary literature, identified a heterozygous, rare, well‑covered missense variant in ***KMT5B*** (chr11:67957408 C>T) as the final candidate gene. *KMT5B* encodes a histone H4K20 methyltransferase and is a "Definitively" curated cause of an autosomal dominant neurodevelopmental disorder (MRD51; OMIM #617788) whose hallmark features — global developmental delay, mild‑to‑moderate intellectual disability, and **macrocephaly** — closely match this family's phenotype, and for which **inherited transmission with markedly variable expressivity within a family** has been directly documented in the literature, mirroring the structure of this pedigree.

---

## 1. Clinical Presentation and Pedigree

The family originates from a non‑consanguineous union. Three sons were born; two are affected and one is clinically unaffected. Family history is notable on the paternal side: a paternal uncle of the affected brothers presents with the same clinical phenotype, Additionally, the father's paternal cousin (father's uncle's son) and the father's paternal aunt's daughter — are also affected. This distribution, with transmission tracked through the paternal line across at least three generations and a mix of affected males and females, is consistent with an **autosomal dominant pattern with variable expressivity**.

Both index patients are educable and were noted to have **mild developmental/cognitive delay** rather than severe intellectual disability. At clinical examination:

| Individual | Age at exam | Head circumference | SD score |
|---|---|---|---|
| IV:1 | 31 y | 57 cm | +1.32 SD |
| IV:2 | 27 y | 59 cm | +2.72 SD |

Both individuals show **macrocephaly**, more pronounced in IV:2.

---

## 2. Methods

### 2.1 Sequencing and sample scope
Genomic DNA from **one affected individual** was analyzed by whole‑exome sequencing (WES). Variants were called, quality‑filtered (VCF `FILTER = PASS`), and annotated with **ANNOVAR** against RefGene, ClinVar, InterVar automated ACMG/AMP classification, and the **ExAC** population frequency database. The complete annotated call set comprised **532,973 positions**.

> **Scope note:** Only a single affected family member has been sequenced and annotated to date. No genotype data are yet available for the second affected brother, the unaffected brother, or the additional affected paternal relatives shown in the pedigree. This analysis therefore identifies a rare, functionally plausible *candidate* variant within one exome — it does **not** demonstrate segregation with disease in this family (see Limitations, Section 5).

### 2.2 Variant filtering strategy
A sequential filter was applied to the full, deduplicated call set:

1. **Quality:** retained variants with VCF `FILTER = PASS`.
2. **ClinVar clinical significance (CLINSIG):** retained variants annotated as *Pathogenic*, *Likely pathogenic*, *Uncertain significance*, *Other*, or *Not provided*.
3. **InterVar automated ACMG classification:** restricted to *Pathogenic*, *Likely pathogenic*, and *Uncertain significance* calls, per the ACMG/AMP variant‑interpretation framework.
4. **Genic/functional location (Func.refGene):** retained exonic variants only.
5. **Functional consequence (ExonicFunc.refGene):** retained *nonsynonymous SNV*, *stoploss*, and *stopgain* variants.
6. **Population frequency (ExAC_ALL):** retained variants with allele frequency **< 0.001**.

**Result:** 387 variants across 271 genes passed all filters, all classified as "Uncertain significance" by InterVar.

### 2.3 Phenotype‑driven prioritization and database review
The 271 genes remaining after Section 2.2 were manually reviewed against the clinical phenotype (mild developmental delay, macrocephaly, autosomal dominant transmission with variable expressivity). Each candidate gene and its corresponding variant were evaluated across the following public genomic and clinical databases:

- **OMIM** (Online Mendelian Inheritance in Man) — to establish gene–disease relationships, inheritance patterns, and the reported clinical spectrum of each candidate gene, and to review previously catalogued allelic variants.
- **ClinVar** (NCBI) — to review previously submitted clinical interpretations of the specific variants and of other variants in the same gene, together with their supporting evidence and submitter concordance.
- **NCBI** resources (Gene, RefSeq, PubMed, dbSNP) — for reference transcript selection, gene summaries and functional annotation, variant identifiers, and systematic retrieval of the primary literature for each candidate gene.
- **Ensembl** — for transcript structure, exon/intron architecture, alternative transcript isoforms, cross‑species conservation, and regulatory/comparative genomic context of the variant position.
- **UCSC Genome Browser** — for visual inspection of the variant in its genomic context, including transcript alignment, conservation tracks (PhyloP/PhastCons), and coordinate verification against the GRCh37/hg19 assembly.

Evidence from these databases was then integrated with the primary literature (Section 4) to identify ***KMT5B*** as the strongest‑supported final candidate gene.

---

## 3. Candidate Variant

| Gene | Position (GRCh37/hg19) | Zygosity | Depth (DP) | Quality | ExAC_ALL |
|---|---|---|---|---|---|
| ***KMT5B*** | chr11:67957408 C>T | Heterozygous | 65 | PASS | 0.0005 |

*(Exact HGVS cDNA/protein nomenclature, and independent confirmation by Sanger sequencing, should be finalized before inclusion in any formal clinical report — see Section 5.)*

---

## 4. Discussion: KMT5B as the Candidate Gene

### 4.1 Gene function and disease association
*KMT5B* (previously known as *SUV420H1*) is located on chromosome 11q13.2 and encodes a SET‑domain histone lysine methyltransferase that catalyzes dimethylation of histone H4 at lysine 20 (H4K20me2), a modification central to chromatin compaction, transcriptional regulation, genomic stability, and DNA damage response [1,2,3]. *KMT5B* was as an autism candidate gene [4] and was firmly established as a neurodevelopmental‑disorder gene by Stessman et al. in a large targeted‑sequencing study of ~11,700 patients with neurodevelopmental delay, which identified deleterious heterozygous *KMT5B* variants among a set of 91 risk genes [5]. This gene‑disease relationship — autosomal dominant *KMT5B*‑related neurodevelopmental disorder / "Intellectual Developmental Disorder, Autosomal Dominant 51" (MRD51; OMIM #617788, gene OMIM #610881) — is now classified **"Definitive"** by the ClinGen Syndromic Disorders Gene Curation Expert Panel, based on case‑level and experimental evidence accumulated since 2014 [6,7].

### 4.2 Core clinical phenotype and match to this family
Across the literature, *KMT5B*‑related neurodevelopmental disorder is characterized by global developmental delay, intellectual disability that is typically **mild‑to‑moderate**, autism spectrum features, hypotonia, and — critically — **macrocephaly**, reported as a prominent and recurring clinical feature across independent cohorts [8–12]:

- The largest deep‑phenotyping cohort to date (n = 43) explicitly lists **macrocephaly** among the core features of the disorder, alongside global developmental delay, autism, and congenital anomalies, with hypotonia and congenital heart defects identified as additional under‑recognized features [8].
- A separate series of three unrelated patients with distinct *de novo* missense and frameshift *KMT5B* variants all presented with macrocephaly, leading the authors to explicitly recommend that *KMT5B* be considered in the differential diagnosis of neurodevelopmental disorders **with macrocephaly and/or overgrowth** [9].
- Functional work in a *Kmt5b*‑haploinsufficient mouse model found that although the mice were smaller overall, brain size was relatively preserved — i.e., **relative macrocephaly** — reproducing the human clinical observation at the model‑organism level and supporting a direct mechanistic link between *KMT5B* loss and increased relative head size [8].
- Additional patient cohorts and case reports (from China, Croatia, and elsewhere) consistently report macrocephaly as a recurring feature alongside autism, intellectual disability, and speech/language delay [10,13,14].

Unlike some other chromatin‑modifier neurodevelopmental genes, **macrocephaly in *KMT5B*‑related disorder has been reported with both missense and loss‑of‑function (nonsense/frameshift) variants** [8,9,14], meaning our candidate variant's missense nature does not weaken — and is directly consistent with — this phenotypic association.

### 4.3 Inheritance pattern: a close match to this pedigree
Most reported *KMT5B* pathogenic variants are *de novo*; however, **inherited cases with pronounced variable expressivity within a family have been specifically documented**, providing a close precedent for the transmission pattern observed in this pedigree (an affected paternal uncle, paternal cousin, and paternal aunt's daughter, alongside the index brothers):

- A maternally inherited *KMT5B* variant was reported in a family in which the affected mother had only **mild** intellectual disability and subtle autistic traits, while her son (carrying the identical variant) had a much more severe neurodevelopmental phenotype — a striking example of variable expressivity of a single inherited *KMT5B* allele within one family [13].
- A paternally inherited frameshift *KMT5B* variant was identified in **two affected brothers**, both of whom inherited the variant from their father, in a Chinese family — directly analogous to the sibling‑pair presentation in our pedigree [14].
- The original OMIM‑cataloged variant series similarly documents at least one inherited (maternally transmitted) missense *KMT5B* variant among the earliest reported cases [6,7].


### 4.4 Convergent evidence from independent groups
Since its initial description, *KMT5B*‑related neurodevelopmental disorder has been independently replicated and further characterized by multiple research groups internationally, strengthening confidence in the gene‑disease relationship itself (as distinct from any single variant): case series and functional studies have been published from the United States [5,8,15], Israel [9], China [14,16], Croatia [15], collectively describing dozens of unrelated affected individuals and converging on a consistent core phenotype of developmental delay, mild‑to‑moderate ID, macrocephaly, hypotonia, and autism spectrum features.

### 4.5 Molecular plausibility
KMT5B is ubiquitously expressed, with demonstrated roles in nervous‑system development; RNA‑sequencing and proteomic studies of patient‑derived material and *Kmt5b*‑deficient mouse models show disrupted expression of pathways governing axon guidance, neuronal dendritic complexity, neuromuscular junction integrity, and myofiber composition, providing a coherent mechanistic link between *KMT5B* haploinsufficiency and the neurodevelopmental/neuromuscular phenotype observed clinically [8,15,17].

---

## 5. Limitations

1. **Single‑sample analysis.** Only one affected individual's exome has been annotated and filtered to date. No genotype data are yet available for the second affected brother, the unaffected brother, or the affected paternal relatives shown in the pedigree, so **segregation of the *KMT5B* variant with the phenotype in this family has not yet been demonstrated.** This is the single most important next step and the primary reason this finding should be reported as a strongly supported *candidate*, not a confirmed molecular diagnosis.
2. Automated ClinVar/InterVar tiers classify the variant only as "Uncertain significance"; the case for *KMT5B* rests on phenotype‑driven, literature‑based reasoning (Section 4), not on an automatic pathogenicity call.
3. Exact HGVS cDNA/protein nomenclature for the variant, and independent confirmation (e.g., Sanger sequencing), should be completed and included in any formal clinical report.
4. Segregation testing in additional relatives — at minimum the second affected brother and the unaffected brother, and ideally the affected paternal uncle, cousin, and aunt's daughter — is the most valuable next step to move this candidate toward a confirmed diagnosis under ACMG/AMP criteria.

---

## 6. Conclusion

In a family with an apparently dominantly transmitted disorder featuring mild developmental delay and macrocephaly, a stepwise quality/ClinVar/InterVar/functional/frequency filtering pipeline applied to the complete WES call set (532,973 annotated positions) from one affected individual narrowed the data to 387 rare, functionally plausible variants across 271 genes. Phenotype‑driven review identified a heterozygous missense variant in ***KMT5B*** as the final candidate gene. *KMT5B* is a "Definitively" curated cause of autosomal dominant neurodevelopmental disorder whose core phenotype — mild‑to‑moderate intellectual disability and macrocephaly, regardless of variant class — closely matches this family, and for which inherited transmission with variable expressivity has been directly documented in independent families, closely mirroring this pedigree's structure. Confirmatory segregation analysis in additional family members and independent variant validation are recommended as the next steps before this candidate can be considered a confirmed molecular diagnosis.

---

## References

1.	Hulen, J., Kenny, D., Black, R., Hallgren, J., Hammond, K. G., Bredahl, E. C., ... & Stessman, H. A. (2022). KMT5B is required for early motor development. Frontiers in Genetics, 13, 901228.
2.	Aksel Kilicarslan, O., Gangfuß, A., Kölbel, H., Muhmann, D., Polavarapu, K., Thompson, R., ... & Roos, A. (2025). Combined Histological and Proteomic Analysis Reveals Muscle Denervation in KMT5B-Related Neurodevelopmental Disorder: A Case Report. Journal of Clinical Medicine, 14(24), 8636.
3.	Wu, H.; Siarheyeva, A.; Zeng, H.; Lam, R.; Dong, A.; Wu, X.H.; Li, Y.; Schapira, M.; Vedadi, M.; Min, J. Crystal Structures of the Human Histone H4K20 Methyltransferases SUV420H1 and SUV420H2. FEBS Lett. 2013, 587, 3859–3868. 
4.	Chen, G., Han, L., Tan, S., Jia, X., Wu, H., Quan, Y., ... & Guo, H. (2022). Loss-of-function of KMT5B leads to neurodevelopmental disorder and impairs neuronal development and neurogenesis. Journal of Genetics and Genomics, 49(9), 881-890.
5.	Stessman, H. A., Xiong, B. O., Coe, B. P., Wang, T., Hoekzema, K., Fenckova, M., ... & Eichler, E. E. (2017). Targeted sequencing identifies 91 neurodevelopmental-disorder risk genes with autism and developmental-disability biases. Nature genetics, 49(4), 515-526.
6.	OMIM. *610881 — LYSINE METHYLTRANSFERASE 5B; KMT5B. Online Mendelian Inheritance in Man. omim.org/entry/610881. https://omim.org/entry/610881
7.	OMIM. #617788 — INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL DOMINANT 51 (MRD51). omim.org/entry/617788. https://omim.org/entry/617788
8.	Sheppard, S. E., Bryant, L., Wickramasekara, R. N., Vaccaro, C., Robertson, B., Hallgren, J., ... & Stessman, H. A. (2023). Mechanism of KMT5B haploinsufficiency in neurodevelopment in humans and mice. Science advances, 9(10), eade1463.
9.	Eliyahu, A., Barel, O., Greenbaum, L., Zaks Hoffer, G., Goldberg, Y., Raas-Rothschild, A., ... & Pode-Shakked, B. (2022). Refining the phenotypic spectrum of KMT5B-associated developmental delay. Frontiers in pediatrics, 10, 844845.
10.	Chen, G., Han, L., Tan, S., Jia, X., Wu, H., Quan, Y., ... & Guo, H. (2022). Loss-of-function of KMT5B leads to neurodevelopmental disorder and impairs neuronal development and neurogenesis. Journal of Genetics and Genomics, 49(9), 881-890.
11.	ClinGen Syndromic Disorders Gene Curation Expert Panel. KMT5B–autosomal dominant complex neurodevelopmental disorder, gene disease validity classification: Definitive. Evaluated 2021 11 03. Available via GenCC (thegencc.org). https://pubmed.ncbi.nlm.nih.gov/39606380/
12.	Faundes, V., Newman, W. G., Bernardini, L., Canham, N., Clayton-Smith, J., Dallapiccola, B., ... & Hurst, J. (2018). Histone lysine methylases and demethylases in the landscape of human developmental disorders. The American Journal of Human Genetics, 102(1), 175-187.
13.	Odak, L., Vulin, K., Meašić, A. M., Šamadan, L., & Tripalo Batoš, A. (2023). Neurodevelopmental disorder caused by an inherited novel KMT5B variant: case report. Croatian Medical Journal, 64(5), 334-338.
14.	Tong, J., Chen, X., Wang, X., Men, S., Liu, Y., Sun, X., ... & Wang, L. (2024). Novel KMT5B variant associated with neurodevelopmental disorder in a Chinese family: a case report. Heliyon, 10(7).
15.	Wickramasekara, R. N., Robertson, B., Hulen, J., Hallgren, J., & Stessman, H. A. (2021). Differential effects by sex with Kmt5b loss. Autism Research, 14(8), 1554-1571.
16.	Özcan, S., & Yeter, B. (2026). A Novel KMT5B Frameshift Variant Presenting with Autism and Psychiatric Features: Intrafamilial Phenotypic Variation–A Case Report. Molecular Syndromology, 17(4), 434-440.
17.	Politano, D., Borgatti, R., Borgonovi, G., Cistaro, A., Danesino, C., Fania, P., ... & Giordano, M. (2025). Bridging Genotype to Phenotype in KMT5B-Related Syndrome: Evidence from RNA-Seq, 18FDG-PET, Clinical Deep Phenotyping in Two New Cases, and a Literature Review. Genes, 16(10), 1174.