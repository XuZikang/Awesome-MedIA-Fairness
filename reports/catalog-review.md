# 目录分类与英文摘要的中文判断证据

本次合并综述与实证论文，沿用2024系统综述的评估/预处理/训练中/训练后方法框架；每篇保留一个主要位置。原始标识、来源和资源链接保存在 data/catalog.json，README不显示逐条Provenance标记。摘要是原文证据的编辑性概述，不等于实验复现。Qoder已完成37篇；其后额度耗尽的条目由主控根据已读取摘要、原始记录和综述方法描述补齐，不冒充模型调用。

## Fairness-related performance and explainability effects in deep learning models for brain image analysis

- 原始发表日期：2022-08-26
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据摘要，该研究训练CNN预测生物性别，比较White与Black及性别交叉亚组的性能和saliency maps，并分析青春期发育这一种族相关混杂因素。其主要贡献是对已训练模型进行公平性评测和可解释性机制探查，而非修改训练数据、训练目标或预测后处理。证据仅来自摘要，未提供完整实验细节或缓解干预，因此方法归为Fairness Evaluation。

证据短句：
- Performance disparities of the trained CNN between White and Black subjects were analyzed and saliency maps were generated for each subgroup at the intersection of sex and race.
- The classification model demonstrated a significant difference in the percentage of correctly classified White male (90.3 % ± 1.7 % ) and Black male (81.1 % ± 4.5 % ) children.
- We illustrate that unfair models can produce different XAI results between subgroups and that these results may explain potential reasons for biased performance.

原文入口：https://doi.org/10.1117/1.jmi.9.6.061102

## How fair is your graph? exploring fairness concerns in neuroimaging studies

- 原始发表日期：2022
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：分类为 Fairness Evaluation：标题表明其关注神经影像图中的公平性问题，且来源表将其标为 FE-benchmarking；但证据仅有标题和综述语境，没有摘要、方法或结果细节，因此无法确认具体图模型、数据集、公平性指标或发现，也不能判断是否包含缓解干预。

证据短句：
- How fair is your graph? exploring fairness concerns in neuroimaging studies
- FE-benchmarking

原文入口：https://proceedings.mlr.press/v182/ribeiro22a.html

## Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations

- 原始发表日期：2021-12
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该文以胸部X线病理分类为场景，跨三个大型数据集和一个多源数据集审计不同患者群体的漏诊差异，主要贡献是公平性评估与基准评测，而非修改训练数据、训练目标或已训练模型的预测，因此归为 Fairness Evaluation。现有证据仅为标题和摘要，缺少模型细节、完整实验设置和统计检验信息，不能确认缓解干预或因果机制。

证据短句：
- Here, we examine algorithmic underdiagnosis in chest X-ray pathology classification across three large chest X-ray datasets, as well as one multi-source dataset.
- We find that classifiers produced using state-of-the-art computer vision techniques consistently and selectively underdiagnosed under-served patient populations
- the underdiagnosis rate was higher for intersectional under-served subpopulations, for example, Hispanic female patients.

原文入口：https://doi.org/10.1038/s41591-021-01595-0

## Fairness in Cardiac Magnetic Resonance Imaging: Assessing Sex and Racial Bias in Deep Learning-Based Segmentation

- 原始发表日期：2022-04-07
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该研究的主贡献是对已有深度学习分割模型做公平性评估，按种族和性别比较 Dice 分数及双心室容积与功能测量误差，并用回归和 ANCOVA 检查混杂因素。文中没有提出修改训练数据、训练目标或已训练模型预测的缓解干预，因此归为 Fairness Evaluation。可得证据仅为摘要，无法核验全文方法细节或未报告结果。

证据短句：
- To assess sex and racial bias, we compared Dice scores and errors in measurements of biventricular volumes and function between patients grouped by race and sex.
- statistically significant differences in Dice scores between races (white ∼94% vs. minority ethnic groups 86–89%)
- racial bias can exist in DL-based cine CMR segmentation models when training with a database that is sex-balanced but not race-balanced such as the UK Biobank.

原文入口：https://doi.org/10.3389/fcvm.2022.859310

## Gender imbalance in medical imaging datasets produces biased classifiers for computer-aided diagnosis

- 原始发表日期：2020-05-26
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：论文主贡献是评估医学影像数据集中性别失衡对分类器性能的影响，属于公平性评测中的测量与基准式分析；摘要仅说明使用三种深度神经网络架构和两个公开胸部X射线数据集在不同性别失衡条件下进行实证观察，没有提出预处理、训练中或后处理缓解算法，因此不归为 mitigation。证据仅来自主要摘要，无法确认完整实验细节、样本规模或统计显著性。

证据短句：
- Our study sheds light on the importance of gender balance in medical imaging datasets used to train AI systems for computer-assisted diagnosis.
- We found a consistent decrease in performance for underrepresented genders when a minimum balance is not fulfilled.
- based on three deep neural network architectures and two well-known publicly available X-ray image datasets

原文入口：https://doi.org/10.1073/pnas.1919012117

## Algorithmic encoding of protected characteristics in image-based models for disease detection

- 原始发表日期：2021-10-27
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该文的主要贡献是面向图像疾病检测模型的子群公平性评估与机制分析，使用测试集重采样、迁移学习、多任务学习和模型检查来考察受保护特征如何被编码以及与性能差异的关系。这些技术主要作为分析或探测手段，而非以修改训练数据、改变训练目标或后处理已训练模型为主的缓解方法，因此归为 Fairness Evaluation。证据仅来自标题和摘要，缺少全文和具体实验细节，不能据此外推数据集规模、统计显著性或其他结论。

证据短句：
- This article aims to shed some light on these issues by exploring new methodology for subgroup analysis in image-based disease detection models.
- We utilize two publicly available chest X-ray datasets, CheXpert and MIMIC-CXR, to study performance disparities across race and biological sex in deep learning models.
- We confirm subgroup disparities in terms of shifted true and false positive rates which are partially removed after correcting for population and prevalence shifts in the test sets.

原文入口：https://arxiv.org/abs/2110.14755

## Feature Robustness and Sex Differences in Medical Imaging: A Case Study in MRI-Based Alzheimer’s Disease Detection

- 原始发表日期：2022
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：根据摘要，论文在 ADNI MRI 数据上比较手工体积特征逻辑回归与 3D CNN，并通过改变数据划分、训练集性别构成和疾病阶段来评估模型稳健性与性别差异。这属于基准测试与公平性评估，没有提出预处理、训练目标或后处理层面的缓解干预，因此归类为 Fairness Evaluation。证据仅来自标题和摘要，未提供完整实验细节、数据集规模或统计显著性，结论应限于摘要所述范围。

证据短句：
- we compare two classification schemes on the ADNI MRI dataset: a simple logistic regression model using manually selected volumetric features, and a convolutional neural network trained on 3D MRI data.
- we do not observe a clear pattern of improved model performance for the majority group in the training dataset.
- the logistic regression model outperforms the 3D CNN, emphasizing the utility of manual feature specification based on prior knowledge

原文入口：https://doi.org/10.1007/978-3-031-16431-6_9

## Fairness of Classifiers Across Skin Tones in Dermatology

- 原始发表日期：2020
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation, Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据所给系统综述，目标论文列于 FE-benchmarking 行，任务为皮肤科分类，敏感属性为肤色，指标为 AP。现有证据仅包括标题、综述表格行和综述上下文，未提供摘要或全文，因此只能将其主要贡献归类为公平性评估中的基准测试；源元数据虽标注 Pre-processing，但证据不支持将其作为主要缓解干预。

证据短句：
- Dermatology ISIC, SD-198 C Skin tone AP
- which does not find an observable trend between model utility and skin tone

原文入口：https://doi.org/10.1007/978-3-030-59725-2_31

## Improving the Fairness of Chest X-ray Classifiers

- 原始发表日期：2022
- 主要方法：Fairness Evaluation
- 原有阶段标签：Not verified
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://proceedings.mlr.press/v174/zhang22a/zhang22a.pdf

## MEDFAIR: Benchmarking Fairness for Medical Imaging

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该文主贡献是构建医学影像公平性基准框架，系统比较已有算法、数据集和模型选择标准，因此归为 Fairness Evaluation，而非提出新的预处理、处理中或后处理缓解方法。证据仅来自主摘要，未提供具体数据集规模、效应量或统计检验细节，无法进一步判断各缓解方法的临床效果。

证据短句：
- we introduce MEDFAIR, a framework to benchmark the fairness of machine learning models for medical imaging
- the under-studied issue of model selection criterion can have a significant impact on fairness outcomes
- state-of-the-art bias mitigation algorithms do not significantly improve fairness outcomes over empirical risk minimization (ERM)

原文入口：https://arxiv.org/abs/2210.01725

## Detecting Melanoma Fairly: Skin Tone Detection and Debiasing for Skin Lesion Classification

- 原始发表日期：2021
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：摘要把自动肤色标签作为两种 bias unlearning 技术的目标来缓解肤色偏差，主导干预属于训练阶段的偏差遗忘，而不是仅做公平性评估、训练数据预处理或已训练模型的后处理，因此归为 In-processing。肤色自动检测与 ISIC 标注是配套步骤，不改变主导分类。现有证据仅包括标题和主摘要，未提供完整实验设计、样本规模、统计检验或两种去偏技术的实现细节，因此无法核实具体机制和效应大小。

证据短句：
- we propose an efficient yet effective algorithm for automatically labelling the skin tone of lesion images
- We subsequently use these automated labels as the target for two leading bias unlearning techniques towards mitigating skin tone bias.
- unlearning skin tone may improve generalisation and can reduce the performance disparity between melanoma detection in lighter and darker skin tones.

原文入口：https://arxiv.org/abs/2202.02832

## Evaluating subgroup disparity using epistemic uncertainty in mammography

- 原始发表日期：2021-07-06
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该文主要比较不同不确定性量化指标在乳腺X线摄影中揭示种族与扫描仪亚组差异的能力，属于公平性测量与机制发现方向的评估研究。摘要未提出或验证预处理、训练目标修改或已训练模型后处理等缓解干预，因此归类为 Fairness Evaluation。证据仅限标题和摘要，无法核实具体评价指标、统计检验细节或临床部署效果。

证据短句：
- we explore how epistemic uncertainty can be used to evaluate disparity in patient demographics (race) and data acquisition (scanner) subgroups for breast density assessment
- on a dataset of 108,190 mammograms collected from 33 clinical sites
- even if aggregate performance is comparable, the choice of uncertainty quantification metric can significantly the subgroup level

原文入口：https://arxiv.org/abs/2107.02716

## Model Selection's Disparate Impact in Real-World Deep Learning Applications

- 原始发表日期：2021-04-01
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该文归为 Fairness Evaluation（公平性评估），因为其核心是对模型选择阶段偏差来源的测量与实证检验，而非修改训练数据、训练目标或已训练模型。摘要表明作者用真实医学影像数据训练的深度学习模型检验指标选择对模型选择结果的影响，属于评测与机制分析。证据仅为标题和摘要，未给出数据集规模、模型细节或定量比较，故不能推断具体差异幅度、统计显著性、性能提升或临床效益。

证据短句：
- human preferences in model selection, remains under-explored in terms of its role in disparate impact across demographic groups
- Using a deep learning model trained on real-world medical imaging data, we verify our claim empirically
- choice of metric for model comparison, especially those that do not take variability into account, can significantly bias model selection outcomes

原文入口：https://arxiv.org/abs/2104.00606

## Harvard Glaucoma Fairness: A Retinal Nerve Disease Dataset for Fairness Learning and Fair Identity Normalization

- 原始发表日期：2023-06-15
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该论文的主要贡献是发布Harvard-GF视网膜青光眼2D/3D影像数据集，并提供平衡种族分组和equity-scaled性能度量，属于公平性基准与评测资源。摘要虽提出并比较了fair identity normalization这一干预方法，但其定位是展示数据集效用，且证据仅来自摘要，缺少完整实验设置与结果细节，因此主类归为Fairness Evaluation。

证据短句：
- we introduce Harvard Glaucoma Fairness (Harvard-GF), a retinal nerve disease dataset with both 2D and 3D imaging data and balanced racial groups for glaucoma detection
- We also propose a fair identity normalization (FIN) approach to equalize the feature importance between different identity groups.
- Our FIN approach is compared with various the-state-of-the-art fairness learning methods with superior performance in the racial, gender, and ethnicity fairness tasks with 2D and 3D imaging data

原文入口：https://arxiv.org/abs/2306.09264

## Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation

- 原始发表日期：2021
- 主要方法：Pre-processing
- 原有阶段标签：Evaluation, In-processing, Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：归为 Pre-processing：可归属于目标论文的直接证据显示，其在 UM-pre-re-distribution 下被记录，综述正文也明确称 Puyol-Antón 等采用分层批重采样并报告公平性改善。同一研究还出现在 in-adversarial 索引中，说明可能涉及对抗式 in-processing，但按“主要贡献”原则，当前证据支持的主干预是训练数据重采样。证据限制在于仅有标题、综述正文和表格抽取，缺少摘要与全文实验细节、效应量和样本量，因此无法核实完整流程，也不能把其他阶段夸大为已确证的主方法。

证据短句：
- Fairness in Cardiac MR Image Analysis: An Investigation of Bias Due to Data Imbalance in Deep Learning Based Segmentation
- Puyol-Antón et al. 3  adopt stratified batch resampling on the baseline model and notice a significant improvement in fairness.
- 2021 3 Heart MRI UK BioBank S Race, Sex ΔDSC, SER-DSC, STD-DSC

原文入口：https://doi.org/10.1007/978-3-030-87199-4_39

## Detecting and preventing shortcut learning for fair medical ai using shortcut testing (short)

- 原始发表日期：2022-07-21
- 主要方法：In-processing
- 原有阶段标签：Evaluation, Pre-processing
- 证据可用性：已读取原始摘要

判断：摘要明确以多任务学习提出用于评估并缓解临床机器学习系统捷径学习的方法，并在放射学与皮肤病学任务中演示，属于通过改变训练目标或学习表征的在处理阶段干预；虽然标题和摘要也强调评估与机制发现，但主要干预手段是多任务学习，且仅有摘要证据，无法确认具体网络结构、数据集规模或定量效果。

证据短句：
- Using multi-task learning, we propose the first method to assess and mitigate shortcut learning as a part of the fairness assessment of clinical ML systems
- demonstrate its application to clinical tasks in radiology and dermatology
- our approach reveals instances when shortcutting is not responsible for unfairness

原文入口：https://doi.org/10.1038/s41467-023-39902-7

## AI Fairness via Domain Adaptation

- 原始发表日期：2021-03-15
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：已读取原始摘要

判断：根据摘要，论文的核心干预是在训练阶段通过生成模型扩充训练集，为代表性不足人群合成更多样本，以缓解导致偏见的训练数据不平衡，因此归类为 Pre-processing，而不是改变训练目标或修改已训练模型。证据仅为主摘要，未提供数据集规模、具体公平性指标、效应量或统计显著性；不能据此断言临床收益或完整实验细节。

证据短句：
- This method uses domain adaptation via training set enhancement to tackle bias-causing training data imbalance.
- it uses generative models that allow the generation of more synthetic training samples for underrepresented populations.
- Our experiments show that starting with an originally biased AMD diagnostics model the method has the ability to improve fairness.

原文入口：https://arxiv.org/abs/2104.01109

## CIRCLe: Color Invariant Representation Learning for Unbiased Classification of Skin Lesions

- 原始发表日期：2023
- 主要方法：In-processing
- 原有阶段标签：In-processing, Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-25069-9_14

## CheXclusion: Fairness gaps in deep chest X-ray classifiers

- 原始发表日期：2021-01-01
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation, Pre-processing
- 证据可用性：已读取原始摘要

判断：原文的主要贡献是在多个胸片数据集上训练诊断分类器，并按性别、年龄、种族和保险类型比较TPR差异，属于Xu等综述中的公平性评测与基准测试。多源数据聚合虽提示可能减小差异，但原文没有将其作为主要干预方法进行验证，因此不宜归为预处理。可用证据仅为摘要，无法进一步确认完整实验设置或临床意义。

证据短句：
- We train convolution neural networks to predict 14 diagnostic labels in 3 prominent public chest X-ray datasets: MIMIC-CXR, Chest-Xray8, CheXpert, as well as a multi-site aggregation of all those datasets.
- We demonstrate that TPR disparities exist in the state-of-the-art classifiers in all datasets, for all clinical tasks, and all subgroups.
- A multi-source dataset corresponds to the smallest disparities, suggesting one way to reduce bias.

原文入口：https://pubmed.ncbi.nlm.nih.gov/33691020/

## RadFusion: Benchmarking Performance and Fairness for Multimodal Pulmonary Embolism Detection from CT and EHR

- 原始发表日期：2021-11-23
- 主要方法：Fairness Evaluation
- 原有阶段标签：Pre-processing
- 证据可用性：已读取原始摘要

判断：该文标题和摘要的主贡献是构建RadFusion多模态基准数据集，并对多种融合模型按性别、种族/族裔和年龄进行公平性评估，属于Xu等综述中的benchmarking/measurement类公平性评估。综述表虽将其列入UM-pre-aggregation，但所给摘要未充分描述具体的预处理干预或新的缓解算法，因此不把数据聚合的归类当作主要贡献，方法判为Fairness Evaluation。

证据短句：
- we present RadFusion, a multimodal, benchmark dataset of 1794 patients with corresponding EHR data and high-resolution computed tomography (CT) scans labeled for pulmonary embolism.
- We evaluate several representative multimodal fusion models and benchmark their fairness properties across protected subgroups
- Our results suggest that integrating imaging and EHR data can improve classification performance and robustness without introducing large disparities in the true positive rate between population groups.

原文入口：https://arxiv.org/abs/2111.11665

## Improving fairness in image classification via sketching

- 原始发表日期：2022
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：该文在系统综述的分类表中被归为 UM-pre-harmonization，核心证据是使用语言引导的素描模型把输入图像转换为素描，属于对输入数据/训练数据的预处理干预，而非改变训练目标或对已训练模型及预测做后处理。现有记录仅来自综述中的概括和分类表，未提供数据集规模、模型细节或完整定量结果，因此方法阶段可判为 Pre-processing，但具体效果强弱与统计显著性不能从可用记录确立。

证据短句：
- use a language-guided sketching model to transform the input images into sketches
- Their result shows less disparity among subgroups, which indicates the potential of data harmonization in mitigating unfairness.

原文入口：https://openreview.net/forum?id=Rq2vt3tnAK9

## Training confounder-free deep learning models for medical applications

- 原始发表日期：2020-11-26
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：根据主要摘要，论文的主要贡献是在端到端训练中学习对混杂因素不变的特征，并同时考虑混杂因素与预测结局的相关性，属于训练目标或表征层面的 In-processing；系统综述表也将其归入 UM-in-adversarial。证据仅限标题和主要摘要，未见完整方法细节、数据集规模或统计结果，因此不据此断言具体对抗架构，也不把任何后处理步骤当作主要贡献。

证据短句：
- Confounders affect the relationship between input data (e.g., brain MRIs) and output variables (e.g., diagnosis).
- In this article, we introduce an end-to-end approach for deriving features invariant to confounding factors while accounting for intrinsic correlations between the confounder(s) and prediction outcome.
- The results show that our method can accurately predict while reducing biases associated with confounders.

原文入口：https://doi.org/10.1038/s41467-020-19784-9

## Representation Learning with Statistical Independence to Mitigate Bias

- 原始发表日期：2021-01
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：摘要明确显示该方法通过对抗训练和新的对抗损失改变训练目标与学习表示，使特征兼顾任务判别力和与受保护变量的统计独立性，因此归为 In-processing。现有证据仅覆盖标题、摘要及综述表中的 UM-in-adversarial 归类，未见全文、数据集规模、性能增益或显著性细节，故不能确认临床效果或其他阶段的具体作用。

证据短句：
- adversarial training with two competing objectives to learn features that have (1) maximum discriminative power with respect to the task and (2) minimal statistical mean dependence with the protected (bias) variable(s).
- Our approach does so by incorporating a new adversarial loss function that encourages a vanished correlation between the bias and the learned features.
- Our results show that the learned features by our method not only result in superior prediction performance but also are unbiased.

原文入口：https://doi.org/10.1109/wacv48630.2021.00256

## Risk of Training Diagnostic Algorithms on Data with Demographic Bias

- 原始发表日期：2020
- 主要方法：In-processing
- 原有阶段标签：Evaluation, In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：题目只表明研究训练于人口学偏倚数据上的诊断算法风险；来源元数据和综述表格将其归入 UM-in-adversarial（对抗式在训练中缓解），并标注皮肤科 ISIC、年龄与性别及 ΔAUC，但未提供摘要、方法或结果细节。因此主方法按表格证据归为 In-processing，同时说明证据仅限标题与表格分类，不能据此断言具体网络结构、数据规模或性能收益。

证据短句：
- Risk of Training Diagnostic Algorithms on Data with Demographic Bias
- UM-in-adversarial
- 2020 74 Dermatology ISIC C Age, Sex ΔAUC

原文入口：https://doi.org/10.1007/978-3-030-61166-8_20

## Estimating and improving fairness with adversarial learning

- 原始发表日期：2021
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：系统综述的表格将目标论文归为“UM-in-adversarial”，并在对抗式 in-processing 段落提到其额外加入一个分支，在不知道敏感属性的测试集上预测公平程度。主贡献因此属于通过对抗学习改变训练目标或学习表征的 in-processing，而不是修改训练数据的预处理或修改已训练模型及其预测的后处理。证据限制是仅有标题、综述性描述和表格归类，未提供原文摘要、数据集、指标或实验结果，所以方法细节只能按综述保守概括，效果不能确认。

证据短句：
- The adversarial architecture is the most common in-processing method
- add an extra branch except for the adversarial one, which predicts the degree of fairness on the test set without knowing the sensitive attributes.
- UM-in-adversarial

原文入口：https://oecd.ai/fr/catalogue/metric-use-cases/estimating-and-improving-fairness-with-adversarial-learning

## Technical Challenges for Training Fair Neural Networks

- 原始发表日期：2021-02-12
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：原文摘要聚焦在深度网络中施加公平性约束时出现的过拟合与意外后果，属于在训练目标或优化中引入公平约束的 in-processing 研究。摘要只说明在面部识别和自动医学诊断数据上实验，未给出具体数据集规模、结果数值或独立临床验证，且全文未读，因此证据有限。

证据短句：
- we observe that these large models overfit to fairness objectives, and produce a range of unintended and undesirable consequences.
- We conduct our experiments on both facial recognition and automated medical diagnosis datasets using state-of-the-art architectures.
- While fairness constraints have been studied extensively for classical models, the effectiveness of methods for imposing fairness on deep neural networks is unclear.

原文入口：https://arxiv.org/abs/2102.06764

## On the fairness of privacy-preserving representations in medical applications

- 原始发表日期：2020
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：综述表将该研究列入训练时表示学习方法；目前缺少原始摘要，不据此宣称下游公平性得到提升。

证据短句：
- On the fairness of privacy-preserving representations in medical applications

原文入口：https://www.springerprofessional.de/on-the-fairness-of-privacy-preserving-representations-in-medical/18418170

## On Fairness of Medical Image Classification with Multiple Sensitive Attributes via Learning Orthogonal Representations

- 原始发表日期：2023-01-04
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：主要贡献是在训练过程中学习公平表示，通过对目标表示与多敏感属性表示施加列空间和行空间正交约束来改变学习到的特征表示，因此归类为 In-processing。证据仅来自标题和摘要，未提供具体数值结果或完整实验细节，文中只说明在 CheXpert 上进行了实验。

证据短句：
- we propose a novel method for fair representation learning with respect to multi-sensitive attributes
- We pursue the independence between target and multi-sensitive representations by achieving orthogonality in the representation space.
- The effectiveness of the proposed method is demonstrated with extensive experiments on the CheXpert dataset.

原文入口：https://arxiv.org/abs/2301.01481

## FairDisCo: Fairer AI in Dermatology via Disentanglement Contrastive Learning

- 原始发表日期：2022-08-22
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：仅依据标题与主要摘要，未读取全文或补充实验细节。方法归为 In-processing，因为其主要干预是在训练中通过解耦表征和对比学习分支移除肤色敏感信息并改进特征提取，属于改变学习表征或优化过程；重采样、重加权和 attribute-aware 是基线比较，不是本文主贡献。摘要仅报告“更公平且更优”的方向性结论，未提供具体数值、显著性、完整数据集规模或临床效用证据，因此结果细节受限。

证据短句：
- a disentanglement deep learning framework with contrastive learning that utilizes an additional network branch to remove sensitive attributes
- We compare FairDisCo to three fairness methods, namely, resampling, reweighting, and attribute-aware, on two newly released skin lesion datasets with different skin types
- Extensive experimental evaluation demonstrates the effectiveness of FairDisCo, with fairer and superior performance on skin lesion classification tasks.

原文入口：https://arxiv.org/abs/2208.10013

## FairAdaBN: Mitigating unfairness with adaptive batch normalization and its application to dermatological disease classification

- 原始发表日期：2023-03-15
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：主要贡献是在训练阶段让批归一化随敏感属性自适应，并加入限制子组间统计均等的损失，改变学习到的表示与优化目标，属于 In-processing；FATE 是评估指标而非缓解阶段。证据仅来自标题与摘要，未读全文，无法核实数据集名称、实现细节、效应量与统计显著性，因此不宣称临床收益或泛化结论。

证据短句：
- we propose FairAdaBN by making batch normalization adaptive to sensitive attribute.
- we derive a novel loss function that restrains statistical parity between subgroups on mini-batches, encouraging the model to converge with considerable fairness.
- Experiments on two dermatological datasets show that our proposed method outperforms other methods on fairness criteria and FATE.

原文入口：https://arxiv.org/abs/2303.08325

## On the Fairness of Swarm Learning in Skin Lesion Classification

- 原始发表日期：2021
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：系统综述将 Fan 等的目标论文归入 UM-in-MISC/In-processing，并描述其通过让每个 swarm learning 客户端只包含同一敏感属性的样本来调整联邦训练过程。现有材料仅有题名、表格分类和这一句方法描述，没有目标论文的结果数据，故公平性改善幅度、统计显著性或临床意义均无法确定。

证据短句：
- where each client in the swarm learning only consists of samples with the same sensitive attribute.
- 2021 88 Dermatology ISIC, Fitzpatrick-17k C Age, Sex DP, EqOdds
- On the Fairness of Swarm Learning in Skin Lesion Classification

原文入口：https://doi.org/10.1007/978-3-030-90874-4_12

## FairPrune: Achieving Fairness Through Pruning for Dermatological Disease Diagnosis

- 原始发表日期：2022
- 主要方法：Post-processing
- 原有阶段标签：Post-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-16431-6_70

## Debiasing Deep Chest X-Ray Classifiers using Intra- and Post-processing Methods

- 原始发表日期：2022
- 主要方法：Post-processing
- 原有阶段标签：Post-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：证据仅含论文标题、系统综述中的表格条目和讨论性上下文，未提供摘要或全文。来源元数据将阶段标为 Post-processing，综述表又将同一文献同时列在 UM-in-constraints 与 UM-post-pruning，正文提到其在敏感属性未知时使用剪枝，因此按元数据和后处理剪枝线索归为 Post-processing；其余阶段与实验效果无法从现有记录确认。

证据短句：
- Debiasing Deep Chest X-Ray Classifiers using Intra- and Post-processing Methods
- Pruning tries to satisfy fairness criteria by distilling the model’s parameters.
- UM-post-pruning 2022 79 Chest X-ray MIMIC-CXR C Race, Sex DP, EqOdds

原文入口：https://proceedings.mlr.press/v182/marcinkevics22a.html

## A Study of Demographic Bias in CNN-Based Brain MR Segmentation

- 原始发表日期：2022
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：系统综述将目标论文归入 FE-benchmarking：任务为脑 MRI 分割，敏感属性为种族与性别，指标为 ΔDSC。证据仅来自综述表格及叙述，未提供摘要或全文，也未显示训练数据修改、训练目标改变或已训练模型及预测后处理，因此主贡献判为公平性评估而非不公平缓解。

证据短句：
- examine fairness by comparing the average Dice Similarity Coefficient (DSC) on each spatial location.
- although unfairness exists in some regions severely, in other regions the DSC shows little or no disparity

原文入口：https://doi.org/10.1007/978-3-031-17899-3_2

## An Investigation into the Impact of Deep Learning Model Choice on Sex and Race Bias in Cardiac MR Segmentation

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：系统综述表格将目标论文归入FE-benchmarking，任务为心脏MR分割，数据为UK Biobank，敏感属性为Race和Sex，指标为ΔDSC，因此主贡献是公平性评估与基准测试。现有证据仅为标题和综述中的归类片段，未提供摘要或全文，无法确认具体模型选择、实验设置、统计结果或是否包含缓解干预。

证据短句：
- 2022 4 Heart MRI UK Biobank S Race, Sex ΔDSC
- FE-benchmarking

原文入口：https://doi.org/10.1007/978-3-031-45249-9_21

## Revisiting skin tone fairness in dermatological lesion classification

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：证据仅包含标题、系统综述表格中的 FE-benchmarking 分类及皮肤色调属性记录，没有摘要或方法细节。该记录表明论文的主要贡献是皮肤色调公平性基准测试与评估，而非修改训练数据、训练目标或已训练模型的后处理干预，因此归为 Fairness Evaluation。由于缺乏可提取的结果，不能确认具体性能差异。

证据短句：
- Target paper: Revisiting skin tone fairness in dermatological lesion classification
- 2023 48 Dermatology ISIC C Skin tone ΔBACC
- "section": "FE-benchmarking", "reference": "CR48"

原文入口：https://doi.org/10.1007/978-3-031-45249-9_24

## Algorithmic encoding of protected characteristics in chest X-ray disease detection models

- 原始发表日期：2023-03
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：论文的主要贡献是面向胸部X线疾病检测模型的亚组分析与机制探查，属于公平性评估中的测量、基准分析和偏差来源追踪，而不是修改训练数据、训练目标或已训练模型。摘要明确以CheXpert和MIMIC-CXR研究种族与生理性别差异，并用测试集重采样、迁移学习、多任务学习和模型检查来评估受保护特征的编码情况。证据仅包含标题、摘要和系统综述表，未提供全文，因此无法确认具体样本量、统计显著性、模型细节或临床效益。

证据短句：
- exploring methodology for subgroup analysis in image-based disease detection models
- We confirm subgroup disparities in terms of shifted true and false positive rates which are partially removed after correcting for population and prevalence shifts in the test sets.
- transfer learning alone is insufficient for establishing whether specific patient information is used for making predictions.

原文入口：https://doi.org/10.1016/j.ebiom.2023.104467

## Algorithmic Fairness of Machine Learning Models for Alzheimer Disease Progression

- 原始发表日期：2023-11-07
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：根据摘要，该文的核心是评估既有纵向预测模型在性别、族裔和种族群体间的公平性指标，属于公平性评估与基准测试；没有证据表明其提出数据预处理、训练目标修改或对已训练模型的预测后处理干预，因此不归为三类缓解方法。分类依据仅限标题与摘要，全文方法细节、统计检验和可复现性无法从现有记录确认。

证据短句：
- To characterize the algorithmic fairness of longitudinal prediction models for AD progression.
- Fairness was quantified across sex, ethnicity, and race groups.
- In this study, models were accurate in aggregate but failed to satisfy fairness metrics.

原文入口：https://doi.org/10.1001/jamanetworkopen.2023.42203

## An Investigation into Race Bias in Random Forest Models Based on Breast DCE-MRI Derived Radiomics Features

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：该文主要考察基于乳腺DCE-MRI影像组学特征的随机森林模型是否存在种族偏倚，并报告种族可识别性与按种族分组的性能差异，属于公平性评测与基准分析；摘要未提出对训练数据、训练目标或已训练模型预测的缓解干预，且仅有摘要级证据，无法确认样本量、统计检验或临床效用。

证据短句：
- we investigate the potential for race bias in random forest (RF) models trained using radiomics features
- radiomics features derived from DCE-MRI data do contain race-identifiable information
- RF models trained to predict tumour molecular subtype using race-imbalanced data seem to produce biased behaviour

原文入口：https://doi.org/10.1007/978-3-031-45249-9_22

## Auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：标题明确为对CNN阿尔茨海默病诊断中的不公平偏见进行审计，来源表将目标文献归入FE-benchmarking，且元数据将阶段标为Evaluation，这些证据只支持公平性评估或基准审计的归类。由于未提供摘要、方法或结果细节，无法确认具体数据集、模型或缓解干预，因此不归为预处理、处理中或后处理。

证据短句：
- Auditing unfair biases in CNN-based diagnosis of Alzheimer’s disease
- FE-benchmarking

原文入口：https://doi.org/10.1007/978-3-031-45249-9_17

## From Head and Neck Tumour and Lymph Node Segmentation to Survival Prediction on PET/CT: An End-to-End Framework Featuring Uncertainty, Fairness, and Multi-Region Multi-Modal Radiomics

- 原始发表日期：2023-03-23
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.3390/cancers15071932

## Higher performance for women than men in MRI-based Alzheimer’s disease detection

- 原始发表日期：2023-04-20
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1186/s13195-023-01225-6

## Visualizing chest X-ray dataset biases using GANs

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://openreview.net/forum?id=bFb3V8ALx4W

## The role of subgroup separability in group-fair medical image classification

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-43898-1_18

## Are sex-based physiological differences the cause of gender bias for chest X-ray diagnosis?

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_14

## Bias in unsupervised anomaly detection in brain MRI

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_12

## Detecting shortcuts in medical images-a case study in chest x-rays

- 原始发表日期：2023-04-18
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1109/isbi53787.2023.10230572

## Evaluating the fairness of deep learning uncertainty estimates in medical image analysis

- 原始发表日期：2024-07
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://proceedings.mlr.press/v227/mehta24a.html

## A comparative study of fairness in medical machine learning

- 原始发表日期：2023-04-18
- 主要方法：Fairness Evaluation
- 原有阶段标签：In-processing, Post-processing, Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1109/isbi53787.2023.10230368

## (De) Constructing bias on skin lesion datasets

- 原始发表日期：2019-06
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1109/cvprw.2019.00335

## Debiasing skin lesion datasets and models? Not so fast

- 原始发表日期：2020-06
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1109/cvprw50498.2020.00378

## Detect and correct bias in multi-site neuroimaging datasets

- 原始发表日期：2021-01
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/j.media.2020.101879

## De-identification and obfuscation of gender attributes from retinal scans

- 原始发表日期：2023
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_9

## EdgeMixup: embarrassingly simple data alteration to improve Lyme disease lesion segmentation and diagnosis fairness

- 原始发表日期：2023
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-43901-8_36

## Bias in machine learning models can be significantly mitigated by careful training: Evidence from neuroimaging studies

- 原始发表日期：2023-01-30
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1073/pnas.2211613120

## Addressing Artificial Intelligence Bias in Retinal Diagnostics

- 原始发表日期：2021-02-11
- 主要方法：Pre-processing
- 原有阶段标签：Evaluation, Pre-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1167/tvst.10.2.13

## Equitable modelling of brain imaging by counterfactual augmentation with morphologically constrained 3D deep generative models

- 原始发表日期：2023-02
- 主要方法：Pre-processing
- 原有阶段标签：Pre-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/j.media.2022.102723

## Disproportionate subgroup impacts and other challenges of fairness in artificial intelligence for medical image analysis

- 原始发表日期：2022
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-23223-7_2

## A Systematic Review of ‘Fair’ AI Model Development for Image Classification and Prediction

- 原始发表日期：2022-10-15
- 主要方法：Fairness Evaluation
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/s40846-022-00754-z

## Pseudo bias-balanced learning for debiased chest x-ray classification

- 原始发表日期：2022
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-16452-1_59

## Rényi fair information bottleneck for image classification

- 原始发表日期：2022-03-09
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2203.04950

## Improving model fairness in image-based computer-aided diagnosis

- 原始发表日期：2023-10-06
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41467-023-41974-4

## Confound removal and normalization in practice: a neuroimaging based sex prediction case study

- 原始发表日期：2021
- 主要方法：Pre-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-030-67670-4_1

## A Penalty Approach for Normalizing Feature Distributions to Build Confounder-Free Models

- 原始发表日期：2022
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-16437-8_37

## Conditional VAEs for confound removal and normative modelling of neurodegenerative diseases

- 原始发表日期：2022
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-16431-6_41

## Fairness by learning orthogonal disentangled representations

- 原始发表日期：2022
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2003.05707

## Fairtune: Optimizing parameter efficient fine tuning for fairness in medical image analysis

- 原始发表日期：2024
- 主要方法：In-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2310.05055

## Mitigating bias in MRI-based Alzheimer’s disease classifiers through pruning of deep neural networks

- 原始发表日期：2023
- 主要方法：Post-processing
- 原有阶段标签：Post-processing
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_16

## Fairness in Deep Learning: A Computational Perspective

- 原始发表日期：2020
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://ieeexplore.ieee.org/document/9113719

## A Survey on Bias and Fairness in Machine Learning

- 原始发表日期：2021-07-13
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1145/3457607

## Algorithmic fairness in artificial intelligence for medicine and healthcare

- 原始发表日期：2023-06-28
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41551-023-01056-8

## Addressing fairness issues in deep learning-based medical image analysis: a systematic review

- 原始发表日期：2024-10-17
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41746-024-01276-5

## Bias recognition and mitigation strategies in artificial intelligence healthcare applications

- 原始发表日期：2025-03-11
- 主要方法：Fairness Evaluation
- 原有阶段标签：Not verified
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41746-025-01503-7

## Algorithmic individual fairness and healthcare: a scoping review

- 原始发表日期：2024-12-26
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1093/jamiaopen/ooae149

## Dissecting racial bias in an algorithm used to manage the health of populations

- 原始发表日期：2019-10-25
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1126/science.aax2342

## The Measure and Mismeasure of Fairness

- 原始发表日期：2018-07-31
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/1808.00023

## Ensuring Fairness in Machine Learning to Advance Health Equity

- 原始发表日期：2018-12-18
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.7326/m18-1990

## Ethical limitations of algorithmic fairness solutions in health care machine learning

- 原始发表日期：2020-05
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/s2589-7500(20)30065-0

## Re-imagining Algorithmic Fairness in India and Beyond

- 原始发表日期：2021-03
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1145/3442188.3445896

## Assessing Bias in Medical AI

- 原始发表日期：2021
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://www.cse.cuhk.edu.hk/~qdou/public/IMLH2021_files/64_CameraReady_ICML_2021_Interpretable_Machine_Learning_in_Healthcare_workshop.pdf

## Addressing fairness in artificial intelligence for medical imaging

- 原始发表日期：2022-08-06
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41467-022-32186-3

## The path toward equal performance in medical machine learning

- 原始发表日期：2023-07
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/j.patter.2023.100790

## What's fair is… fair? Presenting JustEFAB, an ethical framework for operationalizing medical ethics and social justice in the integration of clinical machine learning

- 原始发表日期：2023-06-12
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1145/3593013.3594096

## Where, why, and how is bias learned in medical image analysis models? A study of bias encoding within convolutional networks using synthetic data

- 原始发表日期：2025-01
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/j.ebiom.2024.105501

## Slicing Through Bias: Explaining Performance Gaps in Medical Image Analysis Using Slice Discovery Methods

- 原始发表日期：2024-10-13
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-72787-0_1

## An investigation into the causes of race bias in artificial intelligence–based cine cardiac magnetic resonance segmentation

- 原始发表日期：2025-02-24
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1093/ehjdh/ztaf008

## Understanding-informed Bias Mitigation for Fair CMR Segmentation

- 原始发表日期：2025-12-30
- 主要方法：Pre-processing
- 原有阶段标签：Not verified
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.59275/j.melba.2025-6747

## Shortcut learning in deep neural networks

- 原始发表日期：2020-11-10
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s42256-020-00257-z

## Radiology “forensics”: determination of age and sex from chest radiographs using deep learning

- 原始发表日期：2021-06-05
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/s10140-021-01953-y

## AI recognition of patient race in medical imaging: a modelling study

- 原始发表日期：2022-06
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/s2589-7500(22)00063-2

## Implications of predicting race variables from medical images

- 原始发表日期：2023-07-14
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1126/science.adh4260

## Risk of Bias in Chest Radiography Deep Learning Foundation                     Models

- 原始发表日期：2023-11-01
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1148/ryai.230060

## Unveiling Fairness Biases in Deep Learning-Based Brain MRI Reconstruction

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_10

## Disparities in dermatology AI performance on a diverse, curated clinical image set

- 原始发表日期：2022-08-12
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1126/sciadv.abq6147

## Understanding skin color bias in deep learning-based skin lesion segmentation

- 原始发表日期：2024-03
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1016/j.cmpb.2024.108044

## Rethinking fairness in medical imaging: Maximizing group-specific performance with application to skin disease diagnosis

- 原始发表日期：2026-03
- 主要方法：Pre-processing
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：SPARE以样本效用和群体相似性进行数据重加权；依照综述的数据重分配分类放入pre-processing，组别模型训练为次级贡献。

原文入口：https://doi.org/10.1016/j.media.2026.103950

## A Systematic Study of Race and Sex Bias in CNN-Based Cardiac MR Segmentation

- 原始发表日期：2022
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-23443-9_22

## Demographic bias in misdiagnosis by computational pathology models

- 原始发表日期：2024-04
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41591-024-02885-z

## Unsupervised Bias Discovery in Medical Image Segmentation

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_26

## FairSeg: A Large-Scale Medical Image Segmentation Dataset for Fairness Learning Using Segment Anything Model with Fair Error-Bound Scaling

- 原始发表日期：2024
- 主要方法：In-processing
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2311.02189

## Fair AI-powered orthopedic image segmentation: addressing bias and promoting equitable healthcare

- 原始发表日期：2024-07-12
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41598-024-66873-6

## An investigation of race bias in deep learning-based segmentation of prostate MRI images

- 原始发表日期：2025-12-06
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1038/s41598-025-26189-5

## Diagnosing failures of fairness transfer across distribution shift in real-world medical settings

- 原始发表日期：2022-02-02
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2202.01034

## Towards Unraveling Calibration Biases in Medical Image Analysis

- 原始发表日期：2023
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：原始标题、出版记录与综述分类；具体结论受限

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://doi.org/10.1007/978-3-031-45249-9_13

## No Fair Lunch: A Causal Perspective on Dataset Bias in Machine Learning for Medical Imaging

- 原始发表日期：2023-07-31
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2307.16526

## FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models

- 原始发表日期：2024-07-01
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2407.00983

## Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems

- 原始发表日期：2026-10-28
- 主要方法：Fairness Evaluation
- 原有阶段标签：Pre-processing
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2610.38215

## A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering

- 原始发表日期：2026-10-30
- 主要方法：Post-processing
- 原有阶段标签：In-processing
- 证据可用性：已读取原始摘要

判断：已读取原文Methods 4，明确说明在inference time通过activation steering干预，因此纠正原先In-processing标注为Post-processing。

证据短句：
- mitigate bias at inference time through activation steering

原文入口：https://arxiv.org/abs/2611.00298

## Fairness Metrics based on the AUC in Clinical Predictive AI

- 原始发表日期：2026-11-03
- 主要方法：Fairness Evaluation
- 原有阶段标签：Evaluation
- 证据可用性：已读取原始摘要

判断：依据已读取的原始摘要、标题及2024综述方法分类进行编辑；未取得具体结果的条目在英文TLDR中明确保留证据限制。

原文入口：https://arxiv.org/abs/2611.05222
