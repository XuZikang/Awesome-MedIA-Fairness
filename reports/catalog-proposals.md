# 主目录筛选判断证据

机器建议及中文证据，仅供审核；必须由维护者明确通过后才加入主 README。请填写 review-latest.md 或按文章编号回复助手。

## Learning through Capacity Awareness to Minimize Hospital Readmissions

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation

```markdown
- (*arXiv'26*) **Learning through Capacity Awareness to Minimize Hospital Readmissions**
  [[📝 Paper](https://arxiv.org/abs/2611.11493)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Bias mechanisms + Evaluation + Mitigation` · `Stage: Pre-processing` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文明确将再入院风险预测与出院决策结合，针对弱势群体的删失偏差，定义种族分组并实施仿真测量与政策比较，满足五项纳入标准。
```

### 方法证据

- algorithm：periodically retrained readmission risk predictors
- evaluation：we perform 25-50 Monte Carlo simulations for each experiment
- fairness：can exhibit censoring bias for vulnerable patients
- groups：by group (Caucasian and African American)
- medical：hospital discharge decisions informed by readmission risk

[全文证据](https://arxiv.org/html/2611.11493v1)

## Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*arXiv'26*) **Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits**
  [[📝 Paper](https://arxiv.org/abs/2611.23657)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Theory and measurement` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 文章明确以30天再入院风险预测为临床任务，审计多种模型并系统测量数值执行契约对人口学公平指标及审计判定的影响；包含种族/性别/年龄分层实证和稳定性协议，属于医学算法公平性评测方法贡献。
```

### 方法证据

- algorithm：It audits three tabular model families and two open-weight language models
- evaluation：At the frozen thresholds, strict FP32 changed none of the 4B model’s 204,204 decisions on three GPUs.
- fairness：the demographic-parity gap, the highest minus the lowest selection rate; the equalized-odds gap
- groups：Groups are race and sex for ACS, derived race, ethnicity and sex for HMDA, and race, sex and age band for Diabetes.
- medical：The label is readmission within 30 days, the outcome that readmission risk models predict

[全文证据](https://arxiv.org/html/2611.23657v1)

## Beyond Mean Absolute Error: Ancestry-Stratified Calibration and Explainability for Warfarin Dosing Models.

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*Paper'26*) **Beyond Mean Absolute Error: Ancestry-Stratified Calibration and Explainability for Warfarin Dosing Models.**
  [[📝 Paper](https://europepmc.org/article/MED/42930805)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Bias mechanisms` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文显示该文针对华法林稳定剂量预测这一临床任务，系统评估多种ML模型，并明确实施按祖先标签的留一组验证、亚组校准覆盖率和分层SHAP分析，提供了具体公平性测量与机制证据，符合纳入标准。
```

### 方法证据

- algorithm：Nine model architectures are trained on each of the three feature sets (clinical, genetic, combined) on identical splits.
- evaluation：Empirical coverage is reported overall and per ancestry subgroup, for both methods.
- fairness：MAPIE is well-calibrated overall but hides a per-ancestry fairness gap.
- groups：Groups are the Race (Reported) label in IWPC-6256 (14 labels clear the threshold)
- medical：predicting the stable dose from demographics, comorbidities, medications, and genotype

[全文证据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13706061/fullTextXML)

## A Dynamic Inventory Rationing Model for Last-Mile Delivery of Medication in Liberia's Community Health Program

年度：2026；主题：Fairness Evaluation and Benchmarking、In-processing Mitigation

```markdown
- (*arXiv'26*) **A Dynamic Inventory Rationing Model for Last-Mile Delivery of Medication in Liberia's Community Health Program**
  [[📝 Paper](https://arxiv.org/abs/2610.32051)]
  **Metadata:** `Domain: Healthcare operations` · `Focus: Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Site and geography` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 五项证据均满足：针对儿童疟疾药物配给，使用深度神经网络策略并以α-公平效用约束，明确比较不同地点群体的成本与公平性；属医疗健康运营中的算法公平方法学，故建议纳入。
```

### 方法证据

- algorithm：using deep neural networks to approximate the value function and its gradient
- evaluation：our policy reduces operating costs by about 6% relative to the strongest benchmark
- fairness：The allocation problem must balance these considerations while accounting for fairness across locations.
- groups：across the populations served by the CHAs and the health facility
- medical：Focusing on malaria cases among children under the age of five

[全文证据](https://arxiv.org/html/2610.32051v1)

## Data augmentation for the generalizability and transportability of fairness in a clinical heart failure algorithm

年度：2026；主题：Fairness Evaluation and Benchmarking、Pre-processing Mitigation

```markdown
- (*arXiv'26*) **Data augmentation for the generalizability and transportability of fairness in a clinical heart failure algorithm**
  [[📝 Paper](https://arxiv.org/abs/2611.15618)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Mitigation` · `Stage: Pre-processing` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文以心衰住院死亡预测为临床任务，训练LR/RF/MP并比较SMOTE、CTGAN、重加权和过采样，按种族/族裔分组进行模拟与真实数据公平性评估；属于原始实证方法学评估，符合五项纳入标准。
```

### 方法证据

- algorithm：We trained LR, RF, and MP algorithms to estimate in-hospital mortality.
- evaluation：We present an empirical evaluation of synthetic data augmentation for fairness in tabular data using simulation studies
- fairness：we investigate whether data augmentation improves fairness
- groups：Race and ethnicity information was used for our data augmentation methods and evaluation
- medical：estimating the in-hospital mortality of patients hospitalized with heart failure

[全文证据](https://arxiv.org/html/2611.15618v1)

## Preoperative Mortality Risk Prediction and Equity Using Preoperative Score to Predict Postoperative Mortality in a Diverse US Surgical Population: Retrospective Cohort Study.

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*Paper'26*) **Preoperative Mortality Risk Prediction and Equity Using Preoperative Score to Predict Postoperative Mortality in a Diverse US Surgical Population: Retrospective Cohort Study.**
  [[📝 Paper](https://europepmc.org/article/MED/43050561)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Bias mechanisms` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 评估POSPOM在多样化美国手术人群中的死亡预测及种族/民族亚组公平性，属任务特定算法公平审计；虽事件少且无缓解，仍符合纳入标准。
```

### 方法证据

- algorithm：The Preoperative Score to Predict Postoperative Mortality (POSPOM) is a validated, point-based tool
- evaluation：the POSPOM model demonstrated an AUC of 0.764 for 30-day mortality
- fairness：To evaluate model fairness and calibration across different demographic strata, a stratified analysis was conducted
- groups：Race was categorized as White, Black, Asian, or other, and ethnicity was coded as a binary variable
- medical：estimates postoperative mortality using only preoperative variables, including age, comorbidities, and surgical procedure type

[全文证据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13781298/fullTextXML)

## Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus

年度：2026；主题：Bias Mechanisms and Measurement、Post-processing Mitigation

```markdown
- (*arXiv'26*) **Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus**
  [[📝 Paper](https://arxiv.org/abs/2611.22668)]
  **Metadata:** `Domain: X-ray` · `Focus: Bias mechanisms + Mitigation` · `Stage: Post-processing` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 文本明确在CheXpert胸片二分类上评估CHORD，使用SubPopBench分组并以WGA衡量，报告WGA 71.43%对ERM 31.21%，具备医学任务、算法、公平性、分组与实证五要素；虽为通用方法但有明确医学任务评估。
```

### 方法证据

- algorithm：we propose CHORD (Cross-view Harmonic Outlier Reversal for Debiasing), a multi-view framework
- evaluation：CHORD obtains a WGA of 71.43%
- fairness：Deep models often rely on spurious correlations that fail on underrepresented groups.
- groups：we adopt the binary task and group construction of SubPopBench
- medical：CheXpert \[ 23 \] contains over 200,000 chest radiographs; we adopt the binary task

[全文证据](https://arxiv.org/html/2611.22668v1)

## Multidimensional Suicide Risk Assessment with Machine Learning using Electronic Health Records

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation

```markdown
- (*arXiv'26*) **Multidimensional Suicide Risk Assessment with Machine Learning using Electronic Health Records**
  [[📝 Paper](https://arxiv.org/abs/2611.03357)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Mitigation + Bias mechanisms` · `Stage: Pre-processing` · `Attributes: Age` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 文章在明确的自杀风险临床预测任务中，报告了按年龄组的性能下降并采用年龄匹配重采样减少年龄混杂，属于特定任务下的子群公平性评测与预处理偏倚缓解，故建议纳入。
```

### 方法证据

- algorithm：Logistic regression, random forest, and XGBoost classifiers are evaluated
- evaluation：Table V reports the test size, precision, recall, and F1 score for the calibrated XGBoost classifier within each age group.
- fairness：Performance decreases for older age groups, with the largest declines occurring among patients aged 76 years or older.
- groups：The age groups are 18–25, 26–35, 36–45, 46–55, 56–65, 66–75, 76–85, and 86+
- medical：Suicide prevention remains a critical public health challenge

[全文证据](https://arxiv.org/html/2611.03357v1)

## Contrastive fine-tuning against stain and scanner bias improves robustness and downstream performance across pathology foundation models

年度：2026；主题：Bias Mechanisms and Measurement、In-processing Mitigation、Fairness Evaluation and Benchmarking

```markdown
- (*arXiv'26*) **Contrastive fine-tuning against stain and scanner bias improves robustness and downstream performance across pathology foundation models**
  [[📝 Paper](https://arxiv.org/abs/2611.10093)]
  **Metadata:** `Domain: Histopathology` · `Focus: Bias mechanisms + Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Site and geography + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 该文为原创方法学研究，明确针对病理基础模型编码的扫描仪/中心偏倚，提出LoRA对比微调干预，并在PathoROB、PLISM、HEST、CPTAC、THUNDER上实证评估；分组为采集条件/中心而非人口学属性，但属于医学影像site/scanner bias机制与in-processing mitigation，故建议纳入。
```

### 方法证据

- algorithm：We apply SPECTRA to a diverse set of pathology foundation models
- evaluation：Mean RI increases in all cases
- fairness：their representations have been shown to encode scanner- and site-specific biases
- groups：we hold out two scanners (GT450, S210) and three stains (HRH, KR, MY)
- medical：digital pathology-based cancer diagnosis, biomarker prediction, or prognostic assessment

[全文证据](https://arxiv.org/html/2611.10093v1)

## Federated Transfer Learning for Medical Image Classification under Mixed Skew

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、In-processing Mitigation

```markdown
- (*arXiv'26*) **Federated Transfer Learning for Medical Image Classification under Mixed Skew**
  [[📝 Paper](https://arxiv.org/abs/2611.05035)]
  **Metadata:** `Domain: Dermoscopy` · `Focus: Bias mechanisms + Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Site and geography` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 论文在医学皮肤病变分类任务中提出PAFP算法，显式报告客户端间平衡准确率方差作为跨中心性能差异指标，并实证展示其降低该差异；满足医学任务、算法、公平性、分组与实证评估五项标准。
```

### 方法证据

- algorithm：We propose the Personalized Aligner Federated Pretrained (PAFP) framework, a pFL approach based on a pre-trained model
- evaluation：we report the mean and standard deviation of the balanced accuracy over 5 independent runs
- fairness：reducing inter-client performance variance roughly six-fold relative to the strongest baseline, yielding accuracy and cross-client equity jointly
- groups：inter-client variance of balanced accuracy, computed within each run
- medical：federated skin-lesion classification problem

[全文证据](https://arxiv.org/html/2611.05035v1)

## Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*arXiv'26*) **Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose**
  [[📝 Paper](https://arxiv.org/abs/2611.15348)]
  **Metadata:** `Domain: Physiological signals` · `Focus: Benchmark + Evaluation + Bias mechanisms` · `Stage: Evaluation` · `Attributes: Age + Sex and gender` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文证据显示：该工作在呼气 eNose 疾病筛查这一具体临床任务上评估 10 种分类算法，并实施了性别与年龄分层 AUC 及仅人口学基线比较，属任务特定的经验性亚组差异测量，符合基准与公平评估类研究；但缺少缓解方法、交叉性分析与明确的公平性定性，覆盖有限。
```

### 方法证据

- algorithm：We systematically evaluate 10 methods spanning four families
- evaluation：Table VI presents results of demographic-only models and subgroup analysis.
- fairness：For hepatitis (B18), classification is substantially better in women (AUC=0.763) than in men (AUC=0.552).
- groups：Split the cohort into male (n=457) and female (n=567) subgroups
- medical：a portable, non-invasive route for disease screening via exhaled breath analysis

[全文证据](https://arxiv.org/html/2611.15348v1)

## Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、In-processing Mitigation

```markdown
- (*arXiv'26*) **Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate**
  [[📝 Paper](https://arxiv.org/abs/2611.22904)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Benchmark + Bias mechanisms + Evaluation + Mitigation` · `Stage: Evaluation` · `Attributes: Site and geography + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文明确给出临床FL任务、8种聚合算法的实证审计、医院间影响与性能差异问题、医院分组及54,214次实证运行，五项标准均满足，故建议纳入。
```

### 方法证据

- algorithm：We conduct an empirical audit of eight standard aggregation rules
- evaluation：we execute 54,214 training runs
- fairness：penalizing the smallest hospital on Heart (Switzerland, 6% share)
- groups：Cleveland 40.9% (199/104), Hungary 35.4% (172/89), VA 17.5% (85/45), Switzerland 6.2% (30/16)
- medical：three realistic cross-silo medical datasets from the FLamby benchmark

[全文证据](https://arxiv.org/html/2611.22904v1)

## Metadata-Conditioned Audio Transformers for Adaptive Respiratory Sound Classification

年度：2026；主题：Bias Mechanisms and Measurement、In-processing Mitigation

```markdown
- (*arXiv'26*) **Metadata-Conditioned Audio Transformers for Adaptive Respiratory Sound Classification**
  [[📝 Paper](https://arxiv.org/abs/2611.03769)]
  **Metadata:** `Domain: Physiological signals` · `Focus: Bias mechanisms + Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Age + Sex and gender + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 满足五条证据：属呼吸音临床分类任务；评估AST算法；明确提出采集异质性与人口学混杂造成的分布偏差及编码/缓解问题；界定了设备、部位、年龄、BMI、性别等分组属性并有GEE测量协议；实施了统计测量与消融实验。方法为原创性的在训练阶段条件化缓解，故按偏差机制测量与In-processing缓解纳入；亚组性能差距缺失列入局限。
```

### 方法证据

- algorithm：We propose a family of metadata-conditioning mechanisms for the Audio Spectrogram Transformer
- evaluation：All statistical tests use Generalized Estimating Equation (GEE) models clustered by patient to account for repeated measures.
- fairness：This heterogeneity introduces acquisition-induced distributional bias that confound the underlying pathological signatures.
- groups：diverse patient demographics including sex, age, BMI, and breathing cycle duration
- medical：Respiratory sound classification from auscultation recordings is confounded by heterogeneous acquisition conditions

[全文证据](https://arxiv.org/html/2611.03769v1)

## SPARCL: Spatially Adaptive Regional Coverage for Active Learning in Chest X-ray Analysis

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation

```markdown
- (*arXiv'26*) **SPARCL: Spatially Adaptive Regional Coverage for Active Learning in Chest X-ray Analysis**
  [[📝 Paper](https://arxiv.org/abs/2610.17808)]
  **Metadata:** `Domain: X-ray + Fundus photography` · `Focus: Bias mechanisms + Evaluation + Mitigation` · `Stage: Pre-processing` · `Attributes: Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文明确将区域级Dice差异表述为解剖公平/空间可靠性，提出SI/PC测量并实证比较多种主动学习策略；满足医学任务、算法评估、公平问题、定义区域分组和测量评估五项标准。
```

### 方法证据

- algorithm：We compare SPARCL against 10 strategies across four categories.
- evaluation：Spatial reliability at a fixed 20% annotation budget on the in-house calcification dataset
- fairness：to quantify anatomical fairness across AL rounds
- groups：Anat-Zone Worst is the lowest pooled Dice over the seven lung zones
- medical：Pixel-level annotation for chest X-ray (CXR) lesion segmentation is expensive

[全文证据](https://arxiv.org/html/2610.17808v2)

## Addressing Bias Early in the AI Lifecycle: Social Determinants of Health in Functional and Cognitive Assessment Labels of Nursing Home Residents

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare

```markdown
- (*arXiv'26*) **Addressing Bias Early in the AI Lifecycle: Social Determinants of Health in Functional and Cognitive Assessment Labels of Nursing Home Residents**
  [[📝 Paper](https://arxiv.org/abs/2611.11535)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Bias mechanisms + Theory and measurement` · `Stage: Evaluation` · `Attributes: Sex and gender + Socioeconomic status + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文提供具体临床任务和原始标签公平性审计，实施DI/SPD与置信区间测量，覆盖多个SDoH属性；虽无模型训练，但直接针对下游AI训练标签的偏倚机制，符合任务特异性公平审计。
```

### 方法证据

- algorithm：clinical assessments are subsequently used as target variables for AI models
- evaluation：Using electronic health records of 2,407 residents from 12 nursing homes
- fairness：two group fairness metrics, Disparate Impact (DI) and Statistical Parity Difference (SPD)
- groups：four social determinants of health (SDoH)—sex, educational attainment, lifetime work activity and marital status
- medical：functional and cognitive status in a cohort of 2,407 nursing home residents

[全文证据](https://arxiv.org/html/2611.11535v1)

## Explanation-Aware Fairness Beyond Output Parity: Joint Output-Attribution Regularization for Medical Image Classification

年度：2026；主题：Bias Mechanisms and Measurement、In-processing Mitigation、Fairness Evaluation and Benchmarking

```markdown
- (*arXiv'26*) **Explanation-Aware Fairness Beyond Output Parity: Joint Output-Attribution Regularization for Medical Image Classification**
  [[📝 Paper](https://arxiv.org/abs/2611.13052)]
  **Metadata:** `Domain: Dermoscopy + OCT` · `Focus: Bias mechanisms + Evaluation + Mitigation + Theory and measurement` · `Stage: In-processing` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文为原创方法学研究，明确针对皮肤病变分类和青光眼检测，提出算法公平正则化并实施多模型、多数据集的公平性与效用权衡评估，满足五项证据标准。
```

### 方法证据

- algorithm：Across 960 DINOv2-LoRA models on HAM10000 and Harvard-GF datasets for gender and race fairness
- evaluation：960 trained models across five HAM10000 folds and five Harvard-GF training seeds
- fairness：Can attribution-level fairness provide complementary information to output-only regularization
- groups：gender as the sensitive attribute (Female and Male)
- medical：skin-lesion classification with gender and glaucoma detection with race

[全文证据](https://arxiv.org/html/2611.13052v1)

## Do Large Language Models Show Racial and Sex Bias in Pain Management? A Counterfactual Audit of GPT, Claude, Gemini, Llama, DeepSeek and Qwen

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models

```markdown
- (*arXiv'26*) **Do Large Language Models Show Racial and Sex Bias in Pain Management? A Counterfactual Audit of GPT, Claude, Gemini, Llama, DeepSeek and Qwen**
  [[📝 Paper](https://arxiv.org/abs/2611.14935)]
  **Metadata:** `Domain: Clinical NLP and foundation models` · `Focus: Bias mechanisms + Evaluation + Theory and measurement` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender + Intersectional` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文开展疼痛管理与阿片处方的反事实审计，明确评估17个LLM在种族/性别线索下的输出，并实施大规模统计、等效性与噪声下限分析；为原始任务特异性公平性评估。
```

### 方法证据

- algorithm：24 configurations of 17 proprietary and open-weight models
- evaluation：Every one of the 574 severity differences in the study
- fairness：racial and sex disparities in pain assessment
- groups：every combination of four races and two sexes
- medical：whether LLMs assess pain or recommend opioids differently by the patient’s race or sex

[全文证据](https://arxiv.org/html/2611.14935v1)

## Can General-Purpose Generative AI Supply Training Data for Medical Vision Models? A Multimodal Retrospective Study

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation

```markdown
- (*arXiv'26*) **Can General-Purpose Generative AI Supply Training Data for Medical Vision Models? A Multimodal Retrospective Study**
  [[📝 Paper](https://arxiv.org/abs/2611.10484)]
  **Metadata:** `Domain: X-ray + CT + Fundus photography + Ultrasound` · `Focus: Evaluation + Mitigation + Bias mechanisms` · `Stage: Pre-processing` · `Attributes: Age + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 原文明确以合成数据增强代表性不足的年龄/BMI亚组，并报告亚组层面的性能变化，属医学影像中的预加工公平性缓解与偏差测量；同时讨论生成器诱导偏差与属性保真度，满足五项证据标准。
```

### 方法证据

- algorithm：models trained exclusively on synthetic images were externally validated on real-world datasets and compared with models trained with real images
- evaluation：When synthetic data from both underrepresented age groups were added, subgroup performance improved for both the
- fairness：We also investigated whether synthetic data could improve fairness and accuracy of a medical AI model by augmenting underrepresented real-world data.
- groups：The age prediction cohort is categorized into three groups
- medical：pneumonia recognition on chest x-ray (CXR) images, renal calculus detection on CT, and retinal detachment recognition on fundus photographs

[全文证据](https://arxiv.org/html/2611.10484v1)

## Paradoxical inflation of prediction model performance measures in minority patient subgroups: the role of upstream bias.

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*Paper'26*) **Paradoxical inflation of prediction model performance measures in minority patient subgroups: the role of upstream bias.**
  [[📝 Paper](https://europepmc.org/article/MED/42907563)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文报告针对术后持续阿片使用预测的实证公平性评估：比较Black与White患者AUC，并用倾向评分匹配检验基线特征对差异的解释，符合医学任务、算法评估、公平性问题和实证测量要求。
```

### 方法证据

- algorithm：The logistic regression model to predict POU included key demographic, clinical, and patient-reported predictors
- evaluation：Each Black patient was matched to their nearest one or two White patients without duplication
- fairness：differences in baseline patient characteristics between Black and White patients are sufficient to explain much of the observed AUC disparity
- groups：We conducted subgroup analyses for all models to evaluate model performance separately in Black and White subgroups.
- medical：predicting persistent opioid use (POU) after surgery

[全文证据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13687106/fullTextXML)

## The Predictability Bias of Joint-Embedding Predictive Learning in Medical Imaging

年度：2026；主题：Bias Mechanisms and Measurement

```markdown
- (*arXiv'26*) **The Predictability Bias of Joint-Embedding Predictive Learning in Medical Imaging**
  [[📝 Paper](https://arxiv.org/abs/2610.13237)]
  **Metadata:** `Domain: CT` · `Focus: Bias mechanisms + Evaluation + Theory and measurement` · `Stage: Evaluation` · `Attributes: Not specified` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文把可预测性偏置定义为算法偏差并实施复放审计，报告病理与解剖的 Skill 差异及病理—对照位移；满足医学任务、算法评估、偏差测量、临床分组比较与实证评估五项标准。无人口学公平属性，故按非受保护分组处理。
```

### 方法证据

- algorithm：We trained TAP-JEPA , a ViT-B/3D model, for 240 epochs on 113,611 thoraco-abdomino-pelvic CT volumes
- evaluation：We then audit the learned predictive pathway by replaying the exact masking, teacher, and predictor computations used during training.
- fairness：Prediction lowers the mean Skill (prevalence-normalized average precision) from 0.388 to 0.271 for pathology, but only from 0.921 to 0.873 for anatomy.
- groups：separating pathology from matched control regions in the same organ
- medical：In computed tomography (CT), recurrent anatomy is predictable from context, whereas the sporadic, localized pathology that determines clinical interpretation often is not.

[全文证据](https://arxiv.org/html/2610.13237v1)

## Feature Scaling Beats Architecture Choice in Offline Respiratory Screening for Low-Resource Clinics

年度：2026；主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking

```markdown
- (*arXiv'26*) **Feature Scaling Beats Architecture Choice in Offline Respiratory Screening for Low-Resource Clinics**
  [[📝 Paper](https://arxiv.org/abs/2610.33030)]
  **Metadata:** `Domain: Physiological signals` · `Focus: Bias mechanisms + Evaluation + Benchmark` · `Stage: Evaluation` · `Attributes: Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文显示该研究在呼吸音分类中实施患者分组评测，测量录音来源与类别的强关联及分采样率召回差异，并给出可复用诊断，属算法偏倚机制与评测证据，满足五项标准。
```

### 方法证据

- algorithm：SVM over 30 summary features (MFCC, ZCR and RMS statistics)
- evaluation：using pre-registered patient-grouped cross-validation (25 runs per configuration)
- fairness：what a source shortcut predicts: the models learned recording provenance as well as disease
- groups：a rate-by-class table and within-class recall by rate
- medical：five-class respiratory-sound corpus of 1,211 clips (asthma, COPD, pneumonia, Bronchial, healthy)

[全文证据](https://arxiv.org/html/2610.33030v1)

## Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*arXiv'26*) **Health-System-Wide Mapping of Demographic Information in Routine Clinical Histopathology**
  [[📝 Paper](https://arxiv.org/abs/2611.09851)]
  **Metadata:** `Domain: Histopathology` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 这是计算病理中原原创性的系统测量研究：在明确人口学子组上，用基础模型加多示例学习实证评估人口学信息的可编码性，并设计多组训练与分层评估对照。五项证据均满足，属公平性测量与偏倚机制工作，且非综述或评论。
```

### 方法证据

- algorithm：using pathology foundation-model representations and multiple-instance learning
- evaluation：with pan-organ mean AUROCs of 0.828 for sex, 0.733 for age group, and 0.662 for self-reported race
- fairness：to systematically map information associated with sex, age group, and self-reported race
- groups：we evaluated sex, age group, and self-reported race across 69 organ–demographic combinations
- medical：analyzed 1.3 million hematoxylin and eosin whole-slide images from 257,322 patients across 25 organs

[全文证据](https://arxiv.org/html/2611.09851v1)

## Technological Integration in Triage With AI and Machine Learning Compared With Conventional Triage and Narrative Synthesis of Telehealth for Patient Prioritization in Emergency and Acute Care Settings: Systematic Review and Meta-Analysis.

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare

```markdown
- (*Paper'26*) **Technological Integration in Triage With AI and Machine Learning Compared With Conventional Triage and Narrative Synthesis of Telehealth for Patient Prioritization in Emergency and Acute Care Settings: Systematic Review and Meta-Analysis.**
  [[📝 Paper](https://europepmc.org/article/MED/42896140)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Bias mechanisms` · `Stage: Evaluation` · `Attributes: Age + Race and ethnicity + Sex and gender + Socioeconomic status + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 文章明确针对成人急诊分诊AI预测，并报告亚组表现和具体的公平影响建模框架，符合综述对特定任务和详细公平分析的双重要求；但公平证据为次要且探索性，证据强度有限。
```

### 方法证据

- algorithm：AI-assisted triage systems demonstrated high pooled discriminative performance
- evaluation：Equity modeling was informed by subgroup-stratified performance differences reported in implementation studies, translating subgroup-specific sensitivity changes into avoided FNs per 10,000 visits within each subgroup
- fairness：Equity considerations are particularly important in AI- and telehealth-enabled triage.
- groups：subgroup performance by age, sex, race/ethnicity, language, and socioeconomic status
- medical：AI-assisted prediction of critical care requirements or clinical deterioration

[全文证据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13679870/fullTextXML)

## Generative Artificial Intelligence in Health Research and Care: A Narrative Review of Applications and Implications for Alzheimer's Disease and Related Dementia.

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、In-processing Mitigation、Clinical NLP and Foundation Models

```markdown
- (*Paper'26*) **Generative Artificial Intelligence in Health Research and Care: A Narrative Review of Applications and Implications for Alzheimer's Disease and Related Dementia.**
  [[📝 Paper](https://europepmc.org/article/MED/42939080)]
  **Metadata:** `Domain: MRI + PET` · `Focus: Benchmark + Bias mechanisms + Evaluation + Mitigation` · `Stage: Multi-stage` · `Attributes: Age + Race and ethnicity + Sex and gender + Socioeconomic status + Site and geography + Other` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 该综述明确以ADRD为医学任务，并在第5节及全球视角中给出语音识别种族差异、认知测验群体偏倚、MRI跨人群迁移F1下降、亚组审计与去偏方法等具体公平性分析，满足综述纳入的两项条件；但属于综述而非原始方法学研究。
```

### 方法证据

- algorithm：Bias in generative AI arises from unrepresentative training data and flawed models.
- evaluation：MRI classifiers trained on ADNI (83% White participants) transferred to a Korean cohort with a zero-shot MCI-class F1 of only 0.34
- fairness：applying fairness-aware methods (such as data reweighting and adversarial debiasing)
- groups：higher word error rates for black speakers than for white speakers
- medical：Alzheimer’s disease and related dementia (ADRD) research and care

[全文证据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13701688/fullTextXML)

## Non-Invasive Blood Glucose Monitoring Using Machine Learning and Optical Approaches: A Systematic Literature Review and a Proposed Framework for Reproducible and Clinically Reliable Research.

年度：2026；主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking

```markdown
- (*Paper'26*) **Non-Invasive Blood Glucose Monitoring Using Machine Learning and Optical Approaches: A Systematic Literature Review and a Proposed Framework for Reproducible and Clinically Reliable Research.**
  [[📝 Paper](https://europepmc.org/article/MED/42944435)]
  **Metadata:** `Domain: Physiological signals` · `Focus: Bias mechanisms + Evaluation` · `Stage: Evaluation` · `Attributes: Age + Other + Race and ethnicity + Sex and gender + Skin tone` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 该文针对无创血糖监测这一具体临床任务，提供实质性算法公平分析：指出黑色素与人口学输入导致的捷径学习机制，并提出肤色记录、亚组分析与跨肤色评估框架；但属文献综合而非原始实验，故按综述类纳入。
```

### 方法证据

- algorithm：at least one machine-learning, deep-learning, or comparable mathematical algorithm used for glucose estimation
- evaluation：we rated 62% of the studies as High risk of shortcut learning
- fairness：fairness evaluation across skin tones and body types
- groups：it can differ by age group, sex, ethnicity, or skin pigmentation
- medical：Diabetes Mellitus (DM) is a condition characterised by elevated blood glucose levels

[全文证据](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13708778/fullTextXML)
