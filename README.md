# Awesome-MedIA-Fairness

A collection of research on **medical algorithm fairness**, covering medical imaging, clinical prediction, physiological signals and clinical foundation models.

[![Catalog validation](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/validate-catalog.yml/badge.svg)](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/validate-catalog.yml) [![Link health](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/check-links.yml/badge.svg)](https://github.com/XuZikang/Awesome-MedIA-Fairness/actions/workflows/check-links.yml)

**119 papers** · Evaluation & mitigation · Human-reviewed additions

**Browse:** [Papers](#-papers) · [Taxonomy](#-taxonomy) · [Resources](#-datasets-benchmarks-and-toolkits) · [Weekly review](reports/review-latest.md) · [Contributing](#-contributing)

<details>
<summary>Scope and inclusion criteria</summary>

Studies must address algorithmic fairness, subgroup disparities, bias mechanisms, fairness measurement or mitigation in a medical task. Negative findings are eligible. Predicting a protected attribute does not by itself establish downstream discrimination. General fairness foundations are listed separately.

Original methodology and empirical fairness audits take priority. New reviews and commentaries must analyze fairness in a specific medical disease or task in depth; incidental mentions of bias, ethics or fairness are insufficient. See the [screening policy](docs/screening-policy.md).

</details>

## 🧬 Taxonomy

The methodology follows [Addressing fairness issues in deep learning-based medical image analysis: a systematic review](https://doi.org/10.1038/s41746-024-01276-5). Surveys and empirical studies share the same taxonomy; surveys carry an additional badge.

| Method | Definition |
|---|---|
| ![Fairness Evaluation](assets/badges/fairness-evaluation-fairness-evaluation.svg) | Benchmarking, subgroup comparisons, bias source tracing, mechanism discovery and fairness measurement. |
| ![Pre-processing](assets/badges/pre-processing-pre-processing.svg) | Interventions on training data, sampling, augmentation or data transformation. |
| ![In-processing](assets/badges/in-processing-in-processing.svg) | Interventions on learning objectives, representations, model training or optimization. |
| ![Post-processing](assets/badges/post-processing-post-processing.svg) | Interventions after model training, such as output adjustment, calibration or reviewed model adaptation; predictor freezing must be established from the specific protocol. |

`Stage pending` is an evidence-status bucket for mitigation records whose intervention stage is not yet established, not an additional methodology. Within each category, records run newest to oldest. The latest catalog year is divided by month; missing months remain explicitly unverified. Dates retain the precision supplied by the original record, rather than the discovery date.

<details>
<summary>Tag legend — Domain · Focus · Stage · Attributes · Assets</summary>

| Field | Controlled values |
|---|---|
| **Domain** | ![Clinical NLP and foundation models](assets/badges/domain-clinical-nlp-and-foundation-models.svg) ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) ![Healthcare operations](assets/badges/domain-healthcare-operations.svg) ![Medical imaging](assets/badges/domain-medical-imaging.svg) ![Other biomedical](assets/badges/domain-other-biomedical.svg) ![Physiological signals](assets/badges/domain-physiological-signals.svg) |
| **Focus** | ![Benchmark](assets/badges/focus-benchmark.svg) ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Dataset](assets/badges/focus-dataset.svg) ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) ![Theory and measurement](assets/badges/focus-theory-and-measurement.svg) |
| **Stage** | ![Evaluation](assets/badges/stage-evaluation.svg) ![In-processing](assets/badges/in-processing-in-processing.svg) ![Multi-stage](assets/badges/stage-multi-stage.svg) ![Not applicable](assets/badges/stage-not-applicable.svg) ![Not verified](assets/badges/stage-not-verified.svg) ![Post-processing](assets/badges/post-processing-post-processing.svg) ![Pre-processing](assets/badges/pre-processing-pre-processing.svg) |
| **Attributes** | ![Age](assets/badges/attributes-age.svg) ![Disability](assets/badges/attributes-disability.svg) ![Intersectional](assets/badges/attributes-intersectional.svg) ![Not specified](assets/badges/attributes-not-specified.svg) ![Other](assets/badges/attributes-other.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Site and geography](assets/badges/attributes-site-and-geography.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) ![Socioeconomic status](assets/badges/attributes-socioeconomic-status.svg) |
| **Assets** | ![Code](assets/badges/assets-code.svg) ![Data](assets/badges/assets-data.svg) ![Paper only](assets/badges/assets-paper-only.svg) ![Project](assets/badges/assets-project.svg) ![Weights](assets/badges/assets-weights.svg) |

</details>

## 📝 Papers

Browse by methodology below. The latest year is expanded and grouped by month; expand an earlier year to read its papers. Tags below each title describe the domain, focus, stage, attributes and available assets.

| Methodology | Papers | Latest records |
|---|---:|---|
| [Fairness Evaluation](#fairness-evaluation) | 78 | 2026-11-03 |
| [Pre-processing](#unfairness-mitigation-pre-processing) | 14 | 2026-03 |
| [In-processing](#unfairness-mitigation-in-processing) | 22 | 2024 |
| [Post-processing](#unfairness-mitigation-post-processing) | 5 | 2026-11-07 |

### Fairness Evaluation

#### 2026

##### 2026-11

- (*Archives of Sexual Behavior'26*) **Visual Sexual Health Communication Assisted by AI: The Case of Synthetic Menstruation Images.**

  **Domain:** ![Other biomedical](assets/badges/domain-other-biomedical.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) ![Other](assets/badges/attributes-other.svg) · **Assets:** ![Project](assets/badges/assets-project.svg)

  [[Paper](https://doi.org/10.1007/s10508-026-03518-x)] [[Project](https://osf.io/h5pn3/)]

  **TLDR:** This study audits representational diversity and stereotypical depictions in AI-generated images for menstrual health communication. It manually codes 600 outputs from 15 generators using a reliability-tested codebook across prompts in two languages. The authors report frequent visual flaws and limited body-type diversity, while skin-tone diversity is not similarly restricted and stereotypical portrayals are not predominant.

  **Date:** 2026-11-03

- (*Archives of Orthopaedic and Trauma Surgery'26*) **Skin color representation in orthopedic literature.**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Dataset](assets/badges/focus-dataset.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/42975702/)]

  **TLDR:** This study audits skin-color representation in images from open-access orthopedic journals. It uses a GPT-4o labeling pipeline with human agreement checks to analyze skin presence, figure type and Fitzpatrick skin type across subspecialties. The abstract reports substantial underrepresentation of darker skin; this is an audit of educational-image representation rather than a test of clinical prediction-model fairness.

  **Date:** 2026-11-03

- (*arXiv'26*) **Fairness Metrics based on the AUC in Clinical Predictive AI**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Theory and measurement](assets/badges/focus-theory-and-measurement.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2611.05222)]

  **TLDR:** This study examines how AUC-based fairness metrics should be interpreted in clinical prediction. It characterizes eight metrics through within-group and cross-group AUC decomposition and illustrates their behavior using EuroSCORE II-based simulations. The analysis highlights that subgroup and overall AUC are not directly comparable in the way some fairness interpretations assume.

  **Date:** 2026-11-03

##### 2026-10

- (*Journal of the American Medical Informatics Association'26*) **Subgroup deployment-readiness audit of calibration and clinical utility in perioperative infection prediction.**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) ![Other](assets/badges/attributes-other.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/42962674/)]

  **TLDR:** This study audits subgroup readiness for deployment of a perioperative infection-prediction model. It evaluates discrimination, calibration, threshold errors and decision-curve utility across sex, age and physiological-reserve strata, comparing recalibration and a refit without SMOTE. The abstract reports that aggregate discrimination can mask subgroup miscalibration and that outcome ascertainment affects utility interpretation, so prospective validation remains necessary.

  **Date:** 2026-10-30

- (*Research Square Preprint'26*) **Explainable Machine Learning for 30-Day Hospital Readmission Risk Prediction in Patients with Diabetes: A Comparative Analysis of Model Performance and Algorithmic Fairness**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.21203/rs.3.rs-11517784/v1)]

  **TLDR:** This study evaluates 30-day readmission prediction for diabetic inpatients and audits demographic differences in recall. It compares logistic regression, decision tree and random forest models on a patient-aware and time-aware split of the UCI diabetes hospital dataset, reporting recall gaps across race, gender and age. The tuned random forest has the highest recall but the largest reported race gap, illustrating a trade-off between overall detection and subgroup performance rather than demonstrating effective fairness mitigation.

  **Date:** 2026-10-28

- (*arXiv'26*) **Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems**

  **Domain:** ![Clinical NLP and foundation models](assets/badges/domain-clinical-nlp-and-foundation-models.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2610.38215)]

  **TLDR:** This study audits demographic disparities in clinical multi-agent language-model systems. It evaluates five model families and four aggregation topologies on emergency cases with counterfactual demographic swaps. The abstract reports that aggregation does not neutralize the disparity and that apparently corrective late-stage interventions can leave it unchanged or amplify it.

  **Date:** 2026-10-28

##### 2026-09

- (*Stroke'26*) **Responsible AI for Acute Stroke Management.**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Socioeconomic status](assets/badges/attributes-socioeconomic-status.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/42751787/)]

  **TLDR:** This review examines explainability and fairness in AI for acute stroke management. It synthesizes evidence across large-vessel occlusion detection, ASPECTS scoring and functional-outcome prediction, including racial and socioeconomic disparities. It identifies limited demographic metadata and missing stroke-specific fairness criteria as barriers and recommends jointly evaluating explainability, fairness and generalizability.

  **Date:** 2026-09-17

- (*Arthroscopy'26*) **Editorial Commentary: Calling Balls and Strikes: For Artificial Intelligence Models to Accurately Predict Rotator Cuff Retear, We Must Carefully Define the Strike Zone.**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Commentary](assets/badges/commentary-commentary.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/42701888/)]

  **TLDR:** This editorial commentary discusses bias and trust in AI prediction of early rotator cuff retear. It examines subjective image labels, interrater reliability and generalization problems associated with models trained on a single surgeon dataset. It argues for clearer labeling and governance standards, but the accessible abstract does not report a protected-group fairness experiment.

  **Date:** 2026-09-06

##### 2026-08

- (*Maturitas'26*) **Sex, gender and artificial intelligence in cardiovascular medicine 4.0.**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Theory and measurement](assets/badges/focus-theory-and-measurement.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/42721913/)]

  **TLDR:** This review examines sex- and gender-related algorithmic bias in cardiovascular AI. It analyzes six interacting bias categories and the risks of binary sex stratification, then proposes an operational framework for gender-aware prompts and responsible AI interaction. The contribution is a task-specific conceptual framework and governance agenda rather than a new quantitative subgroup-performance experiment.

  **Date:** 2026-08-29

##### 2026-07

- (*International Journal of Medical Informatics'26*) **The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/42447641/)]

  **TLDR:** This study audits how mortality-prediction models trained on adults or older children transfer to younger pediatric intensive-care patients. It compares discrimination and calibration across age groups in PIC and MIMIC-IV data and evaluates target-cohort retraining and calibration-only updates. The abstract reports the largest degradation in neonates and shows that target-domain retraining improves discrimination and calibration, whereas calibration-only updating cannot restore discrimination.

  **Date:** 2026-07-09

<details>
<summary>2025 · 5 papers</summary>

#### 2025

- (*Scientific Reports'25*) **An investigation of race bias in deep learning-based segmentation of prostate MRI images**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41598-025-26189-5)]

  **TLDR:** This study tests for race bias in deep learning-based prostate MRI segmentation. It varies White and Black representation across training datasets and evaluates models on matched clinical subjects. The abstract reports the best performance for both groups with race-balanced training and a relationship between training representation and the measured segmentation gap.

  **Date:** 2025-12-06

- (*Journal of the Association of Nurses in AIDS Care'25*) **Assessing Variability in ChatGPT Responses: A Case Study on Simulating Online User Inputs.**

  **Domain:** ![Clinical NLP and foundation models](assets/badges/domain-clinical-nlp-and-foundation-models.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Other](assets/badges/attributes-other.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/40298212/)]

  **TLDR:** This study evaluates demographic differences in ChatGPT responses to HIV counseling questions. It uses structured prompts and simulated first interactions to compare two ChatGPT versions across race, gender and sexual-orientation variables. The abstract reports that some groups received less comprehensive advice and that social determinants and culturally sensitive resources were rarely addressed.

  **Date:** 2025-04-29

- (*npj Digital Medicine'25*) **Bias recognition and mitigation strategies in artificial intelligence healthcare applications**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1038/s41746-025-01503-7)]

  **TLDR:** This review examines the origins of bias in healthcare AI and strategies for recognizing and mitigating it. It discusses stakeholder responsibilities and bias-management activities across the model lifecycle. The central recommendation is to assess bias from conception through deployment and longitudinal surveillance rather than at a single development stage.

  **Date:** 2025-03-11

- (*European Heart Journal - Digital Health'25*) **An investigation into the causes of race bias in artificial intelligence–based cine cardiac magnetic resonance segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1093/ehjdh/ztaf008)]

  **TLDR:** This study investigates the sources of race bias in cine cardiac MRI segmentation. It compares race predictability from images and segmentations and uses interpretability and heart-centered cropping. The abstract reports that non-heart image regions strongly contribute to race recognition, motivating closer examination of the image context used by segmentation models.

  **Date:** 2025-02-24

- (*eBioMedicine'25*) **Where, why, and how is bias learned in medical image analysis models? A study of bias encoding within convolutional networks using synthetic data**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/j.ebiom.2024.105501)]

  **TLDR:** This study investigates where and how medical-image biases are encoded within convolutional networks. It uses synthetic brain MRI with controlled disease, morphology and intensity effects to analyze layer-wise feature encoding. The abstract reports that stronger bias encoding need not imply shortcut use and that intensity-related effects can have a stronger influence than morphological effects.

  **Date:** 2025-01

</details>

<details>
<summary>2024 · 8 papers</summary>

#### 2024

- (*JAMIA Open'24*) **Algorithmic individual fairness and healthcare: a scoping review**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1093/jamiaopen/ooae149)]

  **TLDR:** This scoping review examines algorithmic individual fairness and its use in healthcare. It searches multiple bibliographic databases for fairness metrics, mitigation methods and healthcare applications. It complements group-based fairness analyses by focusing on how algorithms treat comparable individuals.

  **Date:** 2024-12-26

- (*npj Digital Medicine'24*) **Addressing fairness issues in deep learning-based medical image analysis: a systematic review**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1038/s41746-024-01276-5)]

  **TLDR:** This systematic review examines methodological approaches to fairness in deep learning-based medical image analysis. It organizes the literature into fairness evaluation and unfairness mitigation through pre-processing, in-processing and post-processing. The review identifies open methodological and clinical challenges and supplies the organizing framework used by this catalog.

  **Date:** 2024-10-17

- (*Lecture Notes in Computer Science'24*) **Slicing Through Bias: Explaining Performance Gaps in Medical Image Analysis Using Slice Discovery Methods**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-72787-0_1)]

  **TLDR:** This study investigates performance gaps in medical image analysis using slice discovery. Its approach examines data subsets that can reveal failures hidden by aggregate evaluation. The available record identifies bias discovery as the contribution but does not establish the size or causes of the reported gaps.

  **Date:** 2024-10-13

- (*MIDL'24*) **Evaluating the fairness of deep learning uncertainty estimates in medical image analysis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://proceedings.mlr.press/v227/mehta24a.html)]

  **TLDR:** This study evaluates whether fairer medical imaging predictions also have reliable uncertainty estimates. It compares fairness interventions on skin lesion classification, brain tumor segmentation and Alzheimer disease score regression. The abstract reports that improvements in subgroup prediction performance can come at the cost of poorer uncertainty estimates.

  **Date:** 2024-07

- (*Scientific Reports'24*) **Fair AI-powered orthopedic image segmentation: addressing bias and promoting equitable healthcare**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41598-024-66873-6)]

  **TLDR:** This study examines bias in AI-based segmentation of hip and knee bony anatomy. It focuses on plain radiographs and evaluates potential sources of unequal segmentation performance alongside mitigation strategies. The accessible abstract establishes an orthopedic fairness assessment but does not fully specify which intervention stage drives the reported mitigation.

  **Date:** 2024-07-12

- (*NeurIPS Datasets and Benchmarks'24*) **FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://arxiv.org/abs/2407.00983)] [[Code](https://github.com/FairMedFM/FairMedFM)]

  **TLDR:** FairMedFM benchmarks fairness in medical imaging foundation models. It provides a standardized evaluation pipeline across multiple imaging datasets, model families and adaptation strategies. The benchmark makes subgroup fairness comparisons more systematic without implying that one foundation model is universally fair across tasks and populations.

  **Date:** 2024-07-01

- (*Nature Medicine'24*) **Demographic bias in misdiagnosis by computational pathology models**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41591-024-02885-z)]

  **TLDR:** This study examines demographic disparities in computational pathology diagnosis. It evaluates whole-slide classification for breast and lung cancer subtyping and glioma mutation prediction using public and internal data. The abstract reports substantial race-associated AUC gaps across tasks, demonstrating that strong overall pathology performance can coexist with subgroup misdiagnosis disparities.

  **Date:** 2024-04

- (*Computer Methods and Programs in Biomedicine'24*) **Understanding skin color bias in deep learning-based skin lesion segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/j.cmpb.2024.108044)]

  **TLDR:** This study investigates skin-color bias in deep learning-based skin lesion segmentation. It evaluates U-Net-based models using three skin-color grouping approaches, including Fitzpatrick estimates, Individual Typology Angle and manual grouping. The design treats skin-color estimation itself as part of the fairness measurement problem rather than assuming one demographic annotation is definitive.

  **Date:** 2024-03

</details>

<details>
<summary>2023 · 25 papers</summary>

#### 2023

- (*Referenced study'23*) **Visualizing chest X-ray dataset biases using GANs**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://openreview.net/forum?id=bFb3V8ALx4W)]

  **TLDR:** This work investigates biases embedded in chest X-ray datasets. Generative adversarial networks are used to visualize differences associated with demographic characteristics. The resulting visualizations support bias-source investigation rather than establishing that a downstream classifier has been debiased.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Unveiling Fairness Biases in Deep Learning-Based Brain MRI Reconstruction**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_10)]

  **TLDR:** This work investigates fairness in deep learning-based brain MRI reconstruction. It extends subgroup assessment from diagnostic classification to the image reconstruction stage. The available record identifies reconstruction bias as the research question but does not establish a particular error disparity or mitigation effect.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Unsupervised Bias Discovery in Medical Image Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_26)]

  **TLDR:** This work addresses bias discovery in medical image segmentation without relying on a fully specified supervised bias label. It studies an unsupervised approach to identifying relevant failures or subgroups. The available record identifies discovery as the main contribution but does not establish quantitative disparities or a validated mitigation benefit.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Towards Unraveling Calibration Biases in Medical Image Analysis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_13)]

  **TLDR:** This work examines calibration-related biases in medical image analysis. It treats the relationship between predicted confidence and observed outcomes as a fairness-assessment problem. The available record identifies calibration bias as the topic but does not establish a particular post-training calibration intervention or numerical result.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **The role of subgroup separability in group-fair medical image classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-43898-1_18)]

  **TLDR:** This study examines the relationship between subgroup separability and fairness in medical image classification. It investigates whether the ability to distinguish demographic groups is related to differences in diagnostic performance. The review identifies subgroup separability as relevant to disparity, without treating sensitive-attribute encoding alone as proof of discrimination.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Revisiting skin tone fairness in dermatological lesion classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_24)]

  **TLDR:** Dermatological lesion classifiers may perform unevenly across skin tones, making fairness evaluation important for clinical imaging. The paper is indexed in a systematic review as a fairness benchmarking study for dermatological lesion classification on ISIC data with skin tone as the sensitive attribute and balanced-accuracy disparity as the recorded metric. The available record does not provide a directly extractable result for this paper, so its empirical findings cannot be established from this evidence alone.

  **Date:** 2023

- (*ICLR 2023'23*) **MEDFAIR: Benchmarking Fairness for Medical Imaging**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://arxiv.org/abs/2210.01725)] [[Code](https://github.com/ys-zong/MEDFAIR)]

  **TLDR:** Comparing bias mitigation methods for medical imaging is difficult because fairness criteria are inconsistent and experimental settings differ. MEDFAIR benchmarks eleven algorithms across nine imaging datasets and three model selection criteria. The benchmark finds that model selection criteria can significantly affect fairness outcomes, while the evaluated bias mitigation algorithms did not significantly improve fairness over empirical risk minimization in in-distribution and out-of-distribution settings.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Bias in unsupervised anomaly detection in brain MRI**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_12)]

  **TLDR:** This work investigates bias in unsupervised anomaly detection using brain MRI. It extends fairness assessment beyond supervised diagnostic classification to anomaly-detection models. The available record identifies the task and fairness question but does not establish a specific mitigation effect or numerical disparity.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_17)]

  **TLDR:** The paper addresses auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease using medical imaging. The title-indicated study design is a fairness evaluation and benchmarking audit of CNN diagnostic models across sex and gender, age, and race and ethnicity, with no mitigation pipeline supported by the record. No result evidence is available in the record, so the audit's empirical findings and practical interpretation cannot be established from the available record.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **Are sex-based physiological differences the cause of gender bias for chest X-ray diagnosis?**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_14)]

  **TLDR:** This study asks whether sex-related physiological differences explain gender bias in chest X-ray diagnosis. It tests a proposed connection between breast-related image differences and unequal model performance. The systematic review reports that the results do not support this particular explanation, motivating further investigation of other bias mechanisms.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **An Investigation into the Impact of Deep Learning Model Choice on Sex and Race Bias in Cardiac MR Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_21)]

  **TLDR:** The paper investigates how deep learning model choice affects sex and race bias in cardiac MR segmentation. The available record places it in fairness evaluation benchmarking for cardiac MR segmentation on UK Biobank, with race and sex as sensitive attributes and Dice similarity coefficient disparity as the reported metric. The available evidence does not report result details, so specific performance or bias findings cannot be established from the available record.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **An Investigation into Race Bias in Random Forest Models Based on Breast DCE-MRI Derived Radiomics Features**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_22)]

  **TLDR:** The study investigates whether random forest models using radiomics features from breast dynamic contrast-enhanced MRI show race bias when predicting tumour molecular subtype. It measures race-identifiable information in the radiomics features and evaluates subgroup performance of subtype models trained on race-imbalanced data. The authors report that race could be predicted from radiomics features with 60-70% accuracy for some feature subsets and that subtype models appeared biased toward the race represented in training.

  **Date:** 2023

- (*JAMA Network Open'23*) **Algorithmic Fairness of Machine Learning Models for Alzheimer Disease Progression**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1001/jamanetworkopen.2023.42203)]

  **TLDR:** The study examines whether machine learning models for predicting progression to mild cognitive impairment and Alzheimer disease perform fairly across sex, ethnicity, and race groups using neuropsychological, MRI, PET, and cerebrospinal fluid predictors. It is a prognostic study evaluating logistic regression, support vector machine, and recurrent neural network models in Alzheimer Disease Neuroimaging Initiative participants with equal opportunity, equalized odds, and demographic parity metrics. The models were accurate in aggregate but failed to satisfy fairness metrics, with lower sensitivity for Hispanic participants than non-Hispanic participants and lower sensitivity for Black and Asian participants than non-Hispanic White participants in several predictions, while sex differences were generally not significant except for some transitions.

  **Date:** 2023-11-07

- (*Radiology Artificial Intelligence'23*) **Risk of Bias in Chest Radiography Deep Learning Foundation                     Models**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1148/ryai.230060)]

  **TLDR:** This study evaluates sex- and race-related bias in a chest radiography foundation model. It compares feature-distribution shifts with disease-detection disparities using CheXpert radiographs and a baseline deep learning model. The design distinguishes demographic differences in learned features from the subgroup performance consequences that must be measured separately.

  **Date:** 2023-11-01

- (*Patterns'23*) **The path toward equal performance in medical machine learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1016/j.patter.2023.100790)]

  **TLDR:** This article distinguishes causes of unequal performance between patient groups in medical machine learning. It separates avoidable model underperformance from differences in the best achievable performance caused by task difficulty. The authors argue that leveling up performance requires diagnosing these mechanisms alongside representation, selection and label biases.

  **Date:** 2023-07

- (*FAIMI resource'23*) **No Fair Lunch: A Causal Perspective on Dataset Bias in Machine Learning for Medical Imaging**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://arxiv.org/abs/2307.16526)]

  **TLDR:** No Fair Lunch examines why different medical-imaging dataset biases may require different mitigation strategies. It distinguishes causal mechanisms related to prevalence, presentation and annotation and provides a three-step reasoning framework. The abstract argues that apparently similar observed disparities can arise from different mechanisms, limiting one-size-fits-all fairness corrections.

  **Date:** 2023-07-31

- (*Science'23*) **Implications of predicting race variables from medical images**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1126/science.adh4260)]

  **TLDR:** This article discusses the implications of predicting race variables from medical images. It considers both risks and research opportunities associated with AI-derived race information. The available abstract frames a health-disparities discussion rather than demonstrating that a race-predictive model is clinically fair or unfair.

  **Date:** 2023-07-14

- (*Nature Biomedical Engineering'23*) **Algorithmic fairness in artificial intelligence for medicine and healthcare**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1038/s41551-023-01056-8)]

  **TLDR:** This perspective considers how insufficiently fair AI systems can undermine equitable healthcare. It connects clinical workflow biases to subgroup inequalities and reviews approaches including disentanglement, federated learning and explainability. The discussion emphasizes that fairness assessment and mitigation must be interpreted in the context of clinical data and deployment.

  **Date:** 2023-06-28

- (*ArXiv 2023'23*) **Harvard Glaucoma Fairness: A Retinal Nerve Disease Dataset for Fairness Learning and Fair Identity Normalization**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Dataset](assets/badges/focus-dataset.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Code](assets/badges/assets-code.svg) ![Data](assets/badges/assets-data.svg)

  [[Paper](https://arxiv.org/abs/2306.09264)] [[Code](https://github.com/luoyan407/Harvard-GF)] [[Data](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A4XMO1)]

  **TLDR:** The paper addresses the scarcity of dedicated public medical imaging datasets for fairness learning in glaucoma detection. It introduces Harvard-GF, a 2D/3D retinal nerve disease dataset with balanced racial groups, and proposes an equity-scaled performance measure while evaluating a fair identity normalization approach. The abstract reports that the fair identity normalization approach showed superior performance against several fairness learning methods across racial, gender, and ethnicity tasks, supporting the dataset's utility for fairness comparisons.

  **Date:** 2023-06-15

- (*2023 ACM Conference on Fairness Accountability and Transparency'23*) **What's fair is… fair? Presenting JustEFAB, an ethical framework for operationalizing medical ethics and social justice in the integration of clinical machine learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1145/3593013.3594096)]

  **TLDR:** JustEFAB addresses the ethical integration of clinical machine learning. It proposes a framework connecting medical ethics and social justice to practical fairness decisions. The available record identifies an ethical framework rather than evidence that a particular model intervention improves subgroup performance.

  **Date:** 2023-06-12

- (*Alzheimers Research &amp Therapy'23*) **Higher performance for women than men in MRI-based Alzheimer’s disease detection**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1186/s13195-023-01225-6)]

  **TLDR:** This study tests whether an MRI-based Alzheimer disease classifier has sex and age biases despite balanced training data. A convolutional network is evaluated across repeated train-validation-test splits and interpreted with layer-wise relevance propagation. The reported higher performance for women shows that demographic balance in training does not automatically ensure equal subgroup performance.

  **Date:** 2023-04-20

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **Detecting shortcuts in medical images-a case study in chest x-rays**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1109/isbi53787.2023.10230572)]

  **TLDR:** This study investigates shortcut learning in chest X-ray analysis. It examines image cues such as drainage devices that may influence diagnostic predictions. The review uses this case to illustrate how clinically incidental visual features can contribute to unfair model behavior.

  **Date:** 2023-04-18

- (*2023 IEEE 20th International Symposium on Biomedical Imaging ISBI'23*) **A comparative study of fairness in medical machine learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1109/isbi53787.2023.10230368)]

  **TLDR:** This study compares fairness approaches in medical machine learning. The review records interventions spanning data redistribution, training constraints and post-training calibration. Its comparative contribution is placed under fairness evaluation rather than arbitrarily assigning the whole study to a single mitigation stage.

  **Date:** 2023-04-18

- (*eBioMedicine'23*) **Algorithmic encoding of protected characteristics in chest X-ray disease detection models**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/j.ebiom.2023.104467)]

  **TLDR:** Chest X-ray disease detection models may encode protected characteristics such as race and biological sex, raising concerns about subgroup performance disparities. Using CheXpert and MIMIC-CXR, the study combines test-set resampling, transfer learning, multitask learning, and model inspection to probe whether protected characteristics are encoded and used by deep learning models. The paper reports shifted true and false positive rates that are partly reduced after correcting for population and prevalence shifts, and finds transfer learning alone insufficient for determining whether patient information is used.

  **Date:** 2023-03

- (*Cancers'23*) **From Head and Neck Tumour and Lymph Node Segmentation to Survival Prediction on PET/CT: An End-to-End Framework Featuring Uncertainty, Fairness, and Multi-Region Multi-Modal Radiomics**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.3390/cancers15071932)]

  **TLDR:** This study combines head-and-neck tumor and lymph-node segmentation with recurrence-free survival prediction from PET and CT. It uses segmentation uncertainty, multimodal radiomics and bias evaluation across age, sex, treatment, HPV status and lesion size. The abstract reports segmentation and survival-prediction results, but those aggregate results alone do not establish equal performance across subgroups.

  **Date:** 2023-03-23

</details>

<details>
<summary>2022 · 12 papers</summary>

#### 2022

- (*PCHIL 2022'22*) **Improving the Fairness of Chest X-ray Classifiers**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf)]

  **TLDR:** This study examines fairness gaps in chest X-ray classification. It benchmarks prediction performance and bias-mitigation strategies across patient subgroups. The systematic review reports that the evaluated mitigation methods did not consistently outperform the baseline with statistical significance.

  **Date:** 2022

- (*MLHC'22*) **How fair is your graph? exploring fairness concerns in neuroimaging studies**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://proceedings.mlr.press/v182/ribeiro22a.html)]

  **TLDR:** The paper addresses fairness concerns in graph-related neuroimaging studies. Its method is title-indicated as an exploration of fairness concerns in neuroimaging graphs, with no abstract or method evidence supplied. Results cannot be established from the available record, which provides only the title and systematic-review context.

  **Date:** 2022

- (*Lecture Notes in Computer Science'22*) **Feature Robustness and Sex Differences in Medical Imaging: A Case Study in MRI-Based Alzheimer’s Disease Detection**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-16431-6_9)]

  **TLDR:** This case study investigates robustness and sex-related performance differences in MRI-based Alzheimer’s disease detection under changes to dataset splits and training-set sex composition. The authors compare a logistic regression model using manually selected volumetric features with a convolutional neural network trained on 3D MRI data from the ADNI dataset, then assess both models across varying splits, sex compositions, and disease stages. The abstract reports no clear pattern of majority-group advantage, finds that the logistic regression model is robust to dataset composition, and notes that CNN performance improves for both male and female subjects when more female subjects are included in training.

  **Date:** 2022

- (*Lecture Notes in Computer Science'22*) **A Systematic Study of Race and Sex Bias in CNN-Based Cardiac MR Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-23443-9_22)]

  **TLDR:** This study evaluates race and sex bias in convolutional-network cardiac MRI segmentation. It examines subgroup performance in an image segmentation setting rather than only diagnostic classification. The available record establishes the audit scope but does not support a specific numerical disparity or causal explanation.

  **Date:** 2022

- (*Lecture Notes in Computer Science'22*) **A Study of Demographic Bias in CNN-Based Brain MR Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-17899-3_2)]

  **TLDR:** The study examines demographic bias in CNN-based brain MR segmentation, focusing on race and sex differences in segmentation performance. The available systematic review describes a fairness evaluation that compares average Dice similarity coefficient at each spatial location in ADNI brain MRI segmentation. The review reports severe unfairness in some spatial regions but little or no disparity in others, supporting component-wise fairness evaluation rather than only overall utility.

  **Date:** 2022

- (*Journal of Medical and Biological Engineering'22*) **A Systematic Review of ‘Fair’ AI Model Development for Image Classification and Prediction**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1007/s40846-022-00754-z)]

  **TLDR:** This systematic review examines fair AI model development for image classification and prediction. It synthesizes methodological approaches rather than presenting a single new mitigation algorithm. It serves as a methodological reference, with applicability to a specific medical task requiring assessment of the underlying studies.

  **Date:** 2022-10-15

- (*Journal of Medical Imaging'22*) **Fairness-related performance and explainability effects in deep learning models for brain image analysis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1117/1.jmi.9.6.061102)]

  **TLDR:** The study examines how sociodemographic-related confounders affect deep learning classifier performance and explainability in brain MRI analysis. A convolutional neural network was trained to predict biological sex from T1-weighted brain MRI scans of 4547 adolescents in the ABCD study, and performance disparities and subgroup saliency maps were analyzed by race and sex. The model showed significant accuracy differences between White and Black male children and subgroup-specific saliency differences in puberty-related brain regions, supporting the interpretation that unfair models can produce different XAI results across subgroups.

  **Date:** 2022-08-26

- (*Science Advances'22*) **Disparities in dermatology AI performance on a diverse, curated clinical image set**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1126/sciadv.abq6147)]

  **TLDR:** This study evaluates dermatology AI on diverse skin tones and uncommon diseases. It introduces the pathologically confirmed Diverse Dermatology Images dataset and tests existing models and dermatologists. The abstract reports poorer performance on dark skin and uncommon conditions and shows that fine-tuning on diverse images can close the measured skin-tone performance gap.

  **Date:** 2022-08-12

- (*Nature Communications'22*) **Addressing fairness in artificial intelligence for medical imaging**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1038/s41467-022-32186-3)]

  **TLDR:** This work addresses fairness concerns in AI systems for medical imaging. It provides a broad discussion of the problem rather than identifying a single intervention stage in the available record. Its value here is to frame fairness assessment, while detailed recommendations require consultation of the original article.

  **Date:** 2022-08-06

- (*The Lancet Digital Health'22*) **AI recognition of patient race in medical imaging: a modelling study**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/s2589-7500(22)00063-2)]

  **TLDR:** This modeling study investigates whether patient race can be recognized from medical images. It treats sensitive-attribute predictability as an empirical question across medical imaging inputs. This encoding question is relevant to fairness audits but is distinct from establishing unequal diagnostic error rates.

  **Date:** 2022-06

- (*Frontiers in Cardiovascular Medicine'22*) **Fairness in Cardiac Magnetic Resonance Imaging: Assessing Sex and Racial Bias in Deep Learning-Based Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.3389/fcvm.2022.859310)]

  **TLDR:** The paper assesses sex and racial bias in deep learning-based cine cardiac magnetic resonance segmentation for biventricular structure and functional quantification. Using short-axis end-diastole and end-systole images from 5,903 UK Biobank subjects, it compares Dice scores and volumetric and functional measurement errors across race and sex groups, with multivariate linear regression and ANCOVA to examine potential confounders. The analysis reports statistically significant racial differences in Dice scores and measurement errors, with minority ethnic groups showing lower agreement, and concludes that racial bias can exist when training data are sex-balanced but not race-balanced.

  **Date:** 2022-04-07

- (*FAIMI resource'22*) **Diagnosing failures of fairness transfer across distribution shift in real-world medical settings**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2202.01034)]

  **TLDR:** This paper investigates why model fairness can fail to transfer across real-world medical distribution shifts. It uses a causal framework and conditional-independence tests to characterize shifts in two medical applications. The results show that identifying the structure of the shift is necessary for selecting an appropriate fairness remedy.

  **Date:** 2022-02-02

</details>

<details>
<summary>2021 · 10 papers</summary>

#### 2021

- (*FAIMI resource'21*) **Assessing Bias in Medical AI**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://www.cse.cuhk.edu.hk/~qdou/public/IMLH2021_files/64_CameraReady_ICML_2021_Interpretable_Machine_Learning_in_Healthcare_workshop.pdf)]

  **TLDR:** This article addresses the assessment of bias in medical AI. It focuses on evaluating the assumptions and evidence behind claims of fair model behavior. The available bibliographic record does not establish a specific empirical result or mitigation protocol.

  **Date:** 2021

- (*Nature Medicine'21*) **Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41591-021-01595-0)]

  **TLDR:** Chest X-ray pathology classifiers may underdiagnose diseases in under-served patient populations, raising concerns about unequal access to care. The study evaluates algorithmic underdiagnosis in chest X-ray pathology classification across three large chest X-ray datasets and one multi-source dataset, focusing on classifiers built with state-of-the-art computer vision techniques. It finds that classifiers consistently and selectively underdiagnosed under-served patient populations, with higher underdiagnosis rates for intersectional groups such as Hispanic female patients.

  **Date:** 2021-12

- (*ArXiv 2021'21*) **RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2111.11665)]

  **TLDR:** RadFusion addresses the lack of multimodal medical imaging benchmarks that combine CT scans with EHR context for pulmonary embolism detection and fairness assessment across demographic subgroups. The study introduces a 1,794-patient benchmark dataset with EHR data and high-resolution CT scans labeled for pulmonary embolism and evaluates several representative multimodal fusion models for performance and fairness across gender, race/ethnicity, and age. The supplied abstract reports that integrating imaging and EHR data can improve classification performance and robustness without introducing large true positive rate disparities between population groups.

  **Date:** 2021-11-23

- (*ArXiv 2021'21*) **Algorithmic encoding of protected characteristics in image-based models for disease detection**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2110.14755)]

  **TLDR:** The study asks how protected characteristics such as race and biological sex become encoded in image-based disease detection models and whether that encoding drives subgroup performance disparities. Using the public chest X-ray datasets CheXpert and MIMIC-CXR, the authors combine test-set resampling, transfer learning, multitask learning, and model inspection to assess subgroup performance and representation encoding. They find subgroup disparities in shifted true and false positive rates that are partially reduced after correcting for population and prevalence shifts, and they conclude that the tested transfer-learning method is insufficient for establishing whether specific patient information is used.

  **Date:** 2021-10-27

- (*ACM Computing Surveys'21*) **A Survey on Bias and Fairness in Machine Learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1145/3457607)]

  **TLDR:** This survey examines bias and fairness across machine-learning applications. It organizes sources of bias, mathematical fairness definitions and technical mitigation approaches. It provides general methodological background for medical fairness research rather than new evidence of a clinical subgroup disparity.

  **Date:** 2021-07-13

- (*ArXiv 2021'21*) **Evaluating subgroup disparity using epistemic uncertainty in mammography**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2107.02716)]

  **TLDR:** The study examines whether epistemic uncertainty can reveal race and scanner subgroup disparities in mammography-based breast density assessment. Using 108,190 mammograms from 33 clinical sites, it compares uncertainty quantification metrics across demographic and data-acquisition subgroups while considering aggregate performance. The abstract reports that aggregate performance can be comparable even when subgroup-level findings depend on the chosen uncertainty quantification metric.

  **Date:** 2021-07-06

- (*Emergency Radiology'21*) **Radiology “forensics”: determination of age and sex from chest radiographs using deep learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/s10140-021-01953-y)]

  **TLDR:** This study tests whether age and sex can be inferred from chest radiographs. It fine-tunes convolutional networks for demographic classification and evaluates them in American and Chinese populations. The reported demographic predictability establishes that such information is encoded in radiographs, not that a disease classifier necessarily discriminates against a group.

  **Date:** 2021-06-05

- (*ArXiv 2021'21*) **Model Selection's Disparate Impact in Real-World Deep Learning Applications**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2104.00606)]

  **TLDR:** The paper Model Selection's Disparate Impact in Real-World Deep Learning Applications examines how human preferences in model selection can produce disparate impact across demographic groups. Using a deep learning model trained on real-world medical imaging data, the authors empirically test whether the choice of metric for model comparison, especially metrics that do not account for variability, biases model selection outcomes. The authors argue that such metric choice can significantly bias model selection outcomes, indicating that fairness evaluation should consider model-selection practices as well as biased training data.

  **Date:** 2021-04-01

- (*Proceedings of the 2021 ACM Conference on Fairness Accountability'21*) **Re-imagining Algorithmic Fairness in India and Beyond**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1145/3442188.3445896)]

  **TLDR:** This work considers how algorithmic fairness should be understood in India and other settings beyond dominant research contexts. Its contribution is a contextual examination of fairness assumptions rather than a medical mitigation experiment. It is retained as methodological background for interpreting fairness across social and geographic contexts.

  **Date:** 2021-03

- (*Proceedings of the Pacific Symposium 2021'21*) **CheXclusion: Fairness gaps in deep chest X-ray classifiers**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://pubmed.ncbi.nlm.nih.gov/33691020/)]

  **TLDR:** The study examines whether deep chest X-ray classifiers trained for diagnostic labels show performance disparities across protected patient attributes. It trains convolutional neural networks to predict 14 diagnostic labels on MIMIC-CXR, Chest-Xray8, CheXpert, and a multi-site aggregation, then compares true positive rates by sex, age, race, and insurance type. The paper reports true positive rate disparities across all datasets, clinical tasks, and subgroups, with the smallest disparities in the multi-source dataset and no significant correlation between disparities and subgroup disease burden.

  **Date:** 2021-01-01

</details>

<details>
<summary>2020 · 5 papers</summary>

#### 2020

- (*Lecture Notes in Computer Science'20*) **Fairness of Classifiers Across Skin Tones in Dermatology**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-030-59725-2_31)]

  **TLDR:** The paper Fairness of Classifiers Across Skin Tones in Dermatology examines whether dermatology image classifiers perform fairly across skin tones. It is a fairness benchmarking study that evaluates classifiers on the ISIC and SD-198 dermatology datasets using skin tone as the sensitive attribute and AP as the metric. The systematic review reports that this study did not find an observable trend between model utility and skin tone, so the available evidence supports a limited or null discrepancy finding rather than a mitigation benefit.

  **Date:** 2020

- (*FAIMI resource'20*) **Fairness in Deep Learning: A Computational Perspective**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://ieeexplore.ieee.org/document/9113719)]

  **TLDR:** This work examines fairness in deep learning from a computational perspective. It provides a general methodological discussion rather than a single medical-imaging intervention. Its role in this catalog is background for evaluating fairness assumptions, with medical applicability determined by the specific downstream setting.

  **Date:** 2020

- (*Nature Machine Intelligence'20*) **Shortcut learning in deep neural networks**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s42256-020-00257-z)]

  **TLDR:** This work examines shortcut learning in deep neural networks. It describes how models can exploit predictive cues that do not reflect the intended task solution. It supplies a general mechanism for interpreting medical AI failures without by itself demonstrating a particular protected-group disparity.

  **Date:** 2020-11-10

- (*The Lancet Digital Health'20*) **Ethical limitations of algorithmic fairness solutions in health care machine learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.1016/s2589-7500(20)30065-0)]

  **TLDR:** This work discusses ethical limitations of technical algorithmic fairness solutions in healthcare. It examines fairness as a normative problem that cannot be resolved by a model metric alone. The available record supports an ethical framing, while specific clinical or empirical conclusions require the original article.

  **Date:** 2020-05

- (*Proceedings of the National Academy of Sciences'20*) **Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1073/pnas.1919012117)]

  **TLDR:** The study examines whether gender imbalance in medical imaging training data produces biased classifiers for computer-aided diagnosis. It reports a large-scale empirical evaluation using three deep neural network architectures and two public chest X-ray datasets for thoracic disease diagnosis under different gender-imbalance conditions. The abstract reports a consistent performance decrease for underrepresented genders when a minimum balance is not met and calls for explicit gender-balance guidance and robustness methods.

  **Date:** 2020-05-26

</details>

<details>
<summary>2019 · 1 papers</summary>

#### 2019

- (*Science'19*) **Dissecting racial bias in an algorithm used to manage the health of populations**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1126/science.aax2342)]

  **TLDR:** This study investigates racial bias in a commercial algorithm used to identify patients for additional care. It compares health needs at the same assigned risk and examines healthcare costs as the algorithmic target. The authors trace the disparity to unequal spending as a proxy for need and report that reformulating the target removes the measured prediction bias.

  **Date:** 2019-10-25

</details>

<details>
<summary>2018 · 2 papers</summary>

#### 2018

- (*Annals of Internal Medicine'18*) **Ensuring Fairness in Machine Learning to Advance Health Equity**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://doi.org/10.7326/m18-1990)]

  **TLDR:** This article examines how clinical machine learning can be designed to advance health equity. It connects model design, historical data bias and clinical interactions to distributive-justice principles. It argues for choosing patient-outcome, model-performance or resource-allocation fairness objectives according to the clinical purpose.

  **Date:** 2018-12-18

- (*FAIMI resource'18*) **The Measure and Mismeasure of Fairness**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Evaluation](assets/badges/stage-evaluation.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg) · ![Survey](assets/badges/survey-survey.svg)

  [[Paper](https://arxiv.org/abs/1808.00023)]

  **TLDR:** This study examines whether widely used mathematical fairness definitions support the outcomes they aim to protect. It groups definitions into constraints on decision effects and constraints on protected-attribute effects, then analyzes the resulting policies. The abstract shows that satisfying formal constraints can produce Pareto-dominated decisions, motivating explicit attention to the intended social objective.

  **Date:** 2018-07-31

</details>

<p><a href="#-papers">↑ All categories</a></p>

---

### Unfairness Mitigation: Pre-processing

#### 2026

##### 2026-03

- (*Medical Image Analysis'26*) **Rethinking fairness in medical imaging: Maximizing group-specific performance with application to skin disease diagnosis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/j.media.2026.103950)]

  **TLDR:** This paper reframes medical imaging fairness as maximizing diagnostic accuracy for each patient group. It introduces SPARE, a data-reweighting algorithm that uses sample utility and group similarity when training group-specific models. The approach explicitly uses additional modeling resources to pursue group-specific performance rather than accepting a single-model accuracy-fairness compromise.

  **Date:** 2026-03

<details>
<summary>2025 · 1 papers</summary>

#### 2025

- (*Machine Learning for Biomedical Imaging'25*) **Understanding-informed Bias Mitigation for Fair CMR Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.59275/j.melba.2025-6747)]

  **TLDR:** This study examines mitigation of ethnicity bias in cardiac MRI segmentation. It compares oversampling, importance reweighting, Group DRO and combinations of these approaches, including experiments on heart-cropped images. The abstract reports that oversampling can mitigate the tested bias, while the broader design also examines how training-time methods interact with data-level interventions.

  **Date:** 2025-12-30

</details>

<details>
<summary>2023 · 4 papers</summary>

#### 2023

- (*Lecture Notes in Computer Science'23*) **EdgeMixup: embarrassingly simple data alteration to improve Lyme disease lesion segmentation and diagnosis fairness**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-43901-8_36)]

  **TLDR:** EdgeMixup addresses fairness in Lyme disease lesion segmentation and diagnosis. Its intervention alters training data through an edge-based mixing strategy. The available record identifies a data-level mitigation approach but does not establish the size or statistical reliability of its fairness gains.

  **Date:** 2023

- (*Lecture Notes in Computer Science'23*) **De-identification and obfuscation of gender attributes from retinal scans**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_9)]

  **TLDR:** This study addresses gender-related information in retinal scans. It investigates de-identification and attribute obfuscation, which the systematic review treats as data-level harmonization. Removing identifiable attribute information is a distinct objective from proving equal downstream diagnostic performance.

  **Date:** 2023

- (*Medical Image Analysis'23*) **Equitable modelling of brain imaging by counterfactual augmentation with morphologically constrained 3D deep generative models**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/j.media.2022.102723)]

  **TLDR:** CounterSynth addresses inequitable brain-imaging predictions associated with imbalance and confounding. It generates morphologically constrained counterfactual MRI augmentations and evaluates them using UK Biobank and OASIS data. The abstract reports improvements in predictive fidelity and equity under the tested imbalance and confounding scenarios.

  **Date:** 2023-02

- (*Proceedings of the National Academy of Sciences'23*) **Bias in machine learning models can be significantly mitigated by careful training: Evidence from neuroimaging studies**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1073/pnas.2211613120)]

  **TLDR:** This study tests whether carefully trained neuroimaging models necessarily exhibit demographic bias. It evaluates Alzheimer disease, schizophrenia and autism models across multiple MRI studies and demographic subgroups. The abstract reports well-generalizing models with low measured bias, showing that unequal performance is not an inevitable outcome of medical machine learning.

  **Date:** 2023-01-30

</details>

<details>
<summary>2022 · 1 papers</summary>

#### 2022

- (*NeurIPS Workshop 2022'22*) **Improving fairness in image classification via sketching**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://openreview.net/forum?id=Rq2vt3tnAK9)] [[Code](https://github.com/ubc-tea/Improving-Fairness-in-Image-Classification-via-Sketching)]

  **TLDR:** The paper addresses subgroup fairness disparities in medical image classification by harmonizing input images through sketching. The reviewed record describes a language-guided sketching model that transforms input images into sketches before classification, which is a pre-processing intervention rather than a change to training objectives or a post-hoc adjustment. The reviewed record reports less disparity among subgroups, suggesting a potential fairness benefit from sketching-based harmonization, but detailed quantitative results cannot be established from the available record.

  **Date:** 2022

</details>

<details>
<summary>2021 · 5 papers</summary>

#### 2021

- (*Lecture Notes in Computer Science'21*) **Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-030-87199-4_39)]

  **TLDR:** For deep-learning segmentation of cardiac magnetic resonance images, the study examines fairness gaps associated with training-data imbalance across race and sex groups. The review extraction reports that stratified batch resampling was applied to a baseline segmentation model, with an adversarial in-processing branch also indexed. The review reports that stratified batch resampling was associated with a significant fairness improvement, although effect sizes and full experimental details cannot be established from the available record.

  **Date:** 2021

- (*Lecture Notes in Computer Science'21*) **Confound removal and normalization in practice: a neuroimaging based sex prediction case study**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-030-67670-4_1)]

  **TLDR:** This study investigates how confound removal and normalization affect neuroimaging-based sex prediction. It compares whole-data and cross-validated confound regression together with Z-score normalization across alternative pipelines. The key fairness-related concern is whether preprocessing choices distort generalization estimates or leave confounding information in the analysis.

  **Date:** 2021

- (*ArXiv 2021'21*) **AI Fairness via Domain Adaptation**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2104.01109)]

  **TLDR:** The paper AI Fairness via Domain Adaptation addresses fairness risks in deep learning diagnostic AI for age-related macular degeneration when training data are imbalanced. Its method uses domain adaptation through training-set enhancement, namely generative models that synthesize additional training samples for underrepresented populations. The abstract reports improved fairness from an originally biased AMD diagnostic model, but effect sizes and statistical details cannot be established from the available record.

  **Date:** 2021-03-15

- (*Translational Vision Science &amp Technology'21*) **Addressing Artificial Intelligence Bias in Retinal Diagnostics**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1167/tvst.10.2.13)]

  **TLDR:** This study examines diagnostic bias caused by retinal-image training imbalance and domain generalization. It constructs an imbalanced diabetic-retinopathy training scenario and compares baseline models with generative data augmentation. The design tests whether synthetic training examples can reduce a deliberately introduced diagnostic gap rather than assuming augmentation guarantees fairness.

  **Date:** 2021-02-11

- (*Medical Image Analysis'21*) **Detect and correct bias in multi-site neuroimaging datasets**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1016/j.media.2020.101879)]

  **TLDR:** This study examines biases introduced when neuroimaging scans are pooled across independent studies. It analyzes dataset identifiability and latent confounding before presenting methods for dataset harmonization. The abstract reports strong dataset-identification performance, demonstrating that combining larger datasets does not automatically remove study-specific information.

  **Date:** 2021-01

</details>

<details>
<summary>2020 · 1 papers</summary>

#### 2020

- (*2020 IEEE/CVF Conference on Computer Vision and Pattern Recogniti'20*) **Debiasing skin lesion datasets and models? Not so fast**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1109/cvprw50498.2020.00378)]

  **TLDR:** This study questions whether apparently debiased skin lesion datasets and models are actually free of bias. It examines data-level debiasing, with the systematic review placing the work under preprocessing and harmonization. The title and review classification warrant caution about debiasing claims, while detailed empirical conclusions require the original methods and results.

  **Date:** 2020-06

</details>

<details>
<summary>2019 · 1 papers</summary>

#### 2019

- (*2019 IEEE/CVF Conference on Computer Vision and Pattern Recogniti'19*) **(De) Constructing bias on skin lesion datasets**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Pre-processing](assets/badges/pre-processing-pre-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1109/cvprw.2019.00335)]

  **TLDR:** This paper investigates how bias is constructed in skin lesion datasets. The systematic review discusses the work in the context of data-level harmonization before model training. The available record supports a focus on dataset bias but does not establish the magnitude of any downstream fairness improvement.

  **Date:** 2019-06

</details>

<p><a href="#-papers">↑ All categories</a></p>

---

### Unfairness Mitigation: In-processing

<details>
<summary>2024 · 2 papers</summary>

#### 2024

- (*Referenced study'24*) **Fairtune: Optimizing parameter efficient fine tuning for fairness in medical image analysis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2310.05055)]

  **TLDR:** FairTune addresses the fairness generalization gap when adapting pretrained models to medical imaging tasks. It uses validation fairness to optimize parameter-efficient fine-tuning choices through bilevel optimization. The approach treats the amount and location of model adaptation as fairness-relevant training decisions rather than assuming perfect training fairness will transfer to test data.

  **Date:** 2024

- (*ICLR'24*) **FairSeg: A Large-Scale Medical Image Segmentation Dataset for Fairness Learning Using Segment Anything Model with Fair Error-Bound Scaling**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Dataset](assets/badges/focus-dataset.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://arxiv.org/abs/2311.02189)] [[Code](https://github.com/Harvard-Ophthalmology-AI-Lab/FairSeg)]

  **TLDR:** FairSeg addresses the lack of medical image segmentation datasets designed for fairness research. It introduces Harvard-FairSeg and a fair error-bound scaling approach that reweights SAM training losses across identity groups. The contribution combines a subgroup-aware benchmark with an explicit training-time mitigation method targeting hard cases.

  **Date:** 2024

</details>

<details>
<summary>2023 · 4 papers</summary>

#### 2023

- (*Lecture Notes in Computer Science'23*) **CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-25069-9_14)] [[Code](https://github.com/sfu-mial/CIRCLe)]

  **TLDR:** CIRCLe targets skin-color-related bias in skin lesion classification. It combines color-based data synthesis with contrastive representation learning to encourage color-invariant features. The method links training-data variation to learned invariance, with the main representation-learning intervention placed under in-processing.

  **Date:** 2023

- (*Nature Communications'23*) **Improving model fairness in image-based computer-aided diagnosis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41467-023-41974-4)]

  **TLDR:** This study seeks to improve fairness in image-based computer-aided diagnosis without substantially reducing overall discrimination. It introduces a learning algorithm based on marginal pairwise equal opportunity and evaluates it on four tasks and independent cohorts. The abstract reports reduced fairness differences for individual and intersectional subgroups while typically changing AUC by less than one percent.

  **Date:** 2023-10-06

- (*ArXiv 2023'23*) **FairAdaBN: Mitigating unfairness with adaptive batch normalization and its application to dermatological disease classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2303.08325)]

  **TLDR:** Dermatological disease classification models can show performance disparities across demographic subgroups. FairAdaBN adapts batch normalization to the sensitive attribute, adds a mini-batch statistical parity loss, and introduces Fairness-Accuracy Trade-off Efficiency to measure fairness improvement relative to accuracy loss. Experiments on two dermatological datasets reported better fairness criteria and FATE than other methods.

  **Date:** 2023-03-15

- (*IPMI 2023'23*) **On Fairness of Medical Image Classification with Multiple Sensitive Attributes via Learning Orthogonal Representations**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2301.01481)]

  **TLDR:** The paper addresses fairness in medical image classification when patients have multiple sensitive attributes. It proposes fair representation learning that seeks independence between target and multi-sensitive representations through column-space and row-space orthogonality constraints. The method's effectiveness is reported through experiments on CheXpert, but specific fairness or performance gains cannot be established from the available record.

  **Date:** 2023-01-04

</details>

<details>
<summary>2022 · 8 papers</summary>

#### 2022

- (*Lecture Notes in Computer Science'22*) **Pseudo bias-balanced learning for debiased chest x-ray classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-16452-1_59)]

  **TLDR:** This study targets biased chest X-ray classification through pseudo bias-balanced learning. It changes the learning procedure to account for bias when explicit balanced training conditions are not assured. The systematic review classifies the approach as training-time mitigation, while the available record does not establish quantitative improvement.

  **Date:** 2022

- (*Referenced study'22*) **Fairness by learning orthogonal disentangled representations**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2003.05707)]

  **TLDR:** This study learns task-relevant representations that are invariant to sensitive or nuisance attributes. It combines orthogonality-based disentanglement with entropy maximization to separate meaningful and sensitive information. The abstract reports competitive performance across five datasets, while downstream fairness remains dependent on the evaluated task and constraints.

  **Date:** 2022

- (*Lecture Notes in Computer Science'22*) **Disproportionate subgroup impacts and other challenges of fairness in artificial intelligence for medical image analysis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-23223-7_2)]

  **TLDR:** This work addresses disproportionate subgroup impacts in medical image analysis. The systematic review includes it among training-time adversarial approaches to unfairness mitigation. The available record supports this intervention category but does not establish numerical gains, clinical benefits or a universally preferred fairness criterion.

  **Date:** 2022

- (*Lecture Notes in Computer Science'22*) **Conditional VAEs for confound removal and normative modelling of neurodegenerative diseases**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-16431-6_41)]

  **TLDR:** This work addresses confounding in normative models of neurodegenerative disease. It uses conditional variational autoencoders for confound removal and normative modeling. The available record identifies the representation-learning intervention but does not establish a particular subgroup fairness gain.

  **Date:** 2022

- (*Lecture Notes in Computer Science'22*) **A Penalty Approach for Normalizing Feature Distributions to Build Confounder-Free Models**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-16437-8_37)]

  **TLDR:** This paper addresses confounding effects in features learned for clinical machine learning. It extends metadata normalization with a penalty-based approximation to a bilevel optimization problem. The method targets more stable confounder-aware feature learning than minibatch-dependent closed-form normalization.

  **Date:** 2022

- (*ECCVW 2022'22*) **FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://arxiv.org/abs/2208.10013)] [[Code](https://github.com/siyi-wind/FairDisCo)]

  **TLDR:** Deep learning models for skin lesion diagnosis can show ethnic disparity, with lesions on darker skin types underrepresented and diagnosed less accurately. FairDisCo is a disentanglement deep learning framework with contrastive learning that uses an additional network branch to remove skin-type information from representations and another contrastive branch to enhance feature extraction, and it is compared with resampling, reweighting, and attribute-aware fairness methods on Fitzpatrick17k and Diverse Dermatology Images. The abstract reports fairer and superior skin lesion classification performance for FairDisCo, but exact gains and statistical significance cannot be established from the available record.

  **Date:** 2022-08-22

- (*ArXiv 2022'22*) **Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41467-023-39902-7)]

  **TLDR:** Clinical machine learning models may learn shortcut correlations in training data and produce unfair subgroup performance, so the task is to detect and prevent shortcut learning in medical AI. The authors propose a multi-task-learning shortcut-testing method for assessing and mitigating shortcut learning as part of fairness assessment and demonstrate it on radiology and dermatology tasks. The abstract reports that the approach reveals cases where shortcutting is not responsible for unfairness, supporting a holistic view of mitigation, while quantitative results cannot be established from the available record.

  **Date:** 2022-07-21

- (*Referenced study'22*) **Rényi fair information bottleneck for image classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2203.04950)]

  **TLDR:** RFIB addresses the joint objectives of predictive utility, fairness and compact representation learning. It derives a variational loss using tunable Renyi divergence and evaluates demographic-parity and equalized-odds constraints on EyePACS classification. The abstract reports favorable utility-fairness metrics relative to compared methods on this medical imaging dataset.

  **Date:** 2022-03-09

</details>

<details>
<summary>2021 · 5 papers</summary>

#### 2021

- (*Lecture Notes in Computer Science'21*) **On the Fairness of Swarm Learning in Skin Lesion Classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-030-90874-4_12)]

  **TLDR:** The paper addresses fairness in swarm learning for skin lesion classification with respect to age and sex. The study examines a federated swarm-learning setup in which each client contains only samples sharing the same sensitive attribute, evaluated on ISIC and Fitzpatrick-17k dermatology data with demographic parity and equalized odds. The available record does not provide target-paper results, so whether this setup improves fairness and by how much cannot be established.

  **Date:** 2021

- (*ArXiv 2021'21*) **Estimating and improving fairness with adversarial learning**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://oecd.ai/fr/catalogue/metric-use-cases/estimating-and-improving-fairness-with-adversarial-learning)]

  **TLDR:** The paper addresses estimating and improving fairness in medical imaging models for sensitive attributes such as age, sex and gender, and skin tone. The supplied review evidence places it in an adversarial in-processing approach, where an adversarial branch reduces sensitive information in latent representations and an added branch predicts fairness on test data without sensitive attributes. No result evidence is available in the supplied record, so performance improvements or clinical benefits cannot be established from it.

  **Date:** 2021

- (*MICCAI-DART 2021'21*) **Detecting Melanoma Fairly: Skin Tone Detection and Debiasing for Skin Lesion Classification**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Benchmark](assets/badges/focus-benchmark.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://arxiv.org/abs/2202.02832)] [[Code](https://github.com/pbevan1/Detecting-Melanoma-Fairly)]

  **TLDR:** Convolutional neural networks for melanoma and skin lesion classification can show performance disparities across skin tones that should be addressed before widespread deployment. The paper proposes an automated skin tone labelling algorithm for lesion images, applies it to annotate the ISIC benchmark, and uses the resulting labels as targets for two leading bias unlearning techniques to mitigate skin tone bias. The primary abstract reports that the skin tone detection algorithm outperforms existing solutions and that unlearning skin tone may improve generalisation and reduce the performance disparity between melanoma detection in lighter and darker skin tones.

  **Date:** 2021

- (*ArXiv 2021'21*) **Technical Challenges for Training Fair Neural Networks**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2102.06764)]

  **TLDR:** Fairness constraints for deep neural networks remain poorly understood in high-stakes settings such as facial recognition and medical imaging. The study empirically tests state-of-the-art architectures on facial recognition and automated medical diagnosis datasets to examine how fairness objectives affect training. The abstract reports that large models overfit to fairness objectives and produce unintended consequences, while specific numerical results and clinical implications cannot be established from the available record.

  **Date:** 2021-02-12

- (*2021 IEEE Winter Conference on Applications of Computer Vision WA'21*) **Representation Learning with Statistical Independence to Mitigate Bias**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1109/wacv48630.2021.00256)]

  **TLDR:** The paper addresses bias in learned representations for prediction tasks, including medical imaging, where dataset or task bias can undermine fair model behavior. It proposes an adversarial training model with two competing objectives and a new adversarial loss that encourages learned features to be maximally task-discriminative while minimally dependent on protected bias variables. In reported evaluations on synthetic data, medical images with task bias, and a gender classification dataset with dataset bias, the learned features yielded superior prediction performance and were described as unbiased.

  **Date:** 2021-01

</details>

<details>
<summary>2020 · 3 papers</summary>

#### 2020

- (*Lecture Notes in Computer Science'20*) **Risk of Training Diagnostic Algorithms on Data with Demographic Bias**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-030-61166-8_20)]

  **TLDR:** The paper addresses the risk that diagnostic algorithms trained on demographically biased medical data will learn and reproduce demographic disparities. The available record classifies the work as an adversarial in-processing mitigation approach on dermatology images with age and sex attributes, but the supplied evidence does not include an abstract or full method. Results and practical effects cannot be established from the available record, which contains only title-level and tabular classification evidence.

  **Date:** 2020

- (*MICCAI-DART 2020'20*) **On the fairness of privacy-preserving representations in medical applications**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Not specified](assets/badges/attributes-not-specified.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170)]

  **TLDR:** This study examines the fairness of privacy-preserving representations in medical applications. The systematic review places its representation-learning approach among training-time fairness methods. The available bibliographic record does not establish whether privacy protection improves downstream subgroup performance.

  **Date:** 2020

- (*Nature Communications'20*) **Training confounder-free deep learning models for medical applications**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![In-processing](assets/badges/in-processing-in-processing.svg)<br>**Attributes:** ![Age](assets/badges/attributes-age.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1038/s41467-020-19784-9)]

  **TLDR:** Deep learning models for medical imaging can learn spurious associations when confounders such as age or sex affect the relationship between images and outcomes. The paper introduces an end-to-end training approach that derives features invariant to confounders while accounting for correlations between confounders and prediction outcomes, evaluated on HIV diagnosis from MRI, adolescent sex differences in NCANDA, and pediatric bone age from X-ray images. The abstract reports that the method predicted accurately while reducing confounder-associated bias, but the available abstract does not provide quantitative effect sizes or statistical comparisons.

  **Date:** 2020-11-26

</details>

<p><a href="#-papers">↑ All categories</a></p>

---

### Unfairness Mitigation: Post-processing

#### 2026

##### 2026-11

- (*Sports Medicine - Open'26*) **Sex-Equitable Machine Learning Prediction of Ankle Reinjury in Individuals with Chronic Ankle Instability: A 2-Year Prospective Cohort Study with Fairness Audit.**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Post-processing](assets/badges/post-processing-post-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1186/s40798-026-01137-3)]

  **TLDR:** This prospective cohort study develops machine-learning models for two-year ankle reinjury prediction in people with chronic ankle instability and audits sex-related performance differences. It compares six algorithms using nested cross-validation and evaluates out-of-fold global versus sex-specific Youden thresholds with equalized-odds and disproportionate-impact measures. Sex-specific thresholding reduces the reported equalized-odds gap without retraining, but the disproportionate-impact ratio remains below the study benchmark and external validation is still required.

  **Date:** 2026-11-07

##### 2026-10

- (*arXiv'26*) **A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering**

  **Domain:** ![EHR and clinical prediction](assets/badges/domain-ehr-and-clinical-prediction.svg) · **Focus:** ![Bias mechanisms](assets/badges/focus-bias-mechanisms.svg) ![Evaluation](assets/badges/focus-evaluation.svg) ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Post-processing](assets/badges/post-processing-post-processing.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://arxiv.org/abs/2611.00298)]

  **TLDR:** This paper studies counterfactual fairness interventions in transformer activations. It introduces MICF, a mechanistic-interpretability framework for identifying sensitive mechanisms and steering activations, including a clinical prediction application. The intervention targets a pretrained model at inference time rather than optimizing a new fairness training objective.

  **Date:** 2026-10-30

<details>
<summary>2023 · 1 papers</summary>

#### 2023

- (*Lecture Notes in Computer Science'23*) **Mitigating bias in MRI-based Alzheimer’s disease classifiers through pruning of deep neural networks**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Post-processing](assets/badges/post-processing-post-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Age](assets/badges/attributes-age.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-45249-9_16)]

  **TLDR:** This study targets bias in MRI-based Alzheimer disease classification. It applies neural network pruning as the main intervention on an already trained classifier. The systematic review places the work under post-processing, while the available record does not establish quantitative gains or whether every model component remains fixed.

  **Date:** 2023

</details>

<details>
<summary>2022 · 2 papers</summary>

#### 2022

- (*Lecture Notes in Computer Science'22*) **FairPrune: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Post-processing](assets/badges/post-processing-post-processing.svg)<br>**Attributes:** ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) ![Skin tone](assets/badges/attributes-skin-tone.svg) · **Assets:** ![Paper only](assets/badges/assets-paper-only.svg)

  [[Paper](https://doi.org/10.1007/978-3-031-16431-6_70)]

  **TLDR:** FairPrune studies how neural network pruning can address unfairness in dermatological disease diagnosis. Its main intervention modifies a trained network through pruning rather than changing the original dataset. The review places this approach under post-processing, while the available bibliographic record does not establish quantitative gains.

  **Date:** 2022

- (*ML4HC 2022'22*) **Debiasing Deep Chest X-Ray Classifiers using Intra- and Post-processing Methods**

  **Domain:** ![Medical imaging](assets/badges/domain-medical-imaging.svg) · **Focus:** ![Mitigation](assets/badges/focus-mitigation.svg) · **Stage:** ![Post-processing](assets/badges/post-processing-post-processing.svg)<br>**Attributes:** ![Race and ethnicity](assets/badges/attributes-race-and-ethnicity.svg) ![Sex and gender](assets/badges/attributes-sex-and-gender.svg) · **Assets:** ![Code](assets/badges/assets-code.svg)

  [[Paper](https://proceedings.mlr.press/v182/marcinkevics22a.html)] [[Code](https://github.com/i6092467/diff-bias-proxies)]

  **TLDR:** Deep chest X-ray classifiers can carry race and sex biases, so the paper targets debiasing for chest X-ray classification. The title names intra-processing and post-processing, while the supplied review context links the work to a pruning strategy for unfairness when the sensitive attribute is unknown. The review positions it as post-pruning mitigation on MIMIC-CXR with race and sex attributes and demographic parity/equalized odds metrics, but numerical results cannot be established from the available record.

  **Date:** 2022

</details>

<p><a href="#-papers">↑ All categories</a></p>

---

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

General fairness foundations, outside the medical catalog:

- [Equality of Opportunity in Supervised Learning](https://dl.acm.org/doi/10.5555/3157382.3157469)
- [Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments](https://www.liebertpub.com/doi/10.1089/big.2016.0047)
- [Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification](https://proceedings.mlr.press/v81/buolamwini18a.html)
- [Fairness and Machine Learning: Limitations and Opportunities](https://fairmlbook.org/index.html)
- [The Problem of Infra-Marginality in Outcome Tests for Discrimination](https://dx.doi.org/10.2139/ssrn.2811449)
- [Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness](https://proceedings.mlr.press/v80/kearns18a.html)
- [Unlocking Fairness: a Trade-off Revisited](https://papers.nips.cc/paper/2019/hash/373e4c5d8edfa8b74fd4b6791d0cf6dc-Abstract.html)
- [Is There a Trade-Off Between Fairness and Accuracy? A Perspective Using Mismatched Hypothesis Testing](https://proceedings.mlr.press/v119/dutta20a.html)
- [On Testing and Comparing Fair classifiers under Data Bias](https://arxiv.org/abs/2302.05906)
- [A Possibility in Algorithmic Fairness: Can Calibration and Equal Error Rates be Reconciled?](https://drops.dagstuhl.de/opus/volltexte/2021/13872/)
- [Bias Preservation in Machine Learning: The Legality of Fairness Metrics Under EU Non-Discrimination Law](https://dx.doi.org/10.2139/ssrn.3792772)
- [The Unfairness of Fair Machine Learning: Levelling Down and Strict Egalitarianism by Default](https://ssrn.com/abstract=4331652)
- [Confounding Factors Need to be Accounted for in Assessing Bias by Machine Learning Algorithms](https://doi.org/10.1038/s41591-022-01847-7)
- [Inherent Tradeoffs in Learning Fair Representations](https://jmlr.org/papers/v23/21-1427.html)
- [On (Assessing) the Fairness of Risk Score Models](https://doi.org/10.1145/3593013.3594045)

## 📣 Community and Updates

- [FAIMI](https://faimi-workshop.github.io/) · [Resources](https://faimi-workshop.github.io/resources/)
- [FAIMI programme discovery leads](docs/workshop-candidates.md)
- [Weekly review packet](reports/review-latest.md) · [review instructions](docs/review-workflow.md) · [Chinese screening evidence](reports/latest.md)
- [Source audit](docs/source-audit-2026-11-04.md) · [original catalog archive](docs/legacy-catalog.md)
- [Weekly automation guide](docs/literature-automation.md): candidate review packets update every Sunday at 10:07 Asia/Shanghai; new papers enter this README only after explicit maintainer approval.

## ⚖️ License

New catalog annotations: [CC BY 4.0](LICENSE-CONTENT). Automation code: [MIT](LICENSE). Referenced papers and original materials retain their own rights.

## 📖 Citation

Please cite the [systematic review](https://doi.org/10.1038/s41746-024-01276-5) when using its taxonomy, and [CITATION.cff](CITATION.cff) for this catalog.

## 🤝 Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Supply an original paper record, publication date, three English TLDR sentences and evidence for the methodology label. Chinese screening notes belong in reports.

## ✉️ Contact

Zikang Xu · zikangxu@mail.ustc.edu.cn
