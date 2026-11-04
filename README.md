# Awesome-MedIA-Fairness

A curated, source-traceable collection on **medical algorithm fairness**, with medical imaging as its historical core and explicit coverage of EHR, clinical language/foundation models, physiological signals and healthcare algorithms.

[![Catalog validation](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/validate-catalog.yml/badge.svg)](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/validate-catalog.yml) [![Link health](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/check-links.yml/badge.svg)](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/check-links.yml)

**Catalog:** 90 main-list papers and 16 surveys/perspectives. **Evidence is recorded per entry:** importing a cited study is not an independent methods audit or reproduction.

Built from the [original catalog](docs/legacy-catalog.md), [Xu et al., npj Digital Medicine 2024](https://doi.org/10.1038/s41746-024-01276-5), and [FAIMI resources](https://faimi-workshop.github.io/resources/). See the [source and migration audit](docs/source-audit-2026-11-04.md).

Weekly Qoder DeepSeek updates: [Chinese digest](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/literature-data/reports/latest.md) · [weekly topic index](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/literature-data/reports/weekly.md) · [screening proposals](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/literature-data/reports/catalog-proposals.md). [Automation guide](docs/literature-automation.md).

## 🎯 Scope

We collect studies that examine **algorithmic fairness, protected-group disparities, bias mechanisms, mitigation, or fairness measurement** in an explicit medical/biomedical task. Null findings and unsuccessful mitigation are relevant; a positive fairness gain is not required.

### Inclusion and evidence

New machine inclusion proposals require all five: (1) a medical task, (2) an identifiable algorithm or model, (3) an explicit fairness/bias question, (4) defined groups/attributes, a subgroup-discovery protocol, or an explicit individual/counterfactual fairness definition, and (5) implemented evaluation with source-grounded evidence. Full-text verification is required before a machine inclusion proposal.

Static accuracy differences between disease classes, generic domain adaptation, ordinary imbalance, and health inequality without an algorithmic fairness question are insufficient. Protected-attribute predictability is evidence of encoding, not by itself proof of downstream discrimination. Reviews, perspectives, broad ethical frameworks and generic fairness theory are separated below.

Historical and reference-list imports remain visible with provenance and evidence labels. **Primary metadata/abstract means that source was retrieved, not that all classifications or findings have been independently re-audited.** Inherited mitigation-stage labels can require correction; post-processing is not assumed to freeze a predictor unless the primary protocol establishes it.

## 📌 Contents

- [Taxonomy](#-taxonomy)
- [Survey Papers](#-survey-papers)
- [Fairness Papers](#-fairness-papers)
- [By Topic](#-by-topic)
- [Datasets, Benchmarks and Toolkits](#-datasets-benchmarks-and-toolkits)
- [Related Repositories](#-related-repositories)
- [Cross-References](#-cross-references)
- [Community and Calls](#-community-and-calls)
- [Contributing](#-contributing)

## 🧬 Taxonomy

| Field | Controlled values |
|---|---|
| **Domain** | `Clinical NLP and foundation models`, `EHR and clinical prediction`, `Healthcare operations`, `Medical imaging`, `Other biomedical`, `Physiological signals` |
| **Focus** | `Benchmark`, `Bias mechanisms`, `Dataset`, `Evaluation`, `Mitigation`, `Theory and measurement` |
| **Stage** | `Evaluation`, `In-processing`, `Multi-stage`, `Not applicable`, `Not verified`, `Post-processing`, `Pre-processing` |
| **Attributes** | `Age`, `Disability`, `Intersectional`, `Not specified`, `Other`, `Race and ethnicity`, `Sex and gender`, `Site and geography`, `Skin tone`, `Socioeconomic status` |
| **Assets** | `Code`, `Data`, `Paper only`, `Project`, `Weights` |
| **Evidence** | `Legacy unverified`, `Primary abstract`, `Primary full text`, `Primary metadata`, `Reviewed source` |

Use the smallest directly supported set. `Sex and gender` is a navigation label, not an assertion that the constructs or measurements are interchangeable. `Intersectional` requires joint-group analysis; multiple separate attributes alone are insufficient.

## 📚 Survey Papers

- (*npj Digital Medicine'25*) **Bias recognition and mitigation strategies in artificial intelligence healthcare applications**
  [[📝 Paper](https://doi.org/10.1038/s41746-025-01503-7)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*npj Digital Medicine'24*) **Addressing fairness issues in deep learning-based medical image analysis: a systematic review**
  [[📝 Paper](https://doi.org/10.1038/s41746-024-01276-5)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*JAMIA Open'24*) **Algorithmic individual fairness and healthcare: a scoping review**
  [[📝 Paper](https://doi.org/10.1093/jamiaopen/ooae149)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*Nature Biomedical Engineering'23*) **Algorithmic fairness in artificial intelligence for medicine and healthcare**
  [[📝 Paper](https://doi.org/10.1038/s41551-023-01056-8)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*FAIMI-listed'23*) **No Fair Lunch: A Causal Perspective on Dataset Bias in Machine Learning for Medical Imaging**
  [[📝 Paper](https://arxiv.org/abs/2307.16526)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*Patterns'23*) **The path toward equal performance in medical machine learning**
  [[📝 Paper](https://doi.org/10.1016/j.patter.2023.100790)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*2023 ACM Conference on Fairness Accountability and Transparency'23*) **What's fair is… fair? Presenting JustEFAB, an ethical framework for operationalizing medical ethics and social justice in the integration of clinical machine learning**
  [[📝 Paper](https://doi.org/10.1145/3593013.3594096)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*Journal of Medical and Biological Engineering'22*) **A Systematic Review of ‘Fair’ AI Model Development for Image Classification and Prediction**
  [[📝 Paper](https://doi.org/10.1007/s40846-022-00754-z)]
  > **Provenance:** [Source 1](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Nature Communications'22*) **Addressing fairness in artificial intelligence for medical imaging**
  [[📝 Paper](https://doi.org/10.1038/s41467-022-32186-3)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*ACM Computing Surveys'21*) **A Survey on Bias and Fairness in Machine Learning**
  [[📝 Paper](https://doi.org/10.1145/3457607)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*FAIMI-listed'21*) **Assessing Bias in Medical AI**
  [[📝 Paper](https://www.cse.cuhk.edu.hk/~qdou/public/IMLH2021_files/64_CameraReady_ICML_2021_Interpretable_Machine_Learning_in_Healthcare_workshop.pdf)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*Proceedings of the 2021 ACM Conference on Fairness Accountability'21*) **Re-imagining Algorithmic Fairness in India and Beyond**
  [[📝 Paper](https://doi.org/10.1145/3442188.3445896)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*The Lancet Digital Health'20*) **Ethical limitations of algorithmic fairness solutions in health care machine learning**
  [[📝 Paper](https://doi.org/10.1016/s2589-7500(20)30065-0)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*FAIMI-listed'20*) **Fairness in Deep Learning: A Computational Perspective**
  [[📝 Paper](https://ieeexplore.ieee.org/document/9113719)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*Annals of Internal Medicine'18*) **Ensuring Fairness in Machine Learning to Advance Health Equity**
  [[📝 Paper](https://doi.org/10.7326/m18-1990)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

- (*FAIMI-listed'18*) **The Measure and Mismeasure of Fairness**
  [[📝 Paper](https://arxiv.org/abs/1808.00023)]
  > **Provenance:** [Source 1](https://faimi-workshop.github.io/resources/)

## 📝 Fairness Papers

> Annual entries are bibliographic records after exact-title/identifier deduplication, not independent experiments. Possible preprint/journal lineage is documented in the source audit; records are not merged solely from similar titles or shared authors. Source year and eventual publication year may differ.

### 2026

- (*Medical Image Analysis'26*) **Rethinking fairness in medical imaging: Maximizing group-specific performance with application to skin disease diagnosis**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.103950)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for dermatology images. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

### 2025

- (*European Heart Journal - Digital Health'25*) **An investigation into the causes of race bias in artificial intelligence–based cine cardiac magnetic resonance segmentation**
  [[📝 Paper](https://doi.org/10.1093/ehjdh/ztaf008)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Investigations into the causes of bias. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Scientific Reports'25*) **An investigation of race bias in deep learning-based segmentation of prostate MRI images**
  [[📝 Paper](https://doi.org/10.1038/s41598-025-26189-5)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for medical image segmentation:. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Machine Learning for Biomedical Imaging'25*) **Understanding-informed Bias Mitigation for Fair CMR Segmentation**
  [[📝 Paper](https://doi.org/10.59275/j.melba.2025-6747)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Mitigation` · `Stage: Not verified` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Bias mitigation. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*eBioMedicine'25*) **Where, why, and how is bias learned in medical image analysis models? A study of bias encoding within convolutional networks using synthetic data**
  [[📝 Paper](https://doi.org/10.1016/j.ebiom.2024.105501)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Investigations into the causes of bias. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

### 2024

- (*Nature Medicine'24*) **Demographic bias in misdiagnosis by computational pathology models**
  [[📝 Paper](https://doi.org/10.1038/s41591-024-02885-z)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for histology:. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Scientific Reports'24*) **Fair AI-powered orthopedic image segmentation: addressing bias and promoting equitable healthcare**
  [[📝 Paper](https://doi.org/10.1038/s41598-024-66873-6)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for medical image segmentation:. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*NeurIPS Datasets and Benchmarks'24*) **FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models**
  [[📝 Paper](https://arxiv.org/abs/2407.00983)] [[💻 Code](https://github.com/FairMedFM/FairMedFM)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Code` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Software toolkits: FairMedFM. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*ICLR'24*) **FairSeg: A Large-Scale Medical Image Segmentation Dataset for Fairness Learning Using Segment Anything Model with Fair Error-Bound Scaling**
  [[📝 Paper](https://arxiv.org/abs/2311.02189)] [[💻 Code](https://github.com/Harvard-Ophthalmology-AI-Lab/FairSeg)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Dataset + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Code` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for medical image segmentation:. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Review-listed'24*) **Fairtune: Optimizing parameter efficient fine tuning for fairness in medical image analysis**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR89)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Sex and gender + Age + Skin tone` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Primary paper link pending; Reference-listed medical fairness work; source category: UM-In-MISC. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'24*) **Slicing Through Bias: Explaining Performance Gaps in Medical Image Analysis Using Slice Discovery Methods**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-72787-0_1)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Investigations into the causes of bias. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Computer Methods and Programs in Biomedicine'24*) **Understanding skin color bias in deep learning-based skin lesion segmentation**
  [[📝 Paper](https://doi.org/10.1016/j.cmpb.2024.108044)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for dermatology images. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

### 2023

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **A comparative study of fairness in medical machine learning**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230368)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing + Post-processing + Pre-processing` · `Attributes: Age + Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-re-distribution. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*eBioMedicine'23*) **Algorithmic encoding of protected characteristics in chest X-ray disease detection models**
  [[📝 Paper](https://doi.org/10.1016/j.ebiom.2023.104467)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)
  > **Version note:** Possible preprint/journal lineage; see the [source audit](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/source-audit-2026-11-04.md). Not counted as independently evaluated methods.

- (*JAMA Network Open'23*) **Algorithmic Fairness of Machine Learning Models for Alzheimer Disease Progression**
  [[📝 Paper](https://doi.org/10.1001/jamanetworkopen.2023.42203)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'23*) **An Investigation into Race Bias in Random Forest Models Based on Breast DCE-MRI Derived Radiomics Features**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_22)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **An Investigation into the Impact of Deep Learning Model Choice on Sex and Race Bias in Cardiac MR Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_21)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **Are sex-based physiological differences the cause of gender bias for chest X-ray diagnosis?**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_14)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-discovery. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'23*) **Auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_17)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Age + Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Proceedings of the National Academy of Sciences'23*) **Bias in machine learning models can be significantly mitigated by careful training: Evidence from neuroimaging studies**
  [[📝 Paper](https://doi.org/10.1073/pnas.2211613120)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Age + Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-aggregation. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **Bias in unsupervised anomaly detection in brain MRI**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_12)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-discovery. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'23*) **CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-25069-9_14)] [[💻 Code](https://github.com/sfu-mial/CIRCLe)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing + Pre-processing` · `Attributes: Skin tone` · `Assets: Code` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Synthesis. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **De-identification and obfuscation of gender attributes from retinal scans**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_9)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-harmonization. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **Detecting shortcuts in medical images-a case study in chest x-rays**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230572)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-discovery. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'23*) **EdgeMixup: embarrassingly simple data alteration to improve Lyme disease lesion segmentation and diagnosis fairness**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-43901-8_36)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-harmonization. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Medical Image Analysis'23*) **Equitable modelling of brain imaging by counterfactual augmentation with morphologically constrained 3D deep generative models**
  [[📝 Paper](https://doi.org/10.1016/j.media.2022.102723)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-synthesis. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Review-listed'23*) **Evaluating the fairness of deep learning uncertainty estimates in medical image analysis**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR12)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Primary paper link pending; Reference-listed medical fairness work; source category: FE-discovery. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2023'23*) **FairAdaBN: Mitigating unfairness with adaptive batch normalization and its application to dermatological disease classification**
  [[📝 Paper](https://arxiv.org/abs/2303.08325)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Sex and gender + Skin tone` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Universal Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Cancers'23*) **From Head and Neck Tumour and Lymph Node Segmentation to Survival Prediction on PET/CT: An End-to-End Framework Featuring Uncertainty, Fairness, and Multi-Region Multi-Modal Radiomics**
  [[📝 Paper](https://doi.org/10.3390/cancers15071932)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2023'23*) **Harvard Glaucoma Fairness: A Retinal Nerve Disease Dataset for Fairness Learning and Fair Identity Normalization**
  [[📝 Paper](https://arxiv.org/abs/2306.09264)] [[💻 Code](https://github.com/luoyan407/Harvard-GF)] [[📊 Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A4XMO1)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Dataset + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Code + Data` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness Dataset. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md)

- (*Alzheimers Research &amp Therapy'23*) **Higher performance for women than men in MRI-based Alzheimer’s disease detection**
  [[📝 Paper](https://doi.org/10.1186/s13195-023-01225-6)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Science'23*) **Implications of predicting race variables from medical images**
  [[📝 Paper](https://doi.org/10.1126/science.adh4260)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Shortcut learning, models recognizing sensitive patient attributes, and fairness in medical AI. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Nature Communications'23*) **Improving model fairness in image-based computer-aided diagnosis**
  [[📝 Paper](https://doi.org/10.1038/s41467-023-41974-4)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Age + Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-in-constraints. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*ICLR 2023'23*) **MEDFAIR: Benchmarking Fairness for Medical Imaging**
  [[📝 Paper](https://arxiv.org/abs/2210.01725)] [[💻 Code](https://github.com/ys-zong/MEDFAIR)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation + Mitigation` · `Stage: Evaluation` · `Attributes: Age + Race and ethnicity + Sex and gender + Skin tone` · `Assets: Code` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness Benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **Mitigating bias in MRI-based Alzheimer’s disease classifiers through pruning of deep neural networks**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_16)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Post-processing` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-post-pruning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*IPMI 2023'23*) **On Fairness of Medical Image Classification with Multiple Sensitive Attributes via Learning Orthogonal Representations**
  [[📝 Paper](https://arxiv.org/abs/2301.01481)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Age + Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Disentanglement Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'23*) **Revisiting skin tone fairness in dermatological lesion classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_24)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Radiology Artificial Intelligence'23*) **Risk of Bias in Chest Radiography Deep Learning Foundation                     Models**
  [[📝 Paper](https://doi.org/10.1148/ryai.230060)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for chest x-rays. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **The role of subgroup separability in group-fair medical image classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-43898-1_18)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Age + Race and ethnicity + Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-discovery. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'23*) **Towards Unraveling Calibration Biases in Medical Image Analysis**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_13)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Miscellaneous. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **Unsupervised Bias Discovery in Medical Image Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_26)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for medical image segmentation:. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'23*) **Unveiling Fairness Biases in Deep Learning-Based Brain MRI Reconstruction**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_10)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness in image reconstruction. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Review-listed'23*) **Visualizing chest X-ray dataset biases using GANs**
  [[📝 Paper](https://openreview.net/forum?id=bFb3V8ALx4W)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-discovery. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

### 2022

- (*Lecture Notes in Computer Science'22*) **A Penalty Approach for Normalizing Feature Distributions to Build Confounder-Free Models**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16437-8_37)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-in-disentanglement. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'22*) **A Study of Demographic Bias in CNN-Based Brain MR Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-17899-3_2)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: FE-benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'22*) **A Systematic Study of Race and Sex Bias in CNN-Based Cardiac MR Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-23443-9_22)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for cardiac MRI:. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*The Lancet Digital Health'22*) **AI recognition of patient race in medical imaging: a modelling study**
  [[📝 Paper](https://doi.org/10.1016/s2589-7500(22)00063-2)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Shortcut learning, models recognizing sensitive patient attributes, and fairness in medical AI. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'22*) **Conditional VAEs for confound removal and normative modelling of neurodegenerative diseases**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16431-6_41)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Age` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-in-disentanglement. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ML4HC 2022'22*) **Debiasing Deep Chest X-Ray Classifiers using Intra- and Post-processing Methods**
  [[📝 Paper](https://proceedings.mlr.press/v182/marcinkevics22a.html)] [[💻 Code](https://github.com/i6092467/diff-bias-proxies)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Post-processing` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Code` · `Evidence: Reviewed source`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Network Pruning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2022'22*) **Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)**
  [[📝 Paper](https://doi.org/10.1038/s41467-023-39902-7)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation + Pre-processing` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Resampling. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*FAIMI-listed'22*) **Diagnosing failures of fairness transfer across distribution shift in real-world medical settings**
  [[📝 Paper](https://arxiv.org/abs/2202.01034)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Miscellaneous. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Science Advances'22*) **Disparities in dermatology AI performance on a diverse, curated clinical image set**
  [[📝 Paper](https://doi.org/10.1126/sciadv.abq6147)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: AI fairness for dermatology images. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'22*) **Disproportionate subgroup impacts and other challenges of fairness in artificial intelligence for medical image analysis**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-23223-7_2)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-in-adversarial. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ECCVW 2022'22*) **FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning**
  [[📝 Paper](https://arxiv.org/abs/2208.10013)] [[💻 Code](https://github.com/siyi-wind/FairDisCo)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Skin tone` · `Assets: Code` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Contrastive Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Review-listed'22*) **Fairness by learning orthogonal disentangled representations**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR83)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Primary paper link pending; Reference-listed medical fairness work; source category: UM-in-disentanglement. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Frontiers in Cardiovascular Medicine'22*) **Fairness in Cardiac Magnetic Resonance Imaging: Assessing Sex and Racial Bias in Deep Learning-Based Segmentation**
  [[📝 Paper](https://doi.org/10.3389/fcvm.2022.859310)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Unfairness Existence. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Journal of Medical Imaging'22*) **Fairness-related performance and explainability effects in deep learning models for brain image analysis**
  [[📝 Paper](https://doi.org/10.1117/1.jmi.9.6.061102)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Unfairness Existence. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'22*) **FairPrune: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16431-6_70)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Post-processing` · `Attributes: Sex and gender + Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Network Pruning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'22*) **Feature Robustness and Sex Differences in Medical Imaging: A Case Study in MRI-Based Alzheimer’s Disease Detection**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16431-6_9)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness & Data Distribution. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*MLHC'22*) **How fair is your graph? exploring fairness concerns in neuroimaging studies**
  [[📝 Paper](https://proceedings.mlr.press/v182/ribeiro22a.html)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Unfairness Existence. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*NeurIPS Workshop 2022'22*) **Improving fairness in image classification via sketching**
  [[📝 Paper](https://openreview.net/forum?id=Rq2vt3tnAK9)] [[💻 Code](https://github.com/ubc-tea/Improving-Fairness-in-Image-Classification-via-Sketching)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Age + Sex and gender` · `Assets: Code` · `Evidence: Reviewed source`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Embellishment. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*PCHIL 2022'22*) **Improving the Fairness of Chest X-ray Classifiers**
  [[📝 Paper](https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Mitigation` · `Stage: Not verified` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness Benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Lecture Notes in Computer Science'22*) **Pseudo bias-balanced learning for debiased chest x-ray classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16452-1_59)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-in-constraints. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Review-listed'22*) **Rényi fair information bottleneck for image classification**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR121)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Primary paper link pending; Reference-listed medical fairness work; source category: UM-in-constraints. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

### 2021

- (*Translational Vision Science &amp Technology'21*) **Addressing Artificial Intelligence Bias in Retinal Diagnostics**
  [[📝 Paper](https://doi.org/10.1167/tvst.10.2.13)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: Evaluation + Pre-processing` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-synthesis. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*ArXiv 2021'21*) **AI Fairness via Domain Adaptation**
  [[📝 Paper](https://arxiv.org/abs/2104.01109)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: Pre-processing` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Synthesis. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2021'21*) **Algorithmic encoding of protected characteristics in image-based models for disease detection**
  [[📝 Paper](https://arxiv.org/abs/2110.14755)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness & Data Distribution. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md)
  > **Version note:** Possible preprint/journal lineage; see the [source audit](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/source-audit-2026-11-04.md). Not counted as independently evaluated methods.

- (*Proceedings of the Pacific Symposium 2021'21*) **CheXclusion: Fairness gaps in deep chest X-ray classifiers**
  [[📝 Paper](https://pubmed.ncbi.nlm.nih.gov/33691020/)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation + Mitigation` · `Stage: Evaluation + Pre-processing` · `Attributes: Age + Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Aggregation. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'21*) **Confound removal and normalization in practice: a neuroimaging based sex prediction case study**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-67670-4_1)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Age` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-in-disentanglement. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Medical Image Analysis'21*) **Detect and correct bias in multi-site neuroimaging datasets**
  [[📝 Paper](https://doi.org/10.1016/j.media.2020.101879)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-harmonization. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*MICCAI-DART 2021'21*) **Detecting Melanoma Fairly: Skin Tone Detection and Debiasing for Skin Lesion Classification**
  [[📝 Paper](https://arxiv.org/abs/2202.02832)] [[💻 Code](https://github.com/pbevan1/Detecting-Melanoma-Fairly)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Mitigation` · `Stage: In-processing` · `Attributes: Skin tone` · `Assets: Code` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness Benchmarking. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2021'21*) **Estimating and improving fairness with adversarial learning**
  [[📝 Paper](https://oecd.ai/fr/catalogue/metric-use-cases/estimating-and-improving-fairness-with-adversarial-learning)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Age + Sex and gender + Skin tone` · `Assets: Paper only` · `Evidence: Reviewed source`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Adversarial Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2021'21*) **Evaluating subgroup disparity using epistemic uncertainty in mammography**
  [[📝 Paper](https://arxiv.org/abs/2107.02716)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness & Uncertainty. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'21*) **Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-87199-4_39)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: Evaluation + In-processing + Pre-processing` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Resampling. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*ArXiv 2021'21*) **Model Selection's Disparate Impact in Real-World Deep Learning Applications**
  [[📝 Paper](https://arxiv.org/abs/2104.00606)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness & Model Selection. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md)

- (*Lecture Notes in Computer Science'21*) **On the Fairness of Swarm Learning in Skin Lesion Classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-90874-4_12)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Age + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Federated Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2021'21*) **RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR**
  [[📝 Paper](https://arxiv.org/abs/2111.11665)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Benchmark + Evaluation + Mitigation` · `Stage: Pre-processing` · `Attributes: Age + Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Data Aggregation. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Emergency Radiology'21*) **Radiology “forensics”: determination of age and sex from chest radiographs using deep learning**
  [[📝 Paper](https://doi.org/10.1007/s10140-021-01953-y)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Shortcut learning, models recognizing sensitive patient attributes, and fairness in medical AI. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*2021 IEEE Winter Conference on Applications of Computer Vision WA'21*) **Representation Learning with Statistical Independence to Mitigate Bias**
  [[📝 Paper](https://doi.org/10.1109/wacv48630.2021.00256)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: In-processing` · `Attributes: Age + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Adversarial Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*ArXiv 2021'21*) **Technical Challenges for Training Fair Neural Networks**
  [[📝 Paper](https://arxiv.org/abs/2102.06764)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Age + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Adversarial Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Nature Medicine'21*) **Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations**
  [[📝 Paper](https://doi.org/10.1038/s41591-021-01595-0)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Age + Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Unfairness Existence. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

### 2020

- (*2020 IEEE/CVF Conference on Computer Vision and Pattern Recogniti'20*) **Debiasing skin lesion datasets and models? Not so fast**
  [[📝 Paper](https://doi.org/10.1109/cvprw50498.2020.00378)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-harmonization. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Lecture Notes in Computer Science'20*) **Fairness of Classifiers Across Skin Tones in Dermatology**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-59725-2_31)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation + Pre-processing` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness & Data Distribution. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Proceedings of the National Academy of Sciences'20*) **Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis**
  [[📝 Paper](https://doi.org/10.1073/pnas.1919012117)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Benchmark + Evaluation` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Fairness & Data Distribution. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*MICCAI-DART 2020'20*) **On the fairness of privacy-preserving representations in medical applications**
  [[📝 Paper](https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation` · `Stage: In-processing` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Legacy unverified`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Disentanglement Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md)

- (*Lecture Notes in Computer Science'20*) **Risk of Training Diagnostic Algorithms on Data with Demographic Bias**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-61166-8_20)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: Evaluation + In-processing` · `Attributes: Age + Sex and gender` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Adversarial Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2) · [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Nature Machine Intelligence'20*) **Shortcut learning in deep neural networks**
  [[📝 Paper](https://doi.org/10.1038/s42256-020-00257-z)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Shortcut learning, models recognizing sensitive patient attributes, and fairness in medical AI. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

- (*Nature Communications'20*) **Training confounder-free deep learning models for medical applications**
  [[📝 Paper](https://doi.org/10.1038/s41467-020-19784-9)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Age + Sex and gender` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Adversarial Learning. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [Original catalog](https://github.com/XuZikang/Awesome-MedIA-Fairness/blob/main/docs/legacy-catalog.md) · [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

### 2019

- (*2019 IEEE/CVF Conference on Computer Vision and Pattern Recogniti'19*) **(De) Constructing bias on skin lesion datasets**
  [[📝 Paper](https://doi.org/10.1109/cvprw.2019.00335)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Mitigation` · `Stage: Pre-processing` · `Attributes: Skin tone` · `Assets: Paper only` · `Evidence: Primary metadata`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: UM-pre-harmonization. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [2024 review](https://www.nature.com/articles/s41746-024-01276-5/tables/2)

- (*Science'19*) **Dissecting racial bias in an algorithm used to manage the health of populations**
  [[📝 Paper](https://doi.org/10.1126/science.aax2342)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary abstract`
  > **Why it qualifies:** Reference-listed medical fairness work; source category: Seminal works on AI fairness. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.
  > **Provenance:** [FAIMI](https://faimi-workshop.github.io/resources/)

## 🧭 By Topic

> A complementary index; a paper may appear in multiple topics.

### Fairness Evaluation and Benchmarking

- (*Medical Image Analysis'26*) **Rethinking fairness in medical imaging: Maximizing group-specific performance with application to skin disease diagnosis**
  [[📝 Paper](https://doi.org/10.1016/j.media.2026.103950)]

- (*European Heart Journal - Digital Health'25*) **An investigation into the causes of race bias in artificial intelligence–based cine cardiac magnetic resonance segmentation**
  [[📝 Paper](https://doi.org/10.1093/ehjdh/ztaf008)]

- (*Scientific Reports'25*) **An investigation of race bias in deep learning-based segmentation of prostate MRI images**
  [[📝 Paper](https://doi.org/10.1038/s41598-025-26189-5)]

- (*eBioMedicine'25*) **Where, why, and how is bias learned in medical image analysis models? A study of bias encoding within convolutional networks using synthetic data**
  [[📝 Paper](https://doi.org/10.1016/j.ebiom.2024.105501)]

- (*Nature Medicine'24*) **Demographic bias in misdiagnosis by computational pathology models**
  [[📝 Paper](https://doi.org/10.1038/s41591-024-02885-z)]

- (*Scientific Reports'24*) **Fair AI-powered orthopedic image segmentation: addressing bias and promoting equitable healthcare**
  [[📝 Paper](https://doi.org/10.1038/s41598-024-66873-6)]

- (*NeurIPS Datasets and Benchmarks'24*) **FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models**
  [[📝 Paper](https://arxiv.org/abs/2407.00983)] [[💻 Code](https://github.com/FairMedFM/FairMedFM)]

- (*ICLR'24*) **FairSeg: A Large-Scale Medical Image Segmentation Dataset for Fairness Learning Using Segment Anything Model with Fair Error-Bound Scaling**
  [[📝 Paper](https://arxiv.org/abs/2311.02189)] [[💻 Code](https://github.com/Harvard-Ophthalmology-AI-Lab/FairSeg)]

- (*Lecture Notes in Computer Science'24*) **Slicing Through Bias: Explaining Performance Gaps in Medical Image Analysis Using Slice Discovery Methods**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-72787-0_1)]

- (*Computer Methods and Programs in Biomedicine'24*) **Understanding skin color bias in deep learning-based skin lesion segmentation**
  [[📝 Paper](https://doi.org/10.1016/j.cmpb.2024.108044)]

- (*JAMA Network Open'23*) **Algorithmic Fairness of Machine Learning Models for Alzheimer Disease Progression**
  [[📝 Paper](https://doi.org/10.1001/jamanetworkopen.2023.42203)]

- (*eBioMedicine'23*) **Algorithmic encoding of protected characteristics in chest X-ray disease detection models**
  [[📝 Paper](https://doi.org/10.1016/j.ebiom.2023.104467)]

- (*Lecture Notes in Computer Science'23*) **An Investigation into Race Bias in Random Forest Models Based on Breast DCE-MRI Derived Radiomics Features**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_22)]

- (*Lecture Notes in Computer Science'23*) **An Investigation into the Impact of Deep Learning Model Choice on Sex and Race Bias in Cardiac MR Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_21)]

- (*Lecture Notes in Computer Science'23*) **Are sex-based physiological differences the cause of gender bias for chest X-ray diagnosis?**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_14)]

- (*Lecture Notes in Computer Science'23*) **Auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_17)]

- (*Lecture Notes in Computer Science'23*) **Bias in unsupervised anomaly detection in brain MRI**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_12)]

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **Detecting shortcuts in medical images-a case study in chest x-rays**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230572)]

- (*Review-listed'23*) **Evaluating the fairness of deep learning uncertainty estimates in medical image analysis**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR12)]

- (*Cancers'23*) **From Head and Neck Tumour and Lymph Node Segmentation to Survival Prediction on PET/CT: An End-to-End Framework Featuring Uncertainty, Fairness, and Multi-Region Multi-Modal Radiomics**
  [[📝 Paper](https://doi.org/10.3390/cancers15071932)]

- (*ArXiv 2023'23*) **Harvard Glaucoma Fairness: A Retinal Nerve Disease Dataset for Fairness Learning and Fair Identity Normalization**
  [[📝 Paper](https://arxiv.org/abs/2306.09264)] [[💻 Code](https://github.com/luoyan407/Harvard-GF)] [[📊 Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A4XMO1)]

- (*Alzheimers Research &amp Therapy'23*) **Higher performance for women than men in MRI-based Alzheimer’s disease detection**
  [[📝 Paper](https://doi.org/10.1186/s13195-023-01225-6)]

- (*Science'23*) **Implications of predicting race variables from medical images**
  [[📝 Paper](https://doi.org/10.1126/science.adh4260)]

- (*ICLR 2023'23*) **MEDFAIR: Benchmarking Fairness for Medical Imaging**
  [[📝 Paper](https://arxiv.org/abs/2210.01725)] [[💻 Code](https://github.com/ys-zong/MEDFAIR)]

- (*IPMI 2023'23*) **On Fairness of Medical Image Classification with Multiple Sensitive Attributes via Learning Orthogonal Representations**
  [[📝 Paper](https://arxiv.org/abs/2301.01481)]

- (*Lecture Notes in Computer Science'23*) **Revisiting skin tone fairness in dermatological lesion classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_24)]

- (*Radiology Artificial Intelligence'23*) **Risk of Bias in Chest Radiography Deep Learning Foundation                     Models**
  [[📝 Paper](https://doi.org/10.1148/ryai.230060)]

- (*Lecture Notes in Computer Science'23*) **The role of subgroup separability in group-fair medical image classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-43898-1_18)]

- (*Lecture Notes in Computer Science'23*) **Towards Unraveling Calibration Biases in Medical Image Analysis**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_13)]

- (*Lecture Notes in Computer Science'23*) **Unsupervised Bias Discovery in Medical Image Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_26)]

- (*Lecture Notes in Computer Science'23*) **Unveiling Fairness Biases in Deep Learning-Based Brain MRI Reconstruction**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_10)]

- (*Review-listed'23*) **Visualizing chest X-ray dataset biases using GANs**
  [[📝 Paper](https://openreview.net/forum?id=bFb3V8ALx4W)]

- (*Lecture Notes in Computer Science'22*) **A Study of Demographic Bias in CNN-Based Brain MR Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-17899-3_2)]

- (*Lecture Notes in Computer Science'22*) **A Systematic Study of Race and Sex Bias in CNN-Based Cardiac MR Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-23443-9_22)]

- (*The Lancet Digital Health'22*) **AI recognition of patient race in medical imaging: a modelling study**
  [[📝 Paper](https://doi.org/10.1016/s2589-7500(22)00063-2)]

- (*ArXiv 2022'22*) **Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)**
  [[📝 Paper](https://doi.org/10.1038/s41467-023-39902-7)]

- (*FAIMI-listed'22*) **Diagnosing failures of fairness transfer across distribution shift in real-world medical settings**
  [[📝 Paper](https://arxiv.org/abs/2202.01034)]

- (*Science Advances'22*) **Disparities in dermatology AI performance on a diverse, curated clinical image set**
  [[📝 Paper](https://doi.org/10.1126/sciadv.abq6147)]

- (*Frontiers in Cardiovascular Medicine'22*) **Fairness in Cardiac Magnetic Resonance Imaging: Assessing Sex and Racial Bias in Deep Learning-Based Segmentation**
  [[📝 Paper](https://doi.org/10.3389/fcvm.2022.859310)]

- (*Journal of Medical Imaging'22*) **Fairness-related performance and explainability effects in deep learning models for brain image analysis**
  [[📝 Paper](https://doi.org/10.1117/1.jmi.9.6.061102)]

- (*Lecture Notes in Computer Science'22*) **Feature Robustness and Sex Differences in Medical Imaging: A Case Study in MRI-Based Alzheimer’s Disease Detection**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16431-6_9)]

- (*MLHC'22*) **How fair is your graph? exploring fairness concerns in neuroimaging studies**
  [[📝 Paper](https://proceedings.mlr.press/v182/ribeiro22a.html)]

- (*PCHIL 2022'22*) **Improving the Fairness of Chest X-ray Classifiers**
  [[📝 Paper](https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf)]

- (*ArXiv 2021'21*) **AI Fairness via Domain Adaptation**
  [[📝 Paper](https://arxiv.org/abs/2104.01109)]

- (*Translational Vision Science &amp Technology'21*) **Addressing Artificial Intelligence Bias in Retinal Diagnostics**
  [[📝 Paper](https://doi.org/10.1167/tvst.10.2.13)]

- (*ArXiv 2021'21*) **Algorithmic encoding of protected characteristics in image-based models for disease detection**
  [[📝 Paper](https://arxiv.org/abs/2110.14755)]

- (*Proceedings of the Pacific Symposium 2021'21*) **CheXclusion: Fairness gaps in deep chest X-ray classifiers**
  [[📝 Paper](https://pubmed.ncbi.nlm.nih.gov/33691020/)]

- (*MICCAI-DART 2021'21*) **Detecting Melanoma Fairly: Skin Tone Detection and Debiasing for Skin Lesion Classification**
  [[📝 Paper](https://arxiv.org/abs/2202.02832)] [[💻 Code](https://github.com/pbevan1/Detecting-Melanoma-Fairly)]

- (*ArXiv 2021'21*) **Evaluating subgroup disparity using epistemic uncertainty in mammography**
  [[📝 Paper](https://arxiv.org/abs/2107.02716)]

- (*Lecture Notes in Computer Science'21*) **Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-87199-4_39)]

- (*ArXiv 2021'21*) **Model Selection's Disparate Impact in Real-World Deep Learning Applications**
  [[📝 Paper](https://arxiv.org/abs/2104.00606)]

- (*Lecture Notes in Computer Science'21*) **On the Fairness of Swarm Learning in Skin Lesion Classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-90874-4_12)]

- (*ArXiv 2021'21*) **RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR**
  [[📝 Paper](https://arxiv.org/abs/2111.11665)]

- (*Emergency Radiology'21*) **Radiology “forensics”: determination of age and sex from chest radiographs using deep learning**
  [[📝 Paper](https://doi.org/10.1007/s10140-021-01953-y)]

- (*ArXiv 2021'21*) **Technical Challenges for Training Fair Neural Networks**
  [[📝 Paper](https://arxiv.org/abs/2102.06764)]

- (*Nature Medicine'21*) **Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations**
  [[📝 Paper](https://doi.org/10.1038/s41591-021-01595-0)]

- (*Lecture Notes in Computer Science'20*) **Fairness of Classifiers Across Skin Tones in Dermatology**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-59725-2_31)]

- (*Proceedings of the National Academy of Sciences'20*) **Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis**
  [[📝 Paper](https://doi.org/10.1073/pnas.1919012117)]

- (*MICCAI-DART 2020'20*) **On the fairness of privacy-preserving representations in medical applications**
  [[📝 Paper](https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170)]

- (*Lecture Notes in Computer Science'20*) **Risk of Training Diagnostic Algorithms on Data with Demographic Bias**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-61166-8_20)]

- (*Nature Machine Intelligence'20*) **Shortcut learning in deep neural networks**
  [[📝 Paper](https://doi.org/10.1038/s42256-020-00257-z)]

- (*Nature Communications'20*) **Training confounder-free deep learning models for medical applications**
  [[📝 Paper](https://doi.org/10.1038/s41467-020-19784-9)]

- (*Science'19*) **Dissecting racial bias in an algorithm used to manage the health of populations**
  [[📝 Paper](https://doi.org/10.1126/science.aax2342)]

### Bias Mechanisms and Measurement

- (*European Heart Journal - Digital Health'25*) **An investigation into the causes of race bias in artificial intelligence–based cine cardiac magnetic resonance segmentation**
  [[📝 Paper](https://doi.org/10.1093/ehjdh/ztaf008)]

- (*Machine Learning for Biomedical Imaging'25*) **Understanding-informed Bias Mitigation for Fair CMR Segmentation**
  [[📝 Paper](https://doi.org/10.59275/j.melba.2025-6747)]

- (*eBioMedicine'25*) **Where, why, and how is bias learned in medical image analysis models? A study of bias encoding within convolutional networks using synthetic data**
  [[📝 Paper](https://doi.org/10.1016/j.ebiom.2024.105501)]

- (*Lecture Notes in Computer Science'24*) **Slicing Through Bias: Explaining Performance Gaps in Medical Image Analysis Using Slice Discovery Methods**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-72787-0_1)]

- (*Computer Methods and Programs in Biomedicine'24*) **Understanding skin color bias in deep learning-based skin lesion segmentation**
  [[📝 Paper](https://doi.org/10.1016/j.cmpb.2024.108044)]

- (*eBioMedicine'23*) **Algorithmic encoding of protected characteristics in chest X-ray disease detection models**
  [[📝 Paper](https://doi.org/10.1016/j.ebiom.2023.104467)]

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **Detecting shortcuts in medical images-a case study in chest x-rays**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230572)]

- (*Science'23*) **Implications of predicting race variables from medical images**
  [[📝 Paper](https://doi.org/10.1126/science.adh4260)]

- (*The Lancet Digital Health'22*) **AI recognition of patient race in medical imaging: a modelling study**
  [[📝 Paper](https://doi.org/10.1016/s2589-7500(22)00063-2)]

- (*ArXiv 2022'22*) **Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)**
  [[📝 Paper](https://doi.org/10.1038/s41467-023-39902-7)]

- (*ArXiv 2021'21*) **Algorithmic encoding of protected characteristics in image-based models for disease detection**
  [[📝 Paper](https://arxiv.org/abs/2110.14755)]

- (*Emergency Radiology'21*) **Radiology “forensics”: determination of age and sex from chest radiographs using deep learning**
  [[📝 Paper](https://doi.org/10.1007/s10140-021-01953-y)]

- (*Nature Machine Intelligence'20*) **Shortcut learning in deep neural networks**
  [[📝 Paper](https://doi.org/10.1038/s42256-020-00257-z)]

### Pre-processing Mitigation

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **A comparative study of fairness in medical machine learning**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230368)]

- (*Proceedings of the National Academy of Sciences'23*) **Bias in machine learning models can be significantly mitigated by careful training: Evidence from neuroimaging studies**
  [[📝 Paper](https://doi.org/10.1073/pnas.2211613120)]

- (*Lecture Notes in Computer Science'23*) **CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-25069-9_14)] [[💻 Code](https://github.com/sfu-mial/CIRCLe)]

- (*Lecture Notes in Computer Science'23*) **De-identification and obfuscation of gender attributes from retinal scans**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_9)]

- (*Lecture Notes in Computer Science'23*) **EdgeMixup: embarrassingly simple data alteration to improve Lyme disease lesion segmentation and diagnosis fairness**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-43901-8_36)]

- (*Medical Image Analysis'23*) **Equitable modelling of brain imaging by counterfactual augmentation with morphologically constrained 3D deep generative models**
  [[📝 Paper](https://doi.org/10.1016/j.media.2022.102723)]

- (*ArXiv 2022'22*) **Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)**
  [[📝 Paper](https://doi.org/10.1038/s41467-023-39902-7)]

- (*NeurIPS Workshop 2022'22*) **Improving fairness in image classification via sketching**
  [[📝 Paper](https://openreview.net/forum?id=Rq2vt3tnAK9)] [[💻 Code](https://github.com/ubc-tea/Improving-Fairness-in-Image-Classification-via-Sketching)]

- (*ArXiv 2021'21*) **AI Fairness via Domain Adaptation**
  [[📝 Paper](https://arxiv.org/abs/2104.01109)]

- (*Translational Vision Science &amp Technology'21*) **Addressing Artificial Intelligence Bias in Retinal Diagnostics**
  [[📝 Paper](https://doi.org/10.1167/tvst.10.2.13)]

- (*Proceedings of the Pacific Symposium 2021'21*) **CheXclusion: Fairness gaps in deep chest X-ray classifiers**
  [[📝 Paper](https://pubmed.ncbi.nlm.nih.gov/33691020/)]

- (*Medical Image Analysis'21*) **Detect and correct bias in multi-site neuroimaging datasets**
  [[📝 Paper](https://doi.org/10.1016/j.media.2020.101879)]

- (*Lecture Notes in Computer Science'21*) **Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-87199-4_39)]

- (*ArXiv 2021'21*) **RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR**
  [[📝 Paper](https://arxiv.org/abs/2111.11665)]

- (*2020 IEEE/CVF Conference on Computer Vision and Pattern Recogniti'20*) **Debiasing skin lesion datasets and models? Not so fast**
  [[📝 Paper](https://doi.org/10.1109/cvprw50498.2020.00378)]

- (*Lecture Notes in Computer Science'20*) **Fairness of Classifiers Across Skin Tones in Dermatology**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-59725-2_31)]

- (*2019 IEEE/CVF Conference on Computer Vision and Pattern Recogniti'19*) **(De) Constructing bias on skin lesion datasets**
  [[📝 Paper](https://doi.org/10.1109/cvprw.2019.00335)]

### In-processing Mitigation

- (*Review-listed'24*) **Fairtune: Optimizing parameter efficient fine tuning for fairness in medical image analysis**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR89)]

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **A comparative study of fairness in medical machine learning**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230368)]

- (*Lecture Notes in Computer Science'23*) **CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-25069-9_14)] [[💻 Code](https://github.com/sfu-mial/CIRCLe)]

- (*ArXiv 2023'23*) **FairAdaBN: Mitigating unfairness with adaptive batch normalization and its application to dermatological disease classification**
  [[📝 Paper](https://arxiv.org/abs/2303.08325)]

- (*Nature Communications'23*) **Improving model fairness in image-based computer-aided diagnosis**
  [[📝 Paper](https://doi.org/10.1038/s41467-023-41974-4)]

- (*IPMI 2023'23*) **On Fairness of Medical Image Classification with Multiple Sensitive Attributes via Learning Orthogonal Representations**
  [[📝 Paper](https://arxiv.org/abs/2301.01481)]

- (*Lecture Notes in Computer Science'22*) **A Penalty Approach for Normalizing Feature Distributions to Build Confounder-Free Models**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16437-8_37)]

- (*Lecture Notes in Computer Science'22*) **Conditional VAEs for confound removal and normative modelling of neurodegenerative diseases**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16431-6_41)]

- (*Lecture Notes in Computer Science'22*) **Disproportionate subgroup impacts and other challenges of fairness in artificial intelligence for medical image analysis**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-23223-7_2)]

- (*ECCVW 2022'22*) **FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning**
  [[📝 Paper](https://arxiv.org/abs/2208.10013)] [[💻 Code](https://github.com/siyi-wind/FairDisCo)]

- (*Review-listed'22*) **Fairness by learning orthogonal disentangled representations**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR83)]

- (*Lecture Notes in Computer Science'22*) **Pseudo bias-balanced learning for debiased chest x-ray classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16452-1_59)]

- (*Review-listed'22*) **Rényi fair information bottleneck for image classification**
  [[📚 Reference listing](https://www.nature.com/articles/s41746-024-01276-5#ref-CR121)]

- (*Lecture Notes in Computer Science'21*) **Confound removal and normalization in practice: a neuroimaging based sex prediction case study**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-67670-4_1)]

- (*MICCAI-DART 2021'21*) **Detecting Melanoma Fairly: Skin Tone Detection and Debiasing for Skin Lesion Classification**
  [[📝 Paper](https://arxiv.org/abs/2202.02832)] [[💻 Code](https://github.com/pbevan1/Detecting-Melanoma-Fairly)]

- (*ArXiv 2021'21*) **Estimating and improving fairness with adversarial learning**
  [[📝 Paper](https://oecd.ai/fr/catalogue/metric-use-cases/estimating-and-improving-fairness-with-adversarial-learning)]

- (*Lecture Notes in Computer Science'21*) **Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-87199-4_39)]

- (*Lecture Notes in Computer Science'21*) **On the Fairness of Swarm Learning in Skin Lesion Classification**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-90874-4_12)]

- (*2021 IEEE Winter Conference on Applications of Computer Vision WA'21*) **Representation Learning with Statistical Independence to Mitigate Bias**
  [[📝 Paper](https://doi.org/10.1109/wacv48630.2021.00256)]

- (*ArXiv 2021'21*) **Technical Challenges for Training Fair Neural Networks**
  [[📝 Paper](https://arxiv.org/abs/2102.06764)]

- (*MICCAI-DART 2020'20*) **On the fairness of privacy-preserving representations in medical applications**
  [[📝 Paper](https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170)]

- (*Lecture Notes in Computer Science'20*) **Risk of Training Diagnostic Algorithms on Data with Demographic Bias**
  [[📝 Paper](https://doi.org/10.1007/978-3-030-61166-8_20)]

- (*Nature Communications'20*) **Training confounder-free deep learning models for medical applications**
  [[📝 Paper](https://doi.org/10.1038/s41467-020-19784-9)]

### Post-processing Mitigation

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **A comparative study of fairness in medical machine learning**
  [[📝 Paper](https://doi.org/10.1109/isbi53787.2023.10230368)]

- (*Lecture Notes in Computer Science'23*) **Mitigating bias in MRI-based Alzheimer’s disease classifiers through pruning of deep neural networks**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-45249-9_16)]

- (*ML4HC 2022'22*) **Debiasing Deep Chest X-Ray Classifiers using Intra- and Post-processing Methods**
  [[📝 Paper](https://proceedings.mlr.press/v182/marcinkevics22a.html)] [[💻 Code](https://github.com/i6092467/diff-bias-proxies)]

- (*Lecture Notes in Computer Science'22*) **FairPrune: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis**
  [[📝 Paper](https://doi.org/10.1007/978-3-031-16431-6_70)]

### Clinical NLP and Foundation Models

### EHR, Physiological Signals and Healthcare

- (*ArXiv 2021'21*) **RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR**
  [[📝 Paper](https://arxiv.org/abs/2111.11665)]

- (*Science'19*) **Dissecting racial bias in an algorithm used to manage the health of populations**
  [[📝 Paper](https://doi.org/10.1126/science.aax2342)]

### Mitigation with Unverified Stage

- (*Machine Learning for Biomedical Imaging'25*) **Understanding-informed Bias Mitigation for Fair CMR Segmentation**
  [[📝 Paper](https://doi.org/10.59275/j.melba.2025-6747)]

- (*ICLR 2023'23*) **MEDFAIR: Benchmarking Fairness for Medical Imaging**
  [[📝 Paper](https://arxiv.org/abs/2210.01725)] [[💻 Code](https://github.com/ys-zong/MEDFAIR)]

- (*PCHIL 2022'22*) **Improving the Fairness of Chest X-ray Classifiers**
  [[📝 Paper](https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf)]

## 🧰 Datasets, Benchmarks and Toolkits

### Datasets

| Resource | Fairness context | Access and limitations |
|---|---|---|
| **[DDI](https://ddi-dataset.github.io/)** | Dermatology and skin-tone evaluation | Follow the original dataset's access terms and annotations. |
| **[Fitzpatrick17k](https://github.com/mattgroh/fitzpatrick17k)** | Dermatology, skin-tone labels | Label reliability and skin-tone estimation are themselves audit questions. |
| **[Harvard Glaucoma Fairness](https://github.com/luoyan407/Harvard-GF)** | Ophthalmology and protected-group benchmarking | [Dataset landing page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A4XMO1). |
| **[Harvard FairSeg](https://ophai.hms.harvard.edu/datasets/harvard-fairseg10k/)** | Ophthalmic segmentation fairness | Check the authors' current data-access requirements. |
| **[CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/)** | Chest radiograph subgroup auditing | Demographic fields, patient splits and label uncertainty must be checked. |
| **[MIMIC-CXR](https://physionet.org/content/mimic-cxr/)** | Chest radiographs linked to clinical context | Credentialed access; do not redistribute patient records. |
| **[ADNI](https://adni.loni.usc.edu/)** | Neuroimaging, age/sex/race analyses | Application-based access and cohort selection constraints. |
| **[UK Biobank](https://www.ukbiobank.ac.uk/)** | Population imaging and demographic analyses | Approved research access; representativeness is not guaranteed. |

### Benchmarks

| Resource | Scope | Access |
|---|---|---|
| **MEDFAIR** | Multi-dataset fairness evaluation and mitigation | [Official code](https://github.com/ys-zong/MEDFAIR) |
| **FairMedFM** | Medical imaging foundation-model fairness | [Official code](https://github.com/FairMedFM/FairMedFM) |
| **CXR-Fairness** | Chest X-ray group metrics and mitigation | [Primary paper](https://proceedings.mlr.press/v174/zhang22a.html) |

### Toolkits

| Toolkit | Purpose | Access |
|---|---|---|
| **Fairlearn** | Group metrics and mitigation tooling | [Project](https://fairlearn.org/) |
| **AI Fairness 360** | Fairness metrics and mitigation implementations | [Official code](https://github.com/Trusted-AI/AIF360) |
| **Aequitas** | Bias and fairness auditing | [Project](https://github.com/dssg/aequitas) |

These resources are entry points, not claims that one metric or mitigation method is clinically sufficient.

## 🔗 Related Repositories

- [MEDFAIR](https://github.com/ys-zong/MEDFAIR)
- [FairMedFM](https://github.com/FairMedFM/FairMedFM)
- [AI Fairness 360](https://github.com/Trusted-AI/AIF360)

## 🔀 Cross-References

General fairness theory supports the medical literature but is not counted as medical empirical evidence:

- [Equality of Opportunity in Supervised Learning](https://dl.acm.org/doi/10.5555/3157382.3157469) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments](https://www.liebertpub.com/doi/10.1089/big.2016.0047) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification](https://proceedings.mlr.press/v81/buolamwini18a.html) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Fairness and Machine Learning: Limitations and Opportunities](https://fairmlbook.org/index.html) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [The Problem of Infra-Marginality in Outcome Tests for Discrimination](https://dx.doi.org/10.2139/ssrn.2811449) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness](https://proceedings.mlr.press/v80/kearns18a.html) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Unlocking Fairness: a Trade-off Revisited](https://papers.nips.cc/paper/2019/hash/373e4c5d8edfa8b74fd4b6791d0cf6dc-Abstract.html) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Is There a Trade-Off Between Fairness and Accuracy? A Perspective Using Mismatched Hypothesis Testing](https://proceedings.mlr.press/v119/dutta20a.html) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [On Testing and Comparing Fair classifiers under Data Bias](https://arxiv.org/abs/2302.05906) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [A Possibility in Algorithmic Fairness: Can Calibration and Equal Error Rates be Reconciled?](https://drops.dagstuhl.de/opus/volltexte/2021/13872/) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Bias Preservation in Machine Learning: The Legality of Fairness Metrics Under EU Non-Discrimination Law](https://dx.doi.org/10.2139/ssrn.3792772) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [The Unfairness of Fair Machine Learning: Levelling Down and Strict Egalitarianism by Default](https://ssrn.com/abstract=4331652) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Confounding Factors Need to be Accounted for in Assessing Bias by Machine Learning Algorithms](https://doi.org/10.1038/s41591-022-01847-7) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [Inherent Tradeoffs in Learning Fair Representations](https://jmlr.org/papers/v23/21-1427.html) · source: [FAIMI](https://faimi-workshop.github.io/resources/)
- [On (Assessing) the Fairness of Risk Score Models](https://doi.org/10.1145/3593013.3594045) · source: [FAIMI](https://faimi-workshop.github.io/resources/)

## 📣 Community and Calls

- [FAIMI](https://faimi-workshop.github.io/) · [Resources](https://faimi-workshop.github.io/resources/)
- [FAIMI 2023–2026 programme leads](docs/workshop-candidates.md): official listings are discovery leads, not independent publication or scope verification.

## ⚖️ License

New catalog annotations and documentation: [CC BY 4.0](LICENSE-CONTENT). Automation code: [MIT](LICENSE). Referenced papers, source-site annotations and original illustrations retain their own rights; the legacy list is preserved with attribution.

## 📖 Citation

Please cite the [2024 systematic review](https://doi.org/10.1038/s41746-024-01276-5) when using its taxonomy or literature analysis, and use [CITATION.cff](CITATION.cff) for this maintained catalog.

## 🤝 Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Provide a primary source, medical task, algorithm, fairness question, group definition and evaluated evidence. Source-list membership alone is not a scientific quality guarantee.

## ✉️ Contact

Zikang Xu · zikangxu@mail.ustc.edu.cn
