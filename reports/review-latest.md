# 每周文献人工审核单 · 2026-11-21

请只修改每篇的“审核决定”和“审核备注”：待审核 / 通过 / 排除 / 暂缓。编号和证据版本请保留。
填写后将此 Markdown 文件交给助手，或在聊天中按编号给出决定；只有明确通过的文章才会进入 README。
模型建议不是你的审核决定；证据不足的通过项仍需补核原文。

已完成的人工决定见 [11 月 23 日审核记录](review-approval-2026-11-23.md)。

## p-fafce843d0071edb38ce

文章：[Investigating Patient Trust and Intention to Act in AI-Supported Clinical Decisions: Cross-Sectional Survey.](https://pubmed.ncbi.nlm.nih.gov/42970578/)

审核决定：待审核
审核备注：
证据版本：4bd9426508d39d0810ca24fa08ef7998af69b635941e44751c25cd323faeb2c3

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该横断面调查（n=1185）比较患者对医生单独、医生+风险计算器、医生+AI三类临床决策支持的信任、行为意向与偏好，覆盖肺癌、脓毒症、抑郁等6个场景，并分析性别、种族、代际等亚组差异及开放式反馈。

纳入判断：文章有明确临床场景和AI支持决策的比较，但核心是患者信任与行为意向调查；未提出或检验算法公平性、偏倚或缓解问题，亚组差异不是模型公平性测量，故不满足算法公平性核心证据。

限制：全文为患者态度调查，未评估具体AI模型的性能、编码或公平性；亚组分析针对信任/意向而非算法输出，公平性仅作为定性主题出现。

建议分类：Not applicable

证据：
- algorithm：Participants were asked about their behavioral intentions, trust, and preferences regarding medical decisions made by (1) a doctor alone, (2) a doctor supported by an RC, and (3) a doctor supported by AI.
- evaluation：We conducted a cross-sectional online survey of US-based adults between June 17, 2024, and July 26, 2024.
- fairness：
- groups：quota sampling balanced on sex, education (with vs without a bachelor’s degree or higher), and generation
- medical：Each participant viewed six clinical scenarios (lung cancer, sepsis, depression, colon cancer, respiratory syncytial virus [RSV] vaccination, and heart failure).

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13741335/fullTextXML)

## p-13cc881c6ffbf754dbd7

文章：[Implications of Image-Level Duplication in Public Glaucoma Datasets.](https://europepmc.org/article/MED/43018943)

审核决定：待审核
审核备注：
证据版本：8c378da9b69357fc9daa004bd81c8f7a7101e6851c3a5099a6c1cfd183a6f523

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究审计3个公开青光眼数据集，发现Harvard-GF与FairVision有1302眼匹配、1031眼为同一OCT volume，跨数据集分类AUC因泄漏升高0.12，且各种族亚组均出现膨胀，提示独立基准与公平性评估可能被高估。

纳入判断：该文为青光眼公开数据集重复审计，含记录链接和按种族亚组的性能膨胀测量，主题高度相关且摘要显示五项证据均具备；但仅有摘要，按规则不能建议纳入，需全文核实公平性分析细节与完整方法。

限制：仅有摘要，缺少全文方法、亚组定义与样本量、公平性指标、代码/数据可用性等信息，无法确认详细公平性分析。

建议分类：Evaluation

证据：
- algorithm：a classifier trained on 1 dataset and evaluated on the other gave an area under the curve of 0.90
- evaluation：Records were linked by exact visual field and demographic fingerprints, with chance modeled from the within-dataset collision rate and permutation.
- fairness：3 public glaucoma datasets used for external validation and fairness evaluation
- groups：Inflation occurred in every racial subgroup and was larger where out-of-sample performance was lower
- medical：In glaucoma AI, a few public datasets from 1 laboratory serve as those independent cohorts.

[分析原文](https://europepmc.org/article/MED/43018943)

## p-21b44eb38a70c944169c

文章：[Applications of Fairness Training in Artificial Intelligence to Ophthalmic Disease Diagnosis using External Eye Photographs](https://europepmc.org/article/PPR/PPR1363752)

审核决定：待审核
审核备注：
证据版本：fc0cf6d9257d3eb7e2d49769d67188ab14ce057e32aa6f79ba20ea2969f54a7d

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：methodology, recall

中文概述：摘要报告利用40,687张外部眼照片开发深度学习与视觉语言模型，对威胁视力DR、晚期AMD和青光眼做二分类，并以ES-AUC评估性别、种族和族裔公平性，比较五种公平训练策略。报告称公平训练部分缩小差异并提升VTDR/AMD的AUC，但模型尚不适合临床部署。

纳入判断：摘要明确显示这是外部眼照片上的多病种分类与公平训练评估，直接相关；但仅有摘要，按规则不能据此suggest_include，且公平训练的具体阶段与完整结果无法核实，故暂hold。

限制：仅有摘要，无法核查五种公平训练策略的具体干预阶段、是否冻结基模型、亚组样本量、完整指标与代码/数据；亦无法判断全文是否包含更详细分析。摘要级证据不能建议纳入。

建议分类：Evaluation, Not verified

证据：
- algorithm：We developed and evaluated deep learning and vision-language models
- evaluation：Fairness training improved VTDR and AMD AUCs to 86·3% and 85·9% while partially mitigating demographic disparities.
- fairness：fairness across sex, race, and ethnicity quantified by the equity-scaled AUC (ES-AUC)
- groups：fairness across sex, race, and ethnicity
- medical：binary classification of vision-threatening DR (VTDR), advanced AMD, and glaucoma

[分析原文](https://europepmc.org/article/PPR/PPR1363752)

## p-53d198d32447f559a258

文章：[Reliable Skin-Tone Fairness in Dermatology AI: From Lesion-Level Leakage to Tone-Adaptive Learning](https://europepmc.org/article/PPR/PPR1345750)

审核决定：待审核
审核备注：
证据版本：a3f0e5aedac4158b594793841a1207409213637171e8694dbe25db92b108986d

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出面向皮肤镜与临床图像的色调自适应预处理流程，并建立按病灶分组、类别分层的评估协议，量化病灶级泄漏和肤色代理指标问题；在三个基准上报告深色皮肤敏感度提升，并发布泄漏审计工具。

纳入判断：摘要明确涉及皮肤色调公平性、三基准评估与预处理干预，五项标准均有摘要证据；但证据级别仅为摘要，无法核验全文，按规则不能建议纳入，故暂缓。

限制：仅有摘要，无法核验全文方法细节、完整结果、消融统计及 leakaudit 实现；因此不能按纳入标准确认。

建议分类：Pre-processing

证据：
- algorithm：We introduce a tone-adaptive pipeline combining selective contrast enhancement with a novel risk-aware augmentation strategy
- evaluation：We evaluate the approach across three complementary benchmarks—HAM10000, PAD-UFES-20, and Fitzpatrick17k
- fairness：Skin-tone fairness remains a challenge in dermatology AI
- groups：darker-skin sensitivity on PAD-UFES-20 from 0.655 to 0.714
- medical：dermatology AI, particularly for darker skin where reduced lesion visibility and limited representation

[分析原文](https://europepmc.org/article/PPR/PPR1345750)

## p-802f852b1e8f331fe15d

文章：[Governed Auditing of Hidden Failure Slice Discovery in Emergency Department Admission Models Agnostic to Sensitive Attributes](https://europepmc.org/article/PPR/PPR1363950)

审核决定：待审核
审核备注：
证据版本：e5ef69529f433d3333a314732a319797e194cc0ffb312574356c61e097f7dc65

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出BASiC与ASAP，在急诊入院预测中利用临床规则和折外误差信号发现隐藏失败切片，并尝试样本加权修复。研究在Kaggle、RIPAS和NHAMCS数据上评估多种模型，发现切片发现较可靠，但修复未带来一致改善，且不建立人口统计学公平或临床有效性。

纳入判断：摘要显示医学预测任务、多模型评估、失败切片发现与加权干预，但仅有摘要不能建议纳入；其属性无关审计与人口统计学公平的关系需全文确认。

限制：仅摘要可用，无法核实全文是否包含受保护群体公平性分析、完整方法或代码；摘要明确不使用敏感人口学属性，且未证明人口统计学公平。

建议分类：Pre-processing

证据：
- algorithm：using logistic regression, random forest, XGBoost and LightGBM
- evaluation：In nested evaluation, weighting increased sensitivity by 0.0058–0.0269
- fairness：Bias-aware Auditable Slices in Clinical Pre-processing
- groups：candidate qualification, prioritization and targeted sample weighting
- medical：Aggregate predictive performance can conceal localized failures in clinical models.

[分析原文](https://europepmc.org/article/PPR/PPR1363950)

## p-8ba36d760ea51eb05928

文章：[Predicting Depression Risk Using Machine Learning Among Students](https://europepmc.org/article/PPR/PPR1362751)

审核决定：待审核
审核备注：
证据版本：937412a2c14da68e388b75e1c006d5ab1142ac42bc312aff2a5515690b27af78

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究基于27,900份学生问卷，比较逻辑回归、随机森林和XGBoost预测非临床抑郁风险，并进行性别公平性与SHAP/LIME可解释性分析；摘要称各模型准确率约84.5%–84.8%，性别差异较小。

纳入判断：摘要显示该研究进行学生抑郁风险预测并对性别做公平性评估，但仅提供摘要，缺少具体指标和完整方法；按规则摘要级证据不能建议纳入，需全文核实。

限制：仅有摘要；摘要未报告公平性指标数值、数据划分、模型调参细节及完整方法，无法核实公平性评估的具体设计与结果稳健性。

建议分类：Evaluation

证据：
- algorithm：Three models were evaluated which are Logistic Regression, Random Forest, and XGBoost.
- evaluation：A post hoc gender fairness evaluation showed minimal performance differences
- fairness：A post hoc gender fairness evaluation showed minimal performance differences across male and female students.
- groups：performance differences across male and female students
- medical：Depression in students is a serious public health issue

[分析原文](https://europepmc.org/article/PPR/PPR1362751)

## p-8fc7d8cd62a109859e45

文章：[Synthetic tabular healthcare data in health informatics: fixed-size substitution and incremental-value controls for predictive utility Application Paper](https://europepmc.org/article/PPR/PPR1358040)

审核决定：待审核
审核备注：
证据版本：78520a94cba95007523d69c84069ac140b48f4421458ddb7a9ed98b6a49876a6

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究构建合成表格医疗数据基准，在固定训练规模与增量价值两种设置下控制样本量和重复预测特征泄漏，评估高斯Copula、CTGAN、TVAE及三种分类器在糖尿病相关数据集上的预测效用，发现合成数据无普遍增益，并明确不涉及公平性结论。

纳入判断：摘要聚焦合成数据预测效用与泄漏控制，虽涉及医疗预测建模和算法评估，但未提出或测量算法公平性问题，未定义受保护群体，公平性仅作为未验证事项被提及。

限制：仅有摘要；未报告人口学分组、亚组指标、偏差机制或缓解评估，无法支持公平性审查。

建议分类：Not applicable

证据：
- algorithm：logistic regression, random forest, and histogram gradient boosting
- evaluation：At fixed size, synthetic substitution produced significantly lower area under the receiver operating characteristic curve (AUC)
- fairness：
- groups：
- medical：three public diabetes-related healthcare datasets

[分析原文](https://europepmc.org/article/PPR/PPR1358040)

## p-9bbed0421308d7921eb5

文章：[Causal-Weighted Machine Learning for RRT Prediction in Acute Kidney Injury: Development, External Validation, and Clinical Decision Support](https://europepmc.org/article/PPR/PPR1367120)

审核决定：待审核
审核备注：
证据版本：6db2feb3d404580aba9b3cb0c00d50620be8ebad55c30887feb157efdf228357

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究开发并外部验证了用于KDIGO 3期AKI患者48小时RRT启动预测的因果加权机器学习流程，采用堆叠集成与IPW元学习，并报告内部AUC 0.894、外部AUC 0.807；摘要还称公平性评估未发现具有临床意义的亚组差距，但未给出亚组定义或指标。

纳入判断：摘要显示该文为AKI-RRT预测的原创方法学与外部验证，并明确提及公平性评估及阴性亚组结果；但摘要未定义亚组/属性、未报告公平性指标或具体数值，且摘要级证据不足以支持纳入，需全文核实其公平性分析细节。

限制：仅有摘要；公平性仅一句结果性描述，未说明受保护属性、亚组划分、公平性指标、置信区间或具体差异，无法核验公平性评估的完整性与有效性。

建议分类：Evaluation

证据：
- algorithm：A regularized stacking ensemble with inverse-probability-weighted meta-learning
- evaluation：fairness assessment showed no clinically meaningful subgroup gaps
- fairness：fairness assessment showed no clinically meaningful subgroup gaps
- groups：
- medical：predicting 48-hour RRT initiation in patients with KDIGO stage 3 AKI

[分析原文](https://europepmc.org/article/PPR/PPR1367120)

## p-a4d951a2b8b867906d60

文章：[HIV-PrivFed: Privacy-Utility-Fairness-Aware Federated Learning for HIV Risk Stratification and Testing Prioritization Under Non-IID Clinical Heterogeneity.](https://europepmc.org/article/MED/43028461)

审核决定：待审核
审核备注：
证据版本：dca11d3563b1e6960408bc3215fe797d5f1711b971b0b6286f421eb9961b1cf0

模型建议：related

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：基于Sialon-II队列（13个欧洲城市MSM，13个自然客户端）开展水平联邦学习，比较十种传统分类器、集中式MLP及local-only/FedAvg/FedProx基线，提出差分隐私FedProx算法HIV-PrivFed，配备客户端级Rényi隐私核算与客户端级公平性审计（仅审计、不强制）。结果显示隐私预算远松于名义目标，客户端级估计不确定性高。

纳入判断：摘要明确给出HIV筛查临床任务、联邦模型实测评估、客户端级公平性审计及以13个城市客户端为分组，满足任务/算法/公平性/分组/实证五项要素；但仅有摘要级证据、未披露子组公平性结果且公平性未实施缓解，故不能建议纳入，按规则不作为suggest_include。

限制：仅见摘要：未报告任何客户端/亚组公平性数值，公平性仅审计未缓解；实际隐私预算（ε=22.1–224.1）无有效保证；队列规模小、无外部验证；摘要未说明代码或数据可得性，不能据此推断全文缺失。

建议分类：Evaluation

证据：
- algorithm：benchmarked ten conventional classifiers and a centralized residual MLP
- evaluation：evaluated HIV-PrivFed, a differentially private FedProx-based algorithm with client-by-client Rényi accounting and client-level fairness auditing
- fairness：client-level fairness auditing (fairness is audited, not enforced)
- groups：cohort of men who have sex with men in 13 European cities
- medical：HIV screening from routinely collected behavioral data could help to prioritize testing

[分析原文](https://europepmc.org/article/MED/43028461)

## p-afe7ffeed3546c2df3d8

文章：[Design-based fairness monitoring for healthcare prediction with complex survey data.](https://europepmc.org/article/MED/42914067)

审核决定：待审核
审核备注：
证据版本：57fe734c772bbe189cec9373c32000dd7324adc6822a8c694e78711f7519c624

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究提出基于复杂抽样设计的公平性监测框架，利用2015—2023年MEPS九轮数据，以随机森林预测高额医疗支出，并按性别、种族/民族和贫困状态评估人口均等与机会均等，估计设计校正的公平性差异及时间趋势。

纳入判断：摘要明确包含医疗支出预测、随机森林、公平性指标、受保护群体和设计校正的实证评估，符合五项标准；但证据级别仅为摘要，按规则不能建议纳入，需全文核实。

限制：仅有摘要，无法核查全文的方法细节、敏感性分析、代码或数据可用性；摘要证据不足以建议纳入。

建议分类：Evaluation

证据：
- algorithm：a Random Forest predicted high annual healthcare expenditure
- evaluation：We used Taylor linearization to estimate design-based standard errors and 95% confidence intervals for survey-weighted fairness disparity ratios
- fairness：We evaluated demographic parity and equalized odds for sex, race/ethnicity, and poverty status.
- groups：for sex, race/ethnicity, and poverty status
- medical：predicted high annual healthcare expenditure

[分析原文](https://europepmc.org/article/MED/42914067)

## p-c081b58879d4f9838b0c

文章：[Explainable, Uncertainty-Aware Ensemble Learning for Brain Tumor Classification from MRI with a Simulated Fairness Audit](https://europepmc.org/article/PPR/PPR1365579)

审核决定：待审核
审核备注：
证据版本：f7a8fceaaacb18fb12ca77464d0d386dbf54a039f1c3da81859144e054fb62b6

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究构建了结合五种卷积网络和ViT的脑MRI肿瘤分类集成模型，评估校准、解释与不确定性，并用流行病学先验模拟年龄/性别标签进行公平性审计，报告各模型亚组差距较小且方向一致。

纳入判断：摘要明确报告脑MRI肿瘤分类及模拟年龄/性别公平性审计，但证据仅限摘要且亚组标签为流行病学先验模拟，无法确认真实患者层面的公平性评估，故暂缓纳入。

限制：仅见摘要，无法核实全文方法、代码与真实患者元数据；公平性标签为模拟生成，而非实际年龄/性别，亚组差距不能等同于真实临床差异。

建议分类：Evaluation

证据：
- algorithm：a logistic regression meta-learner fitted on Out-of-Fold predictions
- evaluation：the gaps were small but pointed the same way in every model
- fairness：we simulated age and sex labels from epidemiological priors to demonstrate a fairness audit
- groups：simulated age and sex labels from epidemiological priors
- medical：Most brain MRI classifiers stop at accuracy

[分析原文](https://europepmc.org/article/PPR/PPR1365579)

## p-cc9092de484d4c94f075

文章：[Routine to Emergency: A Machine Learning Approach for Predicting ED Visits Among Patients with T2D](https://europepmc.org/article/PPR/PPR1358206)

审核决定：待审核
审核备注：
证据版本：3bdff0a2de36931feb6bc147c9c9db6f3ba2d960b55393fb637c30bbdd087f9a

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究利用EHR数据开发六种机器学习模型，预测2型糖尿病患者未来30/60/90天急诊就诊，并报告性别及种族/族裔亚组的判别与召回差异。摘要仅提供有限公平性结果，无法核实完整偏差分析。

纳入判断：摘要显示明确的T2D急诊预测任务、多种ML模型及按性别和种族/族裔的公平性评估，但证据仅限摘要，无法核实完整方法与公平性细节，故暂缓。

限制：仅见摘要，缺少亚组样本量、公平性指标定义、阈值选择及置信区间等细节，无法评估公平性分析的严谨性与可复现性。

建议分类：Evaluation

证据：
- algorithm：Six ML models were developed and compared.
- evaluation：evaluated using area under the receiver operating characteristic curve (AUC ROC), accuracy, precision, recall, and F1 score.
- fairness：Fairness evaluation revealed consistent performance across sex subgroups.
- groups：recall varied across racial and ethnic groups
- medical：patients with type 2 diabetes (T2D)

[分析原文](https://europepmc.org/article/PPR/PPR1358206)

## p-d5f34822605251a88ec8

文章：[An Open, Reproducible Implementation of the CMS Hospital-Wide Readmission Measure on MIMIC-IV](https://europepmc.org/article/PPR/PPR1347611)

审核决定：待审核
审核备注：
证据版本：e659c8eb2ecbf35a3cdb702630ee90628d1b46a62178704be7416465866a3978

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文发布 CMS 医院全因再读入（HWR）指标的开放可复现实现：在 MIMIC-IV 上按计划性再读入算法与专科队列重建标签，使 30 天事件率由 17.6% 降至 15.9%（n=192,879），并公开编码表、Quan-Elixhauser 合并症编码与防泄漏特征规范，附校准基线模型（AUC 0.730），摘要称其做过亚组公平性与时间漂移评估。

纳入判断：属 EHR 临床预测任务的开放复现实现，摘要提到“亚组公平性评估”，但未定义分组、未报告任何亚组指标或公平性结论，公平性仅为评估清单中的一句提及；且证据仅限摘要，不能据此建议纳入。

限制：仅摘要层面：未给出任何亚组属性（种族、性别、年龄等）、公平性指标或亚组结果，也未说明公平性评估设计；无代码/数据链接证据。无法判断是否存在针对再读入任务的实质性公平性分析。

建议分类：Evaluation

证据：
- algorithm：a calibrated baseline model (ROC-AUC 0.730, well-calibrated, decision-curve positive)
- evaluation：
- fairness：evaluated for subgroup fairness and temporal drift
- groups：
- medical：Thirty-day hospital readmission is one of the most studied prediction targets in clinical machine learning

[分析原文](https://europepmc.org/article/PPR/PPR1347611)

## p-e68fcceb7a02de0b9211

文章：[ECG foundation models share an age-related performance disparity that originates in the data, not the models](https://europepmc.org/article/PPR/PPR1357796)

审核决定：待审核
审核备注：
证据版本：edbc492d2ec33e15f0d6e6bed65312ad45c48ea2b299f9bc39db58c805a1a183

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究在四个ECG基础模型、13个队列约540万份ECG上按年龄、性别和种族评估性能差异，发现差异主要集中于年龄并可在外部复现；未训练网络和经典特征模型也重现年龄差距，提示差异源于数据与任务而非预训练模型。

纳入判断：摘要显示该研究涉及临床ECG任务、多个基础模型、明确的公平性差异评估及按年龄/性别/种族分层，并报告大规模实证结果，符合核心标准；但证据等级仅为摘要，按规则不能建议纳入，需全文核验后决定。

限制：仅提供摘要，缺少全文的方法细节、统计结果、代码与数据可用性信息及完整公平性分析；无法核验嵌入几何、缓解实验和外部验证的实施质量。

建议分类：Evaluation

证据：
- algorithm：four architecturally distinct ECG foundation models
- evaluation：5.4 million analysed ECGs, 31 endpoints, six held-out cohorts
- fairness：We measured demographic disparities across four ECG foundation models
- groups：stratified by age, sex and race
- medical：Electrocardiogram (ECG) foundation models are proposed for clinical use

[分析原文](https://europepmc.org/article/PPR/PPR1357796)

## p-3daf0c4282bca4f685cf

文章：[FSD-Net: A Unified Skin-Tone-Aware Framework for Fair Skin Lesion Segmentation and Classification](https://europepmc.org/article/PPR/PPR1370450)

审核决定：待审核
审核备注：
证据版本：0da233be050d6067fb4d25f3ddc0e1c6f772c8a38a8d7500774031c2ff99b2bb

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：methodology, recall

中文概述：FSD-Net在皮肤病变分割与分类两个阶段同时考虑肤色公平性：用连续肤色评分经FiLM调制ViT-B/16分割骨干，并用分割引导的ROI训练Swin-V2-Tiny分类器。在ISIC-2017/2018、PH2及HAM10000上报告Dice、准确率和Equalized Opportunity差距，并辅以消融、Bootstrap置信区间和McNemar检验。

纳入判断：摘要显示该研究针对皮肤病变分割与分类评估肤色公平性，并报告分组指标、消融和统计检验，主题高度相关；但证据仅为摘要，按规则不能建议纳入，需全文核验后再定。

限制：仅有摘要可用，缺少全文的方法细节、数据划分、公平性指标定义、基线配置及代码/数据可用性信息；无法独立核验框架各组件对公平性提升的贡献和结果稳健性。

建议分类：In-processing

证据：
- algorithm：We propose FSD-Net (Fairness-aware Skin Disease Network)
- evaluation：84.2% classification accuracy with an Equalized Opportunity gap of 0.025
- fairness：first framework to enforce and evaluate fairness simultaneously
- groups：underrepresentation of darker Fitzpatrick types in public training datasets
- medical：Deep learning models for skin lesion segmentation and classification

[分析原文](https://europepmc.org/article/PPR/PPR1370450)

## p-fd455cc2a36673f35d55

文章：[MelanoFusion: An Explainable and Uncertainty-Aware Hybrid CNN–Transformer Framework for Dermoscopic Melanoma Detection](https://europepmc.org/article/PPR/PPR1370178)

审核决定：待审核
审核备注：
证据版本：040b05828031626f292dadb8a47c10477854893e4264cf7f5ae4348ce244291d

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出MelanoFusion混合CNN–Transformer框架用于皮肤镜黑色素瘤检测，结合可解释性、不确定性估计与公平导向表征学习；在HAM10000、ISIC 2018和PH²上评估，报告年龄组敏感性差异但性别无显著差异，并提示需外部验证。

纳入判断：摘要明确涉及皮肤镜黑色素瘤的年龄/性别亚组敏感性分析，属医学算法公平性相关研究；但证据仅为摘要，按规则不能建议收录，故列为related。

限制：仅提供摘要，无法核验公平性指标细节、公平导向训练实现、统计检验及代码/数据；作者亦指出需外部验证与临床评估。

建议分类：In-processing

证据：
- algorithm：MelanoFusion, a hybrid framework integrating explainability, uncertainty estimation
- evaluation：subgroup analysis showed significant sensitivity differences across age groups but not sex
- fairness：fairness-oriented representation learning for melanoma detection
- groups：across age groups but not sex
- medical：Melanoma is an aggressive skin cancer requiring early detection

[分析原文](https://europepmc.org/article/PPR/PPR1370178)

## p-12f4eff61a09eab3bddf

文章：[Deep Survival Analysis with Temporal Trajectory Embedding for Substandard Life Insurance Pricing: A DeepSurv Modeling Study of Type 2 Diabetes Mellitus](https://europepmc.org/article/PPR/PPR1360391)

审核决定：待审核
审核备注：
证据版本：ad311f8a3b232c62eec3864a3124c19c751b843f6a8462d232af2b78e19e6d59

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文以约188万份T2DM住院理赔记录构建DeepSurv定价框架，比较EM、GLM与Tweedie模型，并加入Elastic Net、LSTM、SHAP和Bootstrap稳健性检验；但仅在结论泛称提升定价公平性，未开展公平性分析。

纳入判断：摘要仅在结论提及“改善公平性”，未定义群体或提供亚组/差异测量；属附带提及，且摘要级证据不足以建议纳入。

限制：仅有摘要；未报告受保护属性、亚组指标、差异机制或公平性干预评估；公平性仅为结论性表述，无法判断全文是否包含相关分析。

建议分类：Not applicable

证据：
- algorithm：centered on the DeepSurv deep survival model
- evaluation：
- fairness：
- groups：
- medical：Taking type 2 diabetes mellitus (T2DM) as a case study

[分析原文](https://europepmc.org/article/PPR/PPR1360391)

## p-3f9a2ee2dec669d59e15

文章：[A Multi-Model Framework for Explainable Sepsis Mortality Prediction With Dynamic Fairness and Drift Analysis.](https://europepmc.org/article/MED/43056270)

审核决定：待审核
审核备注：
证据版本：97c95306aac9cdda66747d89a6513ef382867c3f8dcb031ebd667708fe6146a4

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：methodology, recall

中文概述：该研究在MIMIC-IV上构建脓毒症死亡预测多模型框架，将公平性重新定义为动态生命周期属性，在15轮再训练与16个交叉子群中监测TPR、FPR、FOR差距，并开展eICU跨机构公平性审计与SHAP稳定性分析。

纳入判断：摘要包含临床预测任务、算法模型评估、明确公平性议题、交叉子群与实证测量，表面上符合五项标准，但证据层级仅为摘要，需全文复核后再定。

限制：仅有摘要，无法核查三种策略的干预阶段、统计与偏差控制细节及完整实验设计；按规则摘要级证据不能建议纳入。

建议分类：Not verified

证据：
- algorithm：the LSTM achieves an AUC of 0.884
- evaluation：Across 30 independent runs, all three strategies converge to final TPR gaps
- fairness：dynamic, lifecycle property rather than a static deployment checkpoint
- groups：15 retraining cycles and 16 intersectional subgroups
- medical：improve risk prediction and resource allocation in critical care

[分析原文](https://europepmc.org/article/MED/43056270)

## p-025d4680a20363b0f28f

文章：[DINOv3-SAM: Fusing Semantic and Anatomical Foundation Models for Robust Medical Image Classification.](https://europepmc.org/article/MED/42972189)

审核决定：待审核
审核备注：
证据版本：44d5086603902abe89d948ea01471312abfc38021a28c4ee92621dff3b584289

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

正式版本线索：[DINOv3–SAM: Fusing Semantic and Anatomical Foundation Models for Robust Medical Image Classification](https://doi.org/10.1007/s10278-026-02405-0)

中文概述：提出DINOv3-SAM双编码器框架，将自监督DINOv3的全局语义特征与冻结的SAM解剖感知特征空间对齐，经CBAM注意力精炼后用于儿科肺炎、心脏增大、RSNA肺炎、COVID-19胸片及皮肤病变分类，报告准确率与AUC提升并强调对数据集偏倚和跨域漂移的鲁棒性。

纳入判断：该文属通用多模态融合/鲁棒性分类方法，虽针对明确临床任务且经经验评估，但通篇未提出算法公平性、偏倚机制或分组差异问题，也没有任何受保护属性或亚组分析，属于仅泛泛提及"dataset bias"的鲁棒性工作，不符合公平性入选条件。

限制：仅有摘要，无法核查全文的公平性内容。文中未定义任何受保护人群或亚组，未报告亚组差异或公平性指标；"fair evaluation"指统一的分层训练/验证/测试协议，"dataset bias"指泛化鲁棒性，均不构成算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：we propose DINOv3-SAM, a dual-encoder framework that synergistically integrates complementary visual representations
- evaluation：
- fairness：
- groups：
- medical：pediatric pneumonia classification, cardiomegaly detection, large-scale RSNA pneumonia detection

[分析原文](https://europepmc.org/article/MED/42972189)

## p-48b9e5d40beb02d005ae

文章：[ARBITER: retrieval-augmented generation for automated PROBAST+AI risk-of-bias assessment of HIV, HBV and HCV prediction models: a proof-of-concept validation study](https://europepmc.org/article/PPR/PPR1351930)

审核决定：待审核
审核备注：
证据版本：060a4e1531f9a7061bb82ff5efef63e28a790c7daf71706d649c717cd393b463

模型建议：exclude

渠道核查：pending；缺少可核验的 journal_title/journal_issns/conference 字段，保留待核验。

中文概述：ARBITER 是一个基于检索增强生成（RAG，使用 Gemini 2.5 Pro）的工具，用于自动化完成 PROBAST+AI 偏倚风险评估：识别研究、区分建模与评价路径，并为每个信号问题给出分类判断及原文证据。在 10 项 HIV/HBV/HCV 预测模型研究上进行概念验证，与 Claude Sonnet 4.6 及人类统计专家对比，三者与专家共识均达到较高一致性（κ≈0.70–0.72）。

纳入判断：该文属方法学/验证研究，任务是自动化风险偏倚评估而非算法公平性研究：摘要未提出任何公平性/差异性问题，未定义受保护人群或属性，也未测量亚组差异或实施偏倚缓解。风险偏倚（risk of bias）与算法公平性中的偏倚不同，故不满足公平性、分组两项核心标准，且非具名疾病下实质公平性综述，按规则排除。

限制：仅有摘要，未见全文方法、提示词设计、样本构成与代码/数据可得性。评估对象是 PROBAST+AI 风险偏倚评定的一致性，不涉及任何人群分组、敏感属性或公平性指标，因此无法支撑算法公平性证据。样本仅 10 项研究，且其中 1 项用于流程迭代。

建议分类：Not applicable

证据：
- algorithm：We developed the Automated Risk-of-Bias Inspection Tool for Evidence Review (ARBITER)
- evaluation：ARBITER Cohen κ=0.701 (95%CI 0.650–0.754)
- fairness：
- groups：
- medical：Clinical prediction models for blood-borne virus infections

[分析原文](https://europepmc.org/article/PPR/PPR1351930)

## p-515324d349beb4aea4b7

文章：[Development and validation of early warning scores predicting 24 h mortality addressing intercurrent medical interventions in Denmark: a multicentre retrospective cohort study of 2·08 million hospital encounters.](https://pubmed.ncbi.nlm.nih.gov/42988715/)

审核决定：待审核
审核备注：
证据版本：e99a83058d4c4ed7f9172b82100b16666e5e78b864c70231b9b064eca5d8c2d2

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：摘要比较NEWS、简化NEWS、DEWS与XGB-EWS对24小时死亡的预测，使用倾向评分处理干预偏倚，并以净获益、AUC和校准评估，报告不同风险亚组的效用异质性。

纳入判断：研究是临床预测模型效用评估，虽提及亚组异质性和干预偏倚，但未提出或测量算法公平性/差异，也无可识别的敏感属性公平性分析；摘要证据不足以纳入。

限制：仅摘要；未报告按年龄、性别、种族等敏感属性的公平性指标或差异结果；“干预偏倚”指治疗混杂而非算法公平；摘要未提供代码或数据链接。

建议分类：Evaluation

证据：
- algorithm：a model based on Extreme Gradient Boosting Early Warning Score (XGB-EWS)
- evaluation：evaluated performance using net benefit, area under the receiver operating characteristic curve, and calibration
- fairness：
- groups：
- medical：The outcome was all-cause mortality within 24 h of the initial NEWS recording.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42988715/)

## p-009e12912fe734931786

文章：[DRLCI: Dual-view Representation Learning Framework for Predicting Drug-Gene Interactions via Causal Intervention.](https://europepmc.org/article/MED/43013439)

审核决定：待审核
审核备注：
证据版本：550311f2d70f7a5e4850ead222cd3501d41d4674bb638acb9b6bc1c485f349b1

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

正式版本线索：[DRLCI: Dual-view Representation Learning Framework for Predicting Drug-Gene Interactions via Causal Intervention](https://doi.org/10.1109/jbhi.2026.3752199)

中文概述：提出DRLCI双视图表示学习框架，用于预测药物-基因相互作用；通过关系感知图卷积、因果干预掩码和因果去偏对比损失抑制混淆因素，并融合医学先验文本，在DrugBank和DGIdb基准上报告最优性能。

纳入判断：摘要的医学任务和GNN方法明确，但公平性证据缺失：没有公平性/差异/编码/缓解研究问题，也没有定义群体或公平评估。因果去偏不等同于公平性分析，故排除。

限制：仅有摘要；未涉及算法公平性定义、受保护群体或亚组公平指标；所谓因果去偏针对硬负样本混淆，而非医疗算法公平性。

建议分类：In-processing

证据：
- algorithm：we propose a dual-view representation learning framework.
- evaluation：Comprehensive benchmark evaluations demonstrate that our framework achieves state-of-the-art performance on the DrugBank and DGIdb datasets.
- fairness：
- groups：
- medical：Investigating drug-gene interactions is essential for advancing personalized medicine and therapeutic innovation.

[分析原文](https://europepmc.org/article/MED/43013439)

## p-0e20310c94fa66bd35f7

文章：[Supporting Ergonomic Risk Assessment: An AI-driven Approach for Action Recognition Using Standard Video Recordings.](https://europepmc.org/article/MED/42925046)

审核决定：待审核
审核备注：
证据版本：cb1ad5d7a29a77139196a73d717b7b94b8d8cc7afd5ecfbb8e02cecb69469fa6

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：提出并评估一种基于2D姿态与图卷积网络的视频动作识别方法，用于自动化OCRA工效学风险评估中的技术动作识别与计数；在37个制造场景数据上比较ST-GCN与2S-AGCN，准确率约60%。

纳入判断：该文属于职业健康AI应用与方法评估，虽涉及工效学风险评估，但未提出算法公平性问题，未定义受保护群体或进行公平性测量；仅有隐私与不公平的泛泛提及，按附带提及规则排除。

限制：全文仅报告整体分类性能与基线比较，未按性别、年龄等群体分层，也未开展算法公平性、偏差机制或缓解效果分析；数据规模小且单中心，不能支持公平性结论。

建议分类：Not applicable

证据：
- algorithm：artificial intelligence-driven approaches for ergonomic risk evaluation
- evaluation：The evaluation employed both Mean Average Precision (mAP) and F1-score
- fairness：
- groups：
- medical：prevention of work-related musculoskeletal disorders (WMSDs)

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13732331/fullTextXML)

## p-1582a8a2e3798f9bf7f2

文章：[Radiology No-Show Calculator: A Social Determinants of Health-Enriched Machine Learning Prediction Model With Financial Analysis.](https://pubmed.ncbi.nlm.nih.gov/42660476/)

审核决定：待审核
审核备注：
证据版本：81b94d84b3de22659e1acce6b231b905594dd18bf4b02409dc3693718b4afa81

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究开发基于随机森林的放射科门诊失约预测模型，纳入区域剥夺指数等16个预测因子，并按人群患病率校准；报告AUC 0.760、ADI相关失约梯度和财务负担，提出针对高风险患者外展。

纳入判断：摘要显示放射科失约预测与ADI梯度，但公平性主要为健康公平/财务表述，缺少模型亚组公平性测量；仅摘要无法确认全文分析，故暂缓。

限制：仅摘要；未报告模型在各社会经济亚组的性能、公平性指标或缓解措施，无法判断全文是否有算法公平性评估；无代码或外部验证信息。

建议分类：Evaluation

证据：
- algorithm：A Random Forest model with 16 predictors
- evaluation：The Random Forest achieved an area under the receiver operating characteristic of 0.760.
- fairness：
- groups：No-show rates demonstrated a clear Area Deprivation Index gradient
- medical：Outpatient radiology appointment no-shows delay timely diagnosis

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42660476/)

## p-2076a6e307f6e08acb19

文章：[A preregistered simulation study provided evidence on the appropriate use of data-driven variable selection in descriptive multivariable regression modeling.](https://pubmed.ncbi.nlm.nih.gov/42486194/)

审核决定：待审核
审核备注：
证据版本：cdbde24a59fcdc37386109f71f9d6b7a26c63fe59733b46beb2fd33e36e56a1f

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该预注册模拟研究比较流行病学描述性回归中的数据驱动变量选择方法（后退法与Lasso），评估变量选择率、模型选择率及回归系数偏倚，并提供方法选择决策框架；未涉及医学算法公平性、群体差异或公平性缓解。

纳入判断：文章评估回归变量选择方法的统计表现（TPR、FPR和系数偏倚），没有提出或测量算法公平性问题，也未定义受保护群体或进行公平性评估，因此不符合医学算法公平性纳入标准。

限制：仅有摘要证据；主题为统计变量选择方法学，而非医学算法公平性研究。文中未定义敏感属性或受保护群体，也未报告亚组公平性指标、偏倚机制或缓解评估。

建议分类：Not applicable

证据：
- algorithm：comparing commonly used variable selection approaches, including backward elimination (BE) with various selection criteria and variants of the least absolute shrinkage and selection operator (Lasso)
- evaluation：We conducted a comprehensive simulation study comparing commonly used variable selection approaches
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42486194/)

## p-220234c949e46cfa70a4

文章：[Computational Nutrition 2.0: From Static Models to Closed-Loop Agentic Systems for Personalized Nutrition.](https://pubmed.ncbi.nlm.nih.gov/42805435/)

审核决定：待审核
审核备注：
证据版本：8897a2ac41b864e29c077c592699c009a7476a5ae6cf16baa611d503f31a1038

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为观点性文章，提出计算营养学2.0，主张以AI智能体推动个性化营养从静态模型走向闭环干预，覆盖代谢反应预测、营养因果推断、饮食相关疾病风险监测与营养政策模拟四个方向。

纳入判断：属展望性评论：虽涉及营养健康任务与AI智能体，但未提出算法公平性研究问题，无群体定义、亚组发现或公平性评测，公平性仅为附带提及，且仅有摘要证据，故排除。

限制：仅有摘要，未提供具体方法、数据或实验；公平性仅在政策权衡中被附带提及一次，缺少亚组定义、公平性指标、编码证据或任何实证测量。

建议分类：Not applicable

证据：
- algorithm：AI agents overcome these limitations by continuously learning from new data
- evaluation：
- fairness：
- groups：
- medical：prediction of personalized metabolic responses to foods

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42805435/)

## p-31cf3e898e1f39daf9dc

文章：[Regional and national variation in donor and recipient characteristics, transplant practice, and outcomes after liver transplantation (the IMPROVEMENT collaborative): a multicentre cohort study.](https://europepmc.org/article/MED/42999582)

审核决定：待审核
审核备注：
证据版本：d04b425f261c34f0214ad8229a9f3de583798b6612ceadae2c43fbdc53d70cea

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：IMPROVEMENT 多中心队列研究汇总 61 个中心、83 个病例序列、5218 例肝移植患者，覆盖五大洲，采用四步分析（世界地图、雷达图、笛卡尔图、混合效应预后模型）刻画供受体风险与风险缓解策略的区域差异，并建立 90 天、1 年、2 年死亡与并发症的预后算法，指出受者因素、冷缺血时间与中心体量是主要决定因素。

纳入判断：具备医学任务（肝移植预后）与算法（混合效应预后模型），但全文的“差异/公平”讨论限于地区间医疗资源与服务可及性差异及结局描述，属医疗不平等而非算法公平性评估：无显式算法公平/偏倚问题、无亚组性能度量或缓解方法比较，五个判据中的 fairness 与 evaluation 均不成立，按规则排除而非作为相关文献推荐。

限制：全文为临床流行病学与预后建模研究：区域/国家差异属描述性结局比较，未定义算法公平性研究问题，未报告任何按人群分组的模型性能差异、偏倚机制或缓解方法比较；女性移植可及性仅在讨论中一句带过。

建议分类：Evaluation

证据：
- algorithm：we developed a model of donor plus recipient aggressiveness, attributing a weight to each predictor
- evaluation：
- fairness：
- groups：outcomes differed according to recipient sex
- medical：integrating donor–recipient profiles, logistical factors, and risk-mitigation strategies

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13743410/fullTextXML)

## p-3295b40be2839e3ffd5b

文章：[BMR-Restormer: A transformer-based blind inpainting network for ultrasound marker removal.](https://pubmed.ncbi.nlm.nih.gov/42551183/)

审核决定：待审核
审核备注：
证据版本：9d803cf521974ec7034e281294408e9f5b5d938c58109657761c26fb0d813c9a

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：提出 BMR-Restormer 盲修复网络，用于去除超声图像中烧录的人工标记（十字、文字、测量线），并评估标记对下游分类、分割、检测模型泛化性的影响，发现模型在含标记数据上训练后会过拟合伪特征，迁移到无标记图像时性能大幅下降。

纳入判断：该文属图像修复/鲁棒性研究：去除超声烧录标记并量化伪特征过拟合造成的性能下降，但未定义任何人口学或其他分组属性，没有亚组公平性度量、差异分析或公平性缓解方案；文中“bias”指伪相关捷径而非群体公平，属通用鲁棒性问题，不符合公平性准入标准，且证据仅为摘要。

限制：仅有摘要，未见全文方法细节、数据集构成与统计检验；研究关注标记伪影导致的伪特征过拟合，未涉及任何人群分组、敏感属性或亚组公平性指标，无法支撑算法公平性判断。

建议分类：Pre-processing

证据：
- algorithm：we propose the BMR-Restormer network specifically optimized for ultrasound marker removal
- evaluation：we conducted three downstream tasks (classification, segmentation, and detection) under different training-testing configurations
- fairness：
- groups：
- medical：leading to degraded performance in computer-aided diagnosis (CAD)

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42551183/)

## p-4d243e183a986cc09be8

文章：[Development and internal validation of a CSF-free machine-learning model to distinguish immune checkpoint inhibitor-induced encephalitis from HSV-1 and anti-LGI1 encephalitis](https://europepmc.org/article/PPR/PPR1354554)

审核决定：待审核
审核备注：
证据版本：4d833fba871c449b0653dd2d2c908f61f3dcd9f84835539ec5f4303954453586

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：该研究基于51例公开回顾性数据，构建并内部验证不含脑脊液特征的随机森林模型，用于区分免疫检查点抑制剂相关脑炎与HSV-1及抗LGI1脑炎，比较含或不含CSF、MRI特征时的判别力、校准与决策曲线表现，全程未涉及算法公平性分析。

纳入判断：该文属脑炎鉴别诊断的机器学习模型开发与内部验证，具备临床任务、算法与实证评估，但未提出算法公平性或偏倚问题，也未定义受保护群体、开展亚组或公平性测量，不满足公平性相关判据，故排除。

限制：仅有摘要可查：样本量小（51例）、仅内部验证、校准差，且可能存在数据来源混杂。摘要未报告任何受保护属性、亚组比较或公平性测量，无法据此判断模型在不同人群中的差异表现。

建议分类：Not applicable

证据：
- algorithm：Random-forest models with 29 features (including CSF) or 25 features (excluding CSF) were evaluated
- evaluation：evaluated by repeated nested cross-validation (5 outer folds × 20 repeats)
- fairness：
- groups：
- medical：distinguish from herpes simplex virus type 1 (HSV-1) and anti-LGI1 encephalitis

[分析原文](https://europepmc.org/article/PPR/PPR1354554)

## p-66a0131f9ccb7890785d

文章：[Development and internal validation of a CSF-free machine-learning model to distinguish immune checkpoint inhibitor-induced encephalitis from HSV-1 and anti-LGI1 encephalitis](https://europepmc.org/article/PPR/PPR1355264)

审核决定：待审核
审核备注：
证据版本：f392b3a885f8854fb4020c39fdc6efc32abcc911d970d88f8cc84b88b57d0fd8

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该摘要开发并内部验证一个不含脑脊液特征的随机森林模型，用于区分ICI相关脑炎与HSV-1及抗LGI1脑炎，报告AUC、校准和决策曲线等性能。

纳入判断：研究聚焦诊断模型性能，未提出算法公平性问题，也未定义受保护群体或开展亚组/差异评估，故不属于医学算法公平性研究。

限制：仅有摘要，样本量51，缺乏外部验证；未报告任何公平性、亚组或敏感属性分析。

建议分类：Not applicable

证据：
- algorithm：Random-forest models with 29 features (including CSF) or 25 features (excluding CSF)
- evaluation：evaluated by repeated nested cross-validation (5 outer folds × 20 repeats)
- fairness：
- groups：
- medical：Immune checkpoint inhibitor-induced encephalitis (ICI-iE) is difficult to distinguish from herpes simplex virus type 1 (HSV-1) and anti-LGI1 encephalitis

[分析原文](https://europepmc.org/article/PPR/PPR1355264)

## p-72d2098ba0d9a6374d16

文章：[Antibiotic Choice for Community-Acquired Pneumonia in Children With Medical Complexity.](https://europepmc.org/article/MED/42838530)

审核决定：待审核
审核备注：
证据版本：626eb9253c1f699cbe5e913bda64217f341b9aae9eea178746879c97dcb750f4

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该队列研究采用目标试验模拟与逆概率加权，比较儿童医学复杂（CMC）非重症社区获得性肺炎初始广谱与窄谱抗生素的结局。847例次住院中，广谱抗生素在至出院时间、进展为重症及30天再就诊方面与窄谱无显著差异，支持对多数CMC使用氨苄青霉素类。

纳入判断：该文是抗生素选择的临床比较效果研究，使用倾向加权而非AI/ML模型，未评估算法公平性、偏见机制或缓解方法，缺乏本综述所需的五项证据，故排除。

限制：仅有摘要；研究为临床疗效比较，未涉及任何AI/ML算法，也未定义公平性概念、敏感属性或亚组差异测量；摘要未报告代码、数据或亚组结果。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：community-acquired pneumonia (CAP) in children with medical complexity (CMC)

[分析原文](https://europepmc.org/article/MED/42838530)

## p-7d6abfecd7636ea459d5

文章：[A multimodal CT-based machine-learning model for differentiating pulmonary sarcomatoid carcinoma from conventional non-small cell lung cancer: an internally validated study](https://europepmc.org/article/PPR/PPR1348078)

审核决定：待审核
审核备注：
证据版本：d122e1fe4299a15efe34d5684cbdfe4dea6bd00e8b6747f30c4502ded8860241

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究基于三个中心的397例患者，比较临床-CT语义特征、影像组学与深度学习特征构建的六种模型，用于病理确诊前区分肺肉瘤样癌（PSC）与常规非小细胞肺癌；全融合模型AUROC 0.890，并分析采集参数异质性带来的残余混杂。

纳入判断：论文为PSC与c-NSCLC的CT多模态诊断模型开发与内部验证，虽具备临床任务、算法建模与实证评估，但缺少明确的算法公平性/偏倚问题及受保护群体定义或亚组发现方案；采集协议混杂属于稳健性与域偏移，不构成公平性研究，故排除。

限制：仅摘要可得，无法核实全文的公平性分析。文中采集异质性属技术/站点混杂，未定义任何受保护人群属性，也未做亚组公平性指标或缓解措施评估。

建议分类：Not applicable

证据：
- algorithm：Six models (clinical-only, radiomics-only, deep-only, clinical+radiomics, clinical+deep and full fusion) were developed and evaluated
- evaluation：
- fairness：
- groups：
- medical：Pulmonary sarcomatoid carcinoma (PSC) is difficult to distinguish from conventional non-small cell lung cancer

[分析原文](https://europepmc.org/article/PPR/PPR1348078)

## p-871ab9f4cc09b5f81ad5

文章：[Mediterranean Diet, Physical Activity, and Sleep in Endometriosis: An Age-Comparable Case-Control Study with Exploratory Machine Learning Discrimination.](https://pubmed.ncbi.nlm.nih.gov/43030256/)

审核决定：待审核
审核备注：
证据版本：8a548a6320c8de5c43b7ada774c057532b6db9386e00f122378132b643863646

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究为病例对照研究（177名女性，77例自报并经手术确诊的子宫内膜症），比较地中海饮食、体力活动、睡眠与症状指标，并用三种机器学习算法做交叉验证判别分析；最佳AUC-ROC为0.933，但限制于前置因素与饮食变量时仅0.67-0.73，作者认为判别主要反映并发症状而非营养因素。

纳入判断：该文虽涉及子宫内膜症临床任务与机器学习算法评估，但通篇无算法公平性/差异/编码/缓解或公平性测量问题，也未定义公平性分组属性或亚组发现协议，仅有判别性能（AUC）报告，不符合纳入所需的五项证据标准。

限制：仅有摘要级证据；研究聚焦饮食、活动与症状的组间比较及判别性能，未涉及任何敏感属性分组、公平性指标、偏倚机制或缓解方法；年龄仅作为混杂因素校正，而非公平性分析维度。

建议分类：Not applicable

证据：
- algorithm：three machine learning algorithms were evaluated with cross-validation
- evaluation：
- fairness：
- groups：
- medical：77 with self-reported, procedure-confirmed endometriosis recruited through a patient association

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43030256/)

## p-906350a279d8b30f4322

文章：[Evaluating Federated Vision-Language and Vision-Only Models for Privacy-Aware Breast Cancer Imaging](https://arxiv.org/abs/2610.36379)

审核决定：待审核
审核备注：
证据版本：2ebdb8d7b114f326f8cb1e0744d17bf7902b22d5cf77c324b197d089b9b81a83

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文评估联邦学习下CLIP类视觉语言模型与纯视觉模型在乳腺热成像分类中的隐私-效用权衡，报告患者级AUC、差分隐私影响和通信成本，并发现BCD数据存在采集年份混杂。

纳入判断：满足医学任务、算法评估与实证测量，但未提出或测量算法公平性；采集年份混杂属于效度/捷径偏倚，而非受保护群体公平问题，且明确亚组分析不可行，故排除。

限制：证据为全文，但研究聚焦隐私保护与预测可靠性，未定义受保护人群，未开展公平性/亚组分析，也未报告公平性指标。

建议分类：Evaluation

证据：
- algorithm：federated learning framework combining pretrained vision-language models
- evaluation：patient-level ROC-AUC with bootstrap 95% confidence intervals
- fairness：
- groups：
- medical：two public breast imaging datasets

[分析原文](https://arxiv.org/html/2610.36379v1)

## p-923f4ac4a8b6eae7cf82

文章：[Anthropometric and Psychological Variables Associated with Body Mass Index: A Sex-Stratified Evaluation of Students from a Romanian University.](https://pubmed.ncbi.nlm.nih.gov/43028626/)

审核决定：待审核
审核备注：
证据版本：ca9123d9bab96d89c7049b1ae2960daf07af823c209aa6fa8bec4b09fdaca260

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该横断面研究在445名大学生中分析颈围、BAI、指长比及心理变量与BMI分类的关联，并按性别分层建立回归与探索性ROC。颈围和BAI为主要相关指标，指长比具初步分类效用，心理指标无独立关联；未涉及算法公平性评估。

纳入判断：研究按性别分层分析BMI相关变量并做ROC，但未提出或测量算法公平性、差异、编码或缓解问题，故不属于医学算法公平性研究。

限制：仅有摘要；未报告算法公平性指标、亚组差异或缓解方法；样本为便利样本，阈值为内部探索性阈值，需外部验证。

建议分类：Not applicable

证据：
- algorithm：Statistical models utilized multivariable linear regressions with collinearity diagnostics and exploratory Receiver Operating Characteristic (ROC) curve analysis.
- evaluation：A cross-sectional evaluation was conducted on a cohort of 445 university students
- fairness：
- groups：cohort of 445 university students (nmale = 199, nfemale = 246)
- medical：evaluated the potential associations and preliminary classification capacities of select anthropometric and psychological variables in relation to body mass index (BMI) status groupings

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43028626/)

## p-93c485e79111c145c215

文章：[Vision-language classification of Torsades de Pointes risk from pseudo-coloured ECG images: do T-wave morphology and colour context help or hinder?](https://arxiv.org/abs/2611.01921)

审核决定：待审核
审核备注：
证据版本：5332c0d6de650d46de6274598454a87af65d804f701f65aa57cd897e82acae4e

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：论文用BiomedCLIP从伪彩ECG图像评估TdP风险，交叉比较图像有无颜色与提示是否命名颜色或描述T波形态，发现颜色信息主要来自图像而非文本；训练后彩色图像各指标优于无色图像。

纳入判断：研究为ECG图像TdP风险的视觉-语言分类评估，虽含算法与实证评价，但公平性、差异、编码或缓解问题缺失，且未定义敏感属性或亚组，故排除。

限制：全文未涉及受保护群体、亚组差异或公平性指标；仅比较颜色与文本提示对分类性能的影响，无法支持公平性纳入。

建议分类：Evaluation

证据：
- algorithm：using a domain-adapted vision–language model, BiomedCLIP.
- evaluation：evaluated zero-shot and with a class-balanced linear probe, under five-fold stratified cross-validation on 9,789 images.
- fairness：
- groups：
- medical：flag Torsades de Pointes risk using the QT-nomogram and pseudo-colouring technique

[分析原文](https://arxiv.org/html/2611.01921v1)

## p-97c54bcea3ab95e0c708

文章：[Learning from Maternal Mortality Confidential Enquiries: Sociodemographic Determinants Relevant to Equitable Guideline Development](https://europepmc.org/article/PPR/PPR1359271)

审核决定：待审核
审核备注：
证据版本：43717dcd78ea6b487d2c045a8e5c7fc73a630d26ae809829b9995245ea21ec79

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该综述比较了16个高收入国家孕产妇死亡保密调查报告中社会人口学决定因素的报告差异，并据此制定国别公平清单以支持女性健康指南的制定与评估。全文未涉及任何AI/ML算法或算法公平性评估。

纳入判断：研究对象为孕产妇死亡监测报告与指南制定的公平清单，不存在被评估的AI/ML算法，也无算法公平性/差异测量或缓解实验；仅泛化地讨论监测报告中的公平议题，属偶然提及，按规则排除。

限制：仅有摘要；未列出具体社会人口学决定因素，无算法模型、亚组公平性指标或缓解方法比较，也未提供任何实证公平性测量结果。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：sociodemographic determinants associated with maternal mortality

[分析原文](https://europepmc.org/article/PPR/PPR1359271)

## p-9d65abc11d11465e0b29

文章：[AI-powered radiology report simplification in Arabic: A prospective evaluation of patient-perceived understandability and clinical safety.](https://pubmed.ncbi.nlm.nih.gov/42546532/)

审核决定：待审核
审核备注：
证据版本：5c82109b6edf3872010adf0c80f210747690edd73bad0b9461e8fc81c1935a98

模型建议：related

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究前瞻性评估本地部署的两阶段大语言模型系统，将放射学报告简化为英语和阿拉伯语，报告患者可理解性及放射科医生判定的临床安全性，但未开展算法公平性分析。

纳入判断：研究属临床NLP系统评估，涉及阿拉伯语患者可理解性与安全性，但未提出或测量算法公平性/差异，公平性为偶提，故列为相关。

限制：仅有摘要；未按语言、性别、年龄等分组比较公平性指标，也未评估偏倚机制或缓解措施；健康公平仅作为结论愿景提及。

建议分类：Not applicable

证据：
- algorithm：The system used a two-stage pipeline: Qwen3-14B-FP8 with structured prompt engineering for English simplification
- evaluation：Patient-perceived understandability was measured on a 5-point Likert scale
- fairness：
- groups：
- medical：simplified radiology reports in plain English and Arabic for Arabic-speaking outpatients

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42546532/)

## p-b1c2ba955b21e73bf64e

文章：[Association between patients’ knee posture and patient satisfaction in primary care consultations](https://europepmc.org/article/PPR/PPR1365698)

审核决定：待审核
审核备注：
证据版本：9e905adea537aa50e41a6014ea62f801f249ea9541f52c7b55b13dd346b4a7bf

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：研究探讨门诊咨询结束前30秒患者膝关节姿势与咨询后满意度的关联，203例患者中中立姿势组满意度高于伸展姿势组；属探索性观察研究，未涉及算法或算法公平性。

纳入判断：该研究分析膝关节姿势与门诊患者满意度的统计关联，未评估任何AI/ML算法，也未提出算法公平性、群体差异或公平性测量问题，不符合纳入标准。

限制：证据仅为摘要，且为探索性观察研究；摘要未报告任何算法、敏感属性、亚组公平性指标或缓解措施。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Mean satisfaction scores were compared across the three knee-posture groups using one-way analysis of variance
- fairness：
- groups：
- medical：the association between patients’ knee posture immediately before the end of an outpatient consultation and post-consultation patient satisfaction

[分析原文](https://europepmc.org/article/PPR/PPR1365698)

## p-b450c1e3be8d7e77257b

文章：[When multi-institutional dataset aggregation masks shortcut-like behavior in Foundation Models for medical imaging.](https://pubmed.ncbi.nlm.nih.gov/42641372/)

审核决定：待审核
审核备注：
证据版本：bf9f2e01145857b608f0f00af2b566c3a03c9f7222ab10040889c0b4449c33f8

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究以乳腺X线摄影分类为任务，将预训练图像编码器（基础模型）作为特征提取器，在十个采集流程、人群与地区各异的队列上训练分类器，发现聚合异质数据会带来依赖数据集的失效模式，误差率、置信度与校准度在数据集间差异明显。表示层面可轻易恢复数据集身份而临床标签可分性较低，提示捷径式行为；测序向量分解显示任务信号多位于数据集对齐子空间。数据集对抗训练、最差组优化与平衡微调可缓解部分数据集聚差异，但常以总体性能下降为代价；探索性元数据分析还发现年龄相关的标签依赖性概率偏移。

纳入判断：摘要明确覆盖五项标准：乳腺X线摄影分类任务、以基础模型编码器为特征提取器、数据集层面的误差/校准差异与数据集身份可解码的编码证据、按数据集与地区划分的组别（并有年龄相关偏移）、以及在十个数据集上完成的实测与缓解实验。但证据等级为摘要，按规则摘要级证据不足以建议纳入，需全文核实指标、样本与缓解阶段后再定。

限制：仅有摘要级证据：未见具体队列规模、划分方式、指标定义与统计检验细节，代码与数据可得性未提及；元数据探索（年龄）为探索性分析，未给出效应量；三种缓解方法的具体设置与冻结/微调范围不明，无法确认其是否真正固定基模型，因此干预阶段只能初步判断。

建议分类：Evaluation, In-processing

证据：
- algorithm：pretrained image encoders as feature extractors
- evaluation：dataset identity is readily recoverable from Foundation Model embeddings, whereas clinical labels are less separable
- fairness：substantial disparities in error rates, confidence, and calibration across datasets
- groups：ten datasets spanning diverse acquisition pipelines, populations, and geographic regions
- medical：feature extractors for mammography classification across ten datasets spanning diverse acquisition pipelines

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42641372/)

## p-b93a39c7c0676b99e9b3

文章：[A deep learning model for detection and staging of osteonecrosis of the femoral head on x-ray images: a retrospective, large-scale, multicentre study in China.](https://europepmc.org/article/MED/42934014)

审核决定：待审核
审核备注：
证据版本：6618e0b85771ac0a33444cf1ab9a0bb4eba082d7da252b29d19acbd9a5b86e2c

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：开发并多中心验证基于YOLOv8的X线髋部检测与分期模型OsteoAID，比较其与放射科及骨科医生的诊断表现，并以MRI为参照。

纳入判断：摘要聚焦ONFH检测与分期的诊断性能及医生对比，未提出算法公平性问题，未定义敏感群体或开展亚组公平性评估，不满足纳入标准。

限制：仅有摘要；未报告按年龄、性别、种族、医院等群体的公平性分析，也无偏倚机制或缓解评估。

建议分类：Not applicable

证据：
- algorithm：based on the You Only Look Once version 8 (YOLOv8) detection network
- evaluation：compared the model's accuracy, sensitivity, specificity, F1 score, and area under the curve (AUC)
- fairness：
- groups：
- medical：detection and staging of osteonecrosis of the femoral head

[分析原文](https://europepmc.org/article/MED/42934014)

## p-c4d939a39c87bfe230c4

文章：[Explainable Classification Models for Identifying Elevated Gastrointestinal Symptom Burden in Honduran Communities: A Cross-Sectional Study.](https://pubmed.ncbi.nlm.nih.gov/43028313/)

审核决定：待审核
审核备注：
证据版本：457063401c4d806a1c5fcda7068179cca894ec4090b54bd2f8838e65ccf4d634

模型建议：related

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：在洪都拉斯5省85个社区1838名12–49岁居民中，评估可解释的人口学与生活方式模型能否识别同时存在多种胃肠道症状负担；加入既往消化系统诊断后AUROC由0.663升至0.726，逻辑回归与复杂机器学习表现相当，并报告校准、决策曲线和亚组表现。

纳入判断：该文属于医学预测模型评估，但摘要未提出算法公平、差异、编码或缓解问题，也未定义受保护群体或公平性指标；仅有亚组表现的一般提及，且摘要级证据不足以建议纳入，故列为相关。

限制：仅摘要证据；未明确公平性属性、分组定义或公平性测量问题，仅有“亚组表现”的笼统表述，无法确认全文是否包含实质算法公平分析；亦无外部验证、代码或数据可用性信息。

建议分类：Evaluation

证据：
- algorithm：Logistic regression was compared with six machine-learning classifiers
- evaluation：Discrimination, calibration, paired differences, community-level uncertainty, decision curves, SHAP explainability and subgroup performance were assessed.
- fairness：
- groups：
- medical：identify community residents aged 12 to 49 years with concurrently elevated gastrointestinal symptom burden

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43028313/)

## p-e325d3be42451c51b6cb

文章：[Memory-guided mutual information optimization in retinal imaging for early stroke detection and subtyping.](https://europepmc.org/article/MED/43014078)

审核决定：待审核
审核备注：
证据版本：940d0f887d3b3761e8ab6d0902a949fa03a923c9fe7154a22eb62ba023c90e40

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：提出 RetCEVD 框架，利用无创视网膜 OCTA 图像进行缺血性脑血管病（ICVD）辅助检测、病因亚型分型及症状状态分类，核心为记忆引导的互信息优化策略，在多中心 24,438 张图像上完成内部与外部验证并报告 AUC。

纳入判断：该文属原创方法学工作，但全文仅描述诊断性能与可解释性，未提出任何算法公平性、偏差机制、亚组比较或公平性度量问题，缺乏定义群体与公平性评估证据，故不符合纳入标准。

限制：仅有摘要：未报告代码、数据可得性、受试者人口学构成，也未涉及任何公平性/偏差分析、亚组指标或敏感属性，无法判断模型在不同人群中的差异表现。

建议分类：Not verified

证据：
- algorithm：RetCEVD introduces a memory-guided mutual information optimization strategy
- evaluation：
- fairness：
- groups：
- medical：a diagnostic framework that uses rapid, non-invasive retinal Optical Coherence Tomography Angiography (OCTA) for auxiliary assessment of ICVD

[分析原文](https://europepmc.org/article/MED/43014078)

## p-e804ebf16ba3c2515d7f

文章：[Explainable machine learning using pretreatment complete blood count parameters and demographic characteristics for gastric cancer risk stratification: a temporal validation study.](https://europepmc.org/article/MED/42959316)

审核决定：待审核
审核备注：
证据版本：1c95829ac0562dc227e654ff7fcc1e10534eb641cbbc7995d1d77684f24e7b93

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究基于单中心胃镜病理确诊队列（477例新发初治胃癌 vs 1567例良性胃病），仅用年龄、性别及治疗前血常规六项指标构建可解释机器学习模型，经时间外部验证（AUC 0.831）、SHAP解释、决策曲线与肿瘤标志物阴性亚组召回分析，强调标签质量（初治、逐例核对、去重）与简化特征集。

纳入判断：论文属于胃癌风险分层的临床预测模型开发与时间验证研究，具备明确的临床任务（胃癌vs良性胃病）、机器学习模型与实证评估，但不存在算法公平性/偏倚/差异测量问题：无亚组公平性指标、无偏倚机制或缓解方法；文中仅在讨论中顺带提及“inequity of access”，属偶发提及，不足以纳入公平性研究库。

限制：全文未开展任何算法公平性分析：年龄与性别仅作为预测变量进入模型，未按性别/年龄等分层报告性能、校准或阈值差异，也未讨论差异机制或缓解措施；单中心回顾性设计，缺乏外部队列与地理可推广性证据。

建议分类：Not applicable

证据：
- algorithm：Eight algorithms spanning linear, kernel, instance-based, probabilistic and ensemble families were trained
- evaluation：In the temporal validation cohort, discrimination remained closely comparable across models
- fairness：
- groups：
- medical：discriminates newly diagnosed, treatment-naïve gastric cancer (GC) from benign gastric disease

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13716773/fullTextXML)

## p-ebc11a06a333203c74b7

文章：[Machine learning for maternal risk prediction in resource- constrained antenatal care: evidence-to-implementation gaps and implications for Sustainable Development Goal 3](https://europepmc.org/article/PPR/PPR1365530)

审核决定：待审核
审核备注：
证据版本：9eb07a9476796b56d01aeb5b01e702e18dccfe3e482af14df4993371b484492e

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究笔记梳理资源受限产前护理中孕产妇风险预测的机器学习证据，指出高准确率可能掩盖漏诊，主张在判别力之外同时评估校准、公平、工作流和前瞻性影响。

纳入判断：摘要将“equity”和“subgroup assessment”作为实施评估清单或缺口一笔带过，未提供具体疾病场景下的亚组指标、机制或缓解分析；且仅有摘要，不能建议纳入。

限制：仅有摘要；缺少具体公平性定义、受保护属性、亚组结果和缓解方法，公平仅作为评估维度被提及。

建议分类：Not applicable

证据：
- algorithm：A Rwandan random-forest model reported 90.6% accuracy
- evaluation：
- fairness：calibration, equity, workflow integration, referral capacity
- groups：
- medical：earlier recognition of maternal risk

[分析原文](https://europepmc.org/article/PPR/PPR1365530)

## p-f352228a5c9bd18d0291

文章：[A Dual-Criterion Variable Inclusion Strategy for Improved Confounder Inclusion in Small-Sample Trauma Cohorts: An Empirical Methodological Study](https://europepmc.org/article/PPR/PPR1348111)

审核决定：待审核
审核备注：
证据版本：7394447d2306e0ecf87d5d4408cadb4932fc455fb0f8022493edab61ccc0ce0f

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：研究在88例脑挫裂伤减压术后患者中提出双标准变量纳入策略，以改善小样本创伤队列的混杂因素纳入，比较ridge回归、随机森林及模型校准，发现该策略减少单阈值筛查的遗漏偏倚并影响危险因素识别。

纳入判断：该文关注小样本临床预测中的混杂变量筛选与模型性能，未提出或评估算法公平性问题，也无受保护群体、差异或缓解分析；不符合五项证据要求。

限制：仅见摘要，无法核查全文方法细节、偏倚控制与统计假设；研究未涉及算法公平性、群体差异或缓解措施，且样本量小、单中心。

建议分类：Not applicable

证据：
- algorithm：A random-forest model was built as a comparator via leave-one-out cross-validation.
- evaluation：
- fairness：
- groups：
- medical：Pulmonary infection is a common severe complication following decompressive craniectomy

[分析原文](https://europepmc.org/article/PPR/PPR1348111)

## p-fc980d34ff004464f5b8

文章：[Simulation-Based Development, Stress Testing, and External Physiological Benchmarking of a DKA Early-Warning Framework Intended for Future Nurse-Facing Evaluation.](https://pubmed.ncbi.nlm.nih.gov/43028810/)

审核决定：待审核
审核备注：
证据版本：5a1d16f574d14495f73285f9bbe79361bac9c6bb2a5790675fe33a7a87db0ee0

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究用两万条合成15小时DKA病程数据，对比验证冻结的BHB+趋势规则与XGBoost模型的灵敏度与误报率，并通过表型匹配的反事实生命体征、阈值网格和校准分析检验模拟器捷径，另用公开IOBP2数据做生理学外部基准，发现葡萄糖分布存在显著不匹配。

纳入判断：属模拟器构建偏差与外部生理分布错配研究（合成数据捷径、阈值网格、IOBP2基准），未提出算法公平性/差异问题，未定义任何人群子组或公平性指标，故不满足公平性与分组证据要求；其偏差机制为模拟器伪相关而非人群不平等。

限制：仅有摘要，无全文方法、代码或数据链接细节；未涉及任何人群敏感属性；未报告按性别、种族、年龄等分组的表现差异；外部基准仅指向分布错配，不验证DKA预测或动力学。

建议分类：Evaluation

证据：
- algorithm：Validation-frozen beta-hydroxybutyrate (BHB) rules and XGBoost models were compared.
- evaluation：Twenty thousand synthetic 15 h episodes were generated at 5 min intervals.
- fairness：
- groups：
- medical：evaluated a simulation-based diabetic ketoacidosis (DKA) early-warning framework

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43028810/)

## p-0aed599c7fa1f8e12a36

文章：[Multiview Integration for Robust Echocardiographic Embeddings: Accessible AI for Clinical Practice.](https://pubmed.ncbi.nlm.nih.gov/43050803/)

审核决定：待审核
审核备注：
证据版本：4eb14fdcae489bffadda6e2e98f5840eb7121160ef163a9b990d2ceae6d06d29

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：开发基于Transformer的多视角超声心动图编码器，将多段视频整合为研究级向量嵌入，并在21项二分类任务上评估；同时用对抗学习降低性别和种族捷径依赖，报告较强对抗权重下可预测性下降但临床性能受损。

纳入判断：摘要显示明确的超声心动图临床任务、算法评估、性别/种族捷径公平性问题及实证测量，符合五项证据；但仅有摘要，不能据此建议纳入，需全文核验。

限制：仅见摘要，无法核查对抗训练细节、公平性定义、亚组指标、统计方法与代码数据可用性；摘要未提供完整消融或外部验证。

建议分类：In-processing

证据：
- algorithm：transformer-based multiview encoder that integrates multiple echocardiographic videos into unified vector embeddings
- evaluation：We varied adversarial weights to assess their impact on demographic shortcut reliance and overall performance.
- fairness：adversarial learning to reduce reliance on demographic shortcuts
- groups：reduced sex and race predictability only at strong weights
- medical：evaluated them on 21 binary classification tasks covering echocardiographic measurements and clinical diagnoses

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43050803/)

## p-3f6acf4e270b22ab1a5d

文章：[Improving Target-Adverse Event Association Prediction via Inverse Node Frequency Transformation to Mitigate Knowledge Graph Topological Bias](https://europepmc.org/article/PPR/PPR1373652)

审核决定：待审核
审核备注：
证据版本：2303c1860759d38583a3233ae98a487a4514db50110ec15f6e00fb3f7299542e

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：methodology

中文概述：提出逆节点频率（INF）归一化方法，用于缓解生物医学知识图中因节点度数分布不均导致的拓扑偏倚（度偏倚），并以元路径特征为基础预测靶点-不良事件关联。结果显示INF提升了低度数靶点的召回率，并在外部未用于建模的关联集上优于两种基准，属知识图谱偏倚缓解类方法研究。

纳入判断：该文在药物安全任务中对图拓扑偏倚提出归一化缓解方法并给出低度数靶点的子群性能对比，符合偏倚机制与缓解的初步线索；但仅有摘要，无法确认其是否构成算法公平性问题的完整论证与评估设计，故暂持。

限制：仅有摘要级证据，未见方法细节、数据划分、统计检验或代码链接；所述偏倚为图拓扑/度数偏倚，摘要未涉及人群敏感属性或下游健康公平性分析。

建议分类：Pre-processing

证据：
- algorithm：machine learning methods have been developed to predict these associations as edges in network data
- evaluation：evaluate their resulting target-AE association prediction performance
- fairness：a generally applicable node degree-based approach for mitigating topological bias
- groups：INF significantly improves the true positive rate (TPR/recall) for low-degree targets
- medical：Identifying significant associations between therapeutic protein targets and adverse events

[分析原文](https://europepmc.org/article/PPR/PPR1373652)

## p-410a2a1c61be26ff729a

文章：[A Distributionally Robust Framework for Safe and Generalizable Utilization of Surrogate Markers](https://arxiv.org/abs/2611.18970)

审核决定：待审核
审核备注：
证据版本：b0d879346189b76704f43feeb36c53a2a3a9e51856d734ae554d3b9e24832d28

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出分布鲁棒框架评估替代终点：将跨治疗臂反事实依赖视为部分识别，通过最大化最坏情况解释方差学习替代标志物变换，并结合迁移学习与去偏机器学习处理协变量偏移。用模拟和CKD试验评估18个月GFR变化对两年GFR变化的替代性。

纳入判断：该文满足临床任务、算法方法和实证评估，但核心是替代终点的部分识别与分布鲁棒估计，不是算法公平性、群体差异或缓解研究；无公平性定义、亚组比较或公平性测量，故排除。

限制：全文未提出或评估算法公平性问题，未定义公平性群体、亚组差异或公平性指标；仅有临床替代终点效度与鲁棒性分析。

建议分类：Evaluation

证据：
- algorithm：maximin optimization problem that learns an optimal surrogate transformation
- evaluation：Simulations demonstrate good finite-sample performance
- fairness：
- groups：
- medical：evaluating 18-month glomerular filtration rate (GFR) change as a surrogate for two-year GFR change

[分析原文](https://arxiv.org/html/2611.18970v1)

## p-46c871af6f5cd511e575

文章：[Preoperative Mortality Risk Prediction and Equity Using Preoperative Score to Predict Postoperative Mortality in a Diverse US Surgical Population: Retrospective Cohort Study.](https://europepmc.org/article/MED/43050561)

审核决定：通过
审核备注：精简表 18。人工已通过。JMIR Perioperative Medicine 的中科院大类分区待核。
证据版本：a272060680441dfdd461e4f20ae4f6d789dbbac39e4d2251329049a47a852bdf

模型建议：suggest_include

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性队列研究利用All of Us数据评估POSPOM术前死亡风险评分在17,262例手术患者中的判别与校准，并按种族/民族亚组描述30天和1年死亡差异；发现高危患者判别下降、黑人患者绝对死亡率更高但事件数少，提示需外部验证和重新校准。

纳入判断：评估POSPOM在多样化美国手术人群中的死亡预测及种族/民族亚组公平性，属任务特定算法公平审计；虽事件少且无缓解，仍符合纳入标准。

限制：基于All of Us EHR数据，30天死亡仅12例，亚组分析为描述性且未做正式校准检验；未实施或比较缓解措施。

建议分类：Evaluation

证据：
- algorithm：The Preoperative Score to Predict Postoperative Mortality (POSPOM) is a validated, point-based tool
- evaluation：the POSPOM model demonstrated an AUC of 0.764 for 30-day mortality
- fairness：To evaluate model fairness and calibration across different demographic strata, a stratified analysis was conducted
- groups：Race was categorized as White, Black, Asian, or other, and ethnicity was coded as a binary variable
- medical：estimates postoperative mortality using only preoperative variables, including age, comorbidities, and surgical procedure type

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13781298/fullTextXML)

## p-8e1089bbb872533b5f51

文章：[Self-report label bias in machine learning screening for undiagnosed diabetes: development, validation and offline on-device deployment of an interpretable HbA1c-anchored tool.](https://pubmed.ncbi.nlm.nih.gov/43033525/)

审核决定：待审核
审核备注：
证据版本：e5ac5d1338b761bf10cfac87e3ef2b034e6d1c7fd3e9e83e816453df201ad743

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：methodology, recall

中文概述：该研究基于NHANES与BRFSS数据，量化自报糖尿病诊断标签如何改变机器学习筛查模型优先识别人群的方式，显示自报标签部分编码了就医可及性；用正-未标记学习校正标签，并开发以HbA1c为锚点的可解释筛查工具，在相同转诊率下与指南规则比较敏感度并做离线部署验证。

纳入判断：摘要明确涉及标签偏倚（自报诊断编码就医可及性）、社会经济属性归因的比较分析以及经验性验证，五项标准在摘要层面均有对应证据；但按规则仅有摘要证据不能直接建议纳入，需获取全文核实亚组定义与公平性评估细节。

限制：仅提供摘要级证据：亚组定义方式、公平性指标细节、标签校正方法的实现与部署评估均未展开；数据为单一调查周期的回顾性资料，外部验证样本小（388人）且需重新校准，缺乏前瞻性验证。

建议分类：Evaluation, Pre-processing

证据：
- algorithm：An Explainable Boosting Machine (EBM) and three guideline rules were compared at equal referral rates
- evaluation：Paired models differing only in their label were compared by Shapley attribution and risk-rank shift
- fairness：Self-reported diagnosis labels partly encode access to care
- groups：Access and socioeconomic items carried 23.8 % of attribution under the self-reported label
- medical：the 13-item EBM found 85 % (95 % CI 75-94) of HbA1c-defined undiagnosed cases

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43033525/)

## p-b34d58a13643bfcc986f

文章：[AI-Based Prediction of Total Porosity Volume Fraction from 3D CT Volumes: A Volumetric Regression Approach](https://europepmc.org/article/PPR/PPR1370350)

审核决定：待审核
审核备注：
证据版本：e1b76d4d035f95054661fbf4133db1d4041a5efbee8cf18ccb0c559433dd8ce9

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出用带全局平均池化的3D CNN从含噪3D CT体积直接回归总孔隙体积分数，绕过体素分割；与Otsu阈值和随机森林基线比较，并分析合成数据中的捷径学习。

纳入判断：该文是工业CT孔隙率回归方法，属于非医学无损检测；未提出算法公平性问题，未定义受保护群体或开展公平性测量，故不满足医学算法公平性纳入标准。

限制：仅提供摘要；研究对象为工业无损检测合成CT数据，不涉及临床任务、受保护群体或算法公平性评估；无法确认全文细节。

建议分类：Evaluation

证据：
- algorithm：using a 3D Convolutional Neural Network (CNN) equipped with Global Average Pooling (GAP)
- evaluation：The 3D CNN was evaluated against classical Otsu thresholding and a Random Forest (RF)
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1370350)

## p-e7d4ce6f3482649fcced

文章：[Multiparametric 0.4-T low-field MRI mapping for metabolic dysfunction-associated steatotic liver disease in rats.](https://europepmc.org/article/MED/43034251)

审核决定：待审核
审核备注：
证据版本：756da0f806def39639296b1850652a1184c9395ad4d54206c24fcff9ebfa5523

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：研究在90只MASLD大鼠中比较0.4-T MRI的T1、FcT1、T2、T2*和PDFF与全切片数字病理，并评估深度学习重建AIRS对T1定量的影响；结果显示各指标与脂肪、炎症、纤维化呈部分阶段依赖相关，AIRS可改变T1绝对值。

纳入判断：该研究评估低场MRI定量指标及深度学习重建对T1测量的影响，未提出或检验算法公平性问题，也未按敏感属性进行亚组比较，不属于医学算法公平性研究。

限制：全文为动物实验，仅评估MRI指标与病理相关性及AIRS重建的测量偏移；未定义算法公平性问题，未按敏感属性分组，也未进行差异或缓解分析。

建议分类：Not applicable

证据：
- algorithm：Image-domain deep-learning reconstruction (SwiftMR version 3.0.13.1; AIRS Medical) was applied only to T1 mapping
- evaluation：AIRS ON produced a mean 2ptIR T1 increase of 10.64 ms relative to AIRS OFF
- fairness：
- groups：
- medical：multiparametric 0.4-T MRI with deep-learning-reconstructed T1 mapping would provide complementary, pathology-correlated readouts in a rat MASLD model

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13769794/fullTextXML)

## p-f6c51344bb4b7f0ff028

文章：[Causally Constrained and Uncertainty-Aware Cardiopulmonary Risk Prediction](https://arxiv.org/abs/2611.17819)

审核决定：待审核
审核备注：
证据版本：cfd8b3752fd45de7176791f07e0d60801132d3d7b26702d9d7b1366327e07330

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出CE-Agent两阶段心肺风险预测框架，将流行病学证据预先编译为因果约束，再拟合临床与胸部CT表型权重，并用闭式不确定性传播处理缺失输入；在NLST与MESA中评估判别、校准、跨医院与跨扫描仪泛化以及联合肺癌和心血管分诊。

纳入判断：该文为心肺风险预测方法学研究，虽含种族/民族与扫描仪亚组泛化评估，但全文未提出或测量算法公平性、差异、编码或缓解问题，也未报告公平性指标；属于临床稳健性与域泛化研究，不符合公平性纳入标准。

限制：全文仅报告按医院、扫描仪及种族/民族分组的外部泛化与校准表现，未定义公平性目标、差异指标或任何缓解干预；亚组性能不等并不构成算法公平性证据。

建议分类：Multi-stage

证据：
- algorithm：a two-stage framework that compiles peer-reviewed epidemiological evidence
- evaluation：CE-Agent outperformed eight survival and ML baselines
- fairness：
- groups：adults from four racial/ethnic groups imaged on four CT scanner platforms
- medical：Routine chest computed tomography (CT) captures pulmonary, cardiac, and vascular phenotypes

[分析原文](https://arxiv.org/html/2611.17819v1)

## p-92a449ec5369eaed3e6f

文章：[Association between biological age acceleration and the risk of aortic valve stenosis: An observational epidemiologic and Mendelian randomization study.](https://pubmed.ncbi.nlm.nih.gov/42998401/)

审核决定：待审核
审核备注：
证据版本：ba3e349831e8cda515531f3ec5daf888befdc70eeb1afdd066b94336f876de29

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究基于RED-CARPET与ARIC队列及孟德尔随机化，评估KDM-BA和PhenoAge计算的生物学年龄加速与主动脉瓣狭窄风险的关联，发现BAA与AVS风险及严重程度相关，并提示KDM-BA加速可能具因果关联。

纳入判断：该文研究生物学年龄加速与主动脉瓣狭窄的关联，虽使用年龄算法并做性别/种族亚组，但未围绕算法公平性、差异或缓解进行设计与测量，故不符合纳入标准。

限制：全文为流行病学关联与孟德尔随机化研究，未提出或检验算法公平性问题；性别/种族仅作协变量或效应异质性亚组，无公平性指标、偏倚机制或缓解评估。

建议分类：Not applicable

证据：
- algorithm：We used the KDM-BA and PhenoAge algorithms to calculate participants’ biological ages
- evaluation：logistic regression analysis showed that both KDM-BA acceleration and PhenoAge acceleration were significantly positively correlated with AVS risk
- fairness：
- groups：we performed subgroup analyses according to a number of strata: age (>61 years vs. ≤61 years), gender (female vs. male)
- medical：Aortic valve stenosis (AVS) is the most prevalent valvular heart disease worldwide

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13769574/fullTextXML)

## p-05c60193f5811117e901

文章：[Hierarchical detection of neonatal brain pathologies using a two-stage deep learning framework from magnetic resonance imaging.](https://pubmed.ncbi.nlm.nih.gov/43031676/)

审核决定：待审核
审核备注：
证据版本：f2115b393ccefbfca6cb890a34e04563f5cf2c022513a7760c517c3a6bfcf28f

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

正式版本线索：[Hierarchical detection of neonatal brain pathologies using a two-stage deep learning framework from magnetic resonance imaging](https://doi.org/10.3389/fnimg.2026.1981436)

中文概述：该研究提出两阶段分层深度学习流程，基于新生儿T1/T2加权脑MRI，先用脑龄差筛查髓鞘化延迟，再用3-D ResNet-18进行正常、HIE与脑积水三分类，并报告阶段2 AUC为0.919。

纳入判断：摘要聚焦新生儿脑病理分层检测和模型性能，未涉及算法公平性、亚组差异、公平性指标或缓解方法，不满足公平性综述纳入标准。

限制：仅有摘要，缺少全文方法、代码和公平性分析；未报告人口学亚组、差异指标或缓解措施，无法评估算法公平性。

建议分类：Evaluation

证据：
- algorithm：hierarchical two-stage deep learning pipeline
- evaluation：Experiments demonstrate that a regression from MRI scan to age with an R 2 of 0.941
- fairness：
- groups：
- medical：Automated neonatal brain pathology detection from magnetic resonance imaging (MRI)

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43031676/)

## p-1d69c85a37b528600868

文章：[SIGHT: A Methodological Appraisal Framework for Evaluating Large Language Models in Ophthalmology](https://arxiv.org/abs/2610.15958)

审核决定：待审核
审核备注：
证据版本：7d0469e88e46326e1625305b13a987f84169bf59b4e8f6e1a484bfed5a449f6d

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文批判性综述眼科大语言模型评价研究，提出SIGHT五域二十项方法学评价框架，关注样本来源、盲法、对照公平性、配对数据处理与透明度，旨在提升研究内部有效性和临床相关性。

纳入判断：摘要表明该文为眼科LLM评价的方法学框架，仅在框架域名称中出现“comparator fairness”，未提供算法公平性、群体差异或公平性实证测量；且仅摘要可见，按规则不能建议纳入。

限制：仅摘要可见；无受保护属性、亚组指标、偏倚机制或缓解措施的具体信息；“fairness”为通用评价域，非算法公平性分析。

建议分类：Evaluation

证据：
- algorithm：ophthalmic LLM evaluation studies
- evaluation：
- fairness：
- groups：
- medical：Large language models (LLMs) are increasingly evaluated across ophthalmic tasks

[分析原文](https://arxiv.org/abs/2610.15958)

## p-1e7d50a645f4a3f54c29

文章：[Amino acid-based formula and &lt;i&gt;Clostridioides difficile&lt;/i&gt;-associated disease in infants: concerns regarding causal interpretation.](https://europepmc.org/article/MED/43018394)

审核决定：待审核
审核备注：
证据版本：c5f982d4b168d2a66b589af49a5e4d9d57f519d2e43f8145395aa3d57e742f6e

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：本文评论氨基酸配方喂养与婴儿艰难梭菌相关疾病关联研究，指出因果推断的混杂、事件数不足等方法学问题，并建议前瞻性研究设计；不涉及AI/ML或算法公平性。

纳入判断：文章为儿科营养与感染领域评论，讨论AAF与CDAD关联的因果解释，未评估AI/ML算法，也未提出或测量算法公平性、子组差异或缓解方法，不符合纳入标准。

限制：仅有摘要/评论文本，无AI或算法，也无子组公平性指标、机制或缓解评估；不能作为医学算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：associated disease (CDAD) in children younger than two years

[分析原文](https://europepmc.org/article/MED/43018394)

## p-2f7dce3877d44026419f

文章：[Healthcare providers' use and acceptance of translation technologies in multilingual healthcare settings: a cross-sectional study.](https://pubmed.ncbi.nlm.nih.gov/42919266/)

审核决定：待审核
审核备注：
证据版本：2dbe3fbccbe731ea3ce456b1ad1ba1774edc9422286aac031742633675178804

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：对443名医疗及心理社会服务提供者开展横断面调查，基于技术接受模型分析翻译技术使用与行为意向，发现感知有用性关联最强，并报告准确性、隐私及治理顾虑。

纳入判断：该研究是翻译技术使用与接受度的横断面调查，仅一般性讨论语言障碍与公平照护；未评估具体医学AI/ML算法的公平性、亚组性能或偏倚机制，且仅有摘要，不能纳入。

限制：仅有摘要，未说明翻译技术是否属AI/ML、具体工具与临床任务；无患者亚组公平性指标、偏倚机制或缓解评估；无法核验全文方法。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：multivariable ordinary least squares regression with HC3-robust inference examined factors associated with behavioural intention to use translation technologies
- fairness：
- groups：
- medical：experiences with language barriers, communication strategies, and acceptance of translation technologies

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42919266/)

## p-57d9615bd4c80bff0bd7

文章：[Acute Stroke Classification Using Asymmetric Data Standardization and Orthogonal-Focal Loss Optimized CNN-ViT Cross-Attention Fusion: A Multicenter External Validation Study](https://arxiv.org/abs/2610.34529)

审核决定：待审核
审核备注：
证据版本：7e6edad25eda400924dd78215773a3f30de1958d2a77cd814b58861f470c8265

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出一种用于急性卒中分型的CNN-ViT交叉注意力CAD系统，结合非对称预处理与正交焦点损失，并进行多中心外部验证；内部F1为95.48%，外部降至58–62%，报告硬件噪声相关域偏移及缺血性卒中敏感性偏低。

纳入判断：摘要聚焦卒中分型模型与跨中心泛化，未提出算法公平性问题，也未定义受保护群体或开展亚组公平性评估；仅报告域偏移和敏感性下降，按规则不足以纳入。

限制：仅基于摘要，未提供公平性/亚组分析、敏感属性定义或公平性指标；外部验证性能下降属于域偏移与稳健性问题，不能作为算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：The architecture utilizes a novel joint cross-attention fusion network optimized by an Integrated Orthogonal-Focal Loss.
- evaluation：multi-center external validation (AISD, BHSD, PhysioNet) using a Mask Anchor filter
- fairness：
- groups：
- medical：Rapid differentiation of ischemic and hemorrhagic stroke subtypes is vital for acute management.

[分析原文](https://arxiv.org/abs/2610.34529)

## p-6302d520f84e30bd29ca

文章：[Intervention-Conditioned Counterfactual Human Digital Twin Generator](https://arxiv.org/abs/2610.40664)

审核决定：待审核
审核备注：
证据版本：4e0497523a15eebe68001a22d1bf51ee4e274790257cc15b6cff26d8ef716bbc

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出CHDT，一种干预条件化的人类数字孪生生成器，用于痴呆患者纵向多模态轨迹估计和模拟临床试验；在ADNI与ALPACA上评估轨迹保真度，强调不规则访视间隔和跨中介变量建模。

纳入判断：论文聚焦痴呆纵向轨迹生成与反事实模拟，虽为医学AI方法学研究并有实证评估，但没有算法公平性、差异、编码、缓解或公平性测量问题，故排除。

限制：全文未提出算法公平性问题，未按受保护群体评估差异，也未报告偏倚机制或公平性缓解措施；性别和人口学仅作为静态协变量。

建议分类：Not applicable

证据：
- algorithm：we propose CHDT, an intervention-conditioned Human Digital Twin generator
- evaluation：Experiments are conducted across four complementary scenarios using real-world ADNI data
- fairness：
- groups：
- medical：we use dementia as the case study because of its long-term, irregular, and multimodal progression

[分析原文](https://arxiv.org/html/2610.40664v1)

## p-9e0c0082c950e7fca73e

文章：[HiSTOR: Structured Treatment-outcome Representation Learning for High-Dimensional Longitudinal Data](https://arxiv.org/abs/2610.17739)

审核决定：待审核
审核备注：
证据版本：908dd10488b3c59c7c09b7e5d49dc1a0336aa3a9b2c5f321ac53560d542d6472

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：提出HiSTOR，用结构化低维表征联合编码当前患者状态与纵向病史，在指定治疗序列下预测一步及多步反事实结局，并在CVSim、CancerSim等模拟数据上评估。

纳入判断：论文关注高维纵向数据的反事实结局预测与混杂调整，表征平衡服务于因果混杂而非算法公平；未定义敏感属性、未做亚组公平性测量，故不满足公平性标准。

限制：全文未见敏感属性定义、亚组公平性指标或算法公平性干预评估；主要证据为反事实预测误差比较。

建议分类：In-processing

证据：
- algorithm：an end-to-end framework that integrates nonlinear dimension reduction with longitudinal counterfactual prediction
- evaluation：Experiments on CVSim and CancerSim demonstrate the superiority of HiSTOR
- fairness：
- groups：
- medical：CancerSim models tumor volume under four treatment options

[分析原文](https://arxiv.org/html/2610.17739v1)

## p-c1f95a81a24c991508ae

文章：[PVminerLLM: structured extraction of patient voice from patient-generated text using large language models.](https://europepmc.org/article/MED/42952888)

审核决定：待审核
审核备注：
证据版本：7cddf0ae4b5153317250568e40034c9502a5922cfa2e8fb8e3eb43e8c0869fce

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：PVminerLLM 提出 PVminer 基准与一个监督微调的大语言模型，用于从患者生成文本中结构化抽取“患者声音”（如社会处境、就医参与等非临床信息），在代码、子代码与证据片段抽取上取得最高约 84%、81%、88% 的 F1，并声称小模型也可达到较好效果。

纳入判断：该文是临床 NLP 信息抽取的模型与基准工作，属于原方法类，但公平性仅以“health equity”一句背景性提及出现，既未定义受保护群体/属性，也未设计公平性评测或偏差分析，五项准入标准中的公平性、分组与公平性测量均不成立；按规则属偶发提及，不作为相关文献推荐。

限制：仅有摘要。摘要只给出抽取任务的 F1 指标，没有子群定义、公平性度量、偏差机制分析或缓解方法；对“健康公平”仅有一句目的性表述，无任何实证公平性评估，也未提供数据或代码信息。

建议分类：Not applicable

证据：
- algorithm：PVminerLLM, a supervised fine-tuned large language model tailored to this task
- evaluation：
- fairness：
- groups：
- medical：Reliable extraction of such information is therefore essential for understanding and addressing non-clinical drivers of health outcomes at scale.

[分析原文](https://europepmc.org/article/MED/42952888)

## p-c2c763dae41b68b833ad

文章：[Association of Immunomodulatory Treatment with Long-Term Visual Outcomes in Behçet Uveitis: A Single-Center Retrospective Study.](https://europepmc.org/article/MED/43001002)

审核决定：待审核
审核备注：
证据版本：55437d8038294d4e468cd25628daa9e2a1b192e0666d25a9472dbbaeb87b5558

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：单中心回顾性研究描述Behçet病相关葡萄膜炎的临床特征与治疗模式，并探索免疫调节治疗与长期视力结局的关联；未涉及人工智能算法或公平性分析。

纳入判断：研究评估免疫调节治疗与视力结局的临床关联，未评估任何AI/ML算法，也未提出公平性、偏倚或亚组差异问题；五项纳入标准均不满足。

限制：仅有摘要，样本量小（30例），为回顾性观察且存在混杂；全文不涉及算法、公平性、亚组公平性指标或缓解评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/43001002)

## p-c72b7ceb52cbb11f8611

文章：[The Federated Tumor Segmentation and Classification (FeTS++) Challenge](https://arxiv.org/abs/2610.18771)

审核决定：待审核
审核备注：
证据版本：df21fed61b95dc7f7a184d7b1b6bcdc2ca2242afd1f19f26d35e0b17f5dd08a3

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文介绍FeTS++ 2027联邦脑肿瘤分割与分类挑战：基于多机构mpMRI，锁定模型架构，评估不同聚合与客户端训练策略在站点异质性和实体标签偏斜下的表现，并采用效率感知排名；论文仅描述挑战设计，未报告结果。

纳入判断：文章涉及医学影像AI与站点标签偏斜，但未提出明确的算法公平性测量，且无实证结果，未达到纳入标准，仅可作为相关联邦基准参考。

限制：全文为挑战设计，明确不报告结果，未提供算法公平性亚组指标或实证评估；站点标签偏斜主要属于联邦异质性与类不平衡，尚非明确的公平性分析。

建议分类：Evaluation

证据：
- algorithm：Participants develop weight aggregation strategies and client training behavior
- evaluation：
- fairness：
- groups：18 of the 26 training sites are entity-pure (16 glioma-only, 2 meningioma-only)
- medical：federated brain tumor segmentation (Task 1) and federated brain tumor classification (Task 2)

[分析原文](https://arxiv.org/html/2610.18771v1)

## p-11142b1729015cc61ea3

文章：[Responsible Artificial Intelligence: Guiding Principles for Orthopaedic Surgery.](https://europepmc.org/article/MED/43037611)

审核决定：待审核
审核备注：
证据版本：0632f0e57ea396ce0d9b27afa185d78b568dc879ae36cd2f7a65a6d6c40f1ced

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：本文为骨科领域负责任人工智能的指导原则类评论，提出透明与可解释、临床可靠性与价值导向、与人类价值对齐、算法公平、公平照护问责、临床专家监督六项原则，主张在肌肉骨骼照护中安全、公平地采用AI。全文仅在原则层面提及公平，未针对具体疾病或任务给出亚组指标、偏差机制或评估框架。

纳入判断：属评论/指导原则类文献，仅泛泛提出公平原则与伦理治理建议，未命名具体骨科疾病或任务，也未提供实质性的算法公平分析（亚组指标、机制或评估框架），不满足评论类两项条件；且证据仅为摘要，不能据此建议纳入。

限制：仅有摘要，无具体骨科疾病或任务，无定义受保护群体、无亚组指标或实证测量结果，公平性仅作为六项原则之一被一句话提及，缺乏可核验的详细分析证据。

建议分类：Not applicable

证据：
- algorithm：reliable, value-oriented models built on representative data and robust processing
- evaluation：
- fairness：algorithmic fairness, meaning defining fairness and balancing tradeoffs
- groups：
- medical：improve musculoskeletal care quality, efficiency, and outcomes

[分析原文](https://europepmc.org/article/MED/43037611)

## p-21e07c40e92ded8603f5

文章：[Between Obligations and Evidence: A Participatory Study of Translating the EU AI Act into Technical Requirements](https://arxiv.org/abs/2611.18439)

审核决定：待审核
审核备注：
证据版本：ac67f0acbbe286c9e0fb4a69d021cada72d84790766b166ba271ae7158ea7e19

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文通过32人参与式工作坊，围绕医疗疼痛估计、招聘与公共交通三个高风险场景，分析欧盟AI法案义务如何转化为技术需求、组织实践与合规证据，指出公平指标不能单独证明非歧视，并讨论监督、责任和部署变化导致证据失效。

纳入判断：文章属于AI法案合规的参与式治理研究，不是医疗算法公平性评估；虽提及疼痛估计场景和公平指标局限，但缺少定义群体与实证公平测量，未满足五项证据标准。

限制：全文为定性工作坊主题分析；医疗疼痛估计仅为假设场景，未定义受保护群体，未报告亚组公平指标或实施医疗算法公平性测量，主要贡献在治理与证据有效性。

建议分类：Not applicable

证据：
- algorithm：A system could accurately estimate pain while supporting interventions that clinicians considered inappropriate.
- evaluation：
- fairness：favorable fairness metrics cannot, by themselves, establish the absence of unlawful discrimination
- groups：
- medical：a multimodal pain estimation system for patients

[分析原文](https://arxiv.org/html/2611.18439v1)

## p-7abe2e1b40324a466501

文章：[Correcting historical bias in machine learning predictions of healthcare utilization in India.](https://europepmc.org/article/MED/43050464)

审核决定：待审核
审核备注：
证据版本：ec79cbc5218c0a5eb04c0f2a13e6f9ef37e483e8986d0f8a5ae97e9be1e57f28

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：methodology, recall

中文概述：基于印度LASI 55,698名老年人数据，训练门诊和住院利用预测模型，比较全样本与排除未满足医疗需求子样本模型在不同社会经济与种姓亚组间的预测差异，并用SHAP和全国成本外推评估历史可及性差异的影响。

纳入判断：摘要显示该研究针对医疗利用预测开展亚组差异实证评估，具备算法、公平性问题、定义群体和测量证据；但仅有摘要，按规则不能建议纳入，需获取全文进一步核验。

限制：仅有摘要，无法核查全文的模型设计、公平性指标、亚组分析细节、缓解措施及完整结果；不能确认代码或数据可用性。

建议分类：Evaluation

证据：
- algorithm：we trained two sets of ML models
- evaluation：We compared model outputs across socioeconomic subgroups
- fairness：We examine prediction differences across disadvantaged populations
- groups：particularly among lower-income and caste-identified groups
- medical：predictions of healthcare utilization among older adults in India

[分析原文](https://europepmc.org/article/MED/43050464)

## p-b3eae538180f8f9919dd

文章：[Causal Humility: Governing the Authority of Fairness Claims Under Causal Uncertainty](https://arxiv.org/abs/2610.25709)

审核决定：待审核
审核备注：
证据版本：6a34eb038a0153a0094d9bcc6a5f0a70cc734b28aa5eb640b77b0247e3265917

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：methodology, recall

中文概述：提出“因果谦逊”治理原则与Causal Cards文档工具，用PC/FCI/GES在UCI Adult收入数据上展示因果发现差异如何使公平相关路径可见、缺失或未定。

纳入判断：全文聚焦通用AI治理与因果公平不确定性，案例为UCI Adult收入预测；无具体医学疾病/临床任务，也无医学算法公平性评估，按范围规则排除。

限制：全文证据；但案例为UCI Adult收入预测，未涉及临床数据、患者群体或具体医学任务，不能支持医学算法公平性入库。

建议分类：Not applicable

证据：
- algorithm：Causal approaches to algorithmic fairness address this explanatory problem
- evaluation：We apply three widely used CD procedures to the same observed feature set
- fairness：Fairness assessment often requires more than identifying disparities in outcomes
- groups：Race , Sex , Age , and Marital Status as fairness-relevant attributes
- medical：

[分析原文](https://arxiv.org/html/2610.25709v1)

## p-fe3978ecbe1170a7faa8

文章：[Balancing transparency and fairness: a proposal for phased visibility in JME's generative AI declaration framework.](https://pubmed.ncbi.nlm.nih.gov/42580885/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-4e22d89fc1a2a51893ed

文章：[Latent profiles of artificial intelligence ethical awareness and their association with professional identity among nursing interns: A multicentre cross-sectional study](https://europepmc.org/article/PPR/PPR1369288)

审核决定：待审核
审核备注：
证据版本：87ea05126cbd9944b280a41f1357a4dc7d5ab8d8558a6f34e429c4f738486e8b

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究对中国12家医院的550名护理实习生开展多中心横断面调查，采用潜在剖面分析基于AI伦理意识六个维度识别出三种意识类型，并比较其专业认同差异及与教育水平、AI熟悉度等因素的关联。

纳入判断：主题为护生AI伦理意识潜在剖面与专业认同的调查研究，未涉及对具体医疗AI/ML算法的公平性评估，也无敏感属性分组比较或偏见测量；“algorithmic fairness”仅在结论中作为伦理教育内容一笔带过，属于偶然提及，不符合纳入标准。

限制：仅有摘要，无全文方法、量表与统计细节；研究关注护理实习生AI伦理意识的潜在类别，未评估任何医疗AI算法的公平性或群体绩效差异，“算法公平”仅作为教育内容被提及。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1369288)

## p-85c646041c7ede02228d

文章：[Advancing FAIR sharing for epidemiological, clinical and public health study data: the German National Research Data Infrastructure (NFDI4Health).](https://europepmc.org/article/MED/43037923)

审核决定：待审核
审核备注：
证据版本：8a525d723c9abc11104ca3bdc77979e809aae0ed4c695738f3bcc42f1a5a11b8

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文介绍德国国家研究数据基础设施NFDI4Health的建设成果：通过健康研究枢纽、本地数据枢纽、FDPG门户、可互操作元数据模式、匿名化与合成数据工具、联邦分析框架等，提升流行病学、临床与公共卫生研究数据的FAIR（可发现、可访问、可互操作、可复用）共享水平。

纳入判断：摘要聚焦健康数据的FAIR共享基础设施与元数据互操作，未涉及医疗算法公平性/偏倚问题，缺少定义的受保护群体或亚组发现协议，也无公平性实证评估。摘要中“AI support for metadata annotation”仅为元数据标注工具，并非被评估公平性的算法，故不满足纳入标准。

限制：仅有摘要级证据；文中“FAIR”指数据管理原则，与算法公平性无关。摘要未提及对任何AI/ML算法进行亚组公平性评估、偏差测量或缓解实验。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：health data is essential for advancing epidemiological, public health and clinical research

[分析原文](https://europepmc.org/article/MED/43037923)

## p-4403cfa217b51b32b9c0

文章：[Application of Explainable Machine Learning for Individualized Risk Stratification and Surgical Optimization in Geriatric Intertrochanteric Fractures.](https://pubmed.ncbi.nlm.nih.gov/42980212/)

审核决定：待审核
审核备注：
证据版本：d72c8af2bdd1fed4965283145e3cb8f3c25451fd84dfa3b5e2a21babac8b014c

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性队列研究纳入628例股骨转子间骨折行头髓内钉固定的患者，用12个临床与影像变量构建随机森林模型预测内固定失败，并用SHAP分析内侧化进钉点与尖顶距（TAD）的非线性交互，发现内侧化进钉点在TAD超过25mm时具有缓冲效应（测试集AUC 0.877）。

纳入判断：摘要聚焦股骨转子间骨折内固定失败的预测建模与SHAP可解释性分析，虽满足临床任务、算法评估与实证测量，但完全没有公平性、差异性、编码或缓解问题，也未定义受保护群体或亚组发现方案，属于与医学算法公平性无关的文献，故排除。

限制：仅有摘要，无法核查模型细节、人群构成与亚组分析；文中未涉及任何公平性、亚组差异或偏倚测量内容，只有整体预测性能与生物力学解释。

建议分类：Not applicable

证据：
- algorithm：A Random Forest model was developed using 12 clinical and radiographic variables to predict implant failure.
- evaluation：The predictive model demonstrated robust performance (AUC: 0.877) on an independent testing set.
- fairness：
- groups：
- medical：Mechanical failure remains a critical complication in the fixation of intertrochanteric fractures.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42980212/)

## p-4d615fab90a24703edd1

文章：[Context is all you need: A causal framework for governing bias in clinical AI.](https://pubmed.ncbi.nlm.nih.gov/42993732/)

审核决定：待审核
审核备注：
证据版本：893978f5ab662c424228b13b61fc2bd838e32e70e170ff35755b2bd7add53d62

模型建议：related

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：文章主张以因果与规范监督区分临床人工智能中临床合理与不合理的群体差异，提出六项标准、四种实现路径，以及兼顾临床敏感性与偏差降低的双向评估设想；未涉及具体疾病或实证实施。

纳入判断：主题直接涉及算法公平，但为通用临床人工智能治理框架，未命名具体疾病或任务，且无已实施的实证或测量评估；摘要级证据不足以建议纳入。

限制：仅有摘要；属概念框架，未指明具体临床任务、队列或子组指标，所提标准与评估路径均未实施，无法核验。

建议分类：Not verified

证据：
- algorithm：a model trained only to detect statistical association
- evaluation：
- fairness：a differential alone does not establish unjustified bias
- groups：race, income, housing status, or gender identity
- medical：Clinical AI systems can produce different recommendations

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42993732/)

## p-af26ec6de648c002a857

文章：[Background Bias Assessment and Mitigation in Plant Disease Detection Using EfficientNet-B0 with Image Processing](https://arxiv.org/abs/2611.00049)

审核决定：待审核
审核备注：
证据版本：f9460969c72abbad76330b4f29c27e744c16da0ac781973c84eebccd1056e1da

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：methodology

中文概述：该文针对植物病害检测中 EfficientNet-B0 的背景捷径偏差，提出原图、仅叶片、仅背景三条件评估协议，并在 PlantVillage 上量化背景偏差系数，发现模型主要依赖叶片特征。属于农业视觉偏差评估，不涉及医学临床任务或受保护人群公平性。

纳入判断：研究对象为植物病害检测，不属于 biomedical/clinical 任务；虽评估背景偏差并有三条件实验，但未涉及医疗算法、定义群体/敏感属性或群体公平性评估，不符合纳入标准。

限制：仅有摘要；未提供医学任务、临床数据或受保护群体/敏感属性定义；背景偏差不等于医疗算法中的群体公平性；未报告群体公平性指标或缓解效果。

建议分类：Evaluation

证据：
- algorithm：combines standard transfer learning using EfficientNet-B0
- evaluation：three-condition evaluation protocol testing models on original, leaf-only, and background-only images
- fairness：
- groups：
- medical：

[分析原文](https://arxiv.org/abs/2611.00049)

## p-d62b2748ad6ed04dbe11

文章：[C3E-RRG:Confounder-Aware Causal Evidence Coupling and Evolution for Chest X-Ray Report Generation.](https://europepmc.org/article/MED/42970651)

审核决定：待审核
审核备注：
证据版本：977d63c6602debfa3ed472677ea2ff296ead8ab73fb4bc16a01c43ea2bca0aec

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：提出C3E-RRG，在胸片报告生成中融合语言先验与疾病共现以构建混杂变量，并通过跨模态证据一致耦合和双向因果演化抑制模板与共现引起的虚假相关；在IU-XRay和MIMIC-CXR上验证。

纳入判断：论文聚焦胸片报告生成的混杂因素与虚假相关，未涉及敏感属性、亚组比较或公平性评价，属于一般去偏/稳健性方法，不构成医学算法公平性研究。

限制：仅有摘要；未定义敏感属性、人群亚组或公平性指标，文中bias指报告模板与疾病共现造成的混杂，不能证明人群间公平性差异。

建议分类：In-processing

证据：
- algorithm：we propose C3E-RRG, a confounder-aware causal debiasing framework for chest X-ray report generation
- evaluation：Experiments on the IU-XRay and MIMIC-CXR datasets demonstrate competitive performance
- fairness：
- groups：
- medical：Chest X-ray report generation aims to produce diagnostic descriptions grounded in imaging evidence.

[分析原文](https://europepmc.org/article/MED/42970651)

## p-0c8552b1982b0a8ff7f6

文章：[A Relational Framework for Artificial Intelligence-Assisted Shared Decision Making.](https://europepmc.org/article/MED/43028666)

审核决定：待审核
审核备注：
证据版本：3c15bb0868a2bab3535c7cafbe380a5a28bd07bbda414bf4349f6f3b37b29a99

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该定性框架综合文章提出AI辅助共享决策的关系框架，围绕AI输出的表面权威、可核验与可质疑性、偏好替代、不确定性与责任分散五项关系关切，转化为可观察的临床要求、临床测试与治理响应，并提出区分技术性能、决策过程、关系质量、公平、安全与治理结果的候选测量框架。

纳入判断：摘要显示为AI辅助共享决策的通用关系与治理框架，仅将equity列为候选测量维度之一，缺少特定疾病或任务的算法公平分析、分组指标、偏差机制或缓解方法评估，也无算法公平的实证测量，故排除。

限制：仅摘要可获取；未报告具体疾病或临床任务、受保护群体定义、公平指标或任何实证测量，公平仅在候选测量框架中被概括提及，未展开机制、分组比较或缓解评估。

建议分类：Not applicable

证据：
- algorithm：observable relational requirements for AI-assisted shared decision making
- evaluation：
- fairness：
- groups：
- medical：can support clinical decision making

[分析原文](https://europepmc.org/article/MED/43028666)

## p-2ffcd2507b0c8b7fa267

文章：[Improving the impact of medical student research through structured mentorship: a clinical research enterprise model.](https://europepmc.org/article/MED/42209435)

审核决定：待审核
审核备注：
证据版本：e6bd90a681d406b6de413340366c4ca1003c83fedefb738cefe5c0062b2ee6e8

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：本文介绍一个医学生临床研究企业式纵向导师制项目，报告2019—2025年的论文产出、引用和职业发展等结果，属于医学教育项目评估。文中仅笼统提及公平与人工智能工具使用，未涉及医疗算法公平性评估、偏倚机制或缓解方法。

纳入判断：文章主题是医学生研究导师制与科研产出，不是医疗AI/算法公平性研究。公平仅作为教育培训可及性的泛泛目标出现，未评估算法偏倚、亚组差异或缓解措施。

限制：仅提供摘要，缺少完整方法、参与者特征和公平性相关分析；没有算法、分组属性、亚组指标或公平性实验证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42209435)

## p-6006fe0002047d48542a

文章：[Nanopath: Fast, Fair, Open Experimentation for Pathology Foundation Models](https://arxiv.org/abs/2611.10014)

审核决定：待审核
审核备注：
证据版本：0af613beee1f087eb8cfefc7a34ffa129d9c8679c7de0abc5bb81ec790d0738f

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：methodology

中文概述：Nanopath 是一个开源框架与基准，用于在单张 H100 上快速训练与评测小型病理基础模型：以 100 万张 TCGA 切片呈现和 10^18 FLOPs 为固定预算，配合 25 分钟内完成的冻结特征评测套件，并与 THUNDER、HEST、PathoBench(CPTAC) 对比 20 个编码器以验证代理评测的保真度。

纳入判断：全文以切片/WSI 病理任务和基础模型评测为核心，具备医学任务、算法与实证测量，但公平性仅指“公平比较实验条件”，未提出针对人群亚组的差异、编码或缓解问题；采集中心鲁棒性属站点偏移，单独不足以构成本综述范围内的算法公平性研究，故列为相关而非纳入。

限制：文中的“fair”指固定数据/算力预算的公平比较，而非算法公平性；未定义人群敏感属性或亚组差异指标。唯一偏倚相关部分是采集中心鲁棒性(CRoMa)与下尾裕度，属域/站点偏移，且模型未做临床验证。

建议分类：Evaluation

证据：
- algorithm：nanopath, an open-source framework and benchmark for rapidly training and evaluating small-scale pathology foundation models
- evaluation：We therefore evaluated six nanopath models and 14 reference models
- fairness：
- groups：
- medical：The suite covers tile classification, semantic segmentation, slide-level progression, mutation prediction, survival prediction, and representation robustness.

[分析原文](https://arxiv.org/html/2611.10014v1)

## p-7652b47d50048b573dbf

文章：[Causal Learning with Invalid Instruments for High-dimensional Imaging Responses](https://arxiv.org/abs/2611.13187)

审核决定：待审核
审核备注：
证据版本：8d2396f838d829bb4fb0d1b13f20bfec6862ecfba45258e69ff879a4e8cd5465

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出Hi-FIVE框架，利用高维影像的空间结构，在候选工具变量多数可能局部无效时估计空间变化的因果效应，并给出可识别性、估计、渐近推断及分布式算法，应用于ADNI中磷酸化tau对FDG-PET的因果分析。

纳入判断：该文是统计因果推断方法学工作，虽包含ADNI的FDG-PET临床任务和实证分析，但没有明确的算法公平性/差异问题、敏感群体定义或公平性测量，属于非公平性因果方法，超出本综述范围。

限制：全文关注工具变量无效性与因果识别偏倚，未涉及算法公平性、敏感属性、亚组差异或公平性缓解与评测，因而不能作为医学算法公平性研究纳入。

建议分类：Not applicable

证据：
- algorithm：we propose High-dimensional Functional-imaging Instrumental Variable Estimation (Hi-FIVE)
- evaluation：Hi-FIVE is illustrated with an analysis of the effect of phosphorylated tau on FDG-PET imaging
- fairness：
- groups：
- medical：effect of phosphorylated tau on FDG-PET imaging in the Alzheimer’s Disease Neuroimaging Initiative

[分析原文](https://arxiv.org/html/2611.13187v1)

## p-99104d3f909768840511

文章：[Rethinking University Mental Health for the AI Era: From Crisis Response to Core Mission.](https://europepmc.org/article/MED/43013291)

审核决定：待审核
审核备注：
证据版本：44100dd440473b0b59df659d27990341273a23aa4b735464830555975e9a2200

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：文章主张将大学生心理健康纳入大学核心使命，提出整合数字工具、分级照护与精准治疗算法的校园心理健康体系，并强调AI治理、安全与公平。

纳入判断：该文为面向大学心理健康体系的评论/综述，未针对具体医学疾病或任务开展实质性算法公平性分析；公平与公平性仅出现在概括性治理建议中，缺少定义群体、测量或评估证据。

限制：仅有摘要；未提供具体算法公平性评估、亚组指标、偏差机制或缓解方法比较，公平仅作为治理原则被提及。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：37% to 58% of first-year students worldwide meet 12-month criteria for a DSM-5 disorder

[分析原文](https://europepmc.org/article/MED/43013291)

## p-a036330c773f5ab14093

文章：[Building and Validating a Data-Governance Workflow for Artificial Intelligence-Based Tuberculosis Detection from Chest Radiographs, and Quantifying the Impact of Data Leakage.](https://europepmc.org/article/MED/42888308)

审核决定：待审核
审核备注：
证据版本：5a03de6de120797b549dbbec40770074188657785468bd28759d4fe281274600

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：提出七步数据治理流程（多源标准化、溯源管理、MD5/pHash/dHash 三重去重、患者级划分、不变性核查、肺分割、指纹版本冻结），在 46,410 张胸片、七个公开来源上量化去重缺失与随机划分造成的数据泄漏对 AUC 的影响，结论是泄漏量级依数据结构而定、必须被测量，治理流程使复用可验证。

纳入判断：该文研究去重、患者级划分等数据治理与数据泄漏对 AUC 的虚高影响，属评测有效性与稳健性问题；摘要未提出任何算法公平性、偏倚机制、敏感属性分组或亚组指标问题，不满足公平性准则，故不纳入。

限制：仅有摘要，未见全文方法与代码；文中不含任何公平性/亚组分析，未按人群属性分层报告性能；泄漏效应在三分类多源任务中不足 0.1 个百分点，主要见于单源探针任务，效应量有限。

建议分类：Evaluation

证据：
- algorithm：applying artificial intelligence (AI) to tuberculosis (TB) detection
- evaluation：repeated 20 times with paired splits and compared with the clean scenario
- fairness：
- groups：
- medical：tuberculosis (TB) detection from chest radiographs (CXR)

[分析原文](https://europepmc.org/article/MED/42888308)

## p-a3955dfee5639efddf72

文章：[Theoretical analysis of transfer learning for temporally dependent observations.](https://pubmed.ncbi.nlm.nih.gov/43023018/)

审核决定：待审核
审核备注：
证据版本：1a443863ecba2430e38874e7be72231a46fbd9de0e364999ac43c5189e401d73

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：本文研究高维向量自回归模型下的迁移学习理论，提出两步迁移学习流程、辅助数据集的信息子集选择方法，以及两种用于参数推断的“去偏”技术，并在温和条件下建立理论性质，最后用模拟数据和EEG数据集检验经验表现。

纳入判断：该文为时间序列迁移学习的通用统计理论研究，摘要中的“去偏”是参数推断偏差校正而非公平性偏差；缺乏敏感属性分组、公平性度量或公平性评估，EEG仅作为示例数据，未构成医学算法公平性研究。

限制：仅有摘要：所谓“debiasing”指统计推断中的偏差校正，与算法公平性无关；未见敏感属性、亚组分析或公平性度量，也未定义具体临床任务。

建议分类：Not applicable

证据：
- algorithm：we focus on high-dimensional vector autoregressive models and provide a two-step procedure to conduct transfer learning
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43023018/)

## p-a9324f28d8acd70d333c

文章：[Ethical guidelines for deploying artificial intelligence applications in the pathology field: Lessons learned from a prospective framework in a large tertiary care academic medical center.](https://pubmed.ncbi.nlm.nih.gov/42761742/)

审核决定：待审核
审核备注：
证据版本：08cd9aaafcb4011e0133eb5034c669021e4e9559db1b7d0883a5e08b9f06c389

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：文章讨论病理学AI中的年龄、性别、种族和族裔代表性偏差，提出覆盖治理、预处理、处理、部署和监测的伦理指南框架，强调公平使用与持续监测。

纳入判断：属伦理/治理指南类评论，仅泛称病理学领域，未命名具体疾病或AI任务，摘要也未提供任务特异性的详细公平性分析或实证测量；按规则排除此类泛化公平建议。

限制：仅见摘要；未给出具体病理AI任务、亚组指标、偏差测量结果或实证评估，也未见框架实施效果与代码数据信息。

建议分类：Multi-stage

证据：
- algorithm：Several artificial intelligence (AI) algorithms have been developed with inherent age, sex, gender, racial, and ethnic biases.
- evaluation：
- fairness：propose an ethical framework for addressing representation and bias in AI in pathology
- groups：marked performance disparities across different demographic groups
- medical：tailored specifically to lab medicine and pathology workflow

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42761742/)

## p-ae502679561d916dd517

文章：[AI alone will not transform healthcare: Learning Health Systems as the framework for responsible AI implementation.](https://europepmc.org/article/MED/43004359)

审核决定：待审核
审核备注：
证据版本：8d1dfa790d8ca8c57e59a45ceb42dc2a807910a0d7a9774f5a8ef6cee4aeb6f5

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：本文为评论文章，主张将医疗AI实施嵌入学习型健康系统（LHS），结合CFIR、ERIC、TEHAI等框架，强调持续评估、治理、子组监测与公平实施。引用美国医院调查指出AI采纳不均和偏倚评估不足，但未对具体临床任务开展算法公平性实证分析。

纳入判断：文章类型为评论，虽提及AI偏倚评估和公平实施，但仅作一般性LHS/治理建议；未针对糖尿病视网膜病变或脓毒症等具体任务给出实质性算法公平性分析，也无实施的公平性测量评估，故排除。

限制：仅评论/概念框架，无原始数据或实验；公平性讨论停留在系统层面的采纳差异、监测建议和治理清单，未提供具体疾病任务的子组指标、偏倚机制或缓解方法比较。

建议分类：Not verified

证据：
- algorithm：The TREWS machine-learning sepsis alert achieved high clinician adoption
- evaluation：
- fairness：more than half did not evaluate bias
- groups：those serving high-need communities were significantly less likely to adopt these tools
- medical：Fewer than half of hospitals reported using AI-based predictive models

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13746506/fullTextXML)

## p-b0b37535e71cc95770d9

文章：[Causal gradient intervention for debiased and evidence-grounded medical visual question answering.](https://pubmed.ncbi.nlm.nih.gov/42526079/)

审核决定：待审核
审核备注：
证据版本：b3b7ecabe3a522a5821c70065a48063d11dfd37d8a7b8f660353b5d106c54811

模型建议：related

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：提出DE-CaGI因果梯度干预框架，用于医学视觉问答；通过辅助分支估计语言与视觉先验造成的捷径偏置梯度，在主干更新中抑制相关分量，并引入多任务证据监督与证据一致性约束，以提升答案准确性和视觉证据对齐。在VQA-RAD和SLAKE上验证。

纳入判断：医学VQA任务与算法明确，并在VQA-RAD/SLAKE开展实证；但其偏置指捷径学习而非受保护群体公平，未定义敏感属性或公平性评估，故仅为相关研究，且摘要证据不能建议纳入。

限制：仅依据摘要，无法核查全文方法、代码与统计细节；研究针对语言/视觉先验和数据结构造成的捷径偏置，未涉及受保护人群属性或群体公平性指标。

建议分类：In-processing

证据：
- algorithm：we propose DE-CaGI, a causal gradient intervention framework
- evaluation：Experiments on VQA-RAD and SLAKE demonstrate stable improvements on both open-ended and closed-ended questions
- fairness：
- groups：
- medical：Medical Visual Question Answering (Med-VQA) aims to answer clinically relevant questions based on medical images.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42526079/)

## p-bd98d28296dc8ae83062

文章：[Equipping the next generation: addressing the unmet need for artificial intelligence education at research performing organizations.](https://europepmc.org/article/MED/42888462)

审核决定：待审核
审核备注：
证据版本：88c15d97dbe3b88734bb3d2858fddbb067268f0c717ada62ee29ec9813d85ca7

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：本文是一篇评论文章，基于对1200余名医学与生命科学学生及博士后的国际调查，指出生成式AI使用率高但缺乏正规培训与机构政策，并呼吁将AI素养纳入科研与临床教育，重审学术诚信框架，制定透明的负责任使用政策。文中仅在一般性建议层面提及识别幻觉与偏见、促进公平获取。

纳入判断：该文为教育政策评论，焦点是科研机构中生成式AI素养与学术诚信治理。文中未界定具体临床/生物医学任务，也未评估任何算法的公平性（无亚组指标、无偏见机制分析、无实证测量），公平与偏见仅为泛泛的伦理建议，故不满足纳入所需的五项证据标准。

限制：仅有摘要层面证据。全文未涉及任何具体医学疾病或临床任务，也未对某个医学AI算法开展公平性测量、亚组比较或缓解方法验证；“bias”“equity”仅出现在通用教育政策建议中。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42888462)

## p-bf40e25d08ab87dffbbc

文章：[CONFIRM: Governing Scientific Reporting for Trustworthy Agentic Neuroimaging](https://arxiv.org/abs/2611.01449)

审核决定：待审核
审核备注：
证据版本：1aee8b341ea8bca7f24ac01d45b83a056aecfe549173c012f8fd2e3f24359329

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出CONFIRM框架，将LLM神经影像分析中的报告决策与执行分离，通过预先固定的分析计划和确定性门控（多重比较、混杂、功效、稳定性、重复）判定发现是否可报告，并构建489条可执行声明的NeuroClaimBench。

纳入判断：论文评估LLM代理神经影像报告中的方法学偏倚（如站点混杂、多重比较），属于科研可重复性与可信性框架，未提出或测量医学算法公平性、群体差异或缓解措施，因此不符合公平性主题。

限制：全文围绕科研报告有效性与混杂控制，未按种族、性别、年龄等群体开展公平性评估，也未定义公平性指标或差异分析；site/scanner仅作为统计混杂因素。

建议分类：Evaluation

证据：
- algorithm：Large language model (LLM) agents can autonomously run neuroimaging analyses
- evaluation：489 executable neuroimaging claims with frozen data
- fairness：
- groups：
- medical：hippocampal volume decreases in Alzheimer’s disease

[分析原文](https://arxiv.org/html/2611.01449v2)

## p-c2d58d64ab882a71dc49

文章：[Is postoperative adjuvant therapy necessary for esophageal cancer patients with pathological complete response after neoadjuvant treatment?](https://pubmed.ncbi.nlm.nih.gov/42731259/)

审核决定：待审核
审核备注：
证据版本：6a673498247d69ee044b408969b5ca308d2cb4e89e870b6fc9bb07be1cdf5a9a

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性队列研究纳入184例新辅助治疗后达病理完全缓解（pCR）的食管癌患者，采用IPTW比较术后辅助治疗与观察的生存差异，发现cT4a为独立预后危险因素，辅助治疗可降低并延迟复发，并提出按cT4a/cN分层选择辅助治疗的风险适应决策方案。

纳入判断：本文为食管癌pCR患者术后辅助治疗的临床预后研究，提出的“风险适应决策算法”是基于生存分析的临床规则，并非受评估的AI/ML系统；文中无算法公平性/偏倚/编码或缓解问题，也未定义敏感属性分组或公平性测量，五项证据标准中公平性、分组与公平性评估均不成立。

限制：仅有摘要，无全文方法学细节；研究为单中心回顾性队列，属临床疗效与预后分层分析，未涉及任何AI/ML模型的公平性评估、亚组公平性指标或偏倚机制。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：184 esophageal cancer patients with confirmed pCR after completed neoadjuvant therapy

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42731259/)

## p-c3083ca58bc9a9905bcc

文章：[Evidence of limited biases in probed language-based assessments.](https://europepmc.org/article/MED/43002526)

审核决定：待审核
审核备注：
证据版本：5d849557f46038278514a23898e5534e3571de8bb5631feaaa1814e2164e44fc

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：methodology, recall

中文概述：该研究评估开放式心理健康自述经大语言模型嵌入加岭回归预测抑郁/焦虑严重度的公平性：1260名参与者的评估误差与性别、年龄、教育、就业、收入等社会人口学变量及语言特征关联有限，但症状越重评估偏差越大；对训练数据下采样可消除该偏差。

纳入判断：摘要同时具备临床任务（抑郁/焦虑评估）、算法（LLM嵌入+岭回归）、明确公平性提问、受保护群体与实证测量五要素，并探索下采样缓解；但按规则仅摘要证据不足以建议纳入，需获取全文核实后判定。

限制：仅有摘要，无法核实亚组样本量、统计检验细节、下采样等缓解策略的具体设计与效应量，也无法确认误差度量与临床可用性讨论；摘要中的“有限偏差”结论需全文佐证。

建议分类：Pre-processing

证据：
- algorithm：converted these descriptions to numeric representations using large-language-model-generated embeddings and applied ridge regression
- evaluation：Most variables showed minimal association with assessment errors
- fairness：exhibit systematic biases that could undermine their clinical utility
- groups：sociodemographic factors (gender, age, education, employment, and income)
- medical：validated depression (Patient Health Questionnaire-9) and anxiety (Generalized Anxiety Disorder Scale-7) scores

[分析原文](https://europepmc.org/article/MED/43002526)

## p-ccc4d9f092e8030e2195

文章：[Medical Fine-Tuning Reshapes, Not Reduces, Patient-Facing AI Risk: A Rubric-Based, LLM-Judge Evaluation Framework](https://arxiv.org/abs/2610.24807)

审核决定：待审核
审核备注：
证据版本：a10e9f4f6666d21d9459a67650e053401e05b9806be64de095d7981195bc4bff

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出面向患者医疗问答大模型的风险敏感评测框架，按六类风险语言及严重度用LLM评审集成评估六个7–9B模型在K-QA上的表现；发现风险语言与事实幻觉基本独立，医学微调并未降低而是重塑风险。

纳入判断：该文提出患者问答LLM风险语言评测框架并实证比较通用与医学微调模型，但未提出或测量算法公平性，也未定义人口学群体、亚组或差异指标，不满足公平性核心条件；仅作为相邻的医疗LLM安全评测相关。

限制：仅200个问题、6个7–9B模型；部分风险类别评审一致性低；缺乏临床医生校准与人口学亚组/公平性分析，不能支持公平性结论。

建议分类：Evaluation

证据：
- algorithm：We apply this framework to six modern 7–9B instruction-tuned models
- evaluation：We apply this framework to six modern 7–9B instruction-tuned models
- fairness：
- groups：
- medical：Patient-facing medical question answering with large language models (LLMs) is moving from research demonstrations to production deployments

[分析原文](https://arxiv.org/html/2610.24807v1)

## p-e91c09dd8b3e74599212

文章：[Clinical AI in Canadian Community Hospitals: A Framework for Implementation Readiness.](https://europepmc.org/article/MED/42880210)

审核决定：待审核
审核备注：
证据版本：d643fe40de0bbedd377a9ef5c8079d1650eae732a428a42f3ad089c7945fe395

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：提出加拿大社区医院临床AI实施准备框架，围绕情境有效性、社会技术工作流整合、人机依赖校准以及安全、公平与治理四个维度，通过模拟系统测试加以落实，并以CHARTwatch早期预警系统作为实践示例。

纳入判断：摘要仅在实施准备框架中列出“equity”维度，属于泛泛的公平AI治理建议；未给出具体临床任务下的亚组分析、偏倚机制或公平性评估，按偶然提及规则排除。

限制：仅有摘要；公平仅作为治理维度之一被提及，未针对具体临床任务报告亚组指标、偏倚机制或算法公平性测量，也未提供任何实证评估结果。

建议分类：Not verified

证据：
- algorithm：guidance for machine learning-enabled medical devices addresses manufacturer responsibilities
- evaluation：
- fairness：
- groups：
- medical：the CHARTwatch early warning system, illustrates the dimensions in practice

[分析原文](https://europepmc.org/article/MED/42880210)

## p-ec7c0f5cb541d6dacee9

文章：[Is it possible to vaccinate AI against bias? An exploratory study in epilepsy.](https://europepmc.org/article/MED/43014131)

审核决定：待审核
审核备注：
证据版本：55d2622a2a5a756195d3d63168045a02733db9e0e59819b3d16e5302f901778b

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该探索性概念验证研究在癫痫临床情景中测试提示指令能否减少六个大语言模型的诊断/治疗准确率差距。富裕与弱势复合画像在性别和社会描述上共同变化；结果按原评分规则重新计算，提示后汇总差距下降，但作者指出不能隔离社会经济偏倚或证明临床有效的去偏干预。

纳入判断：摘要显示其针对癫痫LLM诊断/治疗情景开展公平性测量和提示干预，并报告群体准确率差距，符合任务、算法、公平、群体和测量要点；但仅有摘要且作者承认无法隔离偏倚，无法核验全文细节，故保留待全文评估，不直接建议纳入。

限制：仅提供摘要，无法核验完整方法、模型版本与全部运行；复合画像同时改变性别和社会描述，作者也明确不能隔离社会经济偏倚或确立临床有效去偏；摘要级证据不足以建议纳入。

建议分类：Not verified

证据：
- algorithm：six models, two prompt conditions, and ten repetitions per cell
- evaluation：Diagnostic accuracy under this rubric increased from 43/120 (35.8%) to 66/120 (55.0%)
- fairness：the signed pooled accuracy gap decreased from 45.0 to 26.7 percentage points
- groups：affluent and a disadvantaged composite profile, differing jointly in sex and social descriptors
- medical：One diagnostic and one treatment vignette each had an affluent and a disadvantaged composite profile

[分析原文](https://europepmc.org/article/MED/43014131)

## p-ee8b2a7189a3d8b4887f

文章：[Large Language Models' Simulation of Patient Comprehension of Discharge Summaries: Multimodel Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42912964/)

审核决定：待审核
审核备注：
证据版本：21d37622152aa9daea0671d3a0debe6dd0fd2587124678fab34cdfe44a6b48e4

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究用4个当代LLM按教育、性别和医疗使用生成患者人设，模拟对出院小结的理解回答，并以模态绝对误差和序数距离比较其与99名人类参与者的对齐，考察各亚组公平性及思维链敏感性。

纳入判断：摘要显示其评估LLM模拟不同患者群体回答的公平性，五项标准表面均满足；但证据仅为摘要，按规则不能建议纳入，需全文核验。

限制：仅有摘要，缺少全文方法、样本构成、统计检验、具体亚组数值及代码/数据信息，无法核验公平性评估的完整性和可复现性。

建议分类：Evaluation

证据：
- algorithm：We evaluated 4 contemporary LLMs, GPT-4.1, GPT-5.2, Claude Sonnet 4.5, and Opus 4.6
- evaluation：Model-human alignment was measured using modal mean absolute error and expected absolute ordinal distance.
- fairness：whether persona-based simulation performance was equitable across subgroups
- groups：personas defined by education, gender, and health care use
- medical：simulate diverse patient perspectives on hospital discharge summaries

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42912964/)

## p-ef01908a70510b22bc66

文章：[Progressing From Association to Causation: Examining Prior Antibiotic Exposure and Antimicrobial Resistance Across Three US Health Systems Using Causal Machine Learning.](https://europepmc.org/article/MED/42878671)

审核决定：待审核
审核备注：
证据版本：b0486cc3ce9d2e3edc0004f005d3053935cc0dfd85bdad24470333f36b2c876c

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：利用双机器学习，在三个美国医疗系统的1,165,151次培养事件中估计既往90天抗生素暴露对同类耐药的因果效应，校正35个以上混杂因素，并用逆概率加权、E值、暴露窗口与剂量-反应敏感性分析及阴性对照进行稳健性验证；同时比较既往同类暴露者经验性治疗无效的比例。

纳入判断：该研究以因果机器学习估计抗生素暴露与耐药的因果关系并支持处方优化，属因果推断与临床用药研究；未提出算法公平性/偏倚问题，也无按种族、性别、年龄或机构等群体的差异测量，混杂校正不等于公平性分析，故超出范围。

限制：仅有摘要证据，无法确认全文是否含代码、数据或亚组分析；文中未定义任何公平性属性或亚组，机构间一致性属外部验证而非公平性差异评估。

建议分类：Evaluation

证据：
- algorithm：estimated by double machine learning, adjusting for more than 35 confounders per site
- evaluation：Robustness was assessed via inverse probability weighting, E-values, exposure-window and dose-response sensitivity, and negative-control pairs
- fairness：
- groups：
- medical：Prior antibiotic exposure was consistently associated with increased same-class nonsusceptibility across antibiotic classes and health systems

[分析原文](https://europepmc.org/article/MED/42878671)

## p-04210e1f154be8b67c44

文章：[Development and regional validation of a literacy-fair verbal cognitive screen for older adults in India.](https://europepmc.org/article/MED/43042671)

审核决定：待审核
审核备注：
证据版本：1fc46af8895a04c50520360148498bb5ebc79ae8ea5302749d034d000857ac47

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：methodology

正式版本线索：[Development and regional validation of a literacy-fair verbal cognitive screen for older adults in India](https://doi.org/10.1177/13872877261507060)

中文概述：该研究在印度LASI-DAD队列（n=4096）中开发并验证完全口语化、无读写依赖的认知筛查模型Verbal-4，按识字水平分层比较AUC，并进行留一区域验证与临床CDR对照，报告不同识字组判别力相近且具独立预后信息。

纳入判断：摘要显示研究针对识字相关测量偏倚开发并验证口语化痴呆筛查模型，并按识字水平报告分层AUC及留一区域验证，初步具备医学任务、算法评估、公平性问题、分组定义与实证评估五项要素；但证据仅为摘要，无法核实全文的公平性分析与亚组评估细节，故暂缓判断。

限制：仅有摘要，缺少模型系数、公平性指标定义、缓解措施细节，也无代码或数据链接；按识字分组的公平性证据仅为单一亚组AUC对比，区域验证中判别力衰减原因未明。

建议分类：Evaluation

证据：
- algorithm：we derived a screen from prop-free verbal tasks (LASSO then forward selection)
- evaluation：performed leave-one-region-out validation and addressed incorporation bias
- fairness：To derive and validate a fully verbal, literacy-fair candidate cognitive screening model.
- groups：The sample was 57.5% illiterate
- medical：Brief cognitive screens could narrow India's dementia detection gap

[分析原文](https://europepmc.org/article/MED/43042671)

## p-a837a6597aee491abb27

文章：[AI-Assisted Voice Analysis for Laryngeal Cancer: Primary Care Perspectives on Clinical Implementation](https://europepmc.org/article/PPR/PPR1371788)

审核决定：待审核
审核备注：
证据版本：a18da1e800a2b80033041e2a9fc07c9d30abece8dd2d0e78f3f0c620ad0fe797

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：一项混合方法横断面研究，通过访谈（15人）与匿名问卷（16份）考察基层医生对持续性发声困难的处理方式，以及对语音人工智能用于喉癌风险分层的接受度。结果显示医生普遍将其视为决策支持而非替代临床判断，采纳取决于准确性、流程影响、监督、转诊路径及公平可及性等条件。

纳入判断：该文为临床实施可行性与医生接受度的调查研究，虽涉及喉癌语音AI，但仅在结论中泛泛提及“equity、隐私与问责”，未定义受保护群体、未开展任何算法公平性测量或偏差机制分析，属于偶发提及公平性的文献，按规则排除而非列为相关。

限制：仅为摘要级证据，样本量小且为描述性统计与主题分析，无算法模型、亚组指标或公平性测量；公平性仅作为实施条件被提及一次，缺乏对特定群体的定义或差异分析。

建议分类：Not verified

证据：
- algorithm：Voice-based artificial intelligence may offer a noninvasive approach
- evaluation：
- fairness：
- groups：
- medical：identifying patients at elevated risk for laryngeal cancer

[分析原文](https://europepmc.org/article/PPR/PPR1371788)

## p-f1ccea6d3b9e79ddd33c

文章：[Crossing the Divide: From AI Awareness to AI Assurance in Nursing Administration.](https://europepmc.org/article/MED/43036953)

审核决定：待审核
审核备注：
证据版本：c1b7edc4e8f4377fccd81c375aa313a72f70ca7b537020125d69913ea611296a

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为护理管理视角的评论文章，主张把AI保障（治理、风险管理、持续监测）纳入护理领导职责，提出治理与问责、公平与偏倚缓解、临床性能与安全监测、透明与伦理、员工能力准备五个领导域，属政策与治理框架综述，未针对具体疾病或临床任务开展算法公平性分析或实证测量。

纳入判断：文章为护理管理AI保障的评论/框架性论述，公平与偏倚缓解仅在领导域列表中被泛泛提及，未命名具体医学任务，也未提供亚组指标、偏倚机制、评估框架或缓解方法比较；无实证或详细的任务特异性综合，属偶发提及的治理类文献，且仅有摘要证据。

限制：仅有摘要：无具体疾病或临床任务、无亚组指标或偏倚机制分析、无数据集或实证测量；公平仅作为治理框架中的一项被列举，属泛化倡议，无法据此评估任何算法的公平性表现。

建议分类：Not applicable

证据：
- algorithm：governance, risk management, and continuous monitoring to ensure AI systems are safe, reliable, equitable
- evaluation：
- fairness：equity and bias mitigation
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/43036953)

## p-263284ee8b9a724f7139

文章：[Leveraging AI-ECG Technology for Early Notification and Tracking of AF Development (LATENT): A Randomized Controlled Trial.](https://pubmed.ncbi.nlm.nih.gov/42998297/)

审核决定：待审核
审核备注：
证据版本：504d1b1fa0a063fe9e71a4b63b5f0e29b979534cc4a6736a83b4b2d9adcfb896

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：LATENT为单中心、开放标签随机对照试验，评估AI-ECG风险分层引导的Holter监测能否提高新发房颤、房扑及前房颤心房表现的检出率。14 665名40–85岁无房颤史成人入组，主要复合终点为0.74% vs 0.48%（OR 1.54，P=0.046），作者自述结果统计学上脆弱、对1例事件重分类敏感。

纳入判断：该研究是AI-ECG临床有效性的随机对照试验，满足临床任务与AI算法两项，但未提出任何算法公平性、差异、编码、缓解或公平性测量问题，也未定义敏感属性群体或开展亚组公平性分析；按基线AI风险分层的交互作用属临床效应异质性而非公平性分析，故不满足公平性、群体与公平性评估标准，予以排除。

限制：仅有摘要证据；未报告按性别、年龄、种族等敏感属性分层的检出率、误差或公平性指标；年龄与性别匹配仅用于减少确认偏倚，属研究设计而非公平性分析；无任何公平性测量或缓解方法，无法据此判断算法公平性。

建议分类：Not applicable

证据：
- algorithm：whether AI-enabled ECG (AI-ECG) is effective for detecting atrial fibrillation
- evaluation：
- fairness：
- groups：
- medical：14 665 adults 40 to 85 years of age without previous AF/AFl were randomized to an AI-ECG-guided strategy or usual care

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42998297/)

## p-2e0706f35cfba2dd0a08

文章：[Confronting the Twin Divides: Data Bias and Infrastructure Gaps in AI-Driven Nutrition for the Global South.](https://pubmed.ncbi.nlm.nih.gov/42988168/)

审核决定：待审核
审核备注：
证据版本：2f46e2fd457d643ad0c60a9d816bf4559a5456dd128c046bbf31b222483fb4fa

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：评论讨论全球南方AI营养应用中的数据偏差与基础设施差距，提及FRANI应用及营养不良模型临床使用不足，呼吁在部署前加强本地数据主权、基础设施和治理。

纳入判断：摘要为观点评论，虽点名营养不良与食物识别，但仅有泛化的数据偏差与基础设施论述，未展示分组指标或具体公平性评估；仅摘要不足以判断全文，故暂缓。

限制：仅摘要；缺少方法、分组结果、定量评估与全文细节，不能确认是否满足详细公平性分析要求。

建议分类：Not applicable

证据：
- algorithm：Nutrition science is being rapidly transformed by artificial intelligence (AI).
- evaluation：
- fairness：data bias (e.g., non-diverse datasets, imbalanced samples, and inadequate attention to demographic, cultural, and socioeconomic variation)
- groups：demographic, cultural, and socioeconomic variation
- medical：more than 90% of AI models for malnutrition go unused in day-to-day clinical practice

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42988168/)

## p-50b0d41fc4e4a86d358b

文章：[Weight-space programming for auditing clinical decision networks](https://arxiv.org/abs/2611.05341)

审核决定：待审核
审核备注：
证据版本：6f4b7522f2a992ae94e264f77ef48d0799945e3ca4867609967bd17b7064b2e1

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究评估用前沿语言模型直接读写小型临床决策网络权重，以审计和修复头颈放疗计划分诊网络中的混淆规则、3 Gy 阈值漂移和隐藏触发器；在约42万条请求上验证诊断与权重编辑，并比较黑箱测试、权重统计和微调。

纳入判断：该文是医疗决策网络审计/修复的方法学研究，涉及捷径和触发器偏倚机制，但全文没有算法公平性、差异或受保护群体分析；因此作为相邻工作标记为 related，不满足 suggest_include 的五项标准。

限制：证据仅来自合成请求、小规模网络（433–4,801参数）和单一模型家族；未定义受保护人群或测量公平性差异，不能作为医疗算法公平性证据。

建议分类：In-processing

证据：
- algorithm：Claude Opus 5.5 audited each network blind, without tools, data or code execution
- evaluation：every claim and repair was tested on about 420,000 requests
- fairness：
- groups：
- medical：screen head-and-neck planning requests against four rules

[分析原文](https://arxiv.org/html/2611.05341v1)

## p-661da0b4bcd2cc1ecf87

文章：[Vision Paper: Why Distributed LLM Post-Training and Decentralized Alignment Are Now Essential](https://arxiv.org/abs/2611.05841)

审核决定：待审核
审核备注：
证据版本：3746f91d138b4e258e11c5a68484986112eadab7c21a560761deb05492c2c25a

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文主张将联邦与去中心化学习作为LLM后训练和偏好对齐的一等范式，提出FedDPO、D-DPO及参考漂移缓解SRU，并用小规模GPT-2实验验证参考漂移与DP-效用问题；未涉及具体医学疾病或临床任务。

纳入判断：文章是通用LLM去中心化对齐愿景，虽讨论代表性与公平，但未针对具体医学疾病或临床任务开展算法公平性分析或评估，按范围规则排除。

限制：仅以医疗、法律等作为应用示例，未定义临床任务、患者群体或医学公平性指标；实证评估为小规模分布式DPO收敛与隐私实验，并非医学算法公平性评估。

建议分类：In-processing

证据：
- algorithm：Current methods like RLHF and DPO rest on an invisible assumption: preference data should be centralized.
- evaluation：Appendix A provides preliminary numerical results supporting our claims
- fairness：systematically overrepresent English‑language, Western, and high‑income perspectives
- groups：partitioning along natural lines: language, domain, or demographics
- medical：

[分析原文](https://arxiv.org/html/2611.05841v1)

## p-7ce27dede71de2b2c84e

文章：[Paradoxical inflation of prediction model performance measures in minority patient subgroups: the role of upstream bias.](https://europepmc.org/article/MED/42907563)

审核决定：通过
审核备注：精简表 13。人工已通过。npj Health Systems 的中科院大类分区待核。
证据版本：3d8d3bf0421f806e5a49eafa6afaf9d581942179de4fb1449d775157c4ddc645

模型建议：suggest_include

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究复现两个术后持续阿片使用预测模型在Black患者中AUC反而更高的现象，并用1:1/1:2倾向评分匹配White患者，发现基线特征差异可解释大部分AUC差距，提示上游偏倚可造成少数群体性能虚高，建议亚组AUC报告辅以匹配分析。

纳入判断：全文报告针对术后持续阿片使用预测的实证公平性评估：比较Black与White患者AUC，并用倾向评分匹配检验基线特征对差异的解释，符合医学任务、算法评估、公平性问题和实证测量要求。

限制：单中心回顾性研究；匹配无法排除未测量混杂、标签噪声和测量差异；AUC仅为公平性的一部分，且部分亚组样本量有限。

建议分类：Evaluation

证据：
- algorithm：The logistic regression model to predict POU included key demographic, clinical, and patient-reported predictors
- evaluation：Each Black patient was matched to their nearest one or two White patients without duplication
- fairness：differences in baseline patient characteristics between Black and White patients are sufficient to explain much of the observed AUC disparity
- groups：We conducted subgroup analyses for all models to evaluate model performance separately in Black and White subgroups.
- medical：predicting persistent opioid use (POU) after surgery

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13687106/fullTextXML)

## p-90e758f61454cf309cc5

文章：[Toward equitable fidelity measurement of evidence-based psychosocial interventions.](https://europepmc.org/article/MED/42956225)

审核决定：待审核
审核备注：
证据版本：72fb183c222eb9021ab48f9eb4da614cc6bd2e8f16a828159af50d5636855eff

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：摘要讨论心理社会循证干预中临床医生保真度（fidelity）测量的公平性问题：观察性保真度编码成本高、在资源匮乏环境中很少使用，且编码方案源自以白人、中产为主的临床试验人群。作者基于健康公平实施框架提出考量，并介绍标准化病人、片段编码和AI自动评分等探索，但未报告算法公平性的实证评估。

纳入判断：该文属评论/展望，讨论的是保真度测量工具本身的公平性考量与实施科学问题，并未评估某一AI/ML算法的公平性；摘要缺乏算法被评估、子组实证测量等证据，属公平性偶提及的评论，按规则排除。

限制：仅获取摘要，无全文；摘要未给出任何子组指标、评估设计或实证结果，AI自动评分仅作为“在研工作”被一笔带过，无法确认文中是否存在针对算法系统的公平性分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：many fidelity coding schemes originated from clinical trials testing relatively structured clinical protocols with primarily White, middle-class individuals
- groups：settings serving individuals with diverse identities and adverse social determinants of health
- medical：observational fidelity measurement and interpretation in mental health

[分析原文](https://europepmc.org/article/MED/42956225)

## p-a13199f8b00c3ef3f702

文章：[Systemic ethics framework for artificial intelligence in nursing and healthcare.](https://pubmed.ncbi.nlm.nih.gov/42989488/)

审核决定：待审核
审核备注：
证据版本：af89e5f4027501a88817a095abbcdbc4987f91ec3b8d30de8628a2b473fe7ad5

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文通过整合综述提出护理与医疗AI的系统性伦理框架，归纳规范基础、治理问责、信任透明、数据正义与公平、生命周期伦理等八个概念轴，并构建微观—中观—宏观多层次模型，强调问责安排、人类监督与制度支持。

纳入判断：属护理与医疗AI伦理框架综述，虽提及数据正义与公平，但缺少具体临床任务及实质性算法公平性分析（无亚组指标、偏差机制或评估框架），属泛化伦理建议与偶然提及，故排除；摘要级证据亦不足以支持纳入。

限制：仅摘要可见；未提供具体疾病或临床任务，也未报告算法公平性定义、亚组指标、偏差测量或缓解评估；数据正义与公平仅作为伦理轴被泛述。

建议分类：Not applicable

证据：
- algorithm：is increasingly integrated into nursing and healthcare practice
- evaluation：
- fairness：
- groups：
- medical：clinical decision support, documentation systems, triage tools, predictive monitoring

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42989488/)

## p-ad9e9680fe3ed43e22f2

文章：[Backbone-Informed Adaptation after EEG Pretraining: A Capacity-Controlled Study](https://arxiv.org/abs/2611.07192)

审核决定：待审核
审核备注：
证据版本：c23409cb6353993326a295fd3037a29604296ed601e62ba9bcfab45c0ff58e51

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：该研究在冻结的EEG基础模型（CBraMod、LaBraM）后比较两种下游适配器：遵循骨干通道/时间片段轴的“原生”注意力适配器与参数量匹配的逐token MLP对照。在情绪识别、睡眠分期与EEG事件分类六组配对实验中，原生适配器并无一致优势，结果依赖骨干、任务与下游训练协议。

纳入判断：论文属于EEG基础模型适配器的容量控制方法学比较，虽具备生物医学任务与算法实证评估，但“公平”仅指参数匹配，缺乏明确的分组/敏感属性、公平性度量或缓解问题，按规则不属医学算法公平性研究。

限制：全文未涉及任何受保护群体、公平性指标或差异分析；文中的“fair comparison”仅指可训练参数量匹配，并非算法公平性。仅两个骨干、三个种子，且部分设置（TUEV）受试者不独立、预训练重叠未明。

建议分类：Not applicable

证据：
- algorithm：we compare two designs that receive the same pretrained features
- evaluation：we evaluate the native adapter, capacity-matched token-wise control, and frozen-backbone probe across three seeds
- fairness：
- groups：
- medical：emotion recognition, sleep staging, and EEG event classification

[分析原文](https://arxiv.org/html/2611.07192v1)

## p-ee074914150093fabc5d

文章：[Acute Myocardial Injury in Patients Presenting With Upper Gastrointestinal Bleeding: Prevalence, Predictors, Troponin Dynamics, and In-Hospital Outcomes.](https://pubmed.ncbi.nlm.nih.gov/42997480/)

审核决定：待审核
审核备注：
证据版本：413391cf0c57e60db0a249b2ed64e43a817ad5b19ae238c32030aa8ffb154de8

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该多中心前瞻性队列研究评估上消化道出血患者24小时内急性心肌损伤的患病率、入院相关因素、肌钙蛋白动态及院内结局，采用高敏肌钙蛋白系列检测和24小时landmark分析，未涉及AI/ML算法或算法公平性。

纳入判断：研究聚焦UGIB合并急性心肌损伤的临床流行病学与预后，非AI/ML算法公平性研究；无算法评估、公平性定义、亚组公平性指标或缓解干预，故排除。

限制：全文为临床观察性研究，虽报告性别特异性肌钙蛋白阈值并将性别纳入回归，但未评估算法、亚组公平性差异、偏倚机制或缓解措施；不满足本综述的算法公平性证据要求。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Acute upper gastrointestinal bleeding (UGIB) is a common reason for emergency admission

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13741789/fullTextXML)

## p-0a7ab584ceef7f910746

文章：[Deep Learning-based Semantic Segmentation of Dental Radiographs: Comparative Evaluation of PSPNet, DeepLabv3, UNet, and UNet++](https://arxiv.org/abs/2610.15061)

审核决定：待审核
审核备注：
证据版本：6860acae9ae115570cd2e57a6ff9523e5efe53553904b61b20dca270a91de4a7

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文在统一受控实验设置下比较 PSPNet、DeepLabv3、UNet 与 UNet++ 四种语义分割模型在 1269 张牙科X线片上的表现，考察图像尺寸与批大小的影响，并以 Dice、IoU、准确率、精确率及损失进行评价，UNet++ 取得最高 IoU 与 Dice。

纳入判断：摘要显示该研究是牙科影像分割模型的性能对比，'fair'仅为实验条件控制之意；未定义受保护群体、未做亚组或差异测量，缺乏算法公平性问题与相应实证评估，属于偶然提及而非公平性研究。

限制：仅有摘要，无全文方法、代码或数据可得性信息；文中“fair”指公平受控的实验比较，未涉及任何人群、敏感属性或算法公平性分析，也未报告亚组指标。

建议分类：Not applicable

证据：
- algorithm：we mainly compared four segmentation models
- evaluation：
- fairness：
- groups：
- medical：dental radiographs segmentation plays a critical role

[分析原文](https://arxiv.org/abs/2610.15061)

## p-1423f020303a662753a5

文章：[Direct Effects Multiplicative Inference (DEMI): causal prediction from pairwise clinical relationships, applied to antidepressant response.](https://europepmc.org/article/MED/42892463)

审核决定：待审核
审核备注：
证据版本：274fe1d88c6111a03614622ad8a3fbaefd67ff7a960843ce9b279691deac430f

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：DEMI从All of Us提取4.3亿医学概念对关系，按时间顺序分解直接与间接效应并乘法聚合预测抗抑郁药应答；15种药物平均AUC 0.934，与逻辑回归0.935无显著差异。未评估公平性。

纳入判断：摘要仅报告DEMI与逻辑回归的AUC比较，未涉及算法公平性、差异、编码或缓解问题，也未定义受保护亚组；不满足公平性核心标准。

限制：仅摘要层面证据；缺少全文、代码或数据链接及任何按人群分组的公平性结果；不能据此推断完整论文没有相关分析。

建议分类：Not applicable

证据：
- algorithm：introduces Direct Effects Multiplicative Inference (DEMI), a causal algorithm
- evaluation：Performance was assessed using Area under the Receiver Operating Characteristic curve (AUC).
- fairness：
- groups：
- medical：predicts clinical outcomes from direct, unmediated effects

[分析原文](https://europepmc.org/article/MED/42892463)

## p-18c55d52c86dda3044c3

文章：[Connecting risk prediction to intervention: evidence from a randomized trial testing patient navigation and education to improve postpartum outcomes.](https://pubmed.ncbi.nlm.nih.gov/42705386/)

审核决定：待审核
审核备注：
证据版本：1f26691594885b1a05ae72d9eb9e330c523771ec22ca61d5805f727aa7e2e6ed

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该试点随机对照试验利用既往验证的产后医院使用风险计算器筛选高风险黑人个体，评估产后教育与患者导航干预的可行性和30天医院使用率；未评估算法公平性或偏倚。

纳入判断：研究使用风险计算器招募高风险黑人个体并评估导航干预，但核心问题是可行性与临床效果，未提出或测量算法公平性问题；属偶然提及公平/公平照护，不符合纳入标准。

限制：仅有摘要；研究聚焦干预可行性与临床结局，未报告算法公平性指标、亚组比较或偏倚分析，无法支持公平性评估。

建议分类：Not applicable

证据：
- algorithm：using a validated PHU risk calculator to identify and enroll high-risk participants
- evaluation：
- fairness：
- groups：among Black individuals who gave birth at a Philadelphia academic medical center
- medical：The primary outcome was hospital use within 30 days of discharge

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42705386/)

## p-1cf7f8e7a97808d0cb3c

文章：[Anatomic Classifications and Functional Outcomes in Preaxial Polydactyly of the Hand.](https://pubmed.ncbi.nlm.nih.gov/42598942/)

审核决定：待审核
审核备注：
证据版本：0157e138bda1d9d846319a1822d93f93927180857ee7c68c5ae7f6e363feb8a9

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究回顾性分析58例（59指）术前轴前多指的术后结局，比较Wassel-Flatt与JK解剖分类系统与JSSH、Rotterdam评分及再手术等结局的关联，并评估临时经关节K针固定的影响。全文为临床外科结局研究，未涉及人工智能或算法公平性。

纳入判断：摘要聚焦多指畸形的解剖分类与手术结局比较，属于传统临床回顾性研究，未评估任何AI/ML算法，也未涉及算法公平性、偏倚或亚组差异度量，因此不符合纳入标准。

限制：仅提供摘要，无全文、无代码或数据链接；研究本身不含AI/ML模型、亚组公平性指标或算法偏倚分析，也无任何算法公平性相关讨论。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Preaxial polydactyly is a common congenital hand anomaly with substantial anatomic variability.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42598942/)

## p-1f518fcb9c579e3639fe

文章：[Age, tumor size, and therapy timing are associated with survival in primary spinal Ewing sarcoma: a nationwide analysis.](https://europepmc.org/article/MED/42928284)

审核决定：待审核
审核备注：
证据版本：58a336a48f4548b0ec6f44b94b35aa7364dbd7581e34f894757bf47a303c921d

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究利用国家癌症数据库分析原发性脊柱尤文肉瘤中年龄、肿瘤大小与治疗时机对生存的影响，训练五种机器学习生存模型，并用Extra Survival Trees和SHAP分析预后因素。

纳入判断：摘要显示为脊柱尤文肉瘤预后与治疗时机研究，虽使用机器学习，但未涉及算法公平性、差异或缓解问题；年龄分组用于预后而非公平性评估，故排除。

限制：仅有摘要；未提出算法公平性问题，未定义公平性保护属性，也未开展亚组公平性评估、偏倚机制或缓解分析；年龄及儿童/成人分组仅用于预后比较。

建议分类：Evaluation

证据：
- algorithm：Of the five machine-learning survival models that were trained
- evaluation：Receiver operating characteristic analyses identified prognostic thresholds for age, tumor size, and initiation of chemotherapy.
- fairness：
- groups：Among 413 patients (204 pediatric, 219 adult; mean age 24 years)
- medical：Primary spinal Ewing sarcoma (EwS) is a rare, aggressive small round cell tumor.

[分析原文](https://europepmc.org/article/MED/42928284)

## p-21164ed1e0ca1f42a460

文章：[Knowledge, attitudes, and practices toward artificial intelligence in pharmacy education and practice among pharmacy students and faculty in Bangladesh: a cross-sectional study.](https://europepmc.org/article/MED/42960167)

审核决定：待审核
审核备注：
证据版本：2bde2666659290161d8a3c4e1b686590843b0bdcdd339686f2751b33b4f1d659

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文是孟加拉国药学学生与教师的横断面知识-态度-实践调查，比较其对AI的认知、态度与实践准备，未评估任何医疗算法或算法公平性。

纳入判断：研究问题是AI知识态度实践与教育政策，非医学算法公平性；未评估算法、定义公平性群体或实施公平性测量，故排除。

限制：全文为问卷调查，仅描述性别等人口学差异和AI伦理担忧；无具体医疗算法、公平性指标、偏倚机制或缓解评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13718494/fullTextXML)

## p-28fd16540d52d28aa2c6

文章：[Digital twin control framework uncovers individualized cross-scale links between functional connectivity deviations, communication impairment, and molecular mechanisms in autism.](https://pubmed.ncbi.nlm.nih.gov/42918437/)

审核决定：待审核
审核备注：
证据版本：219bc66363362365bab27970ca71a04a96297a7a3153257c5a02f81b2832dc29

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究提出基于深度对比学习的数字孪生对照框架，量化自闭症个体的功能连接偏差，并将其与ADOS沟通评分及转录组、神经递质、线粒体等跨尺度机制关联。

纳入判断：研究聚焦自闭症个体化神经机制，虽使用AI并做实证关联，但未提出算法公平性问题、敏感群体或公平性评估，不符合纳入标准。

限制：仅有摘要；未定义公平性敏感属性或亚组，未开展差异、编码、缓解或公平性指标评估；数字孪生对照用于疾病效应解耦，并非公平性反事实定义。

建议分类：Not applicable

证据：
- algorithm：We developed a digital twin control analytical framework based on deep contrastive learning.
- evaluation：multi-dimensional analyzes and validation including clinical correlation, transcriptomic decoding
- fairness：
- groups：
- medical：Autism spectrum disorder (ASD) is hallmarked by pronounced inter-individual heterogeneity in brain function and clinical manifestations.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42918437/)

## p-39951319b421108ba981

文章：[CFBrainAug: Modularity-Induced Counterfactual Brain Network Augmentation for Interpretable fMRI-based Autism Diagnosis](https://arxiv.org/abs/2610.32184)

审核决定：待审核
审核备注：
证据版本：0ca82c8e17b5657946236b3415a754c7dbc3d564be603f40217f709c79fb1e85

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：提出CFBrainAug，通过检索标签相反且拓扑相似的脑网络，并在模块数约束下进行反事实增强，联合训练RBF-SVM，实现可解释的fMRI自闭症诊断；在ABIDE I三个站点报告诊断性能与反事实解释。

纳入判断：该文是ASD诊断的反事实数据增强方法，虽列出年龄/性别并按站点评估，但未提出算法公平性问题，也未进行公平性差异或缓解效果的实证测量；属于偶提及混杂因素与类别不平衡，非医学算法公平性研究。

限制：全文聚焦诊断性能与反事实质量，未按年龄、性别或站点等属性开展公平性定义、亚组比较或偏倚测量；将敏感性偏低归因于NC多数类不平衡，属于类别不平衡而非公平性分析。

建议分类：Pre-processing

证据：
- algorithm：CFBrainAug, a counterfactual brain network learning framework
- evaluation：10 repetitions of stratified 5-fold cross-validation
- fairness：
- groups：
- medical：diagnosing Autism Spectrum Disorder (ASD)

[分析原文](https://arxiv.org/html/2610.32184v1)

## p-3d223ee6ca3da41000e6

文章：[Prediction of Systemic Lupus Erythematosus from Genotype and Gene-Expression Data: Batch Correction and Leakage-Free Evaluation](https://europepmc.org/article/PPR/PPR1349594)

审核决定：待审核
审核备注：
证据版本：95d9d8aae377f54a0af84ba006898f1393b065d09a6843b67b9ac805fb662398

模型建议：related

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究利用30个候选单核苷酸多态性与6个基因表达数据集预测系统性红斑狼疮。采用均值型批次校正，并在每个训练折内重新估计预处理与建模以避免数据泄漏，按个体划分折；以ROC-AUC、PR-AUC和MCC及标签置换检验评估。表达模型AUC达0.837至0.915，但仅用研究标签即可达0.857，显示批次与疾病标签强混杂，留出整项研究时性能明显下降。

纳入判断：摘要明确涉及疾病预测的机器学习建模与严格的无泄漏交叉验证，对医学算法评估方法学有参考价值；但全文未提出算法公平性、群体差异或编码偏倚问题，性别与年龄仅作为预测协变量，研究间批次混杂属站点泛化问题，不能单独构成公平性证据，故不满足纳入标准中的公平性与分组两项，不推荐纳入。

限制：仅提供摘要：未见以种族、性别、年龄或社会经济地位等受保护人群为分组的公平性指标、偏倚机制分析或缓解方法。年龄与性别仅作为单核苷酸多态性模型的协变量，批次与研究间差异属于泛化与混杂问题，摘要未将其构建为算法公平性问题，也无代码或数据可用性信息。

建议分类：Evaluation

证据：
- algorithm：leakage-free expression classifiers reached ROC-AUC 0.837 ± 0.033 (L1-penalised logistic regression)
- evaluation：summarised with ROC-AUC, precision–recall AUC (PR-AUC) and the Matthews correlation coefficient (MCC) over 10 × 5-fold cross-validation
- fairness：
- groups：
- medical：Systemic Lupus Erythematosus (SLE) is a complex autoimmune disease

[分析原文](https://europepmc.org/article/PPR/PPR1349594)

## p-408fcf2c00db10ff8789

文章：[It’s about time: Specifying time zero for target trial emulation in psychological research](https://europepmc.org/article/PPR/PPR1363496)

审核决定：待审核
审核备注：
证据版本：73d2069f637f45b63e44befe0175521af06377115c1489222265000860aedbdc

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：该文是面向心理学研究的目标试验模拟（TTE）教程，重点讨论"时间零点"这一常被忽视的基石概念。作者系统枚举时间零点各组成部分的排列组合，说明其错位会引入选择偏倚、治疗后混杂、治疗依赖的合格性变化与不死时间偏倚，并提出决策框架与实践建议，以工作场所AI使用与员工倦怠为例进行演示。

纳入判断：摘要内容为观察性研究因果推断设计（TTE与时间零点对齐）的通用方法学教程，非医学算法公平性研究：没有临床AI/ML算法被评估，没有受保护属性分组、差异度量或公平性定义，也未开展实证测量，不符合纳入的五项证据标准。

限制：仅有摘要，缺少全文与具体分析细节；文中AI使用仅为暴露示例，未涉及医学影像或临床预测算法，也未报告任何算法的公平性评估、亚组指标或缓解方法。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1363496)

## p-491376411d547c037f07

文章：[Causal Outcome Learning with Noisy Proxies](https://arxiv.org/abs/2611.10955)

审核决定：待审核
审核备注：
证据版本：65a356dbb0561f12b425bb6158d082aae83c13499e1b7607ab32aad652304184

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出SCOUT框架：利用高维噪声基线代理变量构建低维混杂调整得分，边学习对治疗有响应的复合结局边控制混杂，并在低维得分空间估计平均与条件平均治疗效应、构建条件随机化检验（含四阶统计量）检测效应异质性；在合成数据、基于CATIE的半合成数据及STEP-BD双相障碍锂盐不良反应观察性研究中验证。

纳入判断：该文为因果推断方法学工作：高维代理变量混杂调整、复合结局学习、ATE/CATE估计与异质性检验。虽属医学任务（双相障碍锂盐不良反应）且提出算法并做了经验评估，但通篇不存在算法公平性/差异/编码/缓解或公平性度量问题，也未定义受保护群体或亚组发现协议，属于超出公平性范围的方法学论文。

限制：全文未按任何受保护属性（种族、民族、性别、年龄、社会经济地位等）做亚组公平性度量或差异分析；治疗效应异质性被作为临床效应修饰处理，而非算法公平性问题；结论仅基于原文提供的模拟与单一观察性队列证据。

建议分类：Not applicable

证据：
- algorithm：We introduce such an algorithm called SCOUT
- evaluation：In synthetic and semi-synthetic experiments, the algorithm achieved competitive ATE estimation accuracy
- fairness：
- groups：
- medical：an observational study of patients with bipolar disorder

[分析原文](https://arxiv.org/html/2611.10955v1)

## p-4aa4395b22cef533ddeb

文章：[Adoption and perception of artificial intelligence by corresponding authors in orthopaedic research: A global cross-sectional study.](https://pubmed.ncbi.nlm.nih.gov/41825826/)

审核决定：待审核
审核备注：
证据版本：759a28c01b43de39b8f49348410deefca7a724b36283bb81b9ccb27986bcf69a

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该横断面调查评估骨科研究通讯作者对生成式AI的使用、态度、培训需求与披露实践，并按职业阶段和性别分析未来使用意愿。结果显示使用广泛但披露不足，男性性别与更积极的未来使用感知独立相关。

纳入判断：主题为骨科研究者对生成式AI的认知与披露调查；虽提及AI偏见担忧及性别差异，但非医学算法公平性研究，缺少临床任务、算法系统、公平性测量或缓解评估，故排除。

限制：仅有摘要；研究对象为作者态度与出版实践，未评估具体医学算法、临床任务或公平性指标，不能支持算法公平性纳入。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/41825826/)

## p-4af28d0a37e706d529ca

文章：[Association between Alzheimer's disease and related dementias and postoperative outcomes after geriatric hip fracture surgery.](https://europepmc.org/article/MED/43013143)

审核决定：待审核
审核备注：
证据版本：b791dcf810ad5e3108a1ab332d418dbf93c1b4250dce0e5a16a51bc85f4be5b2

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：回顾性队列研究，纳入3312例65岁以上髋部骨折手术患者，按电子病历记录的ADRD状态分组，用多因素回归分析ADRD与术后并发症、ICU入住、再入院及1年死亡率的关系，发现ADRD独立关联更差结局。

纳入判断：该文评估痴呆与髋部骨折术后结局的临床关联，属传统观察性研究，既无被评估的AI/ML算法，也无算法公平性/偏倚/缓解问题，不满足algorithm与fairness两项核心准入条件。

限制：仅摘要可及；研究为临床流行病学关联分析，未涉及任何AI/ML算法、模型编码或算法公平性评估；ADRD为临床暴露变量而非受保护的公平性属性，也未开展亚组公平性度量。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：Patients were stratified by ADRD status as documented in the electronic medical record.
- medical：geriatric hip fracture patients

[分析原文](https://europepmc.org/article/MED/43013143)

## p-4f82f9f44262ebd27f40

文章：[International Consensus on Artificial Intelligence in Undergraduate Dental Student Assessment: A Two-Round Modified Delphi and Live Consensus Study](https://europepmc.org/article/PPR/PPR1359981)

审核决定：待审核
审核备注：
证据版本：50cc2ef0b42cb89a17bd668f99aac4d3aaa6573f87e45b637588bbab81ddc3ea

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究通过两轮改良德尔菲法及现场共识投票，形成本科牙科学生评估中使用生成式人工智能的国际共识原则与评估形式分类建议，强调治理、披露、问责、数据保护与AI素养，但未评估任何具体算法。

纳入判断：该文为牙科教育评估中AI使用治理的德尔菲共识，缺乏被评估的医学AI/算法、明确的算法公平性研究问题、受保护群体定义及实证公平性评估；公平性仅为附带提及，属incidental mention，故排除。

限制：仅有摘要；属于牙科教育评估的治理共识，非临床或影像算法研究。公平性仅以“equity”一词在意见归纳中附带提及，未定义受保护群体、未报告亚组指标或偏差测量。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1359981)

## p-58c16252ff091a586ebd

文章：[It’s about time: Specifying time zero for target trial emulation in psychological research](https://europepmc.org/article/PPR/PPR1363497)

审核决定：待审核
审核备注：
证据版本：eaaefede4bc73808c0cd7f211bf3528d5d745de359938e303290ab7263f312fa

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：摘要介绍目标试验模拟（TTE）及“时间零点”在心理学观察性因果研究中的设计作用，讨论时间零点错位导致的偏倚并提出决策框架，以工作场所AI使用与员工倦怠为例。未涉及医学算法公平性、受保护群体或实证公平评估。

纳入判断：摘要聚焦心理学观察性研究的TTE时间零点与因果偏倚，虽提及工作场所AI，但未评估医学算法，也无公平性、群体或实证公平测量，故排除。

限制：仅依据摘要；文章为因果推断教程，未提供医学算法、公平性指标、群体比较或实证测量，无法作为医学算法公平性研究纳入。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1363497)

## p-6d4f29709a1042155a9c

文章：[Challenges and Opportunities for Strong and Dynamic Foundations in the Australian Cancer Plan.](https://europepmc.org/article/MED/43008400)

审核决定：待审核
审核备注：
证据版本：93576dc120a9de2edda4ae98dcd1b782a98dcc8bdad409926dec8730bf55eaed

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：本文为《澳大利亚癌症计划》战略目标4的视角/评论文章，讨论国家癌症数据框架、精准组学、临床试验可及性、数字健康与人工智能治理、患者报告结局等基础设施议题，主张将公平设为默认可测量结果，并特别关注原住民与托雷斯海峡岛民的数据主权及农村偏远地区可及性。

纳入判断：属于视角/评论类文章，虽提及癌症数据基础设施与原住民健康公平，但未针对具体医学任务开展算法公平性分析，缺少被评估的AI/ML算法及任何实施的公平性测量或缓解评估，符合“偶然提及公平”的排除条件。

限制：全文为政策视角与优先事项建议，未评估任何具体AI/ML算法，无算法公平性指标、亚组性能测量或缓解方法比较，也无实证数据；仅泛泛提及公平、数据治理与AI治理。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：particularly pronounced for Aboriginal and Torres Strait Islander peoples
- medical：improve cancer outcomes and experiences for all Australians affected by cancer

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13750873/fullTextXML)

## p-6e502862f36dba96cf40

文章：[Medical leadership between motivation and organisational support: findings from a contemporary survey.](https://pubmed.ncbi.nlm.nih.gov/42814092/)

审核决定：待审核
审核备注：
证据版本：d0e233d378c6448978bdf1c06b0ca4de7dd05a2241084080121b2af9e8792e74

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文报告一项国际横断面问卷调查，分析临床与非临床医疗领导者在领导动机、组织支持（受保护时间、决策支持、共享治理）方面的差距，并将累积支持缺失与感知领导影响力和压力/倦怠关联，提出“动机—支持缺口”框架。

纳入判断：主题为医疗领导力与组织支持调查，非医学算法公平性研究。文中未评估AI/ML算法，无明确公平性/差异问题、受保护群体定义或亚组公平性测量；仅有泛化的公平与AI决策支持背景提及，不满足纳入标准。

限制：仅有摘要；为自愿参与、滚雪球抽样的横断面自报调查（143人，76%来自意大利），无客观治理或绩效指标。未评估任何AI/ML算法，也未开展算法公平性测量；公平与AI仅作为背景性表述出现。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42814092/)

## p-71348eabce0902da8421

文章：[Formation of calcium oxalate kidney stones is related to consumption of some ultra-processed foods: a case-control study.](https://pubmed.ncbi.nlm.nih.gov/42470774/)

审核决定：待审核
审核备注：
证据版本：d6ccdf1f7b4ed5e7c662e6196002584071e8486d9e0143df20735f5c5f873468

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究为德黑兰开展的病例对照研究（366人），用147项食物频率问卷和NOVA分类评估超加工食品摄入与草酸钙肾结石的关联，采用多因素logistic回归。结果显示甜食类摄入与结石风险升高相关，乳制品摄入与风险降低相关，但总超加工食品摄入无显著关联。

纳入判断：本文是膳食因素与肾结石的流行病学病例对照研究，使用传统统计回归，不涉及人工智能/机器学习算法，也无算法公平性、偏倚机制或亚组性能评估问题，不符合纳入标准。

限制：仅有摘要，缺少完整方法、食物分类细节与偏倚控制信息；作者自述存在回忆偏倚，且结果为关联性而非因果。全文未涉及任何算法、模型或公平性分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：investigate the relationship between UPFs and calcium oxalate kidney stones

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42470774/)

## p-743354216635218b0792

文章：[SGLT2 Inhibitors and Risk of Postmenopausal Bleeding in Women: An Active-Comparator, New-User Cohort Study.](https://europepmc.org/article/MED/42957436)

审核决定：待审核
审核备注：
证据版本：f24cf76f154186ab71537f060eaf61df649889c18442d1b5def2fd8d85966518

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究为药物流行病学队列分析，利用 All of Us 数据比较 55-90 岁女性新使用 SGLT2 抑制剂与 DPP-4 抑制剂后绝经后出血风险，采用倾向评分匹配与 Cox/Poisson 模型；结果显示风险无显著升高（HR 1.14，95%CI 0.70-1.84）。

纳入判断：该文是药物不良事件的安全性队列研究，虽按女性人群分析，但未评估任何 AI/ML 算法，也无算法公平性、亚组差异或缓解措施问题，属于非算法公平性文献，故排除。

限制：仅有摘要，无全文；研究对象为药物安全性而非算法；未涉及任何 AI/ML 模型、公平性指标、受保护亚组比较或偏倚机制分析，无法提供算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42957436)

## p-83d7d92e5dd95ce57ac9

文章：[Quality of Life in Patients with Treatment-Resistant Depression Treated with Intranasal Esketamine as Add-On Therapy to an SSRI-A Prospective, Comparative Study in Real-World Clinical Practice.](https://europepmc.org/article/MED/42943341)

审核决定：待审核
审核备注：
证据版本：29006b37f56dfb9149d7efeb9ae1f8c1751fb919a468a851abdf23baa1fc18ff

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：本研究为真实世界前瞻性观察研究，比较鼻内艾司氯胺酮联合SSRI与单用SSRI治疗难治性抑郁12个月的生活质量（WHOQOL-BREF、SF-36）及抑郁症状变化；未涉及人工智能/机器学习、算法公平性、亚组差异或缓解措施。

纳入判断：研究评估艾司氯胺酮治疗难治性抑郁的生活质量，未评估AI/ML算法，也未提出算法公平性、偏倚或缓解问题；五项纳入标准均不满足。

限制：全文为临床疗效与患者报告结局研究，无算法、无公平性评价设计、无定义群体/属性或公平性指标。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13708465/fullTextXML)

## p-93eec9d9c2a10cfd796d

文章：[Learning Features, Not Layouts: Feature-Axis Attention as a Transfer Prior for Medical Imaging](https://arxiv.org/abs/2610.13012)

审核决定：待审核
审核备注：
证据版本：7f04d0cd4ff029ab98332dbdc6c73373f401ec4225fa5cfbe2dd4fa6f394d3a3

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：提出 FAD-ViT，严格解耦空间轴与特征轴，以通道注意力作为主要全局混合算子，并在23个医学分类、分割和低数据任务上评估其迁移优势；属于医学影像架构与迁移学习研究，不涉及算法公平性。

纳入判断：研究问题是特征轴注意力是否改善医学影像迁移，而非算法公平性；无公平性、差异、编码或缓解问题，也无群体属性或公平性测量，不符合纳入标准。

限制：全文未定义受保护人群或公平性指标，也未检验亚组差异、偏见机制或缓解方法；仅报告总体迁移性能与架构消融。

建议分类：Not applicable

证据：
- algorithm：We design FAD-ViT, a backbone that strictly decouples the two axes
- evaluation：we find that shifting global attention from the spatial to the feature axis leaves from-scratch performance essentially unchanged, yet markedly strengthens transfer.
- fairness：
- groups：
- medical：Evaluating comprehensively across 23 classification, segmentation, and low-data tasks

[分析原文](https://arxiv.org/html/2610.13012v1)

## p-9a70a25f501793aaea6a

文章：[ContextLift: Breaking the Spurious Correlation Behind Conditional Emergent Misalignment](https://arxiv.org/abs/2610.21633)

审核决定：待审核
审核备注：
证据版本：98572c6a8caeb2dbcb9ec725f5b6663f4e109777fedcd885396833510f42efc5

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：提出 ContextLift：将微调提示中的情境句移植到通用安全样本，打破条件性涌现错位中的虚假相关；在安全、法律、医疗不良建议微调及良性任务上验证，未涉及临床算法公平性分组评估。

纳入判断：文章提出并实证评估 ContextLift 以缓解 LLM 微调后的条件性涌现错位；虽含医疗不良建议数据，但核心是安全对齐与虚假相关，未定义受保护群体、未做公平性指标或亚组差异分析，故不属医学算法公平性研究。

限制：全文为语言模型安全与错位缓解实验；医疗仅作为有害建议领域之一，未提供临床任务或疾病特异的公平性分析；无敏感属性分组、差异指标或缓解后公平性评估。

建议分类：Pre-processing

证据：
- algorithm：We finetune Qwen2.5-7B-Instruct with QLoRA
- evaluation：ContextLift reduces this to 2.6%, 6.1% and 12.8% at the same data and compute budget
- fairness：
- groups：
- medical：

[分析原文](https://arxiv.org/html/2610.21633v1)

## p-a11377379ca4050b6b0d

文章：[Treatment intensity and survival benefit among older adults with glioblastoma: A population-based analysis.](https://pubmed.ncbi.nlm.nih.gov/42710195/)

审核决定：待审核
审核备注：
证据版本：f6f0369b14b52f4b0b5b104f837ee91a0dc1eb9c817100772e9574126d5a9035

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究基于SEER数据库（2000-2020）回顾性分析21,206例≥65岁胶质母细胞瘤患者，描述手术、放疗与化疗联合治疗强度的年龄趋势，并用中位生存期和24个月限制平均生存时间（ΔRMST0-24）评估各年龄层的绝对生存获益，发现高龄与接受三联治疗概率降低相关，但强化治疗在各年龄层均与更长生存相关。

纳入判断：该文为基于登记数据库的流行病学队列研究，评估年龄与治疗强度及生存关系，未涉及任何AI/ML算法被评估，也无算法公平性、偏倚编码或缓解问题；年龄分层不构成算法公平性研究，故排除。

限制：仅有摘要，无AI/ML模型、无算法公平性指标或缓解方法；年龄分层属临床预后分析，且作者自述存在未测量混杂与永生时间偏倚。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Overall survival (OS) was evaluated using median OS and restricted mean survival time over 24 months
- fairness：
- groups：stratified by age group
- medical：Older adults with glioblastoma (GBM) are frequently treated with de-escalated approaches.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42710195/)

## p-a892e63505daaea0043b

文章：[A Tool for Anonymized Clinical Knowledge Retrieval and Speaker Interaction Analysis of Healthcare Tele-mentoring Sessions](https://arxiv.org/abs/2611.10922)

审核决定：待审核
审核备注：
证据版本：2cac5a8b5b141d04f529ca240451aea19d682817b70b0c2b7d12aec53b82dba7

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：提出 ECHO-TD 本地化仪表盘，用说话人/会话过滤的 RAG 与 MedGemma-4B 检索临床知识，并通过交互图分析发言参与度、中心性和匿名化输出。

纳入判断：该文属临床 NLP/远程教学工具，虽测量发言参与公平性，但未评估算法的群体公平性、差异或缓解，也无受保护属性/亚组公平指标，故不属医学算法公平研究。

限制：全文为系统演示，未报告模型公平性分组指标、受保护属性或缓解实验；所谓参与公平性仅指发言互动。

建议分类：Not applicable

证据：
- algorithm：MedGemma-4B as a locally-hosted language model
- evaluation：
- fairness：
- groups：
- medical：anonymized retrieval of clinical knowledge and analysis of multi-speaker interactions

[分析原文](https://arxiv.org/html/2611.10922v1)

## p-aa065ed711d05a970047

文章：[Evaluation of chromosome-level structural variation for acute myocardial infarction risk prediction](https://europepmc.org/article/PPR/PPR1362124)

审核决定：待审核
审核备注：
证据版本：39617afde775cfed49b7e6eb956eece7d7ad5ca7c80505e5ff9d42e67b7aa90a

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究利用 All of Us 队列中对性别、自报种族和年龄做 1:1 匹配的 3290 例样本，将染色体级别结构变异（全基因组 128 个片段的 LRR 分布统计矩）输入随机森林，进行急性心肌梗死风险预测。10 折交叉验证平均 AUC 仅 0.529，与打乱标签对照（0.491）及随机水平无法区分，结论为宏观结构变异不能解释 AMI 的缺失遗传力。

纳入判断：该文虽为医学（AMI 预测）算法评估，但对性别、种族、年龄做 1:1 匹配仅为消除人口学混杂，用于验证预测信号是否为零，未提出任何公平性、差异测量、群体编码或缓解问题，也无亚组公平性指标。属人口学变量参与的一般预测性能评估，不满足公平性标准。

限制：仅有摘要，未提供完整方法、代码与数据获取信息；未报告任何亚组性能、差异或公平性指标。人口学匹配仅作为混杂控制手段，未构成算法公平性评估。

建议分类：Not applicable

证据：
- algorithm：We evaluated Random Forest models across 10 independent stratified cross-validation splits
- evaluation：The CLSV model achieved a 10-split mean held-out test ROC AUC of
- fairness：
- groups：1:1 matching between cases and controls on sex at birth, self-reported race, and age
- medical：We evaluated whether chromosome-level structural variation (CLSV) provides a predictive signal for AMI

[分析原文](https://europepmc.org/article/PPR/PPR1362124)

## p-b1770139d184f1002ae3

文章：[Efficacy and Safety of Stent-Assisted Coiling Versus Coiling Alone for Ruptured Multilobed Aneurysms: A Multicenter Study.](https://pubmed.ncbi.nlm.nih.gov/42974369/)

审核决定：待审核
审核备注：
证据版本：b6897c1ab760ad9dde6cb86c996bda6d3a8305bf9e9390baada6b03b834eeb5b

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：多中心前瞻性队列比较支架辅助栓塞与单纯栓塞治疗破裂多叶颅内动脉瘤的安全性和疗效，采用重叠权重及双稳健回归分析。研究未涉及AI/ML算法评估或算法公平性问题。

纳入判断：该文评估两种血管内治疗方式的安全性与疗效，不涉及AI/ML算法，也未提出或测量算法公平性问题，不符合纳入标准。

限制：仅有摘要；为观察性临床比较效果研究，未报告算法、敏感属性、亚组公平性或公平性指标分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Overlap weighting (average treatment effect in the overlap population) and doubly robust logistic regression models were applied
- fairness：
- groups：
- medical：627 consecutive patients with ruptured multilobed intracranial aneurysm treated with SAC or coiling alone were included.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42974369/)

## p-b1f1c2e8dcbc74c8d6c7

文章：[Analisi dell’appropriatezza prescrittiva ed evoluzione digitale: integrazione tra ricetta dematerializzata, intelligenza artificiale e manuale Rao.](https://europepmc.org/article/MED/42979883)

审核决定：待审核
审核备注：
证据版本：0d854085847783323b837d29d6649ca4bd78c8a8faff8bb5ee78227a0457d9fa

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该摘要介绍意大利马尔凯大区利用 NotebookLM 分析 36,465 份去物质化处方与 RAO 优先标准的符合性，发现 30% 处方不一致且异常集中于少数开方者，属于处方适当性数字审计，并非医疗算法公平性研究。

纳入判断：摘要描述的是处方适当性审计，公平仅以“ensuring healthcare equity” incidental 提及；缺乏明确的算法公平/差异问题、群体定义及公平性测量，且摘要证据不足以建议纳入。

限制：仅有摘要；未提供算法公平性定义、受保护群体、亚组指标或公平性评估结果。文中“healthcare equity”仅为泛泛政策表述，不能作为算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：Using NotebookLM, an AI-based methodology was developed
- evaluation：analyze 36,465 dematerialized prescriptions from 2025
- fairness：
- groups：
- medical：three critical clinical areas (ophthalmology, breast diagnostics, and electromyography)

[分析原文](https://europepmc.org/article/MED/42979883)

## p-be1ec4309a4ce2fb4aa3

文章：[Oxidation over omega-3: Reinterpreting the paradoxical link between fish oil supplements and accelerated cognitive decline.](https://pubmed.ncbi.nlm.nih.gov/42612547/)

审核决定：待审核
审核备注：
证据版本：3196ba6a0d6959255b00ab2cf04754f7503eeab115957a147cd2b126cfaa49d4

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为致编辑信，评论一项观察性研究：鱼油补充与认知加速下降相关，并由FDG-PET低代谢介导。作者指出四点方法学局限（暴露错分、残余混杂、机制过度推断、情境依赖），并建议血清EPA+DHA剂量建模、负对照敏感性分析、部分容积校正FDG中介分析等改进。全文未涉及任何AI/ML算法或算法公平性评估。

纳入判断：该信评论的是鱼油补充与认知下降的观察性关联及其错分、混杂等统计方法学问题，未评估任何AI/ML算法，也未提出算法公平性、子群差异、编码偏差或缓解措施问题；算法、公平性、分组与实证测量四项标准均不满足，故排除。

限制：仅有信件摘要级文本；属营养流行病学方法学批评，未涉及算法模型、亚组公平性指标、偏差机制测量或任何实证性公平性评估，也未定义受保护属性或分组比较。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：association between omega-3 supplementation and accelerated cognitive decline, mediated by FDG-PET hypometabolism

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42612547/)

## p-c481c3634d23e0326c99

文章：[MRCP-derived radiomics features associated with biliary dilation: a multi-step feature reduction, multivariable regression, and diagnostic classification study.](https://pubmed.ncbi.nlm.nih.gov/42138743/)

审核决定：待审核
审核备注：
证据版本：51db7af9fa128cb22ff815c5ae3d1862fd82b46db788960734d2f674b2c06b5b

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究基于MRCP影像提取三维CBD radiomics特征，经ICC可重复性、低方差、相关性、FDR与Cliff's delta多步降维，纳入年龄、性别和胆囊切除状态的多变量回归，并用随机森林等三种分类器做胆管扩张诊断分类，另在6-10 mm临界管径亚组做探索性分析。

纳入判断：摘要显示为胆管扩张的radiomics诊断分类研究，仅把年龄、性别、胆囊切除史作为混杂变量调整，未提出任何算法公平性/差异/编码或缓解问题，也未按敏感属性报告亚组指标，属公平性偶提之外的无关工作。

限制：仅有摘要，无全文、代码或外部验证细节。文中仅将年龄、性别作为回归混杂因素校正，未定义公平性群体、未报告亚组性能差异、偏倚机制或缓解方法。

建议分类：Not applicable

证据：
- algorithm：Three classifiers (Random Forest, Logistic Regression, and Naïve Bayes) were trained on the seven Bonferroni-confirmed texture features
- evaluation：
- fairness：
- groups：
- medical：identify MRCP-derived radiomics features associated with image-defined biliary dilation

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42138743/)

## p-c52d73c3e19f9160643a

文章：[Comparing Lightweight Models for Physician-Consensus Pharyngitis Classification from Primary-Care Smartphone Images.](https://europepmc.org/article/MED/43028421)

审核决定：待审核
审核备注：
证据版本：5adea896420496252f06237552625faea08e5d7824ba8c44aaabcf2222faa898

模型建议：related

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究在PGUPharyngitis智能手机咽部图像数据集上比较五种轻量级模型（四种CNN与MobileViT-XS）预测医师共识的细菌性/非细菌性咽炎标签，用五折患者级交叉验证评估PR-AUC与AUROC并考察计算效率。结果显示模型区分度中等，且采集设备与标签相关，设备混杂无法排除。

纳入判断：属于医学影像（临床摄影）算法评估，报告了采集设备与标签的分布差异（9.2% vs 26.9%）及设备单变量基线，提示设备混杂这一偏倚机制；但全文未提出算法公平性问题，也未做亚组公平性度量。且证据仅限摘要，不能建议纳入。

限制：仅有摘要：未提供全文、代码或数据链接；无任何按设备（如三星/小米）分层的模型性能或公平性指标，也未报告校准、阈值公平性或缓解措施，因此无法确认真实公平性分析。

建议分类：Evaluation

证据：
- algorithm：Five ImageNet-pretrained lightweight classifiers
- evaluation：Mean PR-AUC across folds ranged from 0.317 to 0.372 and AUROC from 0.663 to 0.708
- fairness：
- groups：Bacterial-label prevalence differed by acquisition device (Samsung 9.2% versus Xiaomi 26.9%)
- medical：predicting physician-consensus bacterial versus nonbacterial labels from smartphone throat images

[分析原文](https://europepmc.org/article/MED/43028421)

## p-d5df31f2d791fe9c70ba

文章：[EXPRESS: Brain Age Gap from Non-Contrast CT Is Independently Associated with Functional Outcome after Acute Ischemic Stroke.](https://europepmc.org/article/MED/43015642)

审核决定：待审核
审核备注：
证据版本：bb4ab3bea8a84c0183ab6e0d351d6bc6a3ff690aa325fd8eae815a8aacb5376d

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究基于1,173例急性缺血性卒中患者的前瞻性多中心队列，用深度学习从对侧非增强CT估计脑年龄，定义BrainAGE（预测年龄减实际年龄），并分析其与90天功能结局的关联。结果显示BrainAGE较高与更差功能结局独立相关，但判别力提升有限。

纳入判断：属预后生物标志物关联研究：虽使用深度学习与CT影像，但全文未提出算法公平性/差异/编码/缓解或公平性度量问题，仅将性别作为调整协变量，不满足fairness与groups证据要求，且为摘要级证据，故排除。

限制：仅有摘要，缺少模型结构、训练验证细节与代码数据信息；未涉及任何算法公平性、亚组差异或偏倚评估，性别仅作为回归协变量。

建议分类：Not applicable

证据：
- algorithm：A deep learning model estimated brain age from contralesional baseline NCCT to minimize lesion-related confounding
- evaluation：
- fairness：
- groups：
- medical：We evaluated whether brain age gap (BrainAGE) derived from routine non-contrast computed tomography (NCCT) is associated with functional outcome after AIS

[分析原文](https://europepmc.org/article/MED/43015642)

## p-e6d3c6428f1e2c8de26d

文章：[Association of Cumulative Pharmacist Interventions and Interprofessional Adherence With Survival Among Patients Requiring Pharmacotherapeutic Optimization in a Pediatric Intensive Care Unit: A Retrospective Time-Dependent Cohort Study.](https://europepmc.org/article/MED/43000161)

审核决定：待审核
审核备注：
证据版本：1c96845bc041b85fffead51c36e3efa111e38ef39deae5a94a5f4021ec5a2271

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性队列研究纳入565例儿科重症监护病房（PICU）患者，采用含时变暴露的扩展Cox比例风险模型，评估累计药师干预数及跨专业团队依从性与PICU内生存的关系，并按PIM-2校正基线严重度，报告总体死亡率11.9%、干预接受率72.2%。

纳入判断：该文研究药师干预与PICU生存的流行病学关联，属临床药物管理与结局评价，既未评估AI/ML算法，也未涉及算法公平性、敏感属性分组或亚组公平性测量，不符合纳入标准中的算法公平性要求，故排除。

限制：仅有摘要证据；研究为观察性药物管理/结局关联分析，未涉及任何AI/ML模型，也未提出算法公平性、亚组差异或偏倚机制问题；无代码、数据或公平性评价细节。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：lower hazard of in-PICU mortality (hazard ratio [HR] = 0.989; p = 0.040)

[分析原文](https://europepmc.org/article/MED/43000161)

## p-ea3b2e02ee0a3aa3db56

文章：[Artificial intelligence, health literacy, and sex and gender specific medicine: navigating the new paradigm in the physician-patient relationship.](https://europepmc.org/article/MED/42979871)

审核决定：待审核
审核备注：
证据版本：5763787e29da76037f96ac0c7f2482c3668338465ad8e0dc8072438e9e3ab4d0

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为观点/评论性文章，讨论生成式AI、健康素养与性别特异医学对医患关系与临床实践的影响，泛泛指出训练数据偏倚会损害女性与少数群体的诊断适宜性，并呼吁公众提升数字健康素养、医生提升"算法素养"，未针对具体疾病或临床任务开展公平性分析或实证测量。

纳入判断：属评论/观点文章，虽提及训练数据偏倚与公平，但未指明具体医学疾病或任务，也无实质性的算法公平分析（亚组指标、机制、框架或缓解比较）与实证评估，属附带提及型文献，不符合纳入条件。

限制：仅摘要可用；未命名具体疾病或临床任务，未报告亚组指标、偏倚机制分析、评测框架或缓解方法比较，属泛泛的公平AI倡议与教育呼吁。

建议分类：Not verified

证据：
- algorithm：current models are trained on datasets heavily affected by bias
- evaluation：
- fairness：To safeguard equity, a focus on training is needed
- groups：for female patients and minorities
- medical：compromising diagnostic appropriateness for female patients and minorities

[分析原文](https://europepmc.org/article/MED/42979871)

## p-f2b6a21e012418a77837

文章：[Morphology-based selvester QRS score for phenotyping acute heart failure in patients with native left bundle branch block.](https://pubmed.ncbi.nlm.nih.gov/42721639/)

审核决定：待审核
审核备注：
证据版本：c5b2039af6802c399b26d7d26ffee59523668092f47e59e5b861e87abd915960

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该摘要评估Selvester QRS评分在伴原生左束支传导阻滞的急性心衰患者中区分HFrEF、HFmrEF、HFpEF和RHF的诊断表现，报告SQS与超声参数相关且对HFrEF区分中等。未涉及AI/算法公平性、敏感人群比较或缓解措施。

纳入判断：临床ECG评分诊断研究，虽评估算法性能，但未提出或测量算法公平性/差异，缺乏敏感属性分组与公平性评价，故不属于医学算法公平性范围。

限制：仅有摘要；单中心回顾性研究；无公平性指标、敏感属性分组、偏倚机制或缓解评估；无代码/数据可用性信息。

建议分类：Not applicable

证据：
- algorithm：SQS was calculated using the 57-point LBBB-adapted Strauss-Selvester algorithm.
- evaluation：Correlation, multivariable logistic regression, and ROC analyses were performed.
- fairness：
- groups：
- medical：Rapid differentiation of left ventricular (LV) systolic dysfunction from right heart failure (RHF) is essential in acute heart failure (AHF).

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42721639/)

## p-f497b8eb950e521f7701

文章：[Association of C-reactive protein to albumin ratio with progression of CKD and all-cause mortality in diabetic CKD.](https://pubmed.ncbi.nlm.nih.gov/42412363/)

审核决定：待审核
审核备注：
证据版本：a120c24724426b36dd0e55bd2f50b84ddf1329589d5a22e67a6c444ddbd7a94b

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究在231例糖尿病合并慢性肾脏病患者中评估C反应蛋白/白蛋白比值（CAR）与CKD进展及全因死亡的关联，采用Kaplan-Meier、Cox回归、限制性立方样条及SHAP机器学习分析，发现CAR为独立预后因子并可提升风险预测效能。

纳入判断：研究为CAR生物标志物的预后关联与预测增量分析，虽使用SHAP机器学习方法，但未提出算法公平性/差异/编码/缓解或公平性度量问题，亚组分析仅验证关联一致性而非公平性评估，故不属医学算法公平性研究。

限制：摘要层面证据，仅涉及单中心回顾性预后建模；按年龄、性别、BMI的亚组分析用于检验关联稳健性，未涉及任何算法公平性、组间差异或偏倚机制分析。

建议分类：Not verified

证据：
- algorithm：We used the SHAP machine learning algorithm to evaluate the predictive performance of CAR
- evaluation：
- fairness：
- groups：
- medical：retrospectively retrieved 231 CKD patients with diabetes

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42412363/)

## p-faa1ff8cf33578158f1a

文章：[Clinical and sociodemographic predictors of AI use for mental health among college students.](https://pubmed.ncbi.nlm.nih.gov/42217639/)

审核决定：待审核
审核备注：
证据版本：0aa62f386be2c4d37ac5e5cea45fb64d8fe6be42862bab821fb97bb41021d329

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：基于2024-2025年Healthy Minds Study两所美国高校675名学生的横截面数据，用层次logistic回归分析大学生将生成式AI用于心理健康支持的临床与社会人口学预测因素，发现重度抑郁、重度焦虑、自杀倾向及亚裔身份与更高使用几率相关，并提示边缘群体使用未受监管AI工具的比例偏高。

纳入判断：该研究把生成式AI使用当作被解释的行为结局，用回归描述使用者的人口学差异，并未评估任何医疗AI算法的公平性（无亚组性能指标、编码偏差或缓解方法）。虽有分组比较与实证测量，但缺少“被评估算法”与“算法公平性/偏倚问题”两项核心要件，属于AI使用行为的流行病学描述而非医疗算法公平性研究，故排除。

限制：仅有摘要，缺乏样本抽样细节、量表与建模协变量说明；横截面设计无法推断因果；仅两所院校，外部效度有限。全文未评估任何AI/ML算法本身，也未提出或实施算法公平性指标与缓解方法，缺乏可核验的代码或数据信息。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Hierarchical logistic regression examined predictors of AI use for mental health
- fairness：
- groups：higher proportions of non-binary/other gender and LGBQ+ students
- medical：predictors of AI use for mental health among college students at two U.S. institutions

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42217639/)

## p-ff7c424314366178daee

文章：[Association Between MIA3 and Coronary Collateral Circulation Formation in Patients with Chronic Total Occlusion](https://europepmc.org/article/PPR/PPR1354723)

审核决定：待审核
审核备注：
证据版本：d8b5f483ec54f6902df9da6ac4329014076a4e211a3193c3825857827743404d

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究纳入489例冠状动脉慢性完全闭塞（CTO）患者，检测血浆MIA3与VEGFA水平，按Rentrop分级分为侧支循环良好组与不良组，采用多因素logistic回归、ROC曲线及NRI/IDI评估MIA3对良好侧支形成的预测价值，并开展临床亚组与交互分析。

纳入判断：该文为CTO患者生物标志物MIA3与侧支循环形成的临床关联及预测效能研究，虽使用回归与ROC/NRI/IDI评估，但未提出算法公平性、偏倚机制或缓解措施问题，亚组分析针对血脂异常而非受保护属性，不满足公平性核心判据。

限制：仅有摘要，缺少样本构成、模型校准与外部验证细节；亚组分析基于血脂异常等临床特征，未涉及任何算法公平性、群体差异或偏倚测量，也无代码或数据可用性信息。

建议分类：Not applicable

证据：
- algorithm：Multivariate logistic regression analysis was used to identify independent factors correlated with good CCC formation.
- evaluation：Receiver operating characteristic (ROC) curves were plotted to evaluate the clinical value
- fairness：
- groups：
- medical：correlation between melanoma inhibitory activity 3 (MIA3) and coronary collateral circulation (CCC) formation

[分析原文](https://europepmc.org/article/PPR/PPR1354723)

## p-116d132a6a15a073e809

文章：[Catalysing system reforms in Pakistan’s Healthcare and Health Professions Education: National Stakeholder priorities for strengthening policy and system Governance](https://europepmc.org/article/PPR/PPR1368269)

审核决定：待审核
审核备注：
证据版本：84ff8430eda0fb41279f41216f1d3319fec2f701d9db0e7ade0ec0241592e1da

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究通过2026年巴基斯坦健康与教育峰会的混合焦点小组讨论，汇集14名利益相关者对医学与口腔教育质量、治理监管、认证及卫生人力留存的看法，提出从投入型转向产出型认证、建立跨机构治理平台等改革建议。文中仅简要提及谨慎、有目的地整合人工智能，未涉及任何算法公平性评估。

纳入判断：文章主题为巴基斯坦卫生专业教育与系统治理改革，属定性利益相关者研究；虽提及人工智能整合，但无算法被评估、无公平性/偏倚问题、无群体定义或实证测量，不符合纳入标准。

限制：仅有摘要；定性政策研究，未评估任何AI/ML算法，无亚组指标、公平性度量或缓解实验；人工智能仅作为教育整合议题被提及。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1368269)

## p-1de4b4c47fd32c7cf15f

文章：[Five-year risk of cardiovascular events in women with history of pregnancy complicated by fetal growth restriction.](https://europepmc.org/article/MED/43050674)

审核决定：待审核
审核备注：
证据版本：f626a011e49d2aea54c200d7e6d05a4922448e83c455d5545e48a0475654ffea

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性队列利用TriNetX数据评估胎儿生长受限与产后5年母亲心血管复合结局的关联，采用倾向评分匹配和Cox回归，未涉及AI/ML算法或算法公平性。

纳入判断：研究问题是FGR与心血管结局的流行病学关联，摘要未提及AI/ML模型、算法公平性/偏倚测量、受保护群体或公平性评估，不符合五项纳入标准。

限制：仅有摘要；为观察性流行病学关联研究，未评估任何算法、亚组公平性指标或缓解措施。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/43050674)

## p-61addd093647a7caaf49

文章：[Longitudinal AI-based home-cage monitoring of locomotor aging in C57BL/6J mice: An exploratory pilot study.](https://pubmed.ncbi.nlm.nih.gov/43052603/)

审核决定：待审核
审核备注：
证据版本：3ab27b41584aa25ea7f7ae32762c0aa97eba4efb671e300867581d128a9848ef

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该探索性先导研究利用AI家庭笼监测系统（DOME）对C57BL/6J小鼠连续行为记录长达9个月，筛选出四项跨队列一致性较高的运动学指标，并按性别归一化以处理雌雄二态性，进而构建候选的运动源性行为衰弱指数（bFI），并在27月龄小鼠中初步观察到其与临床衰弱指数（CFI）的正相关。

纳入判断：该研究属临床前动物行为表型研究，文中出现的队列特异性偏倚与性别二态性归一化属于批次效应与生理差异处理，未构成针对医学算法的公平性、差异性、编码或缓解问题的界定与测量，也无亚组公平性指标或缓解方法比较，属偶然提及，故排除。

限制：仅有摘要，缺少方法、统计与亚组分析细节；样本仅20只小鼠、4个笼具（4个独立实验单元），作者自述需更大规模重复队列验证；未报告任何算法公平性指标、亚组性能差异或缓解方法的定量评估。

建议分类：Not verified

证据：
- algorithm：Digital Online Monitoring Equipment (DOME) AI-powered HCMS
- evaluation：the bFI was positively associated with the Clinical Frailty Index (CFI)
- fairness：
- groups：females exhibited consistently higher locomotor performance than males
- medical：characterize longitudinal aging trajectories in two partially overlapping cohorts of C57BL/6J mice

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43052603/)

## p-9248ffc4421b28b6931d

文章：[Circulating miRNA profiling identifies hsa-miR-23a-3p and a three-miRNA signature associated with serous ovarian cancer](https://europepmc.org/article/PPR/PPR1373555)

审核决定：待审核
审核备注：
证据版本：65537aff5624e7dbfebb4d733fbe296065bf953a7993e63acca59823ecf956fb

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：研究比较卵巢癌患者与对照血浆中8种miRNA，发现hsa-miR-23a-3p及三-miRNA逻辑回归模型具中等区分度，并报告交叉验证后性能下降及样本来源/技术变异等混杂因素。

纳入判断：研究为卵巢癌循环miRNA生物标志物区分病例与对照，未提出或评估算法公平性、亚组差异、敏感属性或缓解措施，仅有ROC/AUC性能，不符合纳入标准。

限制：摘要仅报告病例对照生物标志物性能与内部验证，未涉及算法公平性、亚组差异、敏感属性或缓解措施，无法评估公平性贡献。

建议分类：Not applicable

证据：
- algorithm：Three-miRNA logistic regression models were additionally explored using repeated stratified five-fold cross-validation.
- evaluation：
- fairness：
- groups：
- medical：High-grade serous ovarian carcinoma (HGSOC) is the most lethal subtype

[分析原文](https://europepmc.org/article/PPR/PPR1373555)

## p-c7d769f27ffccb863361

文章：[Cross-cohort analyses of OLFML2B cellular distribution and stromal associations in gastric adenocarcinoma.](https://pubmed.ncbi.nlm.nih.gov/43040151/)

审核决定：待审核
审核备注：
证据版本：7b22909078e4e89bc39dc9b251f02c67af4af4a39244a1d2077c7f425b4cc244

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究整合五个队列的批量、单细胞、空间和蛋白质组数据，分析OLFML2B在胃腺癌中的细胞分布及其与成纤维细胞、ECM、TGF-β程序的相关性，并考察PD-1治疗队列中的反应关联；未涉及算法公平性。

纳入判断：摘要聚焦OLFML2B在胃腺癌中的表达与细胞分布，采用队列和统计比较，但未评估AI/ML算法，也未提出算法公平性、差异、编码或缓解问题；无受保护群体或公平性测量，故排除。

限制：仅有摘要，缺少全文方法、代码和数据细节；研究属于分子生物标志物分析，未定义受保护群体、公平性指标或缓解方法，无法支持纳入。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Random-effects meta-analyses of Spearman rank correlations across five follow-up cohorts
- fairness：
- groups：
- medical：The Cancer Genome Atlas stomach adenocarcinoma cohort showed higher tumour expression

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43040151/)

## p-d577bfdc715f5d3350d6

文章：[Association of objectively measured physical activity with incident spinal stenosis in a Fitbit-linked cohort from the All of Us Research Program.](https://europepmc.org/article/MED/43050913)

审核决定：待审核
审核备注：
证据版本：bca44cea6581aff823ce56f8e4dda12fc5994104e4b159739b52daa923dccf6e

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：利用 All of Us 研究项目中 Fitbit 可穿戴设备数据与电子健康记录链接的回顾性队列（48,709 人、161,900 人年），以时变 Cox 比例风险模型评估客观测量的日均步数与活跃分钟数与新发椎管狭窄（颈段、腰段）的关联，发现步数较高者椎管狭窄风险较低（HR 0.84）。

纳入判断：研究主题为可穿戴设备测量的体力活动与新发椎管狭窄的流行病学关联，不属于医学算法公平性研究：没有待评估的 AI/ML 算法，也无算法公平性、差异、编码、缓解或公平性度量问题，更无按群体分层的性能比较。文中对 race、sex、education 的调整属混杂控制，不构成公平性证据，故排除。

限制：仅有摘要，无全文及代码或数据链接；该研究为暴露与结局的流行病学关联分析，未构建或评估任何临床决策算法，未开展亚组公平性度量、偏倚机制或缓解方法分析；race、sex 等仅作为混杂因素校正。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Incident spinal stenosis, cervical stenosis, and lumbar stenosis were identified using standardized SNOMED concepts

[分析原文](https://europepmc.org/article/MED/43050913)

## p-e9bbb6c62205518a6b32

文章：[Tenecteplase vs Alteplase in Basilar Artery Occlusion Treated with Endovascular Thrombectomy: A Propensity Score-Matched Analysis of 90- and 180-Day Outcomes.](https://europepmc.org/article/MED/42217837)

审核决定：待审核
审核备注：
证据版本：6d64618e6e6e9102d819c6c395a242510b63023e511c187b75b783b3b3ed7124

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究利用TriNetX回顾性队列（553例基底动脉闭塞行血管内取栓患者），通过倾向性评分匹配比较替奈普酶与阿替普酶桥接溶栓在90天和180天的出血、死亡、功能依赖及康复利用等结局，未发现显著差异，仅康复利用信号在多重检验校正后消失。

纳入判断：该文是两种溶栓药物的临床比较有效性研究，无AI/机器学习或算法被评估，也无算法公平性/偏倚/编码差异或公平性度量问题；人群分层仅为混杂调整，不构成敏感属性的公平性评估，故不满足算法公平性纳入标准。

限制：仅有摘要，无全文方法、代码或补充材料；研究为药物比较有效性分析，未涉及任何AI/ML模型、算法公平性指标、亚组公平性评测或偏差机制；倾向性评分匹配属于混杂控制而非算法公平性干预。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：basilar artery occlusion stroke treated with IV thrombolysis plus endovascular thrombectomy

[分析原文](https://europepmc.org/article/MED/42217837)

## p-1346d065a32670a53db3

文章：[Critical Validation of Deep Learning-Based Cervical Vertebral Fracture Detection on Computed Tomography Localizer Radiographs.](https://europepmc.org/article/MED/42970201)

审核决定：待审核
审核备注：
证据版本：e86364b2403bf3e427530a2bd0d923783eba6ef87b01337e14fed771dd29fca4

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究在346例创伤患者的CT定位片上评估深度学习颈椎骨折检测，比较全图二分类与先定位颈椎再分类的两步流程，并用置换检验、遮挡测试、Grad-CAM、混杂因素分析及按解剖部位的亚组分析检验模型有效性，发现全图模型虽PR-AUC更高，但并不主要依赖骨折区域，属于典型捷径学习案例。

纳入判断：该文聚焦模型有效性与捷径学习（混杂/伪相关线索），亚组仅为解剖部位而非敏感属性，未提出算法公平性、差异或编码问题，也无公平性度量或缓解方法，按规则不足以纳入。

限制：仅有摘要可查；所谓亚组分析仅按解剖骨折位置划分，未涉及任何敏感属性、人群分组或公平性指标，也未报告组间差异或缓解干预，无法据此判断算法公平性。

建议分类：Evaluation

证据：
- algorithm：deep learning-based methods can reliably detect such fractures on localizer radiographs
- evaluation：assessed through a permutation test, occlusion testing, gradient-weighted class activation mapping
- fairness：
- groups：
- medical：early detection of cervical vertebral fractures in trauma patients

[分析原文](https://europepmc.org/article/MED/42970201)

## p-d6abeded64d1a68e9115

文章：[Same day discharge following bimaxillary osteotomy surgery a single center retrospective study.](https://pubmed.ncbi.nlm.nih.gov/42993311/)

审核决定：待审核
审核备注：
证据版本：9ce7dc6bca9ad559b2ca724400c26adc64979925c98c7784ee19df9741ceacfd

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性队列描述80例双颌截骨术患者同日出院与留院过夜的并发症记录，报告未调整混杂因素的比例差异，未涉及人工智能、算法公平性或受保护群体分析。

纳入判断：研究比较双颌截骨术后的出院安排与并发症，未评估AI/ML算法，也未进行算法公平性、偏倚机制或亚组公平性分析，不符合纳入标准。

限制：仅提供摘要；研究为单中心回顾性、非随机、未调整混杂的临床可行性观察，无算法或公平性证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Complication proportions were compared without adjustment for confounding.
- fairness：
- groups：
- medical：who underwent bimaxillary osteotomy, with or without adjunctive procedures

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42993311/)

## p-2a813b12a1e170b90af2

文章：[Ethical Decision-Making in Nursing Management: Comparing Nurse Managers and Generative Artificial Intelligence](https://europepmc.org/article/PPR/PPR1359832)

审核决定：待审核
审核备注：
证据版本：299e7171272a08d24572f361b9c79490222613adf0c8d3ab3bc43c48ce0d4fe5

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：探索性研究，比较西班牙某公立大学医院护理管理者的伦理决策与三种生成式AI模型在相同管理情景下的回答一致性和重复稳定性。结果显示总体一致性相近，但模型在拒绝执行与知情同意等情景上系统性偏离人类众数；作者强调稳定性、专业一致性与伦理正当性是三个独立问题，不主张临床有效性。

纳入判断：该文考察生成式AI在护理管理伦理决策中的一致性与稳定性，属于人机一致性/治理研究。文中“fairness-related actions”仅指伦理决策内容，未提出算法公平性问题，未定义受保护群体或亚组发现协议，也未实施公平性测量评估，属于偶然提及公平，故排除。

限制：仅有摘要，无全文方法与数据；未定义任何患者群体或敏感属性，未做亚组公平性指标分析；“公平”仅作为伦理决策选项出现，并非算法公平性研究；也未涉及临床任务或疾病结局。

建议分类：Evaluation

证据：
- algorithm：Models received the complete questionnaire in new web conversations
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1359832)

## p-2d4258f545c1b26784f5

文章：[Concurrent cognitive, behavioral and systemic physiological features mark preclinical Alzheimer’s disease](https://europepmc.org/article/PPR/PPR1354470)

审核决定：待审核
审核备注：
证据版本：b19ad20ea74f24baa22dbfe5f7fb5abc46c3f9c87d55b0d283a4e266a600cabc

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：研究纳入644名自报认知正常的老年人，以血浆p-tau217界定临床前阿尔茨海默病亚组，描述其认知、行为及生理特征，并构建概念验证AI分类器整合多域临床数据，较单独认知筛查提高p-tau217高风险个体识别。

纳入判断：摘要聚焦临床前AD多域表型与p-tau217分类器，未提出或评估算法公平性、亚组差异或敏感属性；仅具临床相关性，故排除。

限制：仅有摘要，缺乏算法细节、亚组性能及敏感属性分析；未报告公平性、差异或缓解评估，不能支持医学算法公平性纳入。

建议分类：Not applicable

证据：
- algorithm：A proof-of-concept AI classifier integrating routine multidomain clinical data
- evaluation：improved identification of p-tau217-high individuals relative to cognitive screening alone
- fairness：
- groups：
- medical：biomarker-defined, risk factor - controlled preclinical AD subgroup

[分析原文](https://europepmc.org/article/PPR/PPR1354470)

## p-481a4db85e5cf700e6a2

文章：[Early Catheter Ablation for Patients With Atrial Fibrillation and a Stroke History: A Target Trial Emulation Analysis.](https://pubmed.ncbi.nlm.nih.gov/42821842/)

审核决定：待审核
审核备注：
证据版本：0e8db7adcda3a865b0f246ad601bd3cf7b71b18307a3330e7d35d10b8b255170

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究采用目标试验模拟（克隆-删失-加权法）比较房颤合并缺血性卒中患者早期导管消融与药物治疗的长期结局，纳入6家中心431例患者，报告MACE、再住院、死亡及mRS/AD8功能认知结局的关联，属观察性因果效应估计研究。

纳入判断：该文为房颤卒中亚组导管消融疗效的目标试验模拟分析，属临床比较效果研究；未评估任何AI/ML算法，也未提出算法公平性/差异/编码/缓解或公平性测量问题，虽有临床任务与经验评估，但不满足算法与公平性两项准则。

限制：仅有摘要，无全文；研究未涉及AI/ML模型或算法公平性评估，仅以性别比例等形式描述人群构成，未见任何亚组公平性指标、偏倚机制或缓解方法。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：patients aged 18-85 years with AF and a history of ischemic stroke

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42821842/)

## p-596a0bc151428ccc8ae7

文章：[Value-Based Care in Neurosurgery: Results from Maryland’s Global Budget Revenue Program](https://europepmc.org/article/PPR/PPR1344342)

审核决定：待审核
审核备注：
证据版本：2cd68e91b5070e385b76751e73789f599a5038ca3c5a3b5cada6d146c5aa038a

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：研究评估马里兰全球预算收入模型对垂体手术费用、住院时长、再入院及不同保险和年龄患者构成的影响，报告费用下降与低收入患者可及性改善，但未涉及AI/ML算法或算法公平性。

纳入判断：摘要仅评估支付政策与手术结局及可及性，未评估AI/ML算法，也未进行算法公平性测量；健康公平提及不构成算法公平研究。

限制：仅有摘要；无AI/ML算法，也无算法公平性评估；属于支付政策回顾性研究，不能支持纳入。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：average hospital charges per patient decreased significantly ($37,615 to $34,059, p = 0.04)
- fairness：
- groups：The proportions of patients aged 65 years or older (20.8% to 27.0%, p = 0.033)
- medical：procedure codes for pituitary surgery performed between January 2012 and January 2018

[分析原文](https://europepmc.org/article/PPR/PPR1344342)

## p-7d86f34b5b0505602795

文章：[How to tackle inequities in bereavement support for ethnically diverse communities: a national qualitative study using experience-based co-design.](https://pubmed.ncbi.nlm.nih.gov/42902353/)

审核决定：待审核
审核备注：
证据版本：3cd87167d1a803e69648ec9758d46b0f489c8d8c6c87a4c0c151ef4826bc9c92

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该全国定性研究通过访谈、焦点小组和共创工作坊，识别族裔多元群体在丧亲支持获取上的障碍与促进因素，提出文化安全照护、反种族主义实践和社区合作建议，并形成逻辑模型。研究未涉及AI/ML算法或算法公平性评估。

纳入判断：摘要显示为丧亲支持服务的定性公平性研究，未评估任何AI/ML算法或算法公平性指标，不属于医学算法公平性研究。

限制：仅摘要；无算法、模型、数据集或代码信息，也未报告算法公平性指标或缓解方法，无法判断医学算法公平性贡献。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：We conducted interviews (n = 53) and focus groups (n = 9)
- fairness：People from ethnically diverse communities experience inequities in accessing bereavement support
- groups：121 bereaved people from 13 ethnically diverse backgrounds
- medical：formal bereavement support services can better serve ethnically diverse communities

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42902353/)

## p-875da7d10afd9f30ec2b

文章：[Clinical equipoise as inclusion criterion to control for confounding in observational studies.](https://pubmed.ncbi.nlm.nih.gov/42854534/)

审核决定：待审核
审核备注：
证据版本：a49c74b56fb7f3d05980dc598c22e71c9c406611e04289da1f688f043830273b

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究以专家治疗推荐分歧作为临床均势代理，评估不同分歧层级下肱骨近端骨折治疗组基线可比性，发现更严格纳入标准可改善组间平衡但减少样本量。研究不涉及医学AI/ML算法或算法公平性评估。

纳入判断：研究关注观察性研究中的混杂控制与纳入标准，未评估医学算法，也未提出或测量算法公平性/偏倚问题，不符合纳入标准。

限制：仅有摘要；未报告AI/ML模型、算法公平性指标、受保护亚组或公平性干预与评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：patients with proximal humerus fractures

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42854534/)

## p-9a0944cda37da259a878

文章：[Propensity Score Matching Unmasks Core Predictors of Psychosis Conversion in Clinical High-Risk Individuals.](https://pubmed.ncbi.nlm.nih.gov/42960986/)

审核决定：待审核
审核备注：
证据版本：cd94dfd327dbe648783b2504f526977e24b5e5be6a28b1bb19d8cbe3123f87bc

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究在920例临床高危精神病(CHR-P)个体中随访3年，使用倾向性评分匹配(PSM)平衡年龄、性别、教育程度及6个认知域等混杂因素，再以多因素logistic回归与ROC分析识别精神病转化的独立预测因子。PSM后模型AUC由0.685升至0.808，GAF下降率单项准确率约73%，作者据此强调早期精神病预测中需控制认知与人口学混杂。

纳入判断：该文是临床预后预测建模研究，以倾向性评分匹配控制认知与人口学混杂并提升AUC，属于统计混杂校正而非算法公平性问题：未定义受保护群体、未测量亚组性能差异、未讨论编码偏倚或缓解方法。摘要亦无公平性相关词句，故不符合纳入标准。

限制：仅有摘要，无全文方法细节、代码或数据链接。PSM仅用于消除混杂以提升预后预测准确性，未涉及任何敏感属性亚组的算法公平性定义、差异度量或偏倚缓解设计，也未报告分组公平性指标。

建议分类：Not applicable

证据：
- algorithm：multivariate logistic regression were conducted in the entire and PSM cohorts
- evaluation：Receiver Operating Characteristic curves quantified predictive accuracy
- fairness：
- groups：
- medical：Predicting psychosis conversion in clinical high-risk for psychosis (CHR-P) individuals

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42960986/)

## p-9ea0a6100ead36f59229

文章：[Extracapsular and joint-dominant hand and wrist MRI patterns in psoriatic and rheumatoid arthritis: an exploratory case-control study.](https://pubmed.ncbi.nlm.nih.gov/42978735/)

审核决定：待审核
审核备注：
证据版本：fde4f16acc1e268d55bc26ddbf491d71a0a7512f61e09414d83a58b61c6af789

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该探索性病例对照研究比较41例银屑病关节炎与41例类风湿关节炎患者手/腕3.0T MRI的预设影像学特征，发现关节囊外软组织炎症、附着点相关特征更支持PsA，而关节积液、腕部滑膜炎与骨侵蚀更支持RA，并报告了读者间与读者内一致性系数。

纳入判断：研究为PsA与RA的MRI影像模式诊断学比较，采用Firth校正logistic回归仅作统计校正，未评估任何AI/ML算法的公平性、偏倚机制或缓解方法，也无亚组差异指标或公平性度量，不符合纳入所需的算法公平性证据标准。

限制：仅有摘要；未涉及任何算法或AI模型，也未按年龄、性别等属性进行亚组公平性比较；年龄与性别仅作为校正混杂因素进入回归模型；样本量小、无外部验证，结论本身声明需独立验证。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：compare prespecified hand and wrist magnetic resonance imaging (MRI) features between PsA and RA

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42978735/)

## p-a8215224fac5c572c2b3

文章：[The C-reactive protein to lymphocyte ratio and 28-day mortality in critically ill patients with sepsis: a retrospective propensity score-matched cohort study.](https://pubmed.ncbi.nlm.nih.gov/43011466/)

审核决定：待审核
审核备注：
证据版本：d0bafca4af884569f4987a256e2c02a6f94ccc8916029d1bc3530dd42d401b3f

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：基于MIMIC-IV的回顾性倾向评分匹配队列，评估脓毒症患者C反应蛋白/淋巴细胞比与28天及长期全因死亡率的关联和预测价值；未涉及算法公平性、偏倚机制或缓解评估。

纳入判断：研究聚焦脓毒症生物标志物预后关联，虽使用回归与ROC评估，但无AI/ML公平性、差异或缓解问题，亦无定义公平群体，故不符合纳入标准。

限制：仅有摘要；未报告公平性指标、受保护属性或算法偏倚分析；常规亚组与交互分析不能替代算法公平性评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：ROC curve analysis and subgroup analysis
- fairness：
- groups：
- medical：critically ill patients suffering from sepsis

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43011466/)

## p-a879f645b9e32d620670

文章：[Leveraging Artificial Intelligence in Healthcare in Cambodia: Enhancing Access and Patient Outcomes.](https://europepmc.org/article/MED/42948795)

审核决定：待审核
审核备注：
证据版本：6467cf750a148b6395588eafaad351f5b63c4b8612d20715bfca67e4a9328790

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：一篇关于柬埔寨医疗人工智能应用与准备度的叙述性视角文章，梳理AI在影像诊断、远程医疗、公共卫生监测、临床决策支持与卫生管理中的潜在用途，并讨论基础设施、数据质量、算法偏倚、治理与公平可及等实施前提，不含任何实证研究或亚组分析。

纳入判断：叙述性观点文章：虽点名结核、糖尿病、癌症等具体应用，但未提供任何针对某一任务的算法公平性实质分析，无亚组指标、机制或缓解方法比较；分组定义与实证测量评估两项证据标准均不满足，属偶提公平议题，按规则排除。

限制：全篇为叙述性视角文章，未做系统检索、定量综合或任何实证测量；算法偏倚仅在伦理风险清单中泛泛提及，缺少具体疾病或任务下的亚组指标、偏倚机制分析或缓解方法比较，公平论述停留在农村与城市可及性及治理建议层面。

建议分类：Not applicable

证据：
- algorithm：Machine learning algorithms identify patterns within data to generate predictions or classifications
- evaluation：
- fairness：
- groups：
- medical：AI may also strengthen pathology services through the automated analysis of histopathological images

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13712576/fullTextXML)

## p-aa8feb0bc600e4f4a402

文章：[Machine Learning Classification of Bipolar Disorder Across Mood States Using Natural Language Processing and Speech Analysis: Observational Study.](https://europepmc.org/article/MED/42967232)

审核决定：待审核
审核备注：
证据版本：4fcde67737c2b6f239c6fef058bba613a142c96d7507d958030cb2f5f45c3479

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究分析61例双相障碍患者与99名健康对照的语音和自然语言特征，采用LASSO逻辑回归与嵌套交叉验证，报告双相障碍识别AUC 0.916，并比较不同心境状态；属于临床机器学习分类研究。

纳入判断：未满足公平性准则：无明确的算法公平、差异、编码、缓解或公平度量问题，年龄性别匹配不等同于亚组公平分析，故排除。

限制：全文未提出算法公平性问题，也未按年龄、性别等亚组报告性能或差异；年龄性别匹配仅用于控制混杂，非公平性评估或缓解，且缺少外部验证。

建议分类：Not applicable

证据：
- algorithm：We applied least absolute shrinkage and selection operator (LASSO)–regularized logistic regression
- evaluation：Classification metrics were computed from the participant-level averaged out-of-fold probabilities
- fairness：
- groups：
- medical：the model achieved high diagnostic discrimination for BP vs HC (AUC=0.916)

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13723951/fullTextXML)

## p-b6013b3588eaf73c1be0

文章：[Fitting Dynamic Conditional Densities to Cross-Sectional Returns with Persistent Tail Intensities](https://arxiv.org/abs/2610.32011)

审核决定：待审核
审核备注：
证据版本：0e2f68bfdf1c549dc24ce98f2219e2c8b25151a985a224622d0f482a3037d371

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：该文提出DCD-SM（样条混合动态条件密度）模型，通过得分驱动更新在保持参考尾部阶数的前提下刻画横截面股票收益左、右尾部强度的持续性，使用Wald检验与样本外密度、分位数损失评估，并在19个美日股票横截面面板上实证。属金融时间序列统计方法研究，不涉及医学影像或临床AI公平性。

纳入判断：主题为金融横截面收益的动态尾部密度建模与检验，既非生物医学任务，也不涉及算法公平性、群体差异或缓解措施，超出医学算法公平性综述范围。

限制：全文为金融计量/统计方法论文，缺少生物医学或临床任务、AI/ML算法公平性、受保护群体定义及子组差异测量等全部纳入要件；无任何与医疗算法公平性相关的证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://arxiv.org/html/2610.32011v1)

## p-ba6fa6408cc8bbe26dd7

文章：[Development and validation of a cuff size prediction model for pediatric blood pressure measurement outside the office.](https://pubmed.ncbi.nlm.nih.gov/42207271/)

审核决定：待审核
审核备注：
证据版本：e0e65a66cc239cf391f2dada1b21a08258ef7df9fb3766cd717a292e9e2ff214

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：基于NHANES数据开发线性回归模型，用年龄、性别、身高、体重等EHR变量预测儿童中臂围以确定动态血压监测袖带尺寸，并在儿科高血压门诊107人外部验证；报告预测一致性（⍴c=0.94）与袖带尺寸符合率（83.2%）。

纳入判断：该文属预测模型开发与外部验证，评估的是整体预测精度与袖带尺寸一致性；虽将性别作为预测变量，但未提出问题化的算法公平性/差异问题，无亚组分层指标、偏倚机制或缓解方法，按规则排除。

限制：仅有摘要级证据；全文的方法细节、代码与数据可用性未知。摘要未报告任何按性别、年龄、种族等亚组的性能比较或公平性度量。

建议分类：Not applicable

证据：
- algorithm：Using linear regression, we considered piecewise and polynomial effects of age, sex, height, and weight as predictors of AC
- evaluation：We validated the model in pediatric hypertension clinics at an academic medical center
- fairness：
- groups：
- medical：determine cuff size for ambulatory blood pressure monitoring (ABPM)

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42207271/)

## p-d329a221375326aba663

文章：[Artificial Intelligence Applications in General Surgery in the United States of America: A Bibliometric Analysis.](https://pubmed.ncbi.nlm.nih.gov/42104780/)

审核决定：待审核
审核备注：
证据版本：f2820364b1d083ac2c86af316764af17284a7d062664c43a5958be4d4e551c76

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文是对美国普外科人工智能研究的文献计量分析，纳入2020—2025年59篇文献，统计作者、主题、期刊、国别与资助分布，采用H指数、AIS、布拉德福德定律及泊松/负二项回归等指标，发现研究集中于手术流程识别与临床决策支持，且资金更倾向临床可落地的应用。

纳入判断：文献计量学研究，虽涉及普外科AI临床应用，但核心问题是研究产出与资助格局，未评估任何算法的公平性、亚组差异或偏倚机制；结论中“equity-focused AI development”仅为泛泛的公平AI建议，缺乏亚组指标、机制或缓解方法的具体分析，不满足公平性标准。

限制：仅提供摘要，无全文方法、数据或代码信息。文中未涉及任何算法公平性指标、亚组比较或偏倚机制分析，仅在结论中以一句泛泛的“公平导向”建议收尾，属偶发提及。

建议分类：Not applicable

证据：
- algorithm：Surgical workflow recognition (n = 19) and clinical decision support (n = 18)
- evaluation：
- fairness：
- groups：
- medical：focused on AI use in general surgery were included

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42104780/)

## p-e2c8854d96deaa4b99ad

文章：[Racial Composition and Single-Input Dominance in the First Hospice Special Focus Program Cohort.](https://pubmed.ncbi.nlm.nih.gov/42895138/)

审核决定：待审核
审核备注：
证据版本：eaa7e207a21888bd2b7f34ad4dbb56223ed4c89d4c9468d46c8867bd00de01e0

模型建议：related

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究审计美国临终关怀特别关注项目（SFP）的复合质量算法：对2024年11月CMS目录中7115家临终关怀机构做横断面分析，用逻辑回归检验入选与机构规模、患者种族构成及独立质量指标（HVLDL）的关系，并对50家入选机构的复合评分做标准化输入分解。结果显示入选与黑人患者比例显著相关，且48/50家入选机构的评分恶化主要由单一输入驱动，提示算法可能不成比例地影响服务黑人患者的机构。

纳入判断：摘要明确评估联邦临终关怀监督复合算法入选结果与患者种族构成的关联，含7115家机构的实证测量与评分输入分解，五项标准均有摘要证据；但依据仅摘要不得建议纳入的规则，定为related而非suggest_include。

限制：仅有摘要，缺少完整抽样、变量定义、模型设定与敏感性分析细节；为观察性横断面分析，不能推断因果；仅基于单一批次50家入选机构，且该项目2025年因诉讼暂停，外部适用性与时间稳定性有限。

建议分类：Evaluation

证据：
- algorithm：Federal quality oversight increasingly uses composite algorithms built from administrative counts and caregiver-reported experience
- evaluation：Cross-sectional analysis of all 7115 active hospices in the November 2024 CMS Provider Data Catalog.
- fairness：SFP selection identified hospices with worse independent quality but usually reflected a single input and disproportionately affected Black-serving hospices.
- groups：Selectees served more non-White patients (median, 35% vs 17%; P < .001), an association persisting after HVLDL adjustment
- medical：the Hospice Special Focus Program (SFP) selected 50 hospices for intensified oversight and possible Medicare termination

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42895138/)

## p-f773c3a00472650dfad3

文章：[Good Enough to Sequence: Fluorometry-Guided Salvage of Low-Volume and Compromised Paediatric DNA in Custom Amplicon Next-Generation Sequencing.](https://pubmed.ncbi.nlm.nih.gov/43028320/)

审核决定：待审核
审核备注：
证据版本：e48224c92a69d57044851db5ea81aaecb11983778a564a3aafa5173c542de48b

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究基于314例儿童样本，比较Qubit与Nanoquant定量及A260/280质量分组对定制扩增子NGS建库产量、测序深度与覆盖度质控指标的影响，并提出约20 ng/µL的输入阈值以降低建库失败风险。属实验室样本质量控制方法学，不涉及AI算法评估或算法公平性分析。

纳入判断：研究内容为测序前DNA定量与质量控制的实验室方法学，虽含建库失败的ROC/逻辑回归预测，但未评估任何AI/ML算法的公平性或偏倚，也未定义人口学亚组或公平性指标，不满足医学算法公平性研究的入选标准。

限制：仅有摘要证据；分组依据为DNA浓度与纯度，而非人群或敏感属性；全文是否含其他分析无法从摘要判定，但摘要中未见任何算法公平性、偏倚测量或缓解评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43028320/)

## p-35e6e11c24cb884c5eeb

文章：[Clinical and molecular characteristics associated with megakaryocytic dysplasia in patients with myelodysplastic syndromes.](https://pubmed.ncbi.nlm.nih.gov/43043920/)

审核决定：待审核
审核备注：
证据版本：8608b4c5da3ac77fe9fe837a96b7b5ad2464a49c8b39c6e3c893758ad6b28ee2

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究169例骨髓增生异常综合征患者，比较伴或不伴巨核细胞发育异常者的临床、细胞遗传学及突变特征，发现EZH2突变是唯一独立相关因素。该研究为临床-分子关联分析，未涉及AI/ML算法或算法公平性。

纳入判断：摘要聚焦骨髓增生异常综合征中巨核细胞发育异常的临床与分子关联，无AI/ML算法被评估，也未涉及公平性、差异、编码或缓解问题及受保护群体，故排除。

限制：仅有摘要，缺少全文方法学细节与外部验证信息；且内容与算法公平性无关。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：morphologic abnormality in myelodysplastic syndromes (MDS)

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43043920/)

## p-c953684f67e297ff37a6

文章：[Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models](https://arxiv.org/abs/2611.21215)

审核决定：待审核
审核备注：
证据版本：54b32c6eb87979f1b666520d3c9fa53193926cc3f6bdfb55a68e96862ffc9b00

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：Open-fMIND 构建并发布大规模开放 fMRI 分区时间序列语料，覆盖 322 项 OpenNeuro 研究、11,379 名受试者，支持脑基础模型自监督预训练，并在 HCP-YA、ABIDE、ADHD-200 上评估下游预测性能。

纳入判断：该文是开放 fMRI 预训练语料与下游评测，虽涉及诊断/认知预测和年龄性别覆盖，但未提出或检验算法公平性、亚组差异或缓解问题，不符合公平性研究纳入标准。

限制：全文未定义公平性目标或报告按年龄、性别、站点等亚组的模型性能差异；人群覆盖和站点/运动效应仅为数据质量或使用注意事项，且无公平性缓解方法。

建议分类：Not applicable

证据：
- algorithm：We test whether Open-fMIND supports the pretraining of a published fMRI foundation model, Brain-Semantoks
- evaluation：Three frozen encoders are compared on the same downstream tasks
- fairness：
- groups：Age and sex coverage is uneven and inherited from the source studies
- medical：we predict diagnosis, sex, and age in 5 classes of equal size with class-balanced logistic regression

[分析原文](https://arxiv.org/html/2611.21215v1)

## p-11a0ba65de9fc94bbcd8

文章：[Navigating the cultural iceberg: Addressing algorithmic bias, hallucination, and semantic flattening in AI-assisted qualitative thematic analysis.](https://pubmed.ncbi.nlm.nih.gov/42721502/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；缺少可核验的 journal_title/journal_issns/conference 字段，保留待核验。

## p-0e0b644cf1773f4a50f3

文章：[Next-Generation Brain Health Monitoring Enabled by Integrated Wearable AI Infrastructure.](https://europepmc.org/article/MED/42936287)

审核决定：待审核
审核备注：
证据版本：279083f8c53522b46fb9ed2b47492d86f0b16dbc7360b7db63a568c0d3c39427

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：综述可穿戴AI用于阿尔茨海默病、帕金森病和TDP-43蛋白病等神经退行性疾病的早期监测，涵盖多模态传感、边缘计算、联邦学习、临床验证与治理；公平性仅作为设计原则简要提及。

纳入判断：虽点名具体神经退行性疾病并提及公平性，但属于综述中的原则性建议，缺乏对特定疾病/任务的详细公平性分析或实证评估，按规则应排除而非作为相关推荐。

限制：全文为广泛技术综述；公平性内容分散于肤色相关PPG误差、亚组校准和审计建议，未针对特定疾病或任务提供实质性亚组指标、偏差机制实验或缓解方法比较。

建议分类：Not applicable

证据：
- algorithm：Multimodal models that incorporate gait, sleep, cardiac, and speech signals estimate disease risk
- evaluation：
- fairness：Equity monitoring must be embedded in federated training, not added as an afterthought.
- groups：patients with darker skin tones, for whom PPG‐derived HRV is less accurate, or older patients with atypical gait patterns
- medical：This review focuses on Alzheimer's disease, Parkinson's disease, and TDP‐43 proteinopathies

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13697001/fullTextXML)

## p-21c05110656354a438ee

文章：[Density Peak Clustering: A Systematic Survey of Methods, Applications, Challenges, and Future Research Directions](https://europepmc.org/article/PPR/PPR1352750)

审核决定：待审核
审核备注：
证据版本：b677af6b7530a3c8a742e5d376c058ea93d02c0bd219c980333027a00a794433

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：这是一篇关于密度峰值聚类（DPC）的系统性综述，梳理2014年以来的方法演进、八大方法族（自适应邻域与密度估计、图与流形建模、自动确定簇数、分配与不确定性、表示学习、隐私/联邦/增量计算、可扩展执行、采样与优化等辅助策略）及其适用假设与计算代价，并列举医疗、网络安全、遥感、交通等领域应用，最后提出面向鲁棒、可解释、公平、隐私保护等方向的未来研究议题。

纳入判断：该文为通用聚类算法（DPC）综述，医学仅作为应用领域之一被顺带提及，未指明任何具体疾病或临床任务；公平性仅在结尾未来方向中以“fairness-aware”一笔带过，属于偶发提及，缺少针对具体医学情境的子群度量、偏倚机制或缓解比较等实质性分析，故不纳入。

限制：仅有摘要，未见正文与实验细节；摘要中“healthcare”仅为泛化应用领域列举，未给出具体疾病或临床任务，也未提供任何子群指标、偏倚机制或缓解方法的实质分析，“fairness-aware”仅出现在未来方向罗列中。证据不足以判定其属于医学算法公平性研究。

建议分类：Not applicable

证据：
- algorithm：Density Peak Clustering (DPC) is a widely studied unsupervised clustering method that identifies cluster centers using local density and relative separation
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1352750)

## p-2929aa6bb236b998782c

文章：[What Factors Influence Hospital Admission for Mandible Fractures in Emergency Departments Across the United States?](https://pubmed.ncbi.nlm.nih.gov/42235594/)

审核决定：待审核
审核备注：
证据版本：472f925508d720678d7b89fa3d6c90380dd2eb6bfc60d13a1f2e609acb1ba8f3

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：基于2022年全国急诊样本的回顾性队列，分析下颌骨骨折患者入院及费用的生物、情境和社会经济预测因素。结果显示男性、多发骨折、合并中面部骨折和枪伤与入院相关，无保险患者入院可能性较低。

纳入判断：该文有临床任务、分组和统计分析，但核心不是算法公平性；仅在结论泛泛提及“improve equity”，属于偶然提及，按规则排除。

限制：仅有摘要；研究使用多变量 logistic 模型识别入院预测因素，并非评估 AI/ML 算法的公平性，也未报告分组模型性能、偏倚机制或缓解措施。

建议分类：Not applicable

证据：
- algorithm：A multivariable logistic model was used to identify independent predictors of admission.
- evaluation：A multivariable logistic model was used to identify independent predictors of admission.
- fairness：
- groups：male sex (OR: 1.23; 95% CI: 1.11 to 1.36)
- medical：mandible fractures presenting to EDs across the United States

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42235594/)

## p-442a05aaacc8e4189c99

文章：[Promoting Just Culture: Implementing a Medication Error Reporting Process in Nursing Education.](https://pubmed.ncbi.nlm.nih.gov/42089774/)

审核决定：待审核
审核备注：
证据版本：52b2587f2d597aa308666234b643323a8a6d21ef19dc9ce8ed59b765e129508b

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：护理教育中的用药错误报告质量改进项目：培训临床教师使用标准化报告流程（事件上报系统、复盘工具、学生行为分类算法、第二受害者支持），比较培训前后的教师调查结果，教师处理用药错误的信心显著提升，并称促进公平。全文未涉及AI/ML算法或算法公平性分析。

纳入判断：该文为护理教育中用药错误上报流程的质量改进项目，文中“算法”指人工分类学生行为的流程，并非AI/ML模型；公平/公正文化仅作为管理理念被提及一次，缺少明确的受保护属性、亚组比较与公平性测量，属于偶然提及，不符合纳入标准。

限制：仅有摘要；无算法模型、无受保护群体定义、无亚组或公平性指标；公平仅在结论处被提及一次；无代码或数据链接信息。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：aimed to promote a just culture when medication errors (MEs) occur

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42089774/)

## p-4ba526797d8b268917d7

文章：[Toward Clinically Trustworthy Deep Learning in Cardiology: A Unified Mathematical Synthesis of Representation, Optimization, and Reliability.](https://europepmc.org/article/MED/43028492)

审核决定：待审核
审核备注：
证据版本：fd14cf23f94badc3c76c4afb8f76109c3116249dc52ad685b26fbc3d3b176dc8

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该系统综述基于79篇文献，从统一的数学视角梳理心脏病学可信深度学习中的表示学习、优化、不确定性、鲁棒性、公平性、可解释性与泛化，并提出概念性审计框架；作者强调相关指标仅具理论性，并非实际临床指标。

纳入判断：该文是心脏病学可信深度学习的宽泛系统综述，公平性仅作为概念之一被附带提及，未提供特定疾病或任务的实质性算法公平性分析；按综述入选规则不予推荐，且摘要级证据不足以建议纳入。

限制：仅见摘要；公平性只在可信性概念列举中出现，未见具体心血管疾病或任务下的亚组指标、偏倚机制、评测设计或缓解方法；作者自述所提指标纯属理论。

建议分类：Evaluation

证据：
- algorithm：unifying mathematical perspective on the notion of trustworthy deep learning in cardiology
- evaluation：
- fairness：
- groups：
- medical：automated analysis of electrocardiography, imaging of the heart, and multimodal clinical datasets

[分析原文](https://europepmc.org/article/MED/43028492)

## p-4de41133d806ea411327

文章：[Object Detection in Computer Vision: A Comprehensive Review of Algorithms, Datasets, and Evaluation Techniques.](https://europepmc.org/article/MED/42944526)

审核决定：待审核
审核备注：
证据版本：b940692af232820230af48fd099b1738018d3e2ce0fc330e82989a389b6b0343

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：一篇面向通用计算机视觉的目标检测综述，系统梳理传统方法、CNN/Transformer/LLM 检测器、通用与领域数据集（含医学影像数据集）以及 mAP、IoU 等评估指标；公平性仅在“未来挑战”和数据集偏差的一般性描述中被顺带提及，未针对任何医学任务做公平性分析。

纳入判断：该文是通用目标检测综述，未以某一具体医学疾病或任务为分析对象，也没有提供该场景下的实质性算法公平性分析（无亚组评估、偏差机制或缓解对比），属于公平性偶然提及，按规则排除。

限制：全文为通用 CV 综述，医学仅作为应用场景与数据集举例（脑肿瘤、肺部病变、MIMIC-CXR、ISIC 等）；公平性只出现在挑战展望及“年龄、族裔、性别偏差”等泛泛表述中，缺少亚组指标、偏差机制测量或缓解方法比较的任何具体证据。

建议分类：Not applicable

证据：
- algorithm：a comprehensive review of computer vision-based object detection algorithms and related research trends
- evaluation：
- fairness：
- groups：
- medical：Medical imaging datasets provide annotated images from modalities such as X-ray, MRI, CT, and ultrasound for clinical tasks

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13709326/fullTextXML)

## p-5ff397bb1086a10ff761

文章：[Contribution of artificial intelligence research to the development of inclusive applications for people with disabilities: A scoping review (2015-2025).](https://europepmc.org/article/MED/42879324)

审核决定：待审核
审核备注：
证据版本：05789be02dcd34110c33769e113cceb5d8778c91ba3884507456cbd03c334471

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为2015—2025年范围综述，检索四个数据库并纳入93项健康AI研究，考察其对残障人士包容性应用的支持程度。约60%研究提及公平，但仅12.9%落实具体措施（如工具适配、样本多样性），6.5%让残障人士参与共同设计或验证，并指出算法偏见与数据代表性不足等问题。

纳入判断：主题虽涉及健康AI中的算法偏见与残障群体，但这是覆盖多类残障的泛化公平综述：未命名具体疾病或临床任务，也未在该情境下给出亚组指标、偏见机制或缓解方法比较等细致公平分析，且仅12.9%研究落实公平措施，属泛化公平倡导型综述，按规则排除。

限制：仅提供摘要，无全文方法、亚组指标或任务细节；综述横跨运动、感官、认知、沟通与心理社会等多类残障，未锚定具体疾病或临床任务，公平性分析停留在措施计数与宏观公平倡导层面，无法判定是否满足综述纳入条件。

建议分类：Evaluation

证据：
- algorithm：This scoping review examines the extent to which AI research in health contributes to the development of inclusive technologies for PWD
- evaluation：only 12 (12.9%) implemented concrete measures (e.g., adapting tools for vulnerable groups or ensuring sample diversity)
- fairness：This exclusion is driven by algorithmic bias, non-representative datasets, and limited involvement of PWD
- groups：people with disabilities (PWD), representing 16% of the global population
- medical：

[分析原文](https://europepmc.org/article/MED/42879324)

## p-6c2d4e6ce2f485ff83ff

文章：[Advancing Equitable and Trustworthy AI in Breast Cancer Detection Through Interpretable Deep Learning](https://europepmc.org/article/PPR/PPR1361567)

审核决定：待审核
审核备注：
证据版本：ce0f534bb4a88574dd834591c964a781c9f02c43f7e5344b01d667328524bd79

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：methodology, recall

中文概述：该文为PRISMA系统综述，聚焦乳腺癌钼靶筛查中深度学习模型的公平性与人口学偏倚，提出解释图“reasoning bias”及多指标热图偏倚评估框架，并指出种族、年龄和乳腺密度交叉亚组证据不足。

纳入判断：摘要明确为乳腺癌钼靶深度学习公平性系统综述，涉及种族、年龄和乳腺密度亚组及解释偏倚；但证据仅限摘要，无法确认全文是否具备实质性、细粒度的公平性综合分析，故暂缓而非建议纳入。

限制：仅有摘要，无法核验全文是否实际提供细粒度亚组指标、偏倚机制分析或综述结果；该文为综述并主要提出未来研究框架，非原始实证评估。

建议分类：Evaluation

证据：
- algorithm：Deep learning (DL) methods — particularly Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs)
- evaluation：systematic literature review follows the PRISMA 2020 guidelines to synthesize evidence from 50 peer-reviewed studies
- fairness：fairness and equity across demographically diverse patient populations
- groups：Black women, elderly patients, and those with high breast density
- medical：Breast cancer remains the most frequently diagnosed cancer among women worldwide

[分析原文](https://europepmc.org/article/PPR/PPR1361567)

## p-8133fbf008b01c6049b4

文章：[Trustworthiness Evaluation of Medical Vision-Language Models: A Scoping Review and a Proposed Minimum Evaluation Checklist.](https://europepmc.org/article/MED/42933376)

审核决定：待审核
审核备注：
证据版本：d0a049ff0690fd1b3bc2048ae8646d850d29f5bfef0a3304ecc74e187e4440ca

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该范围综述系统梳理医学视觉-语言模型的可信度评估实践，提出八项最低可信度评估清单（MiTEC）并做回溯打分：稳健性11/29、幻觉7/29，而公平性与可解释性各仅4/29（13.8%），亚组分析、形式化校准与图像依赖对照均少见。

纳入判断：该文为可信度（含稳健性、幻觉、公平性等八个维度）范围综述，公平性仅以“4/29（13.8%）”的计数形式出现，未命名具体医学疾病或任务，也没有该场景下实质性的算法公平性分析（如亚组指标、机制或缓解方法比较），属于附带提及；且仅有摘要证据，不满足综述纳入所需的两项条件。

限制：仅有摘要可查：公平性只是可信度八个维度之一，未指明具体疾病或影像任务，也未给出亚组定义、公平性指标或偏差机制的具体分析，因此无法核验其公平性综合的深度。

建议分类：Evaluation

证据：
- algorithm：Medical vision-language models combine images and text to answer questions, generate reports
- evaluation：
- fairness：Interpretability and fairness were each evaluated in 4/29 (13.8%)
- groups：
- medical：evaluated an image-and-language model in a medical imaging context

[分析原文](https://europepmc.org/article/MED/42933376)

## p-9830d51967755c683818

文章：[Explainable and Trustworthy AI for Diabetic Retinopathy: A Systematic Review and Diagnostic Meta-analysis](https://europepmc.org/article/PPR/PPR1350140)

审核决定：待审核
审核备注：
证据版本：1a52047f3404643d5b4a42d0ad0d334d5ea6655d940341d60b319c38062cf82e

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文为糖尿病视网膜病变（DR）可解释与可信AI的系统综述和诊断Meta分析，汇总10项研究的诊断性能，并讨论可解释性、校准、不确定性、泛化、公平性、隐私和部署证据。

纳入判断：摘要明确DR任务和AI评估，但公平性仅作为可信AI维度被笼统提及（亚组公平性有限及建议），缺乏具体亚组证据；仅摘要不足以判断全文是否有详细公平性综合，故暂缓而非纳入。

限制：仅有摘要；未见具体亚组公平性指标、敏感属性定义、偏倚机制或缓解方法比较，无法核验全文是否包含详细的DR公平性分析。

建议分类：Evaluation

证据：
- algorithm：assessed the state-of-the-art explainable and trustworthy-AI methods for DR
- evaluation：
- fairness：calibration, subgroup fairness, privacy-preserving learning and prospective human-AI evaluation were limited
- groups：
- medical：Diabetic Retinopathy (DR) detection and severity grading

[分析原文](https://europepmc.org/article/PPR/PPR1350140)

## p-a25ee48f36a8a2dc7e0f

文章：[Beyond Mallampati: From Universal Bedside Tests to Precision Airway Risk Stratification.](https://europepmc.org/article/MED/42930806)

审核决定：待审核
审核备注：
证据版本：a1a4fd6df627bcc49de394d4734d29d85d908a502a19a6fed820be2007ecd5af

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该叙述性综述主张将困难气道评估从统一床旁筛查转向按表型和预试概率分层的精准风险评估，整合超声、影像和机器学习；第7.2节讨论气道AI模型的肤色、性别、族裔等公平性暴露，并呼吁分层报告。

纳入判断：文章为困难气道风险评估综述，虽明确提及气道AI模型的肤色、性别、族裔等公平性暴露及分层报告建议，但仅作简要列举和通用建议，未提供具体亚组测量、评估框架或缓解方法比较；按综述入选标准，公平性分析不够具体，故不纳入。

限制：为叙述性综述，无原始实验或公平性亚组测量；公平性仅一节简要讨论，未给出气道模型的具体亚组指标、机制验证或缓解方法比较，证据不足以支持纳入。

建议分类：Evaluation

证据：
- algorithm：A deep-learning model using a small number of smartphone photographs of the face and neck
- evaluation：
- fairness：Models that ingest facial images, voice or anthropometry are exposed to a specific and well-documented failure mode.
- groups：skin tone and lighting in facial image datasets; sex differences in neck anatomy and soft-tissue distribution; ethnic variation in craniofacial morphology
- medical：Securing the airway is among the most routine, the most consequential and the most poorly predicted interventions in medicine.

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13706562/fullTextXML)

## p-a3363b572857c391c86e

文章：[Machine Unlearning for Federated Socially Fair k-Means Clustering](https://arxiv.org/abs/2610.13717)

审核决定：待审核
审核备注：
证据版本：2c8765bb74a80f952bbb4ac33218fb6c91e7ceda3af439fa9d60ea11e8115306

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：提出面向联邦社会公平 k-means 的精确机器遗忘方法：按机构与人口组分别构建可复用摘要，服务器按全局组规模加权初始化，并用带保护的公平细化；证明同种子重放可精确复现重训轨迹，并在 Adult、Bank、Credit 与 ACS 数据上测量重放加速、证书失败与公平代价。

纳入判断：方法为通用联邦公平聚类与精确遗忘，虽以医院患者分层为例，但所有实证均为金融与人口普查数据，缺少生物医学/临床任务及医疗场景下的公平性测量，按范围规则排除。

限制：全文实验使用 Adult、Bank、Credit 与 ACS 等非医疗表格数据；医院患者分层仅为动机性举例，未在临床任务或医疗数据上评估公平性与遗忘效果，故不满足医疗算法公平性的纳入条件。

建议分类：In-processing

证据：
- algorithm：exact machine unlearning for federated socially fair
- evaluation：All 810 replay comparisons match fresh training exactly
- fairness：minimize the largest group-average squared distance to the nearest center
- groups：Demographic groups are fixed attributes of records, such as census SEX categories.
- medical：

[分析原文](https://arxiv.org/html/2610.13717v1)

## p-cc8d5c0e4ff2868dbbd2

文章：[Protocol for Conducting a Scoping Review on The Use of AI in Automated Scoring of Short-Answer Questions in Medical Education](https://europepmc.org/article/PPR/PPR1346575)

审核决定：待审核
审核备注：
证据版本：0ab743afc235847b7f9c91d331b8ff191cd9f8995e5ec2e929c9736551e53cd4

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文是一篇范围综述方案，计划梳理医学教育中AI自动评分简答题的模型、评分性能、信效度及公平性比较，采用JBI方法和PCC框架，纳入2015年以来的实证研究。摘要未报告任何已完成的公平性分析或结果。

纳入判断：仅为范围综述方案，未提供具体临床任务或实质性公平性分析；全文仅将公平性列为待考察维度，且未定义受保护群体或实施评估，不满足纳入标准。

限制：仅有摘要，且为研究方案；未给出具体疾病/临床任务、受保护群体、公平性指标或实证结果，无法评估其公平性证据。

建议分类：Not applicable

证据：
- algorithm：machine learning, deep learning, transformer-based models, large language models
- evaluation：
- fairness：compared the scoring performance, reliability, validity, and fairness of AI-based systems with human graders
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1346575)

## p-fb55a16fedc7a47752c1

文章：[Beyond AUROC: External Validation, Calibration, and Explainability of Machine Learning Models for 30-Day Hospital Readmission Using Electronic Health Records—A Rapid Systematic Review](https://europepmc.org/article/PPR/PPR1346087)

审核决定：待审核
审核备注：
证据版本：218320d5810eec359004dc5d7fde6160566cec94d302f2fd4bcb1676824b3170

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该快速系统综述评估EHR 30天再入院预测模型的验证、校准、可解释性与亚组公平性报告情况，发现公平性分析仅占4.5%，并提出超越AUROC的最小评估集。

纳入判断：综述明确针对EHR 30天再入院预测并报告公平性分析仅7项(4.5%)；但摘要只给出报告率，未提供亚组指标、机制或具体公平性框架，也未定义分组属性，故不能建议纳入。

限制：仅摘要；无法确认全文是否对7项公平性分析研究给出亚组指标、偏倚机制或具体评估框架；摘要未定义受保护属性。

建议分类：Evaluation

证据：
- algorithm：machine learning (ML) algorithms predicting 30-day hospital readmission using EHRs
- evaluation：inclusion of 156 studies coded based on their abstracts
- fairness：clinical utility, and subgroup fairness
- groups：
- medical：EHR-based machine learning studies predicting 30-day hospital readmission

[分析原文](https://europepmc.org/article/PPR/PPR1346087)

## p-0ef43e765130077b006e

文章：[Artificial intelligence in chronic kidney disease care: An integrative review of outcomes and sociotechnical factors.](https://europepmc.org/article/MED/43057074)

审核决定：待审核
审核备注：
证据版本：fcf8b1a65f9d056ba9e98094dbb411a1e1210a2dac13ca1a77c4d73bb5eaf8ee

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该整合综述梳理CKD照护中AI技术的临床使用结局及社会技术因素，纳入25项研究，报告患者结局、照护流程、资源使用及社会技术报告不均，并指出公平性等报告不足。未开展CKD场景下的算法公平性分析。

纳入判断：该综述虽聚焦CKD中AI的临床结局，但公平性仅作为报告维度偶然提及，未提供具体的算法公平性分析、亚组评估或机制研究，按要求应排除。

限制：仅有摘要；公平性仅作为社会技术报告维度被一句带过，缺少亚组指标、偏差机制或公平性评估框架；无法据此判断全文是否有更详细公平性分析。

建议分类：Not applicable

证据：
- algorithm：AI-enabled technologies evaluated during clinical use in CKD care
- evaluation：
- fairness：
- groups：
- medical：Chronic kidney disease (CKD) requires ongoing monitoring, treatment adjustment and coordinated care.

[分析原文](https://europepmc.org/article/MED/43057074)

## p-280deca54061942c17e6

文章：[Machine Learning Validation Pipelines: From Tabular Benchmarking to Conformal Calibration and Execution-Grounded Agentic Testing](https://europepmc.org/article/PPR/PPR1370333)

审核决定：待审核
审核备注：
证据版本：92796ffc5b19f0012a22249e6450ca72308df6ba8bf49cf332c9986a3576d876

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出五层机器学习验证流程，涵盖基准测试与泄漏防护、可解释性审计、共形校准、部署前门控及执行级多智能体验证，并以金融ML元分析和临床分诊等高风险场景说明失败模式。

纳入判断：摘要仅在临床分诊等高风险场景中泛泛提及，未针对具体医学任务分析公平性；公平审计与少数群体覆盖结果未与临床亚组或医学评价关联，且为摘要级证据，不能建议纳入。

限制：仅摘要级证据；无法核实全文是否包含具体临床任务的公平性分析；可见元分析聚焦金融ML，临床分诊仅为示例。

建议分类：Multi-stage

证据：
- algorithm：standard k-fold cross-validation and regularized baselines are entirely inadequate
- evaluation：
- fairness：Class-conditional Mondrian conformal calibration answers the Minority Coverage Collapse Theorem
- groups：
- medical：clinical triage, where failures can be devastating

[分析原文](https://europepmc.org/article/PPR/PPR1370333)

## p-b739156d3045cfb0e9ce

文章：[Artificial Intelligence in Neglected Tropical Diseases: Current Applications, Challenges, and Opportunities](https://europepmc.org/article/PPR/PPR1371479)

审核决定：待审核
审核备注：
证据版本：6f6dcb82f243bdd0b91f5f9084819560a6225e100a4a922b9a3ad41b264fb61b

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文是对AI应用于被忽视热带病（NTDs）的系统综述，纳入289项研究，涵盖诊断、预后、监测、暴发预测、治疗监测与药物发现，指出外部验证、前瞻性评估及数据治理、可解释性、公平性等方面存在不足。

纳入判断：此为系统综述，摘要未指明具体NTD疾病或任务，且公平性仅在“数据治理、健康系统整合、可解释性、公平性、可解释性”清单中一带而过，缺乏针对该场景的实质性算法公平性分析（亚组指标、机制或评估框架），符合偶然提及类文献的排除条件。

限制：仅有摘要可读；全文的公平性分析无法核实。摘要中公平性仅作为部署考量之一被列举，未给出具体疾病或任务的亚组指标、偏倚机制或缓解方法比较。

建议分类：Not applicable

证据：
- algorithm：Over 70% of studies employed supervised machine learning or deep learning applied to imaging
- evaluation：
- fairness：
- groups：
- medical：applications in disease diagnosis (40.1%), prognosis (17.7%), surveillance (15.2%)

[分析原文](https://europepmc.org/article/PPR/PPR1371479)

## p-ee87c34c3078786f90ec

文章：[Beyond scales: Artificial intelligence, language, and behavior in suicide risk modeling-a narrative review.](https://europepmc.org/article/MED/43035089)

审核决定：待审核
审核备注：
证据版本：9da18354d5c6ef1a7c0a9b777af7f9d7b7f2f5f59d4c811f2eaa2341ebe08534

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该叙述性综述总结人工智能在自杀想法与行为预测中的多模态应用，涵盖电子健康记录与理赔数据、临床文本自然语言处理、语音与面部行为信号、神经影像及被动传感，并讨论判别与校准、外部验证、类别不平衡和部署伦理，仅泛泛提及算法偏见与公平。

纳入判断：文章为自杀风险人工智能的叙述性综述。摘要虽提及算法偏见与公平，但未针对该临床任务提供具体公平分析、亚组指标、偏见机制或评估/缓解框架，属于偶然提及，未满足详细公平性分析条件。

限制：仅获得摘要，无法核实全文是否包含具体亚组指标、偏见机制或公平性评估与缓解方法；摘要中公平仅作为伦理与实施挑战列出，证据不足以支持纳入。

建议分类：Not applicable

证据：
- algorithm：machine learning, deep learning, and large language models
- evaluation：
- fairness：algorithmic bias and equity
- groups：
- medical：AI-enabled prediction and characterization of suicidal thoughts and behaviors

[分析原文](https://europepmc.org/article/MED/43035089)

## p-a633a59806919d28b53e

文章：[A Qualitative Study of African Americans' Experiences with Healthcare: Developing Cultural Competency Training for Cancer Care.](https://pubmed.ncbi.nlm.nih.gov/42995326/)

审核决定：待审核
审核备注：
证据版本：7da34b3af63bdc7413b898e263e60df87e4642a8863d0359de9724c0907279ff

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究通过30名非洲裔美国人半结构访谈，探讨癌症照护中的就医可及性、文化观念与种族偏见经历，并据此开发文化胜任力模拟教育模块。

纳入判断：虽涉及癌症照护中的种族偏见与健康差异，但研究对象是文化胜任力培训，未评估任何AI/ML算法或算法公平性，故不满足算法与公平性核心标准。

限制：仅有摘要，且为社区定性访谈与教育需求开发，未涉及AI/ML算法、数据集或算法公平性测量。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Individual semi-structured interviews using vignettes and open-ended questions
- fairness：
- groups：African American (AA) community experiences
- medical：Racial disparities in cancer care persist

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42995326/)

## p-17659a43f827691e5628

文章：[Reinforcement Learning Under Runtime Confounding: Policy Learning and Off-Policy Evaluation](https://arxiv.org/abs/2610.40056)

审核决定：待审核
审核备注：
证据版本：6e4b25f99ada49212f82081863ddf51a59e652007a623794bfa7c5540fea3a25

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：提出运行时混杂下的强化学习框架，包括可部署策略学习、半参数有效离策略评估及运行时遗憾差距检验；以临床决策支持等为例，但未开展医学任务或公平性实证评估。

纳入判断：文章是通用强化学习统计方法，医疗仅作动机示例；未针对具体医学任务，也未提出或测量算法公平性，且无实证评估，不符合纳入标准。

限制：全文为统计理论和方法贡献，仅以临床决策支持作动机示例，未定义具体医学任务、保护群体或公平性指标，也无实证或测量评估。

建议分类：In-processing

证据：
- algorithm：develop policy learning algorithms under runtime-confounding
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://arxiv.org/html/2610.40056v1)

## p-1f719bc172ff6ac3b1d8

文章：[Etiology and Anatomical Level of Lower-Limb Amputations in Two Iranian Referral Hospitals: A Retrospective Record-Based Study.](https://pubmed.ncbi.nlm.nih.gov/42940562/)

审核决定：待审核
审核备注：
证据版本：d0e9045df28b9de008f8e66f69946e41ba3ede2c9f5b1430312db27d36cb6f44

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：回顾性分析伊朗两家医院229例下肢截肢记录，描述创伤、血管病和感染等病因及截肢平面，并发现年龄与医院差异；未涉及AI/ML模型或算法公平性评估。

纳入判断：研究使用ICD编码规则重建病因并比较医院间差异，但未评估AI/ML算法，也无算法公平性、偏倚或缓解问题，故排除。

限制：仅有摘要；研究为临床流行病学描述，未报告任何模型、亚组公平性指标或缓解措施。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：In an adjusted major-versus-minor model, older age and treatment at Al-Zahra Hospital were associated with major amputation
- fairness：
- groups：descriptive differences by age, etiology, and hospital
- medical：characterize demographic, etiologic, and anatomical patterns of lower-limb amputation

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42940562/)

## p-2511def0b4e92255227b

文章：[Exploring Racial Bias in Rating Facial Attractiveness Among Artificial Intelligence Platforms.](https://europepmc.org/article/MED/42906598)

审核决定：待审核
审核备注：
证据版本：da9a461ec7aa23f2a510a5a8c0cc3ce47cc1b9364126a0cdca722ef44f61f536

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究用五个商业AI面部分吸引力评分平台，对Black、White、Latino、Asian四组各30张标准化女性图像打分，发现White组平均分最高(8.18)、Black组最低(6.91)，组间及平台间差异显著，提示评分可能偏向Eurocentric面部特征。

纳入判断：摘要明确报告了种族分组、多平台评分对比与显著性检验，属于任务特异的算法公平性审计，五项证据均可满足；但证据等级仅为摘要，无法核实全文方法学细节，按规则不得直接建议纳入。

限制：仅有摘要：缺少平台版本、图像标准化流程、统计模型与效应量细节；刺激为AI生成的库存图而非真实患者照片，未评估对临床决策或患者结局的下游影响。

建议分类：Evaluation

证据：
- algorithm：evaluating AI-generated facial attractiveness scores across ethnic groups using multiple AI-based rating platforms
- evaluation：White females received the highest average score (8.18), followed by Asian (7.79), Latino (7.72), and Black (6.91)
- fairness：assign differing attractiveness scores across ethnic groups despite standardized image characteristics
- groups：women from diverse ethnic backgrounds (Black, White, Latino, and Asian)
- medical：when consulting with patients who seek cosmetic enhancement based on societal standards

[分析原文](https://europepmc.org/article/MED/42906598)

## p-31196b8a7558e691e421

文章：[What Language Models Add to Healthcare-Equity Rankings, and What They Could Have Known](https://arxiv.org/abs/2610.38056)

审核决定：待审核
审核备注：
证据版本：2569b8322564d73ea96a3f10c9faa27dd3174fb35faf34d8b2871899109c3753

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文评估语言模型文本表示与筛选特征对2020–2025年美国医疗保健股票排名的影响，并检验训练截止日期相关的前视/后见偏差，非临床算法公平性研究。

纳入判断：研究任务是医疗保健股票收益排名，不是生物医学/临床任务；也未提出或测量算法公平性、亚组差异或缓解方法，故不属于本综述范围。

限制：全文为金融选股与LLM前视偏差评估；未涉及临床任务、敏感人群分组、算法公平性指标或缓解措施。

建议分类：Not applicable

证据：
- algorithm：The system ranks US healthcare and life-science equities monthly over 2020–2025 from a contest-selected random forest
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://arxiv.org/html/2610.38056v1)

## p-5e14e8326ab1970479b8

文章：[The Ethics of Autonomous Clinical AI: Shifting From Model Accuracy to Model Impact.](https://pubmed.ncbi.nlm.nih.gov/42913471/)

审核决定：待审核
审核备注：
证据版本：17a1786ff3e3352a39a277a0cc5748a3c0ddc7ed6c656e7d7da72adf05acd920

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文为观点/评论文章，主张自主临床AI的伦理评估应从模型准确率转向完整诊疗路径结局，并转述Nichol等人的九项试验建议，包括预设亚组表现、随访照护与模型变更等义务。全文未针对任何具体疾病或临床任务提供实质性的算法公平性分析，也无亚组指标或实证测量。

纳入判断：属评论/观点类文章，仅笼统提出伦理治理与“亚组表现”义务等一般性建议，既未指明具体医学疾病或任务，也未提供该情境下的实质性公平性分析（亚组指标、机制或评估框架），且无实证/测量评估，符合附带提及类排除标准。

限制：仅有摘要级证据：未指明具体疾病或临床任务，无亚组公平性指标、偏倚机制或缓解方法比较，也无实证测量结果；摘要未说明全文是否含这些内容，但摘要本身不足以支持纳入。

建议分类：Not verified

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42913471/)

## p-79ee704c380a3242315c

文章：[Evaluating four consumer artificial intelligence chatbots on smartphone dermatology images: diagnostic accuracy, the contribution of clinical context, and skin-tone equity](https://europepmc.org/article/PPR/PPR1365867)

审核决定：待审核
审核备注：
证据版本：3a30568071ea2474e94f206ac0d6ce2a81f17955f5184f0c27b11bf581bf4d4f

模型建议：hold

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究在3,005例SCIN智能手机皮肤图像上评估四款消费级AI聊天机器人，比较单图、多图、图像加临床背景及纯文本四种条件下的诊断准确率，并按Fitzpatrick肤色分层检验公平性，发现表现最好的模型存在浅色与深色皮肤间的准确率差异。

纳入判断：摘要显示这是皮肤科诊断任务，实际测评了四款聊天机器人，并在Fitzpatrick肤色分层下报告准确率差异，五项标准均有摘要支持；但证据层级仅为摘要，按规则不能suggest_include，需获取全文核实后决定。

限制：仅有摘要证据，缺少全文方法细节、模型版本与提示设置、统计方案及代码或数据可用性信息；无法核实完整评估设计与公平性分析的细节。

建议分类：Evaluation

证据：
- algorithm：GPT-5.4-Pro, Claude-Opus-4.6, Gemini-3.1-Pro and Grok-4.20-Reasoning were evaluated
- evaluation：3,005 cases from the crowdsourced Skin Condition Image Network (SCIN) dataset with physician-validated ground truth
- fairness：For top-1 accuracy, Fitzpatrick skin tone disparity was significant only for Grok
- groups：56.0% light versus 45.1% dark skin
- medical：Patients increasingly upload smartphone photographs to consumer artificial intelligence (AI) chatbots seeking dermatological diagnoses

[分析原文](https://europepmc.org/article/PPR/PPR1365867)

## p-941651f4cc3f2fc37b20

文章：[Comparative evaluation of training strategies using partially labelled datasets for segmentation of white matter hyperintensities and stroke lesions in FLAIR MRI.](https://pubmed.ncbi.nlm.nih.gov/42659784/)

审核决定：待审核
审核备注：
证据版本：ffd0c8544f424a9efbe5594f524c5649338bec5bc9872cd170654275fdfb6078

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究在FLAIR MRI上比较六种利用部分标注数据训练联合白质高信号（WMH）与缺血性卒中病灶（ISL）分割模型的策略，汇总2052例MRI体数据，发现伪标签策略效果最佳，可稳定分割WMH并检出多数FLAIR阳性ISL。

纳入判断：摘要聚焦部分标注数据下的分割训练策略比较，属方法学与性能评估；全文未涉及算法公平性、亚组差异、敏感属性或缓解措施，仅为普通性能研究，故排除。

限制：仅有摘要，缺乏各策略的详细方法与统计结果；未涉及任何人群分组、公平性指标或偏差分析，也未报告代码与数据获取方式。

建议分类：Not applicable

证据：
- algorithm：we systematically evaluated six accessible strategies for training a joint WMH and ISL segmentation model using partially labelled data
- evaluation：We aggregated privately held and publicly available datasets to curate a large-scale cohort of 2052 MRI volumes
- fairness：
- groups：
- medical：deep learning models to automatically segment and differentiate these pathologies

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42659784/)

## p-a27cbdea53664651a807

文章：[AI-Supported Semiquantitative CT Characterization of COVID-19 Pneumonia Across SARS-CoV-2 Wild-Type, Alpha, and Delta Variants and Its Association with Clinical Parameters.](https://europepmc.org/article/MED/43028567)

审核决定：待审核
审核备注：
证据版本：bfea29623f987b4310a6b4b7f8b834662408a5ec9967c1b39c30a2b7fc4a27b3

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该回顾性单中心研究使用AI CT肺炎分析原型对255例COVID-19患者的肺部阴影进行半自动定量，比较野生型、Alpha和Delta变异组的CT衰减、体积及COVID-19概率，并分析其与临床和实验室参数的相关性。

纳入判断：研究虽使用AI算法并比较不同病毒变异组的定量输出，但未提出算法公平性、差异或编码问题，也未按敏感属性进行公平性测量，核心公平性证据缺失。

限制：研究仅按病毒变异分组，未涉及种族、性别、年龄等敏感属性或算法公平性指标，也未评估偏倚机制、差异表现或缓解方法，因此不满足算法公平性纳入标准。

建议分类：Evaluation

证据：
- algorithm：a deep learning algorithm intended exclusively for research purposes and not for clinical use
- evaluation：global mean opacity attenuation differed significantly among the wild-type, Alpha, and Delta groups
- fairness：
- groups：subgroups defined by SARS-CoV-2 wild-type/variant determined by whole-genome sequencing or genotypic sequence analysis
- medical：255 patients with pulmonary CT datasets and a confirmed SARS-CoV-2 diagnosis

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13762066/fullTextXML)

## p-d4ccac7ce879b6812b7a

文章：[Impact of Unrestricted Artificial Intelligence Scribe Deployment in a Single Health System on Clinician Workload and Productivity : A Quality Improvement Study.](https://europepmc.org/article/MED/42932880)

审核决定：待审核
审核备注：
证据版本：7fdba2165829fa29f659799e43ee7609cbe6b8f84fd3dae955254d631b145df1

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究为单家医疗系统的回顾性质量改进研究，采用中断时间序列分析，评估902名门诊临床医生启用环境AI病历记录助手（Heidi）后文档负担的变化，并按使用强度（未使用者、低使用者、高使用者）分组比较。结果显示启用后记录活跃时间小幅下降、病历长度增加，且高使用者变化更明显；当日与工作时间外病历完成率及wRVU均无差异。

纳入判断：研究评估AI病历记录助手对临床文档工作量与效率的影响，患者人口学特征仅作为混杂因素调整，未提出算法公平性、群体差异或编码偏倚问题，也未按敏感属性做亚组公平性度量。虽属医学任务并有实证评估，但缺少公平性核心要素，故排除。

限制：仅有摘要，缺少全文方法、亚组定义与补充材料；观察性设计存在未测量混杂，且无法区分AI生成与医生撰写的病历。文中未按患者或临床医生的敏感属性开展算法公平性分析。

建议分类：Not verified

证据：
- algorithm：To evaluate the association between AI scribe (Heidi) enrollment and documentation burden
- evaluation：Retrospective quality improvement study using an interrupted time series (ITS) indexed on each clinician's enrollment month
- fairness：
- groups：
- medical：Ambient artificial intelligence (AI) medical scribes may reduce documentation burden and clinician burnout

[分析原文](https://europepmc.org/article/MED/42932880)

## p-7b736b8d23744e060972

文章：[Green AI for Telehealth.](https://europepmc.org/article/MED/42969789)

审核决定：待审核
审核备注：
证据版本：8d2741c9f99ac9d1acf321fa7fcf2b5e93c454192c3c26be9255259e8462a892

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：文章讨论加拿大远程医疗中的绿色AI，提出IoT-fog-cloud资源感知架构，并主张评估临床性能、资源使用、组织适配与可持续性，同时将公平可及列为负责任AI的考量之一。

纳入判断：摘要属于远程医疗绿色AI的泛论，仅一次提及公平可及，没有具体医学任务下的算法公平性分析、亚组指标或实证测量，按附带提及规则排除。

限制：仅有摘要；未给出具体疾病或临床任务、具体AI算法、亚组定义或公平性指标，也没有实施的实证评估。公平性仅泛泛提及。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42969789)

## p-014d28297e30dc61bb6f

文章：[Translation and Cross-Cultural Adaptation of the Chronic Rhinosinusitis Control Test for Global Use.](https://pubmed.ncbi.nlm.nih.gov/42262654/)

审核决定：待审核
审核备注：
证据版本：01cb4175062c6f25b58908ed4cd057a8071d079a568396a619b507df66846575

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

正式版本线索：[Translation and Cross‐Cultural Adaptation of the Chronic Rhinosinusitis Control Test for Global Use](https://doi.org/10.1002/alr.70194)

中文概述：该研究采用生成式人工智能（ChatGPT、Copilot、Perplexity 等大语言模型）与人工语言学家协作的混合流程，将慢性鼻窦炎控制测试（CRCT）翻译并跨文化适配为37种语言，并对各步骤译文的准确性与有效性进行定性与定量评估，作者称此举可促进数据公平。

纳入判断：本文是患者报告结局量表的翻译与跨文化适配研究，属语言验证工作。虽使用大语言模型并提及“data equity”，但未提出算法公平性/差异性问题，未定义群体属性，也未开展公平性测量，不满足公平性与群体两条证据标准，属偶然提及公平的文献，故排除。

限制：仅有摘要：未定义任何受保护群体或亚组，未报告公平性/差异性指标、偏倚测量或缓解方法；“data equity”只是泛泛表述，缺乏针对算法公平性的实证分析。

建议分类：Not applicable

证据：
- algorithm：forward translations were performed with three large language models (LLMs)
- evaluation：
- fairness：
- groups：
- medical：psychometrically validated to measure chronic rhinosinusitis control

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42262654/)

## p-0f29043f64118c8a4f09

文章：[Fluorescence Encoding-Enabled Multiplexed Droplet Digital Recombinase Polymerase Amplification-CRISPR/Cas12a Assay for Rapid Screening of Lower Respiratory Tract Infection-Associated Bacterial Pathogens.](https://pubmed.ncbi.nlm.nih.gov/42937587/)

审核决定：待审核
审核备注：
证据版本：e5339a2e01b9761686c85549a962a4b9657779e3ef95058716c5853b9703aed4

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文提出荧光编码多重液滴数字RPA-CRISPR/Cas12a检测平台，结合机器学习解码，实现下呼吸道感染相关细菌病原体多重定量，并用临床样本验证与培养结果的一致性。

纳入判断：研究为病原体核酸检测方法学开发，虽使用机器学习解码并开展临床一致性验证，但未提出算法公平性问题，也无群体定义、亚组比较或偏差测量，故不属于医学算法公平性研究。

限制：仅提供摘要，缺少方法细节与公平性相关分组、差异或缓解分析；所述“编码”为荧光信号编码，并非人口学属性编码。

建议分类：Not applicable

证据：
- algorithm：machine learning-assisted decoding pipeline
- evaluation：
- fairness：
- groups：
- medical：lower respiratory tract infection-associated bacterial pathogens

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42937587/)

## p-16d932da8047442b4c63

文章：[Worldwide survey on artificial intelligence in occupational therapy.](https://pubmed.ncbi.nlm.nih.gov/42585570/)

审核决定：待审核
审核备注：
证据版本：e2c404de91a116b283b8bdf4cc7a80d69a49ac61e6b47dfef508a5d061773730

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：摘要报告了一项全球职业治疗师调查，了解其对人工智能的知识、使用情况和态度；研究未评估具体算法、群体公平性指标或缓解措施。

纳入判断：该文是职业治疗中人工智能应用态度调查，未涉及具体AI/ML算法评估、明确受保护群体或公平性测量，且证据级别仅为摘要，不满足纳入标准。

限制：仅有摘要，缺少问卷细节、亚组公平性指标和算法层面评估；公平仅作为定性主题出现。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42585570/)

## p-2857d68b3a9af48583e2

文章：[Excessive Weight Loss with Zepbound Is Associated with Higher Rates of Adverse Events, Electrolyte Imbalances, and Hospitalization than Moderate Weight Loss](https://europepmc.org/article/PPR/PPR1346607)

审核决定：待审核
审核备注：
证据版本：eac610e393b1c32a9c0000e93ad7c5142d378d6fff43a90622605a5eba7b25ed

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：研究利用去标识化EHR比较Zepbound首年减重≥30%与5%-15%者的不良事件，发现过度减重与更高不良事件、住院及电解质异常相关；LLM仅用于事件提取，未评估算法公平性。

纳入判断：研究为Zepbound减重幅度的药物安全性观察分析，使用EHR和LLM提取不良事件，但未评估算法公平性，也未定义敏感属性或公平性亚组，故不符合纳入标准。

限制：摘要仅提供观察性药物安全性比较，未涉及医疗AI/ML算法的公平性、敏感属性或亚组公平性测量；不能作为算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：The rate of any weight loss-attributable adverse event was significantly higher
- fairness：
- groups：
- medical：we compared 1,039 Zepbound initiators (1.7%) whose first-year weight loss reached ≥30%

[分析原文](https://europepmc.org/article/PPR/PPR1346607)

## p-29e9e0f870fc81357c24

文章：[Nursing, Artificial Intelligence, and the Algorithmic Time Machine: Safeguarding Techno-Temporal Justice for Person-Centred Care.](https://europepmc.org/article/MED/42952232)

审核决定：待审核
审核备注：
证据版本：32e4b53e4730ac58d43de821e12e675bf1dcb5745277b228362f16dcbd659a9d

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：论文提出“算法时间机器”与“技术-时间正义”概念，讨论AI如何通过分类、预测、推荐和压缩重塑护理时间与护士能动性，并主张以时间敏感框架评估AI是否支持公平、人性化、以人为中心的照护。

纳入判断：文章讨论护理时间与AI治理概念，未建立具体医学任务，也未提供算法公平性测量、亚组比较或缓解评估，属一般性伦理/公平倡议，故排除。

限制：仅摘要；属概念/话语性论文，未针对具体疾病或临床任务，无算法、数据、亚组指标或实证公平性评估，无法核验详细公平分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42952232)

## p-2a0b7223fe49d5fe9cd3

文章：[Decision-to-Delivery Interval and Perinatal Outcomes Following Emergency Cesarean Section in Southern Ethiopia](https://europepmc.org/article/PPR/PPR1340265)

审核决定：待审核
审核备注：
证据版本：c767599ce3cfe7c244f921d7f64a833bdfeae350c4c67493225c775e461f35ac

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究为埃塞俄比亚某医院急诊剖宫产决策至分娩间期（DDI）的横断面调查，纳入284例产妇，用描述统计与二元logistic回归分析DDI延长（>30分钟）的相关因素及其与围产结局（如1分钟Apgar评分）的关联。

纳入判断：研究主题为急诊剖宫产时间间期与围产结局的临床流行病学分析，全文不含AI/ML算法，也不存在算法公平性、群体差异测量或缓解问题；虽提及既往剖宫产等因素，但属临床危险因素而非公平性分组分析，故不符合纳入标准。

限制：仅有摘要，无全文方法与数据细节；研究为单中心观察性设计，未涉及任何AI/ML模型、算法公平性定义、群体公平性指标或偏倚缓解措施，也没有算法层面的评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：assess the decision-to-delivery interval and its associated perinatal outcomes

[分析原文](https://europepmc.org/article/PPR/PPR1340265)

## p-3646728625d955d7bac3

文章：[Navigating barriers: The journey of women surgeons in Türkiye Across decades.](https://pubmed.ncbi.nlm.nih.gov/42648007/)

审核决定：待审核
审核备注：
证据版本：5dc82dc99955e6b190b540d8cb0347d4c1a906f88bc6160ef6bebacf80f3d6af

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：文章为土耳其女性外科医生职业历程的视角评论，描述历史先驱、性别刻板印象、骚扰与晋升障碍，以及机构改革建议。未涉及医学人工智能算法、模型公平性评估或缓解方法。

纳入判断：该文为外科领域性别平等视角评论；虽提及女性代表性不足和偏见，但没有评估任何医学算法、模型或算法公平性指标，属于医疗队伍不平等而非算法公平研究，故排除。

限制：仅有摘要，且主题为外科人力资源与性别不平等，不含AI/ML算法、亚组性能比较、公平性指标或实证算法评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：women cluster in specialties with predictable schedules, whereas prestige-intensive surgical fields remain male dominated
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42648007/)

## p-6ddbcaab5d3278c65a4a

文章：[Americans' views about artificial intelligence in healthcare: 2022-2026.](https://europepmc.org/article/MED/42965045)

审核决定：待审核
审核备注：
证据版本：ab14d3b0195d5e1c87723ce75b1e6726a6fd32cdda547ee4b53a62b6c20610b6

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文汇总2022—2026年16项美国全国民调，描述公众对医疗AI的了解、信任与使用情况，例如部分人因无力负担或难以获得诊疗而转向AI健康问答，并讨论行政与临床角色的区分及隐私、监督方面的担忧。全文属民意调查的叙述性综合，未评估任何具体医疗AI算法，也未测量亚组公平性。

纳入判断：该文是对美国公众对医疗AI态度的民调综述，不涉及具体疾病或临床任务，也未对任何AI/ML算法开展评估，缺乏算法公平性或偏差的测量设计、分组协议与实证结果；其“公平”讨论指向医疗服务可及性而非算法公平，属偶然提及，故按规则排除。

限制：证据全部为受访者自报的民调快照，不同机构问卷与抽样不一致，作者亦自述存在措辞与顺序效应。文中未涉及具体模型、亚组性能差异或算法偏差度量，所提“公平”仅为就医可及性层面的宏观推断。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13721133/fullTextXML)

## p-750bf3589b72386d1cf9

文章：[Real-time peri-operative data integration and clinical decision support: an open interoperable platform for patient data.](https://pubmed.ncbi.nlm.nih.gov/42298974/)

审核决定：待审核
审核备注：
证据版本：c399f02790df67511a2ba981d4e8f1a92d2faaaf5f657d84c25a44e409625f37

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：介绍一个开放、可互操作的围手术期数据平台，基于 Apache Kafka 实时整合监护仪、注射泵、呼吸机、脑电与检验数据，采用本地存储与匿名化治理；自2019年已收录118915名患者、77张手术室或重症监护床位的波形与数值数据，支持实时临床决策与多中心研究。

纳入判断：该文为数据平台与基础设施工程报告，未评估任何人工智能或机器学习算法的公平性，未定义受保护群体或开展亚组比较，也无差异、偏倚编码或缓解方法的实证测量；仅在结论中泛泛提及临床公平，属偶然提及，按规则排除。

限制：仅有摘要，未提供算法模型细节、公平性指标或亚组比较；结尾的“clinical equity”属泛化表述，不足以构成算法公平性研究证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Modern intensive care units (ICU) and operating rooms (OR) generate vast quantities of physiological data

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42298974/)

## p-7a7241c81548105604e8

文章：[Identifying patients at elevated risk of stroke after transcarotid artery revascularization.](https://pubmed.ncbi.nlm.nih.gov/42323112/)

审核决定：待审核
审核备注：
证据版本：176a7b4ecb4403668dc9779552db677990c39ed2c736f80b3bb8404378a560a6

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：利用VQI数据（61,111例TCAR）以CART和随机森林识别院内卒中相关因素，并按症状状态、P2Y12依从性和支架数量分组，报告调整后卒中风险差异。

纳入判断：研究为TCAR术后卒中风险因素分析，使用CART/随机森林但未提出或评估算法公平性，未按敏感属性或公平指标进行亚组比较。

限制：仅有摘要，无法核实全文；研究聚焦卒中风险因素，无公平性定义、敏感属性分组或偏倚/缓解评估。

建议分类：Not applicable

证据：
- algorithm：Two complementary machine learning methods were used to identify factors associated with stroke after TCAR.
- evaluation：These groups had in-hospital stroke risks of 0.74%, 1.60%, 1.85%, and 3.96%, respectively.
- fairness：
- groups：
- medical：in-hospital stroke after TCAR

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42323112/)

## p-873f8add702e04deb02e

文章：[Artificial Intelligence in Longevity Research: From Molecular Clocks to Interventional Geroscience](https://europepmc.org/article/PPR/PPR1357971)

审核决定：待审核
审核备注：
证据版本：39cb590d693d1edc8e759a1812296895090c332f45420b906ff0bd14d5da185f

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：叙述性综述梳理AI衰老时钟（表观基因组、蛋白质组、视网膜、心电、MRI等）在年龄估计、预后关联、干预反应与替代终点验证四类属性上的证据，提出证据阶梯与转化链，并指出校准报告不足与因果推断缺口。

纳入判断：该文为叙述性综述，虽涉及AI衰老时钟这一任务，但公平性仅泛化提及（祖源与社会因素混杂），未提供具体情境下的亚组度量、偏倚机制或缓解比较，属偶然提及；且仅有摘要，故排除。

限制：仅有摘要；未见针对具体任务报告的亚组公平性指标、偏倚机制分析或缓解方法比较，公平性仅以“祖源与社会因素混杂”一句泛化带过，无可引用证据片段。

建议分类：Not applicable

证据：
- algorithm：Machine learning has accelerated senolytic and mTOR-pathway candidate nomination
- evaluation：
- fairness：
- groups：
- medical：Deep-learning clocks across epigenomic, proteomic, retinal, electrocardiographic, and magnetic resonance imaging (MRI) modalities

[分析原文](https://europepmc.org/article/PPR/PPR1357971)

## p-883b35cbccb829e5d82d

文章：[Retinal imaging for cerebrovascular risk stratification: evidence, limitations, and practical thresholds for the ophthalmologist.](https://pubmed.ncbi.nlm.nih.gov/42390572/)

审核决定：待审核
审核备注：
证据版本：b78e889dfe91fcc78b3af10da278fb903db3a45a63b4d48fdf8619f884a80e41

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该叙述性综述评估视网膜影像（眼底、血管几何、OCT/OCTA及AI oculomics）用于脑血管风险分层的证据成熟度与临床转化局限，并提出面向眼科医生的模式化框架。

纳入判断：文章虽涉及视网膜AI与脑血管风险，但未提出算法公平性问题，缺少定义群体、亚组测量或公平性分析，故排除。

限制：仅有摘要；未报告算法公平性、亚组比较、偏倚机制或缓解方法，也无具体公平性评测指标、数据或结果。

建议分类：Not applicable

证据：
- algorithm：artificial intelligence (AI) and oculomics
- evaluation：Evidence was appraised with emphasis on study design, population size, confounding control, external validity
- fairness：
- groups：
- medical：inform clinical decisions about cerebrovascular risk

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42390572/)

## p-8c77e8f6e91acd395a98

文章：[Detecting Language-Related Disparities in Spiritual Care Using Artificial Intelligence.](https://pubmed.ncbi.nlm.nih.gov/42902576/)

审核决定：待审核
审核备注：
证据版本：fb1eb2d7fbbd744be9ff7629f4ebd6295ebb4ddfb486010d4e53f66b4f39c244

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该摘要报告一项基于电子健康记录的研究，使用自然语言处理识别灵性照护文档，并用逻辑回归分析患者语言与正式灵性照护获取及时间的关系，发现非英语使用者获取率更低、支持更晚。

纳入判断：研究用NLP测量语言相关灵性照护获取差异，属于医疗不平等观察，未评估AI/ML算法在不同群体中的公平性、编码或缓解措施；且仅有摘要，不能建议纳入。

限制：仅见摘要，缺少模型构建、验证、亚组性能及算法公平性评估细节；研究关注的是照护获取差异，而非AI系统本身的公平性。

建议分类：Evaluation

证据：
- algorithm：Natural language processing identified spiritual care documentation
- evaluation：Logistic regression assessed associations between patient language and spiritual care access and timing.
- fairness：
- groups：Non‑English speakers had 59% lower odds of receiving formal spiritual care
- medical：spiritual care, a domain largely documented in unstructured clinical notes

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42902576/)

## p-9320409dfec5a4ff0cd3

文章：[A multinational pharmacoepidemiology atlas of prescription medication associations with all-cause mortality across six population cohorts](https://europepmc.org/article/PPR/PPR1367355)

审核决定：待审核
审核备注：
证据版本：107ef6007b4ea137229af5d383491aba6278b67d0b54e2de9a96211d6e969231

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该研究在英、美、芬兰、香港和日本六个队列（893万人、14.9亿条处方）中，用时依Cox模型筛查处方药与全因死亡的关联，发现VZV疫苗、阿托伐醌-氯胍等少数药物呈负相关，并提示健康使用者偏倚不能完全解释VZV疫苗信号。

纳入判断：本文为药物流行病学关联筛查研究，虽具临床任务与统计建模，但不存在明确的算法公平性/偏倚问题、受保护群体划分或公平性评测，仅将社会经济因素作为混杂变量调整，属于无关的偶然提及，故排除。

限制：仅有摘要；未涉及任何算法公平性、亚组差异、敏感属性或缓解方法的分析，社会经济因素仅作为混杂调整变量出现。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：associations with all-cause mortality using time-dependent Cox models in six cohorts

[分析原文](https://europepmc.org/article/PPR/PPR1367355)

## p-9d5bd94b760b9bad9a79

文章：[Participation in an integrated telemedicine and psychological counseling program and psychological outcomes in patients with HCC: a multicenter retrospective cohort study.](https://europepmc.org/article/MED/42955103)

审核决定：待审核
审核备注：
证据版本：7d3007698cfe2a514629f0b148300b0dc378bc912b0c8c65f1727f53ddde1cdf

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究评估HCC患者参与整合远程医疗与心理咨询项目的累计程度与12个月心理结局的关联，发现较高参与度与抑郁、焦虑、睡眠和痛苦评分较好相关，但疾病特异性生活质量较低；为多中心回顾性队列，非算法公平性研究。

纳入判断：该文为HCC远程医疗/心理咨询参与度与心理结局的临床队列研究，未评估任何AI/ML算法的公平性、偏倚机制、亚组差异或缓解措施，故不符合纳入标准。

限制：仅有摘要；未涉及AI/ML算法、公平性定义、受保护群体或亚组公平性评估；不能据此判断算法偏倚或缓解效果。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：patients with hepatocellular carcinoma (HCC)

[分析原文](https://europepmc.org/article/MED/42955103)

## p-9ebb0211c5729745c2dd

文章：[Modifications of diagnosis-related group payment for hospital care: a systematic review](https://europepmc.org/article/PPR/PPR1351285)

审核决定：待审核
审核备注：
证据版本：ed4dc67ea1a61208002baa473ebf598b2c7a62b6e8d0cecbf75c2cacebd46e51

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：系统综述评估DRG支付方式修改（主要为捆绑支付）对患者结局、质量、利用、成本和公平性的影响；发现捆绑支付与较低住院总费用相关，但公平性证据有限。该文不属于医学AI/ML算法公平性研究。

纳入判断：文章评估DRG支付改革而非医学AI/ML算法；仅笼统提及公平性证据有限，缺乏针对特定疾病或任务的算法公平性分析，故排除。

限制：仅有摘要；未涉及AI/ML算法或算法公平性评估，公平性仅作为支付政策结局之一被笼统提及，证据有限。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1351285)

## p-a5f1ff2ceb89d9e47906

文章：[Health Care Delays, Mental Health Care, and Discrimination among US Sexual and Gender Minority Adults: Intersectional Analysis of State-level Policies.](https://europepmc.org/article/MED/42913961)

审核决定：待审核
审核备注：
证据版本：e0f836bc413cb88384b261d0537fbb0e7e92be530c5ddc3095838d56048f9862

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：研究分析美国性与性别少数成年人中，州级政策包容性与就医延迟、心理健康服务使用和医疗歧视的关联，采用交叉性多层分析；未评估任何AI/ML算法或算法公平性。

纳入判断：该文为健康服务与政策公平性流行病学研究，未涉及AI/ML算法、其公平性测量或缓解，故不符合算法公平性范围。

限制：仅有摘要；非算法研究，无模型、预测任务或算法公平性评价，无法支持医学算法公平性纳入。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：intersectional strata explained somewhat more variation in DMS score (2.42%)
- fairness：
- groups：racial equity, sexual orientation inclusiveness, and gender inclusiveness
- medical：delays in health care, mental health service use, and discrimination in medical settings

[分析原文](https://europepmc.org/article/MED/42913961)

## p-a74fb8515fa29c366d7b

文章：[Feasibility and equity in the assessment of parent-child interactions: Lessons from three approaches.](https://europepmc.org/article/MED/42956222)

审核决定：待审核
审核备注：
证据版本：d1c1bcb692036bf3413a79e572d8d02ef69601031bb5d52b99efa38dd4729973

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文比较三种亲子互动观察与编码方法（视频会议实时编码、智能手机App结合AI支持编码、可穿戴设备家庭自然情境录像）的可行性、成本、生态效度与公平可及性，并讨论临床与伦理影响，样本量分别为114、27、27。

纳入判断：摘要聚焦亲子互动观察方法的可行性、成本与参与公平性，属发展心理学评估方法比较；虽提及AI支持编码，但未构成对AI/ML算法的公平性/偏倚测量问题，也无疾病或临床任务及分组算法性能比较，属偶然提及公平性的非算法公平研究。

限制：仅有摘要：未提供任何算法层面的分组公平性指标、偏差测量或缓解实验；'equity'主要指参与可及性与多样性，而非模型公平性评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42956222)

## p-ac7d03b2cfb060f1819b

文章：[Report-Derived Labels, an Image Teacher and the Gap to Expert Labels in Knee MRI: An Analysis of One Entry to the RSNA 2026 Knee Abnormality Detection Challenge](https://arxiv.org/abs/2610.40708)

审核决定：待审核
审核备注：
证据版本：5f9838e3ad79820152d3e873de0da9d5043a8ffd75982f47731bc708acaa59c6

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：分析RSNA 2026膝MRI挑战中报告标签、图像教师及混合训练目标与专家标签的一致性，并评估2.5D ResNet50、共现发现秩校正及性别/扫描仪校正；发现更好目标未带来明确模型增益，报告参考可能奖励报告习惯。

纳入判断：文章分析报告弱标签与专家标签的一致性、教师蒸馏及后处理校正，属标签噪声与评测研究；虽触及性别和扫描仪分组，但未提出或评估算法公平性、未报告群体性能差异，故排除。

限制：全文可用，但核心并非公平性研究：没有明确的公平性/差异问题、敏感群体公平指标或缓解评估；性别和扫描仪分析服务于标签与参考可靠性。因此不能按公平性论文纳入。

建议分类：Evaluation, Post-processing

证据：
- algorithm：a 2.5D ResNet50 trained on the report labels alone scored 0.877
- evaluation：we report every comparison against two references with different strengths
- fairness：
- groups：Sex is present in 94.6% of training studies, the manufacturer and model in all
- medical：knee MRI studies with their DICOM series and reports

[分析原文](https://arxiv.org/html/2610.40708v1)

## p-ad34653fafb8bef10710

文章：[From Prediction to Action: Population Health World Model for Digital Medicine](https://arxiv.org/abs/2610.24662)

审核决定：待审核
审核备注：
证据版本：b1fa0854ca16618ea07fae66a71839a6dd9cc31e9ac9a7bb6f76f0d45711fcc2

模型建议：exclude

渠道核查：pending；正式发表身份追踪仍处于待重试、身份复核或冲突状态，不能由历史关联覆盖。

发现通道：recall

中文概述：文章提出数字医学的人群健康世界模型（PHWM），主张从预测转向行动，统一建模潜在健康状态、干预、约束与反馈，并提出表征学习、跨尺度干预智能及验证、公平与治理三项能力。

纳入判断：该文为泛数字医学观点文章，虽提及公平和子群，但未命名具体疾病或任务，也未提供实质性算法公平分析、指标或实证评估；按规则排除，而非列为相关。

限制：全文为观点/框架文章，未针对具体疾病或任务开展实证；公平仅作为验证维度泛泛提及，缺乏定义子群、公平指标、偏差机制或实验评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：readmission, hospitalization, treatment escalation, or which alert should fire next

[分析原文](https://arxiv.org/html/2610.24662v2)

## p-c26def1ad664f90b88d2

文章：[Prognostic prediction models for psoriatic arthritis in psoriasis: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42312903/)

审核决定：待审核
审核备注：
证据版本：20ff83441254f202b802227447ce36cad0a1aca639435f8ede4a3c767b2a0036

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该系统综述纳入15项研究、490个预后模型，评估银屑病患者发生银屑病关节炎的风险预测模型之预测性能、偏倚风险与报告质量；摘要未涉及算法公平性、亚组差异或缓解措施。

纳入判断：该综述虽针对银屑病关节炎这一具体临床任务，但摘要只评估预测性能、偏倚风险和报告质量，没有算法公平性、亚组差异或缓解分析，不满足综述纳入所需的详细公平性证据。

限制：仅有摘要，未提供全文；未报告公平性/亚组分析、敏感属性定义或模型代码/数据可用性，无法进一步核验。

建议分类：Not applicable

证据：
- algorithm：Fifteen studies were included after full-text screening, comprising of 490 models
- evaluation：systematically identify and evaluate the predictive performance, risk of bias and reporting quality
- fairness：
- groups：
- medical：estimate the risk of psoriatic arthritis in patients with psoriasis

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42312903/)

## p-ca3d70e3725b143a1044

文章：[The Prevalence and Clinical Characteristics of Atrial Fibrillation and Reflux Esophagitis Among Individuals Undergoing Health Checkups.](https://europepmc.org/article/MED/42875209)

审核决定：待审核
审核备注：
证据版本：1918ea14e3d573b66a6b61104488c7598c4df80428b2e4caa3f62286907de0d4

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究为健康体检人群的横断面流行病学分析，纳入5205名接受胃镜检查的成年人，考察房颤与反流性食管炎的关联；结果显示房颤组食管炎患病率更高，但多因素logistic回归校正性别、年龄等因素后关联不再独立，提示由共同混杂因素解释。

纳入判断：该文为房颤与反流性食管炎的临床流行病学关联研究，全文摘要未见AI/算法被评估，也未提出算法公平性、差异或测量问题，仅有常规流行病学混杂校正；不满足医学任务之外的算法与公平性判据，故排除。

限制：仅提供摘要，无法核查全文方法与数据；研究不涉及任何AI/机器学习模型，也不涉及算法公平性、亚组差异或偏倚评估，仅有性别、年龄等临床协变量调整。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：AF was observed in 36 participants (0.7%)

[分析原文](https://europepmc.org/article/MED/42875209)

## p-cdb91e4a7fe04fb245d1

文章：[Digital Transformation of Rehabilitation Care: A Systems-Based Narrative Review and Conceptual Framework for Connected, Intelligent, and Hybrid Rehabilitation.](https://europepmc.org/article/MED/43028647)

审核决定：待审核
审核备注：
证据版本：e241c2315fa7b016e96dc6982a327d063ec73827a5cdd5940e720c38af3c6203

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为康复领域数字化（远程监测、人工智能、居家与混合照护）的叙事综述，提出由互联、智能、混合三类能力构成的系统框架，并强调互操作性、数据治理、公平与持续评估等社会技术条件。

纳入判断：综述未针对特定疾病或康复任务提供实质性算法公平性分析（无亚组指标、机制或评估框架），公平仅作治理要素附带提及，按规则属附带提及类，排除。

限制：仅提供摘要：无具体疾病或康复任务的公平性分析，无亚组指标、偏倚机制或缓解方法比较；“equity”仅出现在治理条件清单中一次，属附带提及。

建议分类：Not applicable

证据：
- algorithm：intelligent rehabilitation transforms these data into interpretation, prediction, feedback, personalization, and adaptation
- evaluation：
- fairness：
- groups：
- medical：Digital transformation is reshaping rehabilitation through remote monitoring, artificial intelligence

[分析原文](https://europepmc.org/article/MED/43028647)

## p-d336159d7b8908016928

文章：[reFLASH: a proof-of-concept meta-analytic framework to validate surrogate endpoints in the absence of randomized clinical trial data.](https://pubmed.ncbi.nlm.nih.gov/42641770/)

审核决定：待审核
审核备注：
证据版本：b29d17124f231dcde028a2bcf73fd641025bf2c2ca1ce6dd315bee9117f0f637

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：提出 reFLASH 元分析框架：将 12 项滤泡性淋巴瘤随机试验拆分为单臂试验并重新配对，用 IPTW 模拟随机化，评估 30 个月完全缓解对无进展生存期的替代终点效度。属于肿瘤学统计方法研究，不涉及医学算法公平性。

纳入判断：该文虽评估一种统计建模框架并报告经验结果，但未提出或测量医学算法公平性、群体差异、编码偏倚或缓解措施，不符合公平性研究纳入标准。

限制：仅有摘要；研究聚焦替代终点验证与配对策略稳健性，未报告公平性定义、受保护群体、亚组差异或偏倚测量。

建议分类：Not applicable

证据：
- algorithm：We propose a proof-of-concept strategy that creates synthetic comparative evidence
- evaluation：Trial-level surrogacy between CR30 and PFS was quantified
- fairness：
- groups：
- medical：validating surrogate endpoints traditionally requires individual patient data

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42641770/)

## p-dfd76ee4553e36909d88

文章：[Predicting PANSS symptoms in schizophrenia spectrum disorders using speech only: an international, multi-centre, computational secondary analysis across multiple languages.](https://pubmed.ncbi.nlm.nih.gov/42991136/)

审核决定：待审核
审核备注：
证据版本：cebb4d02e52ddd901b1059e14a0ad5c7a35e891a381500232e14c7381e493121

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该国际多中心计算二次分析汇总10国453例精神分裂症谱系障碍患者的语音，将录音切分为6664段，比较16种算法预测8个PANSS条目，并按年龄、性别、教育程度和症状严重度做偏倚检查。预训练多语言嵌入表现最佳；除男性N4准确率较低外，未见年龄、性别或教育偏倚，但高症状严重度下性能下降。

纳入判断：摘要显示明确的临床任务、算法评估、按年龄/性别/教育/症状严重度的偏倚检查及RMSE实证结果，符合入选标准；但证据仅限摘要，无法核验详细公平性方法与结果，按规则不能suggest_include，暂予hold。

限制：仅摘要证据：未提供偏倚检查的具体分层指标、效应量、阈值、置信区间或任何缓解措施，无法核验公平性分析深度；也未报告代码或数据。

建议分类：Evaluation

证据：
- algorithm：we compared 16 algorithms in separate item-specific models
- evaluation：We found no bias by age, sex, or education, aside from reduced N4 accuracy in males
- fairness：Best model per item underwent bias checks for age, sex, education, and symptom severity.
- groups：for age, sex, education, and symptom severity
- medical：patients with schizophrenia spectrum disorders

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42991136/)

## p-eb717c28000374405fc3

文章：[Prognostic factors associated with outcomes after knee cartilage repair across different procedure types: a systematic review.](https://europepmc.org/article/MED/42902365)

审核决定：待审核
审核备注：
证据版本：8670778c98bb8a1c0d3cce9eb53d3c5ac44c1b36c2d142c70b99c53865287ee9

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该系统综述按手术类型与疾病背景分层，汇总膝关节软骨修复术后预后因素（年龄、性别、BMI、病变大小、既往手术等），并开展偏倚风险与队列重叠核查；全文未涉及算法公平性议题。

纳入判断：研究问题为软骨修复的临床预后因素，而非医疗算法公平性；缺少被评估的算法、明确的公平性/差异测量问题及相应实证评估，故不纳入。

限制：全文为预后因素系统综述，无AI/ML算法被评估，缺少公平性/差异测量、亚组公平性指标或缓解方法；仅提及部分原研究的机器学习特征排序，且明确不将其等同于调整后效应。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：prognostic factors associated with outcomes after knee cartilage repair

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13682157/fullTextXML)

## p-ef2c73c3a8803f2d0255

文章：[Short- Versus Long-Course Radiation in Total Neoadjuvant Therapy for Locally Advanced Rectal Cancer: A Propensity-Matched National Cancer Database Analysis.](https://pubmed.ncbi.nlm.nih.gov/42598830/)

审核决定：待审核
审核备注：
证据版本：e66813a1007ce1a57cb2832adb9afa033742dd076ae71a951bad5fbdc52d0dd0

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究利用国家癌症数据库比较局部晚期直肠癌全程新辅助治疗中长程与短程放疗的总生存及病理结局；倾向评分匹配后生存无差异，长程组淋巴结降期率较高。未涉及AI/ML算法或公平性分析。

纳入判断：摘要为直肠癌长/短程放疗的倾向评分匹配比较，未评估AI/ML算法、公平性、受保护群体或差异指标，不符合医学算法公平性纳入标准。

限制：仅有摘要，无法评估全文细节；且摘要显示为治疗方式比较，不含算法公平性、受保护群体差异或缓解措施分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Adults with clinical stage II or III rectal adenocarcinoma

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42598830/)

## p-f70258d0543a394a6653

文章：[Antidopaminergic Medications and Clinical Outcomes in Huntington Disease: Evidence From the PROOF-HD Placebo-Controlled Trial.](https://europepmc.org/article/MED/42912861)

审核决定：待审核
审核备注：
证据版本：6642ba0515afcfbc4eec3c62563f09b50a02de463f57bffa620c5cfee2569cc4

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究基于PROOF-HD安慰剂组247例早期亨廷顿病患者，比较抗多巴胺药物暴露与否及剂量/类别与78周临床结局轨迹的关联，发现暴露组cUHDRS、TFC、认知和运动下降更快，属药物流行病学分析。

纳入判断：本文是亨廷顿病安慰剂组的事后药物暴露分析，使用统计模型比较用药组结局，不评估AI/ML算法，也没有算法公平性、差异或缓解问题，故排除。

限制：全文为药物暴露与临床结局关联研究；未涉及AI/ML模型、敏感属性公平性评估或算法偏倚缓解，不能作为医学算法公平性文献。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：we performed a post hoc analysis of placebo arm data
- fairness：
- groups：participants were categorized based on ADM use: On-ADMs
- medical：Huntington disease (HD) is a progressive neurodegenerative disease

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13714897/fullTextXML)

## p-fa3ca2ed93703292ee6b

文章：[Striving for Equity in Cystic Fibrosis Research: Perspectives from Black and Hispanic/ Latino(a) Individuals with CF.](https://pubmed.ncbi.nlm.nih.gov/42896705/)

审核决定：待审核
审核备注：
证据版本：6d753cd7736a16c07af3c32a18e56cf9732c9f222d475b2721c7d8aeaec8a253

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究通过半结构化访谈，探讨黑人及西班牙裔/拉丁裔囊性纤维化患者对临床研究的看法、参与障碍与促进因素，并提出以社区支持和信息透明为核心的纳入改进方案。研究聚焦临床研究代表性不足的社会文化因素，未涉及任何算法或AI模型。

纳入判断：研究主题为囊性纤维化临床研究参与的健康公平与定性访谈，不涉及任何AI/ML算法、模型编码差异或算法公平性评估，属于健康差异研究而非医学算法公平性研究，故不纳入。

限制：仅有摘要，缺少访谈提纲、编码框架与完整主题细节；研究本身不含算法、数据集或模型评估，无法提供算法公平性证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Twenty PwCF were interviewed from 2024 to 2025.
- fairness：
- groups：who identify as Black/African American race and/or Hispanic/Latino(a) ethnicity
- medical：Black and Hispanic people with cystic fibrosis (PwCF) experience worse health outcomes.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42896705/)

## p-102f2c250012d5cd6b69

文章：[Association of bilingual language use with brain age: MRI evidence from bilinguals, translators, and interpreters.](https://pubmed.ncbi.nlm.nih.gov/43041269/)

审核决定：待审核
审核备注：
证据版本：c8b0e766fc5046460c5ec540e87144971cca28539cfb3c617fdfc6e7ab1182af

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：研究用六个预训练脑龄模型比较105名捷克语-英语双语者（非专业双语者、笔译和同传）的年龄校正脑龄差，未发现经FDR校正的组间差异；结果强调脑龄推断对模型选择和年龄偏差校正敏感。

纳入判断：研究评估双语职业经验与MRI脑龄差距的关联，虽使用预训练模型并比较组间差异，但未提出算法公平性、偏倚机制、敏感属性差异或缓解问题，属于非公平性神经影像研究。

限制：证据仅来自摘要，未提供完整模型与统计细节；研究问题是双语经验与脑龄差异，不包含算法公平性评估。

建议分类：Evaluation

证据：
- algorithm：Brain age was estimated using six pretrained models.
- evaluation：Group differences and age × group interactions were tested across models with FDR correction.
- fairness：
- groups：44 non-professional bilinguals, 35 translators, 26 simultaneous interpreters
- medical：Bilingualism has been linked to cognitive reserve and later onset of Mild Cognitive Impairment

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43041269/)

## p-15ed546d8e15d79fd402

文章：[Longitudinal pre-diagnostic blood samples predict osteoporosis risk.](https://pubmed.ncbi.nlm.nih.gov/42871651/)

审核决定：待审核
审核备注：
证据版本：e8d8818c07b7f8722fffba9ad65a5ba48d1ec30cd22e7e5b9fdeaf8d7e457c7d

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该研究基于丹麦献血者队列的538份纵向血浆代谢组样本（99例prediagnostic骨质疏松患者与99名匹配对照），比较横断面与纵向建模的预测性能：纵向LASSO轨迹模型AUC为0.67–0.76，优于横断面的0.57–0.63，最佳模型独立验证AUC为0.70。全文摘要未涉及算法公平性、亚组差异或偏差机制的分析。

纳入判断：医学任务与机器学习模型（LASSO、随机森林）明确，但研究目标是提高骨质疏松预测的纵向采样信息量，未提出或测量任何算法公平性问题：无受保护群体定义、无亚组性能比较、无偏差或缓解分析，属于公平性偶提之外的普通预测建模研究，不满足纳入标准。

限制：仅有标题与摘要，缺少全文方法、代码与数据细节；匹配对照未按敏感属性分组，无任何亚组公平性指标、偏差机制或缓解实验证据。

建议分类：Not applicable

证据：
- algorithm：least absolute shrinkage and selection operator (LASSO) logistic regression and random forest
- evaluation：
- fairness：
- groups：
- medical：99 pre-diagnostic osteoporosis cases and 99 matched controls in the Danish Blood Donor Study

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42871651/)

## p-28adaf06b29241ce8db3

文章：[Continual learning in oncology AI: A framework for safe clinical translation.](https://pubmed.ncbi.nlm.nih.gov/43063946/)

审核决定：待审核
审核备注：
证据版本：dc5d85d4bb7aae7fb24ac345ead5417fa7a69f8f92f886964fde2013a2b0efae

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文综述肿瘤学AI中的持续学习方法，讨论灾难性遗忘、校准与重训等转化障碍，并提出包含亚组安全、校准稳定性等六项安全转化标准。公平性仅作为持续学习临床转化的一项风险被提及。

纳入判断：该文为持续学习综述，虽提及代表性不足人群的隐性退化和亚组安全，但未命名具体疾病或任务，也未提供该场景的详细算法公平性分析，属于附带性提及，按规则排除；摘要级证据也不能建议纳入。

限制：仅有摘要，无法核实全文是否针对具体疾病或任务提供详细的公平性分析；摘要未给出具体亚组指标、实验或代码信息。

建议分类：Not verified

证据：
- algorithm：review CL methods and their oncology applications
- evaluation：
- fairness：hidden regressions in underrepresented populations
- groups：
- medical：oncology applications, predominantly in imaging and pathology

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43063946/)

## p-517e6927ff88a49bc260

文章：[Relapse of ANCA-Associated Vasculitis With Kidney Involvement: A Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/43044903/)

审核决定：待审核
审核备注：
证据版本：c3cda9c8050090e412955c3a14df251699db953473cdef60b45148f737260e80

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该研究为法国多中心回顾性队列，分析ANCA相关性血管炎肾受累患者的复发模式、危险因素及复发与肾衰竭/死亡的关联，并评估现有复发风险评分的区分度；未涉及算法公平性、亚组差异或偏倚缓解。

纳入判断：研究聚焦临床复发预测与风险评分区分度，未提出或评估算法公平性问题，缺少定义群体、亚组发现或公平性测量，不符合医学算法公平性范围。

限制：仅有摘要，无法核查全文方法、亚组分析或公平性指标；摘要未报告任何按人群属性分层的算法公平性评估或偏倚干预。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43044903/)

## p-636203d18db253767e77

文章：[How did data sharing evolve in the decade since the FAIR Principles?](https://arxiv.org/abs/2611.20319)

审核决定：待审核
审核备注：
证据版本：4ab5f40b93c13b8f2195eec3a4e571db4b44603d247a6430005edbac7b973925

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：对2011–2025年PMC开放获取子集680余万篇生物医学论文进行纵向分析，提取数据可用性声明、仓储链接与JATS4R合规性，并考察学科、地区、资助方、开放获取层级及作者性别相关的数据共享差异。

纳入判断：本文分析生物医学文献的数据可用性声明与FAIR实践，按性别、地区等描述数据共享差异，但未评估任何医疗AI/算法，也未提出算法公平性测量、偏倚机制或缓解问题，故排除。

限制：证据为全文，但研究属科研数据共享与开放科学计量，并非医疗算法或临床任务；性别由姓名推断，且未涉及算法公平性评估或缓解。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：large-scale longitudinal analysis of over 6.8 million biomedical articles from the PubMed Central Open Access Subset
- fairness：
- groups：female first-authored articles’ scores declined more than male first-authored ones’
- medical：

[分析原文](https://arxiv.org/html/2611.20319v1)

## p-85640a44163a7e495a79

文章：[Prognostic Factors for Survival in ICI-Treated NSCLC: An Umbrella Review of Evidence Certainty and Clinical Relevance.](https://europepmc.org/article/MED/43033040)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-a3bb94685f1bec630254

文章：[Attitudes Towards Risks and Benefits of Using Generative Artificial Intelligence (GenAI) for African American Family Members of a Person with Dementia.](https://europepmc.org/article/MED/43041993)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-cf956d481a5b46de9c2b

文章：[Artificial Intelligence as a Catalyst for Value-Based Care in Vascular Disease.](https://europepmc.org/article/MED/43035227)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-f0405d6bf007e5f2b22c

文章：[Orbital morphometry on computed tomography for sex estimation: A systematic review and meta-analysis.](https://pubmed.ncbi.nlm.nih.gov/43057131/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-73c317778f11b9f63bbd

文章：[Operationalizing fair AI in healthcare: a scoping review of bias mitigation, monitoring, auditing, and governance strategies.](https://europepmc.org/article/MED/42948540)

审核决定：待审核
审核备注：
证据版本：03ee48ef2f39e2a41c857915d95d00d1df1f229085a1afeaed1e1b290217cf1a

模型建议：exclude

渠道核查：pending；缺少可核验的 journal_title/journal_issns/conference 字段，保留待核验。

中文概述：该文为范围综述，梳理2022–2026年文献与监管文件，归纳医疗AI生命周期中的偏见缓解策略（重加权、重采样、合成数据、联邦学习、对抗去偏、反事实公平）、公平性指标选择、审计与部署后持续监测，并提出机构—国家—超国家三级治理框架与可操作建议。覆盖影像、电子病历等举例，但以治理与流程为主，未针对具体疾病或临床任务开展公平性实证。

纳入判断：属综述，但未指明具体疾病或临床任务，公平性分析停留在跨领域的策略、指标与治理层面（如预测均等、机会均等、人口统计均等的通用描述），不符合综述入选所需的“特定任务＋该情境下实质性公平性分析”双重条件；亦无亚组实证测量，故不作为相关文献推荐。

限制：证据仅为全文叙述性综述：检索限定每库前200条、仅英文开放获取、未做质量或偏倚风险评估，作者亦承认可能存在EU监管框架偏向。全文未给出任何针对特定疾病或任务的亚组指标、数据集或实证测量结果，仅有文献计数与策略罗列。

建议分类：Multi-stage

证据：
- algorithm：the challenges associated with the deployment and monitoring of fairness in AI systems for healthcare purposes
- evaluation：
- fairness：What bias mitigation strategies are reported in the literature to support fair AI in healthcare?
- groups：reducing its reliance on sensitive attributes (e.g., race or gender) or related proxies
- medical：The rapid development of AI technologies for healthcare brings with it an increased awareness of ethical and fairness concerns.

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13711374/fullTextXML)

## p-5730bd1f390c5e421069

文章：[Toward Evidence-Based Human-Centered AI and Human-AI Interaction: A Cross-Domain Systematic Review](https://europepmc.org/article/PPR/PPR1349059)

审核决定：待审核
审核备注：
证据版本：5ad1638b7438052dbd04b59ef9797f9d0f73e91e93ba11460981fd4d074d509f

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文是一篇跨领域系统综述，整合44项关于以人为本AI（HCAI）与人机交互（HAX）的实证研究，梳理测量方法、框架类别、AI角色（人类主导/协作/AI主导）及各领域结论；指出客观任务表现多有改善，而信任、满意度、负荷等主观结果差异较大，仅在“其他领域”一句提及公平性。未聚焦任何具体医学疾病或临床任务。

纳入判断：属跨领域人机交互综述而非医学算法公平研究：未指明具体医学疾病或临床任务，公平性仅在罗列其他领域关注点时被一次提及，缺少子组指标、机制或缓解方法等实质分析，符合“偶然提及”排除标准；摘要级证据也不足以建议纳入。

限制：仅有摘要级证据，无法核查全文是否包含具体医学任务或实质性算法公平分析。摘要中公平性仅作为跨领域罗列出现一次，未给出子组指标、偏倚机制或缓解方法比较；亦无数据集、代码或模型细节。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1349059)

## p-8217ed4660a11d38095e

文章：[Bias in Medical AI in Relation to Patient Empowerment and Digital Equity: Scoping Review.](https://europepmc.org/article/MED/43002731)

审核决定：待审核
审核备注：
证据版本：daf81a2665c2d679dfb4dc88879677d4a8f55fd96990fdd95b4d63e5e606c5a9

模型建议：related

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该范围综述综合22项研究，将医疗AI偏见视为技术、社会、设计与结构多层现象，并映射其与患者赋权各维度、数字鸿沟及交叉性劣势的关系；指出赋权常由参与、信任等代理指标推断，去偏策略多为建议而少实证评估。

纳入判断：该文为范围综述，系统梳理医疗AI偏见与患者赋权、数字公平，并以神经重症治疗决策支持为例讨论种族、语言与社会经济地位交叉劣势；但整体不聚焦单一临床任务，且去偏策略未获实证验证，故列为相关而非建议纳入。

限制：证据来自异质性较高的22项研究，未做方法学质量或偏倚评估；整体并非单一疾病或任务下的原始实证公平性研究，去偏干预未经验证，赋权多为间接编码。

建议分类：Evaluation

证据：
- algorithm：machine learning (ML) models, large language models (LLMs), and rule-based systems
- evaluation：Across the 22 included studies, bias was predominantly described as a multilayered sociotechnical phenomenon
- fairness：algorithmic bias can lead to systematically different outcomes across population groups
- groups：race, gender, age, socioeconomic status, and language proficiency
- medical：medical AI, understood as the application of AI-based systems within health care settings

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13747314/fullTextXML)

## p-b297260bff58f92dec74

文章：[Ethical dimensions of artificial intelligence in nursing and midwifery: A systematic review and responsible AI toolkit.](https://europepmc.org/article/MED/42981742)

审核决定：待审核
审核备注：
证据版本：ae8dcaae2d7046c6eafaff38704814de518486764f6e31b72986d6357beea287

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文为系统综述，梳理护理与助产领域人工智能的伦理维度，归纳出维护人性、安全性、自主与问责、透明与隐私、公平正义、队伍准备六大主题，并提出负责任AI工具包。公平仅作为其中一个主题被概括提及，未针对具体临床任务给出亚组指标、偏差机制或缓解方法比较。

纳入判断：属伦理类系统综述，仅在主题层面笼统提及算法偏见与公平，未锚定任何具体疾病或临床任务，也未提供实质性公平性分析（亚组指标、机制或缓解方法比较），仅属附带提及，按规则排除；且证据仅限摘要，不能据此建议纳入。

限制：仅有摘要可用，未见全文方法、检索结果与各主题的详细证据；公平相关论述停留在“算法偏见与公平实施”的概括层面，无具体任务、数据集、分组属性或量化结果。

建议分类：Not applicable

证据：
- algorithm：Artificial intelligence (AI) techniques, models, and tools are increasingly used in healthcare
- evaluation：
- fairness：concentrated on algorithmic bias and equitable implementation
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42981742)

## p-d7ca83ef5595247c6b0e

文章：[Sexually transmitted co-infections as biological modifiers of HPV-driven cervical carcinogenesis: a systematic integrative review.](https://europepmc.org/article/MED/43016629)

审核决定：待审核
审核备注：
证据版本：6bc89c302b596dcbc14d3faa526fb630febc102af4d572c4b5fbc5ac7be45fa8

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文系统综述CT、HSV-2和HIV与HPV共感染对宫颈癌发生的影响，评估流行病学、机制与GRADE证据，并提出分层筛查建议；未涉及AI/ML算法或算法公平性。

纳入判断：文章为宫颈癌STI共感染的临床系统综述，虽涉及人群差异和证据分级，但未评估任何AI/ML算法，也未提出算法公平性、偏倚测量或缓解问题，故不符合纳入标准。

限制：证据来自系统综述与观察性研究，无AI/ML模型、算法公平性指标、敏感属性分层或缓解实验；无法据此判断算法偏倚。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Cervical cancer affects approximately 660,000 women annually

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13751401/fullTextXML)

## p-2308c78840b3881bc14d

文章：[Smoking and dementia risk: an updated systematic review and meta-analysis of 61 prospective cohort studies and implications for tobacco control.](https://pubmed.ncbi.nlm.nih.gov/43034842/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-b7ac23993de63dc9a3e9

文章：[Machine learning-based risk prediction of hepatocellular carcinoma in patients with chronic hepatitis B: current evidence and future directions.](https://europepmc.org/article/MED/43064890)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-5a21404654990f140f62

文章：[AI for Postoperative Pain and Opioid Stewardship in Pediatric Surgery: A Systematic Review.](https://pubmed.ncbi.nlm.nih.gov/42998968/)

审核决定：待审核
审核备注：
证据版本：b9e405565381fe77f97635a29104f092813768009de0893953f1bd73dc24b39a

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文系统综述AI在儿科术后疼痛与阿片类药物管理中的应用，涵盖自动疼痛评估、家庭监测、阿片长期使用预测及PCA相关预测，指出多数研究仅内部验证且缺乏临床影响证据，并呼吁外部验证与公平性评估。

纳入判断：摘要明确为儿科术后疼痛与阿片管理综述，但公平性仅作为未来评估建议出现，无具体亚组分析、机制或公平性方法，属于偶然提及，故排除。

限制：仅见摘要；未提供任何亚组公平性指标、偏倚机制或缓解方法；公平性仅在结论中作为未来需求被提及。

建议分类：Not applicable

证据：
- algorithm：AI, machine learning, deep learning, computer vision, multimodal sensing
- evaluation：
- fairness：
- groups：
- medical：pediatric postoperative pain management and opioid stewardship

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42998968/)

## p-00a0602fd722007f0f24

文章：[Artificial Intelligence for sepsis prediction: A review of real-world clinical implementation.](https://europepmc.org/article/MED/43008935)

审核决定：待审核
审核备注：
证据版本：6ea5150aa613022a9e44a05018ebb56fb28caaf01a564178757b324f1a301d6b

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

正式版本线索：[Artificial Intelligence for sepsis prediction: A review of real-world clinical implementation](https://doi.org/10.1016/j.cmi.2026.10.036)

中文概述：该文为脓毒症AI预测工具临床实施的叙述性综述，总结其对结局与流程指标的影响，并列举数据异质性、警报疲劳、信任、伦理、算法偏倚和公平等推广障碍。

纳入判断：摘要明确脓毒症预测任务并提及算法偏倚，但公平内容仅为障碍列举，缺少可核验的详细分析；需全文才能决定综述是否满足详细公平分析条件。

限制：仅提供摘要；公平/偏倚仅作为实施障碍词出现，未见亚组指标、机制或具体评估框架，无法判断全文是否有详细公平分析。

建议分类：Not verified

证据：
- algorithm：AI systems can support dynamic sepsis risk prediction
- evaluation：
- fairness：ethical concerns, algorithmic bias
- groups：
- medical：AI sepsis prediction tools

[分析原文](https://europepmc.org/article/MED/43008935)

## p-38be472f7cef8bd16935

文章：[Toward a Common Language for Trustworthy AI in Healthcare](https://europepmc.org/article/PPR/PPR1345874)

审核决定：待审核
审核备注：
证据版本：b093eb9d00591dcb86425a6875222548a352960bfa9eb944a8cab9c926065b66

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文对2015—2025年675篇医疗可信AI文献开展范围综述，用主题综合与语义分析考察可解释性、公平性、偏见等八个概念的定义与重叠，发现概念混用与不一致，并提出统一框架与研究缺口。

纳入判断：摘要表明这是一篇泛医疗可信AI概念综述，公平性与偏见仅是八个概念之一，未指明具体疾病或任务，也未给出针对该情境的详细公平性分析（亚组指标、机制或干预比较），故不满足综述纳入的两项条件。

限制：仅有摘要；未见具体疾病或临床任务，也缺少受保护群体、亚组指标或公平性缓解方案等细节，无法确认全文是否包含任务特异性算法公平性分析。

建议分类：Not applicable

证据：
- algorithm：Artificial Intelligence (AI) is increasingly integrated into healthcare
- evaluation：
- fairness：validation, <italic>Fairness</italic> , and <italic>Bias</italic>
- groups：
- medical：supporting tasks involving diagnosis, prognosis, treatment, and monitoring

[分析原文](https://europepmc.org/article/PPR/PPR1345874)

## p-220173ecbe71aeffc6a2

文章：[Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-7177fc75cf105ecbb6ba

文章：[Artificial Intelligence for Cardiovascular Health Behavior Change: A Narrative Review of Patient-Facing Tools.](https://pubmed.ncbi.nlm.nih.gov/42978091/)

审核决定：待审核
审核备注：
证据版本：cde54f9974aba7192e72cf241d3f855f2a94935cb79d32329a335f2382640cd6

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：一篇叙述性综述，检索2010至2025年10个数据库，纳入19项评估面向患者的心血管健康教育及行为改变AI工具（对话代理、机器学习、强化学习）的实证研究，按AHA Life's Essential 8框架归纳其对高血压、糖尿病、心衰等的作用，并讨论接触强度、健康素养与数字健康决定因素。

纳入判断：该文虽点名心血管疾病具体任务，但属叙述性综述，摘要中公平性仅为泛泛提及与治理性建议，未见亚组公平性指标、偏差机制或缓解方法比较，属附带提及；摘要层面也不足以支撑纳入。

限制：仅有摘要，无全文方法、亚组指标或补充材料；摘要未给出任何按种族、收入、年龄或城乡划分的算法公平性量化结果，公平性仅以“limited reporting on safety and equity”等概括性表述及治理建议出现。

建议分类：Not applicable

证据：
- algorithm：AI-enabled interventions such as conversational agents, machine-learning models, and reinforcement-learning systems
- evaluation：
- fairness：
- groups：racial/ethnic minoritized populations, low-income communities, older adults, and rural residents
- medical：Cardiovascular disease (CVD) is the leading cause of death in the United States

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42978091/)

## p-de1d8f363bb788b48fb8

文章：[Bias Mitigation Across the Healthcare Artificial Intelligence Lifecycle: A Structured Narrative Review](https://europepmc.org/article/PMC/PMC13662775)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-0cddb9f876c8091ae26a

文章：[AI-Enabled Patient Profiling for Personalized Nursing Care and Health Support: Scoping Review.](https://europepmc.org/article/MED/42955065)

审核决定：待审核
审核备注：
证据版本：eae4082cea2d05212dbe6ea1ddde8cb62434268e4fabf1403fe2205273a736b1

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：一项范围综述，纳入61项研究，梳理AI患者画像（机器学习、聚类、深度学习、NLP、LLM、数字孪生等）在个性化护理与健康支持中的应用，指出多数研究仅评估算法性能、可行性与可用性，对公平性、可操作性与长期结局评估不足。

纳入判断：该文为护理领域AI患者画像的范围综述，覆盖范围宽泛，未锚定具体疾病或任务；公平性仅出现equity的笼统提法，无亚组指标、机制或缓解方法分析，属附带提及；且仅有摘要证据，不满足综述类“具体任务+实质公平性分析”的双重条件。

限制：仅有摘要：未指明具体疾病或具体护理任务，未报告亚组指标、公平性测量方法、偏倚机制或缓解措施比较；公平性仅在结果与结论中各被笼统提及。

建议分类：Not applicable

证据：
- algorithm：Common AI approaches included machine learning, clustering, deep learning, natural language processing
- evaluation：
- fairness：
- groups：
- medical：support personalized nursing care and health support

[分析原文](https://europepmc.org/article/MED/42955065)

## p-1113bff507608d38b282

文章：[Sense of belonging among underrepresented medical students: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/43012928/)

审核决定：待审核
审核备注：
证据版本：6363a5b9c9f55d2b3003e869fcbdd5fe64d0f14da9c2bf4ab942d8fc449e0fe9

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为范围综述，系统梳理代表性不足医学生的归属感研究：检索六个数据库并纳入41篇文献，归纳出归属感的阻碍因素、后果、保护性努力与院校促进因素四大主题，主张将归属感视为核心教育成果。全文聚焦医学教育中的社会心理与制度文化问题，未涉及任何AI/ML算法或算法公平性评估。

纳入判断：主题为医学教育中代表性不足学生归属感的范围综述，属社会科学与教育研究；缺少被评估的AI/ML算法、算法公平性/偏差测量问题、明确分组或亚组发现协议以及算法层面的实证评估，不符合纳入标准。

限制：仅有摘要，但摘要已清楚显示研究对象为医学生归属感的定性/综述性证据，不含算法、数据集、亚组性能指标或缓解方法；无法也无需据此推断算法公平性内容。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43012928/)

## p-3bf01c8442618790c2a0

文章：[Effectiveness of AI-Driven Digital Mental Health Interventions and Their Implications for Health Service Delivery: A Systematic Review and Meta-Analysis (2013–2025)](https://europepmc.org/article/PPR/PPR1347001)

审核决定：待审核
审核备注：
证据版本：85dabc04e16a2e27b81149e646b74f5b759f0a62c51728f9d0e82e5a86d7835f

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文为系统综述与荟萃分析，汇总2013—2025年AI驱动数字心理健康干预（含App、远程医疗、AI增强CBT、对话式智能体）对抑郁、焦虑与情绪结局的疗效，并汇总AUC、敏感度、特异度等算法性能指标。共纳入385项研究，报告中等程度的症状改善，但异质性和验证、公平性、实施等结局报告不一致。

纳入判断：该综述虽点明抑郁、焦虑等具体精神疾病任务，但公平性仅作为“报告不一致”清单中的一项附带提及，摘要未给出任何亚组指标、偏差机制、公平性评估框架或缓解方法比较，未构成针对该场景的实质性算法公平性分析，属偶发提及，且摘要级证据不足以提出纳入建议。

限制：仅提供摘要，缺少具体亚组指标、偏差机制或缓解方法的细节；公平性仅在结论中以“equity”一词附带提及，未见明确的公平性研究问题、受保护属性定义或公平性测量结果，无法据此评估其是否完成实质性的算法公平性分析。

建议分类：Not verified

证据：
- algorithm：algorithmic performance was summarised using area under the curve (AUC), sensitivity, and specificity
- evaluation：
- fairness：
- groups：
- medical：moderate improvements in depression, anxiety, and mood outcomes compared with comparator conditions

[分析原文](https://europepmc.org/article/PPR/PPR1347001)

## p-3c4b3e103c0522d5e458

文章：[Decision-Supported Collaborative Care for Gestational Diabetes: A Narrative Review of Development Pathways and Evaluation in Routine Clinical Practice.](https://pubmed.ncbi.nlm.nih.gov/42953578/)

审核决定：待审核
审核备注：
证据版本：8e878c4a342662c412035d83e749027a88afc2cd7d5baa1459a8d9842fc1a514

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该叙述性综述将妊娠期糖尿病决策支持协同照护界定为以工作流为中心的照护模式，梳理将血糖与临床情境连接到可解释决策逻辑及角色分工（分诊、升级、闭环反馈）的系统组件，提出从可操作场景到安全护栏与工作流整合的开发路径，以及结合临床结局、流程、实施与系统层面的多维评价方案，并讨论告警负担、角色责任、数据治理隐私与数字公平等推广障碍。

纳入判断：文章为妊娠期糖尿病数字照护模式的叙述性综述，具备明确临床任务，但摘要中公平性仅以"数字公平"一词出现在障碍列举中，未定义分组属性、未给出亚组指标、偏差机制或缓解评估，属偶然提及；且仅有摘要证据，无法判断是否有任务特定深入公平性论述，故排除。

限制：仅有摘要，缺少检索与筛选细节、纳入研究清单及结果数据；摘要未呈现任何亚组公平性指标、偏差机制或缓解方法比较，"数字公平"仅作为推广障碍之一出现，无法核实是否存在任务特定的实质性公平性分析。

建议分类：Not applicable

证据：
- algorithm：links glucose and clinical context to interpretable decision logic
- evaluation：
- fairness：
- groups：
- medical：Gestational diabetes mellitus (GDM) requires frequent glucose monitoring

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42953578/)

## p-430b36001e0294414011

文章：[Generative Artificial Intelligence in Clinical Practice: How Should Rheumatologists Evaluate and Monitor Emerging Tools?](https://europepmc.org/article/MED/42901770)

审核决定：待审核
审核备注：
证据版本：2f70f0bdc88eb0c66c93be74a57fc9177dc6c3be9c1759a2ba4e124baa27df57

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：这是一篇关于风湿科生成式AI应用的叙述性综述，提出以“情境复杂性”和“对患者照护的影响程度”两维度构成的评估与监测框架，讨论工作流收益、临床有效性、安全、隐私、治理与实施，并建议按风险等级进行本地测试与持续监测。

纳入判断：该文为叙述性综述/框架建议，虽涉及风湿科生成式AI，但未针对具体疾病或具体临床任务提供实质性的算法公平性分析（无亚组指标、机制或缓解方法比较），公平性仅为泛化建议式提及，且无经验性测量评估，故按附带提及类文献排除。

限制：仅有摘要，无法核实全文是否包含具体疾病或任务层面的亚组指标、偏倚机制或缓解方法比较；公平性仅在“关注不同患者群体的表现”一处被泛泛提及，未给出分组定义或测量方案。

建议分类：Not applicable

证据：
- algorithm：Generative artificial intelligence (AI) is increasingly being used in rheumatology practice
- evaluation：
- fairness：
- groups：
- medical：increasingly being used in rheumatology practice, to assist with tasks such as documentation

[分析原文](https://europepmc.org/article/MED/42901770)

## p-4ea708e31a2a75722a92

文章：[Artificial intelligence in healthcare: clinical applications, evidence maturity, risks, and life-cycle governance.](https://europepmc.org/article/MED/42967409)

审核决定：待审核
审核备注：
证据版本：0bc1c91daa38aeacf56e84150b7d2377b95cdf9d6610ef466713dce95068d3a1

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：一篇采用批判性叙述综合的医疗卫生AI综述，基于28篇文献梳理临床应用、证据成熟度、风险与全生命周期治理。结论强调需明确预期用途、情境验证、风险相称的人工监督、可追溯性以及公平与安全评估。文中将“偏倚”列为反复出现的风险之一，但未针对任何具体疾病或任务展开算法公平性分析。

纳入判断：该文属泛化医疗卫生AI治理叙述综述，未指明具体疾病或临床任务，也未提供该情境下实质性的算法公平性分析（无亚组指标、机制刻画或缓解方法对比）；偏倚/公平仅一次列举式提及，属偶发提及，且摘要证据不足，故不纳入。

限制：仅有摘要级证据，无法核实全文方法与细节；语料为判断性选取的28篇，文档计数自述为描述性、无推断效力；所涉任务宽泛且未锚定具体疾病，公平性仅作风险清单式列举，缺少亚组指标、偏倚机制或缓解方法比较。

建议分类：Not applicable

证据：
- algorithm：Artificial intelligence (AI) is increasingly used across clinical, administrative, and public health settings
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/MED/42967409)

## p-62e5a416316a8b47bef5

文章：[In-context learning for medical artificial intelligence.](https://pubmed.ncbi.nlm.nih.gov/43008739/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-6f0c6198a978a06dad8c

文章：[Evaluating AI-generated clinical documentation: a narrative review of quality frameworks and the case for a purpose-built instrument.](https://europepmc.org/article/MED/43014021)

审核决定：待审核
审核备注：
证据版本：7b7447aa600928c7a4fd3d23f7ab52a696252fd0f86e49c9b26d43441d542102

模型建议：hold

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文为叙述性综述，梳理AI scribe在临床文书生成中的应用与质量评估框架，总结六类文书功能和四类AI错误模式，并指出公平性与语言偏见尚未充分解决，呼吁建立专用评估工具。

纳入判断：摘要显示其针对AI临床文书质量评估这一具体任务，并提及公平性与污名化语言，但未展示详细公平性分析；因仅有摘要，按规则暂缓而非纳入。

限制：仅有摘要，未提供全文；公平性仅一句概括，缺少亚组指标、偏见机制细节、具体评估框架或缓解方法比较；无法确认是否满足综述的详细公平性分析要求。

建议分类：Evaluation

证据：
- algorithm：Artificial Intelligence (AI) scribes have emerged as a promising solution
- evaluation：
- fairness：Equity and linguistic bias remain largely unaddressed
- groups：
- medical：Clinical documentation is a cornerstone of safe, high-quality healthcare

[分析原文](https://europepmc.org/article/MED/43014021)

## p-8dc4661353918aab18b0

文章：[Beyond Imaging Overuse: Reframing Appropriateness as a Framework for Value-Based and Sustainable Radiology.](https://europepmc.org/article/MED/43028538)

审核决定：待审核
审核备注：
证据版本：d9f3200fc0f238801e82cb7e6ece2693283bd17c9117c17cc725405a5a6ffc28

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为影像检查适当性（appropriateness）的叙述性综述，综合临床结局、辐射防护、成本、组织效率、公平性、偶然发现与环境可持续性等证据，并提出覆盖申请、设备与方案选择、报告、随访及服务评价的操作路径。文中未提出或评估任何具体医学算法的公平性方法。

纳入判断：属影像过度使用与适当性框架的综述，公平性仅泛泛提及，未针对具体医学任务提供实质性算法公平性分析；AI 仅作为需前瞻验证的应用被提及，不符合医学算法公平性纳入标准。

限制：仅有摘要；公平性仅作为多维质量框架中的列举维度出现，缺少具体疾病或影像任务、亚组指标、偏倚机制或缓解方法的实证分析，AI 应用仅被要求前瞻验证。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Diagnostic imaging is central to contemporary healthcare

[分析原文](https://europepmc.org/article/MED/43028538)

## p-96098d2de647e51623a0

文章：[Federated Learning for Early Cancer Detection: Opportunities, Challenges, and Future Directions.](https://pubmed.ncbi.nlm.nih.gov/42960413/)

审核决定：待审核
审核备注：
证据版本：b7e5d6fea23ac082e4bf14f02333a52a3577792f237ff38ebdff2f876682d2aa

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该综述梳理联邦学习在癌症早筛中的应用，涵盖影像、数字病理、多组学与临床数据，介绍安全聚合与差分隐私等隐私技术，概述按癌种划分的应用，并讨论监管、运营与转化障碍，最后提出多模态与纵向联邦学习、基础模型适配、临床工作流前瞻评估以及社区与低资源站点参与的路线图。

纳入判断：综述虽点名乳腺、肺、宫颈筛查等具体任务，但摘要未提出算法公平性差异问题，未定义受保护群体或亚组发现方案，也无任何公平性测量或缓解评估；唯一相关表述是“社区与低资源站点公平参与”的泛化建议，属附带提及，按规则排除。

限制：仅有摘要，无法核查全文是否包含亚组指标、偏差机制或缓解方法的详细分析；摘要中与公平相关的表述仅为“公平参与”的泛化建议，未见具体公平性度量、亚组比较或数据与代码链接，也未报告具体性能数值。

建议分类：Not applicable

证据：
- algorithm：Federated learning (FL) addresses this constraint by training models across institutions without transferring patient data.
- evaluation：
- fairness：
- groups：
- medical：Early detection of cancer remains one of the most effective strategies to reduce cancer mortality.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42960413/)

## p-98a16a93af978c39cfbf

文章：[Gut Dysbiosis at the Intersection of Depression and Addiction: A Microbiota–Gut–Brain–Reward Framework and Digital Precision Behavioural Health Agenda for the United Arab Emirates](https://europepmc.org/article/PPR/PPR1367656)

审核决定：待审核
审核备注：
证据版本：8af1b27c7cebf52e20ab7f0fe91fc4fa211f3acec5b741f3d5b87a681a61218e

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：综述提出微生物群–肠–脑–奖赏框架，探讨肠菌失调经炎症、内分泌、代谢和奖赏机制影响抑郁与成瘾，并讨论数字表型、可穿戴设备与AI的精准行为健康应用；未涉及算法公平性评估。

纳入判断：摘要虽点名抑郁和酒精使用障碍，但仅泛泛提及公平/治理，未提供算法公平性指标、亚组分析、机制或缓解评估；属偶然提及，按规则排除。

限制：仅提供摘要；未报告算法、公平性指标、亚组比较或缓解评估，仅一次泛泛提及“equity”，不足以构成医学算法公平性分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Depression and addiction, despite substantial comorbidity, are frequently investigated separately.

[分析原文](https://europepmc.org/article/PPR/PPR1367656)

## p-98cb804d876d46d15704

文章：[Final thoughts: A value-based vision for safety and quality innovation in surgery.](https://pubmed.ncbi.nlm.nih.gov/42697087/)

审核决定：待审核
审核备注：
证据版本：bc2adf0aeb76bf1cc099583055cbd502f88bb5d5c3bf79e0e0c9ac856416fd2e

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：本文为外科价值导向创新的叙事性观点文章，讨论人工智能、数字健康、机器人与精准诊断等新技术在外科中的安全、质量、成本与公平落地，呼吁基于患者重要结局与资源投入进行评估，并提出各方协作与公平可及。全文未针对具体疾病或算法开展公平性测量。

纳入判断：该文为外科价值医疗的观点/评论，仅在结尾泛泛提及技术可能"worsening disparities"与"equitable implementation"，属偶发提及；未命名具体疾病或任务，也无算法公平性分析或测量，不满足评论类例外条件，故排除。

限制：仅有摘要，属叙事性评论；公平与差异仅以概括性表述出现，未给出任何具体算法、亚组指标、偏倚机制或缓解方法的实证分析，也无疾病或任务限定。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42697087/)

## p-d5d5a571790e4e6c752d

文章：[Interdental Cleaning and Digital Support in Community Periodontal Prevention: A Narrative Review and Proposed Implementation Framework](https://europepmc.org/article/PPR/PPR1357934)

审核决定：待审核
审核备注：
证据版本：793ad63dfe83d527a8bd16372b962c135188a8ae1ec0c49feafc2a7447514531

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：这是一篇关于社区牙周预防的叙述性综述，讨论牙缝清洁、移动健康、远程口腔医疗及AI辅助牙周评估，并提出概念性实施框架；未开展系统评价或定量合成，也未经前瞻性验证。

纳入判断：该文属于牙周预防的叙述性综述，虽涉及AI辅助评估，但未对具体算法开展公平性测量或亚组分析，也未提供针对该场景的实质性公平性讨论，仅笼统提及公平性需前瞻评估，不符合纳入标准。

限制：仅有摘要；未提供任何算法公平性分析、亚组指标、偏倚机制或缓解方法；公平性仅在结论中作为待评估事项被提及一次。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Periodontal prevention requires effective daily plaque control

[分析原文](https://europepmc.org/article/PPR/PPR1357934)

## p-e3a70eecbc25d447c39c

文章：[AI Agents and Agentic AI in Medicine: An Autonomy-Centred Scoping Review and Research Agenda](https://europepmc.org/article/PPR/PPR1364145)

审核决定：待审核
审核备注：
证据版本：7c7b1422ee2e4f63f1f42ea45887d3ec6f9c12788130e2cfa39fb6d761addea4

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文为以自主性为中心的医学AI智能体范围综述：提出六级临床自主性量表（按人类判断介入位置与动作可逆性分级）、七项面向自主性的评估维度、评估要求与自主级别的映射及十项失效模式分类，并给出研究议程与监管建议。

纳入判断：该文属综述，仅泛泛提及公平设计与公平治理建议，未命名具体疾病/任务，也未提供针对该场景的实质算法公平性分析，属偶发提及；同时缺少定义群体、公平性评估实施等证据，按规则排除。

限制：仅有摘要级证据；全文未指向任何具体疾病或临床任务，公平性仅以“equity-aware design”泛泛提及，无亚组指标、偏倚机制、编码证据或缓解方法的实质分析。

建议分类：Not applicable

证据：
- algorithm：We introduce a six-level scale of clinical agent autonomy that grades systems
- evaluation：
- fairness：
- groups：
- medical：moving from research prototypes towards clinical deployment

[分析原文](https://europepmc.org/article/PPR/PPR1364145)

## p-e55b1175139a88707ed1

文章：[Integrating diversity, equity, and inclusion in generative AI applications for healthcare education: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42407288/)

审核决定：待审核
审核备注：
证据版本：a530ef3002e22e0e803067c14761883f6273d30e06384f3250b45a6a33b67171

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文为范围综述，综合16项研究，考察生成式AI在医学教育中如何识别与整合多样性、公平与包容（DEI），指出概念界定不清、缺少多元伙伴参与、缺乏对DEI落实情况的评估等缺口，并呼吁建立覆盖GenAI全生命周期的DEI框架与制度问责。

纳入判断：该文是医学教育中GenAI的DEI范围综述，未针对具体疾病或临床任务，也未提供亚组公平性指标、偏差机制或缓解方法的实质性分析，属于泛化的公平/伦理建议类综述；且证据仅为摘要，不满足五项证据标准。

限制：仅有摘要，未见具体疾病或临床任务、亚组指标、偏差机制或缓解方法的细节；内容为医学教育场景的DEI整合综述，未提供算法公平性测量或实证评估。

建议分类：Not applicable

证据：
- algorithm：Capabilities of generative AI (GenAI) tools continue to advance
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42407288/)

## p-2dc7893202614a28f741

文章：[Data-centric, robust, and explainable multimodal deep learning for clinical decision support: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42667902/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-31dd08c87fcdfb2c9189

文章：[AI-generated patient instructions as safety-critical communication: a provisional evidence-informed framework for clinical deployment.](https://pubmed.ncbi.nlm.nih.gov/42607431/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-496be92504999e54331b

文章：[Application of geospatial technologies in mental health research: A scoping review of progress and future directions.](https://europepmc.org/article/MED/43042965)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-aca067eb1061051f9b86

文章：[Bias and equity in large language model-based applications for health care: a scoping review.](https://europepmc.org/article/MED/43052083)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-d3566a29f4f70f84cac4

文章：[Intelligent immunotherapy: AI-driven optimization of CAR-T therapy in hematologic malignancies.](https://pubmed.ncbi.nlm.nih.gov/42904142/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-171787f0269c1c87c800

文章：[Multi-omics data integration in bioinformatics: methods, applications, and the path toward biological reasoning.](https://pubmed.ncbi.nlm.nih.gov/42995320/)

审核决定：待审核
审核备注：
证据版本：a5223fdb80a8d14486a308b0898e3dd4e7f4e47f7f30b426493985f671fae0ff

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该综述梳理多组学数据整合策略、机器学习方法及疾病应用，并基于慢性淋巴细胞白血病公开数据再分析，比较缺失数据下不同整合策略的表现，提出支持生物学推理的四项模型标准。

纳入判断：文章聚焦多组学整合、缺失数据处理与生物学推理，未提出或评估医学算法公平性问题，缺乏公平性定义、群体比较或公平性指标，故排除。

限制：仅有摘要，缺少检索与纳入细节、完整结果及方法学细节；未涉及算法公平性、受保护群体、亚组差异或公平性缓解评估。

建议分类：Not applicable

证据：
- algorithm：machine learning methods used to implement them
- evaluation：A reanalysis of a publicly available chronic lymphocytic leukemia dataset revealed
- fairness：
- groups：
- medical：applications in various diseases

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42995320/)

## p-2bad63dad27f37ed4849

文章：[Green Pathology: start small, think big. Awareness paper by the Advisory Board of the European Society of Pathology.](https://pubmed.ncbi.nlm.nih.gov/42983055/)

审核决定：待审核
审核备注：
证据版本：89c3da30f0a95e8fbad6aafe1ee7af55a6d6fc14c19a629f0b12dc877249d2c8

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：欧洲病理学会顾问委员会的绿色病理意识文件，汇总多机构与国际视角，讨论解剖病理实验室及数字基础设施的环境碳足迹、废物管理、数字碳减排和实施框架，旨在推动可持续病理实践。

纳入判断：文章主题为病理实验室环境可持续性与碳减排，虽提及AI的数字碳足迹，但未评估医学算法、未定义受保护群体、未提出或测量算法公平性，也未实施公平性评价；健康公平仅作背景提及，不构成算法公平研究。

限制：仅有摘要；全文是否包含算法公平性分析无法由摘要确认，但摘要未报告任何算法、分组比较或公平性指标。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42983055/)

## p-2cdd0fa40c0fdda31e91

文章：[Utilising digital technologies for mycetoma management: A comprehensive review of advances and opportunities.](https://pubmed.ncbi.nlm.nih.gov/42993714/)

审核决定：待审核
审核备注：
证据版本：2d10a64484ea83dd66dda72ecc541a61b4cc5cc23e6e872412e98d16b118c822

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为足菌肿数字技术综述，梳理远程医疗、mHealth、电子健康记录、AI影像与病理图像分析、区块链等在诊疗、随访、培训和药物研发中的应用及挑战；公平性仅泛泛提及数字鸿沟与健康不公平。

纳入判断：虽涉及足菌肿AI病理图像诊断这一具体任务，但公平性讨论仅停留在数字鸿沟、资源可及性与伦理治理的泛化表述，未构成算法公平性研究问题或评测，两项综述准入条件未同时满足。

限制：全文未报告任何亚组指标、公平性评测框架、偏倚机制或缓解方法，也无原始实证结果；AI部分仅概述病理图像识别应用，缺乏算法公平性分析。

建议分类：Not applicable

证据：
- algorithm：AI algorithms were used to analyse histopathological section images
- evaluation：
- fairness：
- groups：
- medical：AI algorithms were used to analyse histopathological section images to detect characteristic features of mycetoma with high precision

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13742912/fullTextXML)

## p-35418e9ff44987d99dbe

文章：[Data, AI and healthcare equity: why Africa is being left behind and how synthetic data can close the gap.](https://pubmed.ncbi.nlm.nih.gov/42986603/)

审核决定：待审核
审核备注：
证据版本：6c650fb14ef3d5d8e54342b6f0ba1cf896aa1083e96e340077a57af620c91532

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：评论文章指出全球仅约2%的AI训练数据来自非洲，而非洲承担逾20%的疾病负担，主张将合成数据作为短期内弥合数据鸿沟的务实且合乎伦理的手段，并配套非洲本土化的治理框架、基础设施投资与可互操作数据体系。

纳入判断：该文为观点评论，讨论数据稀缺与认识论不公及合成数据政策建议，未针对具体医学任务开展算法公平性测量、偏差机制分析或缓解方法评估，属于泛化的健康公平与治理论述，不满足五项证据标准。

限制：仅有摘要，无具体疾病或临床任务、无亚组指标、无公平性度量或实验评估；合成数据在公平性上的效果仅为主张，未给出方法细节或实证结果。

建议分类：Not verified

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42986603/)

## p-890a1e7b312acb803ad3

文章：[Distinguishing artificial intelligence from robotic execution in total knee arthroplasty: a narrative review and evidence map.](https://pubmed.ncbi.nlm.nih.gov/42989357/)

审核决定：待审核
审核备注：
证据版本：552a01774cbcddd7ce6ad669d60b46f022bfa5f30ca900ad2e548b0c3e11b1ab

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：综述区分全膝关节置换术中机器人执行与AI/ML预测功能，按临床路径梳理证据成熟度并提出功能特异性评价与报告建议，指出AI增量获益证据不足。

纳入判断：该文为TKA中AI与机器人执行区分的叙述性综述；仅在报告建议中泛泛提及公平性和亚组表现，未针对该任务提供实质性算法公平性分析或测量结果。

限制：仅将公平性、亚组表现和多样性验证列为未来报告建议，未提供具体公平性指标、机制分析、基准或缓解评估；全文为叙述性证据地图。

建议分类：Not applicable

证据：
- algorithm：AI and machine learning (ML) may support radiographic interpretation, implant sizing, patient selection
- evaluation：
- fairness：subgroup performance, access, and fairness
- groups：Performance should be tested across age, sex, body mass index, ethnicity, comorbidity burden
- medical：Total knee arthroplasty (TKA) remains the definitive surgical treatment for end-stage knee osteoarthritis

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13741776/fullTextXML)

## p-9ca0cac29da6ce5f1c90

文章：[Chest physiotherapy for pneumonia in children.](https://pubmed.ncbi.nlm.nih.gov/42992515/)

审核决定：待审核
审核备注：
证据版本：88fd4e4c7a8ca816712f8e006bbf7767222d4c78779f21c5c5958b5aceba2863

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：Cochrane系统综述评估儿童肺炎胸部物理治疗的疗效与安全性，纳入12项随机对照试验，未涉及人工智能、算法公平性或亚组公平性分析。

纳入判断：该文是儿童肺炎胸部物理治疗的Cochrane综述，没有评估AI/ML算法，也没有算法公平性、偏倚机制或亚组公平性测量，不符合纳入标准。

限制：仅有摘要，且主题为物理治疗干预而非医学算法；未提供算法、敏感属性或公平性评估证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Pneumonia is the single largest infectious cause of death in children aged under five years

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42992515/)

## p-a75fcd8d53770af74dd9

文章：[Prognostic accuracy of the maternal serum IGFBP4/SHBG ratio for spontaneous preterm birth in asymptomatic pregnancies: a systematic review.](https://pubmed.ncbi.nlm.nih.gov/42971281/)

审核决定：待审核
审核备注：
证据版本：8fd398a71be00942d7e3db8a842ec3113be0ad928260f65a695a459984d5fc3d

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该系统综述评估孕妇血清IGFBP4/SHBG比值对无症状妊娠自发性早产的预后准确性，纳入7项研究并报告敏感度与特异度，证据确定性极低，未涉及算法公平性。

纳入判断：该文是早产预后生物标志物准确性的系统综述，未评估AI/ML算法，也未提出算法公平性、差异、编码、缓解或公平测量问题，不符合医学算法公平性范围。

限制：仅摘要层面证据；未评估AI/ML模型，也未报告公平性、亚组差异、偏倚机制或缓解措施；纳入研究少且部分重叠，均由检测开发者资助。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Two reviewers independently extracted data and assessed risk of bias (QUADAS-2)
- fairness：
- groups：
- medical：spontaneous preterm birth in asymptomatic pregnancies

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42971281/)

## p-02d4bc36bdd7bda2726e

文章：[Artificial Intelligence in Bioengineering: Innovations, Challenges, and Future Directions: A Narrative Review.](https://europepmc.org/article/MED/42939059)

审核决定：待审核
审核备注：
证据版本：c7a02357669694e2b1f77bc1d479735ad0c97a97da3af80ff7398a502cfdc9e0

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

正式版本线索：[Artificial Intelligence in Bioengineering: Innovations, Challenges, and Future Directions: A Narrative Review](https://doi.org/10.3390/bioengineering13101204)

中文概述：该文为AI在生物工程中的叙述性综述，跨影像、生理信号、可穿戴与机器人等领域总结创新、挑战与未来方向；公平性仅作为数据集偏倚、域偏移等泛化挑战之一被简要提及，未提供针对具体临床任务的算法公平性分析。

纳入判断：综述泛泛提及bias与fairness，未针对具体疾病或任务给出亚组指标、机制或缓解评估，不满足综述纳入所需的“具体任务+实质性公平性分析”双重条件；无群体定义与公平性实证测量。

限制：全文仅泛述数据集偏倚、代表性、域偏移与公平性，未界定受保护群体或人口学属性，也无亚组指标、偏倚机制测量或缓解方法的实证比较；作为综述亦未聚焦单一医学任务。

建议分类：Not applicable

证据：
- algorithm：AI or machine-learning methods have a substantive role in the analysis
- evaluation：
- fairness：A first concern is dataset bias and representativeness
- groups：
- medical：AI-assisted detection of tumor metastases

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13701786/fullTextXML)

## p-301e288ddbc786daf5fb

文章：[Language, power, and access: large language models and equity in medicine.](https://pubmed.ncbi.nlm.nih.gov/42711214/)

审核决定：待审核
审核备注：
证据版本：f8691e8d8123116ca584f8e4da20657389e9c64aea0f7d9d7950050a1514209b

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：这是一篇关于大语言模型在麻醉、围手术期与重症监护中应用的编辑评论，提出概念性“偏见金字塔”框架，用以解释不公平如何在全球知识生态、机构信息环境与个体临床工作流三个层面产生，并主张在模型嵌入常规实践前通过治理、教育与协同行动促进公平实施。文中强调学习型医疗系统的反馈循环可能放大或改善公平性，但未报告任何具体任务的分组指标或实证评估。

纳入判断：属编辑评论类低优先级文献：虽涉及麻醉/围手术期/重症监护等临床领域，但未指明具体疾病或具体临床任务，且仅泛化提出治理、教育与协同行动等公平实施建议，缺少该情境下的亚组指标、机制分析或缓解方法比较等实质算法公平性分析。摘要级证据不可建议纳入，且未定义分组属性、无实证测量，故按偶提公平性/治理议题处理予以排除。

限制：仅有摘要级证据，无法核实全文是否包含具体任务的分组指标、机制测量或缓解方法比较；摘要本身只呈现概念框架与治理建议，未给出数据集、模型、评价指标或量化结果，也未界定受保护属性或亚组发现方案。

建议分类：Not verified

证据：
- algorithm：Large language models (LLMs) are increasingly being integrated into anaesthesia
- evaluation：
- fairness：explains how inequity can emerge across global knowledge ecosystems
- groups：
- medical：integrated into anaesthesia, perioperative medicine, and critical care

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42711214/)

## p-304203b461b8ba725929

文章：[Artificial intelligence in pediatric nephrology: current applications and emerging frameworks for evidence generation.](https://pubmed.ncbi.nlm.nih.gov/41739204/)

审核决定：待审核
审核备注：
证据版本：0f9df2cd22160fd8eea26b3f0e24e9525cd956f9d5300edb0e6d4b831e9b17e3

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为叙述性综述，概述人工智能在儿童肾脏病学中的已有与近期应用，涵盖慢性肾病、透析、移植、影像、病理与基因组学，并讨论人工智能虚拟试验与数字孪生等证据生成框架，以及儿童特有的伦理、监管与公平性考量。

纳入判断：属叙述性综述且范围宽泛（多任务并列），摘要中公平性仅为泛泛伦理与公平性提及，未针对某一具体疾病或任务给出实质性算法公平性分析（无亚组指标、机制或评估框架细节），属偶然提及；且仅摘要证据，不足推荐。

限制：仅有摘要可用：未见任何具体任务的亚组指标、偏倚机制或缓解方法比较，公平性仅以“伦理、监管与公平考量”一句带过；无法据摘要判定全文是否有实质性算法公平性分析，但现有证据不足以入选。

建议分类：Not applicable

证据：
- algorithm：AI-based methods offer complementary approaches to address these challenges, spanning diagnostic support, prognostic modeling
- evaluation：
- fairness：
- groups：
- medical：established and near-term applications in chronic kidney disease, dialysis, transplantation, imaging, pathology, and genomics

[分析原文](https://pubmed.ncbi.nlm.nih.gov/41739204/)

## p-3864f35402ae4a571243

文章：[The Prevalence of Nutritional Disorders in Inflammatory Bowel Disease: A Systematic Review and Meta-Analysis.](https://pubmed.ncbi.nlm.nih.gov/42892557/)

审核决定：待审核
审核备注：
证据版本：8569b7bd3e5ecbc424fa43a7bf0d229fdb17dcff5a6c158d67724e37b566c782

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为系统综述与Meta分析，汇总201项观察性研究，估计炎症性肠病患者中营养不良、超重/肥胖及肌少症等营养障碍的患病率，并按性别、年龄、疾病亚型与活动度、诊断标准、研究场所和地区开展亚组分析。全文未涉及任何AI/ML算法，也未评估算法公平性。

纳入判断：主题为炎症性肠病营养障碍患病率的流行病学Meta分析，缺少被评估的AI/ML算法，也未提出算法公平性、偏倚机制或缓解问题；按性别、地区等亚组分析属患病率异质性，不构成算法公平性证据，不符合纳入标准。

限制：仅有摘要证据：无算法模型、无公平性指标或偏倚测量；亚组分析针对流行病学患病率异质性，而非算法层面的差异机制或缓解干预；未提供代码或数据信息。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：The epidemiology of nutritional disorders in inflammatory bowel disease (IBD) remains poorly characterized.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42892557/)

## p-3c97a473cc273036eb91

文章：[Overcoming inequity in cancer screening: Can modern technologies close the gap?](https://pubmed.ncbi.nlm.nih.gov/42772653/)

审核决定：待审核
审核备注：
证据版本：b3f32e37c748405ef3e93e5b0fd1eeb82db39dd92640368e1a8efafad8df53c7

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：本文为综述/评论，讨论癌症筛查项目获益分布不均的问题，并评述多基因风险评分、AI辅助影像、多癌种早期检测和生命历程风险模型四类新兴技术可能复制或放大既有不平等的风险；主张通过训练数据多样化、早期纳入公共医疗体系及配套诊断随访能力建设来实现公平影响。

纳入判断：摘要虽提及祖先偏差、训练数据多样性不足等公平风险，但属泛化的公平性挑战罗列与政策建议，缺乏针对特定疾病/任务的实质性公平分析（无亚组指标、机制量化或方法比较），按规则判为偶然提及类文献，排除。

限制：仅有摘要级证据，且为跨多种技术的宏观评论：未给出具体疾病或单一任务，未提供任何亚组指标、偏差机制实证测量、评估框架或缓解方法比较，也未涉及作者自有的实证研究。

建议分类：Not applicable

证据：
- algorithm：Four emerging technologies-polygenic risk scores (PRS), artificial intelligence (AI)-assisted imaging, multi-cancer early detection (MCED) tests
- evaluation：
- fairness：each technology also carries the risk of reproducing or amplifying existing inequities
- groups：trials conducted in predominantly white, middle-income populations
- medical：Cancer screening programmes have substantially reduced cancer mortality in high-income settings

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42772653/)

## p-463e6a0b4bc2a1c37160

文章：[Humanity in the loop: Reframing artificial intelligence and the global medical imaging divide.](https://europepmc.org/article/MED/42913184)

审核决定：待审核
审核备注：
证据版本：e70830cb421ef7213e444c6f941fa5822bb528d8de7eec7c53f612a9eb491712

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为叙述性综述，讨论判别式、生成式与智能体AI在低中收入国家医学影像中的潜在收益与不公平风险，并提出超越“人在回路”、涵盖患者、劳动力、社区、数据、系统与全球六个维度的“Humanity-in-the-Loop”社会技术治理框架。

纳入判断：该文为治理导向的叙述性综述：虽提及AI可能加剧影像不公平，但未针对具体疾病或任务给出实质性算法公平分析（无亚组指标、机制测量或缓解方法比较），也未实施任何评估；属一般性公平AI/伦理治理建议，且仅摘要级证据，按规则排除。

限制：仅有摘要证据，无具体疾病或影像任务、无亚组指标、无偏差机制的具体测量或缓解方法比较，也无实证或基准评估；治理框架属一般性公平AI建议。

建议分类：Not applicable

证据：
- algorithm：This narrative review examines the potential for discriminative, generative and agentic AI
- evaluation：
- fairness：it may also reinforce existing inequities
- groups：Low- and middle-income countries (LMICs) face persistent shortages in imaging equipment
- medical：Access to radiology and nuclear medicine remains profoundly unequal across global health systems

[分析原文](https://europepmc.org/article/MED/42913184)

## p-4ed7ef43eee0a12e09fe

文章：[Prognostic Evidence for Artificial Intelligence-Derived PET Tumour-Burden Biomarkers in Cancer: A Systematic Review.](https://europepmc.org/article/MED/43028436)

审核决定：待审核
审核备注：
证据版本：cdeefb835cc4542b6dbdefe1ce013ae7b3e3f379506202ef7faba29448969d51

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该系统综述汇总35项报告，评估AI自动测量PET代谢肿瘤体积（MTV/TMTV）与癌症预后的关联，并与专家测量比较；结论为预后关联有限，尚不能证明可替代专家测量或改善治疗结局。

纳入判断：该文为PET肿瘤负荷AI预后价值的系统综述，仅讨论预后关联和偏倚风险，未涉及算法公平性、差异群体或缓解评估；且仅有摘要证据。

限制：仅有摘要，缺乏全文方法、亚组及公平性分析细节；该综述聚焦预后证据与偏倚风险，未报告算法公平性评估。

建议分类：Evaluation

证据：
- algorithm：Artificial intelligence (AI) can automate tumour-burden measurement on positron emission tomography (PET)
- evaluation：This review evaluated prognostic evidence for AI-derived PET tumour-burden biomarkers
- fairness：
- groups：
- medical：prognostic evidence for AI-derived PET tumour-burden biomarkers

[分析原文](https://europepmc.org/article/MED/43028436)

## p-5246d1ff466f50a66dd4

文章：[Educating pharmacists for an artificial intelligence augmented profession: A narrative review of curricular and accreditation imperatives.](https://pubmed.ncbi.nlm.nih.gov/42498609/)

审核决定：待审核
审核备注：
证据版本：d21b1cdcb5d2e487a919be8f3f4708bbd9b5f6b17fe1de92b014c0cff86442db

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：文章从加拿大视角出发，对药学教育改革与认证要求进行叙述性综述，综述了国际同行评议文献及FIP、WHO、UNESCO等机构指南；提出四级AI能力层级（通用、跨专业、药学专属、角色专属），并总结六项教学原则与五项认证杠杆，指出CCAPP标准20是最具影响力的认证工具。内容为课程与认证层面的能力框架讨论，未涉及具体医学任务的算法公平性评估。

纳入判断：该文是药学教育与认证的叙述性综述，属评论/综述类；虽提及“equity”，但仅作为跨专业AI治理能力的一项列举，未指明任何具体医学疾病或任务，也未提供实质性算法公平性分析（亚组指标、偏倚机制、评测框架或缓解方法比较），不满足综述类入选的两个必要条件，属偶发提及。

限制：仅有摘要，无方法、数据或实证评估细节。全文未针对任何具体疾病或临床任务开展算法公平性分析，公平/公平性仅在跨专业能力中被一笔带过，也未给出亚组指标、偏倚机制或缓解方法比较。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42498609/)

## p-7af0f4754b3f9f27c53e

文章：[Monoclonal gammopathy of clinical significance: the pathogenic paraprotein and a precision medicine roadmap.](https://europepmc.org/article/MED/43001490)

审核决定：待审核
审核备注：
证据版本：75276bf479b9aafcfef1785f1c4f7fb3b454b6f30d0f4893cf6e3eecfb0fc1cf

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为MGCS叙述性综述，讨论致病性副蛋白介导的器官损伤、诊断进展及克隆导向治疗的精准医学路线图；仅在讨论中笼统提及人工智能与多组学可用于风险分层，未评估任何算法或公平性问题。

纳入判断：主题为血液肿瘤临床综述，缺乏被评估的AI/ML算法、明确公平性/差异问题、受保护群体及实证测量；不符合纳入标准。

限制：仅有摘要，无法核对全文；摘要未提供算法、亚组定义、公平性指标或实证评估，人工智能仅一句展望。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Monoclonal Gammopathy of Clinical Significance (MGCS) challenges the traditional binary classification

[分析原文](https://europepmc.org/article/MED/43001490)

## p-7df805d09c7cdd1d74b3

文章：[The Evolving Landscape of Vision Rehabilitation: Current Status and Future Directions.](https://pubmed.ncbi.nlm.nih.gov/42081173/)

审核决定：待审核
审核备注：
证据版本：610f60b35cf45c36628126c09903eadca1d3ae918ca8b96854608110f205d4ec

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：一篇关于视力康复领域现状与未来方向的综述，强调生物心理社会框架、多学科协作、神经可塑性与人工智能辅助技术、心理社会支持及服务体系落地障碍，呼吁以参与度、心理健康和生活质量为核心结局指标，并在卫生系统中推进包容与公平。

纳入判断：该文为视力康复综述，涉及临床任务，但未评估任何AI/算法，也未提供亚组指标、偏倚机制、缓解方法或公平性度量框架；公平/包容仅在结尾作为政策口号出现，属附带提及。且仅有摘要级证据，不足以判断全文是否包含所需的详细算法公平性分析，故按规则排除。

限制：仅有摘要，未见具体算法、数据集或亚组公平性分析；文中“包容与公平”仅为一次泛化表述，指向服务可及性与全球承诺，而非医学算法公平性评估。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：multidisciplinary vision rehabilitation in clinical practice

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42081173/)

## p-85ee21f0a94aed14ddbc

文章：[Conversational Capacity in Triadic Telemedicine: A Conceptual Framework and Evidence Synthesis.](https://pubmed.ncbi.nlm.nih.gov/42545789/)

审核决定：待审核
审核备注：
证据版本：cdccc8416be9e11ffa99e657d5228720dcad0f3ba923aff6793651643caa00b7

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为叙述性综述与概念框架，提出以“会话能力”（解释、翻译、倡导、适应四项功能）界定三方远程医疗中的促进者，并构建会话能力谱系与临床情境矩阵，讨论AI作为第三方的局限，以及高脆弱人群更易被分配AI的“公平悖论”。

纳入判断：属概念框架与叙述综述，仅笼统提及AI部署中的公平悖论，未针对特定疾病或任务提供实质性算法公平性分析，无亚组指标、机制或缓解方法比较，也无实施层面的实证评估，符合偶提公平应排除的情形。

限制：仅有摘要，无具体疾病或临床任务，也无亚组指标、偏倚机制或缓解方法的实证测量；“公平悖论”仅为概念性推断，未定义受保护属性或评估方案，不构成算法公平性研究。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：triadic clinical communication, shared decision-making, and AI-mediated interaction

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42545789/)

## p-8de34a8daf73b620c73c

文章：[Artificial Intelligence/Machine Learning-Enabled Precision Nutrition Modestly Improves Anthropometric Outcomes and Systolic Blood Pressure: A Systematic Review and Meta-analysis.](https://pubmed.ncbi.nlm.nih.gov/42777836/)

审核决定：待审核
审核备注：
证据版本：fe05b22d1d372e7103a2d3273fa66b889ee91e4632d8f9876d140a021f417641

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该系统综述/Meta分析评估AI/ML赋能的精准营养在饮食、代谢、行为、实施与公平结局中的效果，报告体重、BMI、腰围和收缩压的小幅改善，但证据确定性低至极低、异质性较大。

纳入判断：摘要仅报告精准营养AI/ML干预的效果Meta分析，公平/公平性仅作为泛泛结局提及，未定义受保护群体、亚组比较或算法偏倚测量，不满足算法公平性证据标准。

限制：仅摘要可用；未提供具体研究、亚组数据或公平性分析细节，无法核实公平相关测量、群体定义及偏倚机制。

建议分类：Not applicable

证据：
- algorithm：AI/ML-enabled analytical approaches and technologies in precision nutrition
- evaluation：
- fairness：
- groups：
- medical：personalized nutrition across the lifespan

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42777836/)

## p-a70d74f3666fd35a258b

文章：[Artificial Intelligence in Gynecology and Obstetrics: Medico-Legal, Ethical, and Governance Challenges-A Narrative Review.](https://europepmc.org/article/MED/43028780)

审核决定：待审核
审核备注：
证据版本：457d0f7f7875cb9fb6c8cd818dde42efad92b385f59ae7ee68eda781d93cb7b3

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该叙述性综述梳理妇科与产科AI的医疗法律、伦理与治理挑战，提出生命周期治理框架及七项机构要求，其中包含公平监测。但公平与歧视仅作为风险域和治理要求泛泛提及，未针对具体疾病或任务提供算法公平性分析。

纳入判断：摘要仅将歧视与公平列为治理风险之一，未命名具体疾病或任务，也未给出亚组指标、偏倚机制或公平性评估框架，属泛泛提及；且仅有摘要证据，不足以建议纳入。

限制：仅有摘要；缺少全文方法细节、亚组指标或任何具体公平性评估结果，无法确认是否存在针对特定任务的实质性公平分析。

建议分类：Not applicable

证据：
- algorithm：AI errors, bias, or opacity in this specialty therefore carry major clinical and legal consequences.
- evaluation：
- fairness：
- groups：
- medical：Artificial intelligence (AI) is entering gynecologic and obstetric imaging, risk prediction, decision support

[分析原文](https://europepmc.org/article/MED/43028780)

## p-c9ba14389fe134cfa35c

文章：[Artificial general intelligence and the clinical laboratory: a paradigm shift toward Lab 2.0.](https://pubmed.ncbi.nlm.nih.gov/42402007/)

审核决定：待审核
审核备注：
证据版本：6520ffc21b079a8e8cf1e5ef4c48f2fc1c156824282f46de3a98c1c9056ef97e

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：观点文章提出临床实验室从被动确认检测的“Lab 1.0”转向主动分层干预的“Lab 2.0”，设想由智能体推理、虚拟细胞因果建模与医学数字孪生构成概念路线图，并提出扩展质量指标框架的算法质量指标（aQIs）以持续监测AI模型表现。作者自述机制仍属设想，需实证验证。

纳入判断：该文为观点/评论类文章，提出概念路线图与治理性建议（aQIs、FHIR互操作、实验室人员角色），未涉及具体医学任务下的算法公平性分析；公平性只出现一次笼统表述（“考虑公平维度”），属于偶发提及。既无定义群体或亚组发现协议，也无任何已实施的实证或测量评估，故不符合纳入所需的五项证据条件。

限制：仅有摘要；未开展任何实证评估。公平性仅一句笼统提及“考虑公平维度”，未给出具体疾病或实验室任务、受保护属性、亚组指标或缓解方法，也未报告算法质量指标的具体测量设计与数据。

建议分类：Not verified

证据：
- algorithm：increasingly capable AI can accelerate this loop
- evaluation：
- fairness：
- groups：
- medical：Clinical laboratory medicine faces converging structural pressures

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42402007/)

## p-ce2af7c8557686d0ea9e

文章：[Artificial intelligence and machine learning in pharmaceutical research and health care: Ethical challenges and a framework for responsible implementation.](https://pubmed.ncbi.nlm.nih.gov/42498132/)

审核决定：待审核
审核备注：
证据版本：a39e02fc3979d47ca54befa1e71552a3b45e4ca1aa8823e9ce83fa83daefee5c

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：一篇叙述性综述，综合2015—2026年127项研究，梳理AI/ML在药物研发与医疗中的伦理挑战（偏见、问责、隐私、公平），并提出含技术安全、治理信任、以人为本三大支柱的伦理治理框架。

纳入判断：该文为宽泛的伦理与治理综述，未锁定具体疾病或临床任务，也未给出具体的算法公平性分析（如亚组指标、偏倚机制或缓解方法比较）；公平与偏见仅作为伦理挑战之一被提及，属于偶发提及类文献，按规则排除。

限制：仅有摘要，缺少全文方法、具体疾病或临床任务、亚组指标与实测证据；公平性仅作为伦理议题之一被列举，未提供可核验的算法公平性分析细节。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42498132/)

## p-d281f0d16e400ebc1734

文章：[India's participatory approach to developing a national AI strategy for health: lessons for collective learning.](https://pubmed.ncbi.nlm.nih.gov/42866166/)

审核决定：待审核
审核备注：
证据版本：d91fbd9f18198e3d6537f47213f9a6eafc9cd770d01bff87135a1cf216e7636a

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：文章记录印度国家AI健康战略SAHI的三阶段参与式制定过程，涵盖情境分析、四区域咨询及300余名利益相关者综合，提出技术前提与治理实施条件双框架，并将公平作为运营要求。其贡献在战略制定方法，不涉及具体医学任务或算法公平性实证评估。

纳入判断：摘要显示为国家级AI健康战略制定与治理框架的政策方法学，并非具体医学AI算法公平性研究；公平仅作为战略原则提及，缺乏特定任务、定义群体或实证评估，故排除。

限制：仅有摘要；未提供具体疾病或临床任务、被评估算法、受保护群体、公平性指标或实证测量，无法核验算法公平性分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42866166/)

## p-f8544bc5d16b8bbf91e1

文章：[The AI health divide: Three challenges and recommendations to improve design, transparency, and access for low-SES communities.](https://pubmed.ncbi.nlm.nih.gov/42762121/)

审核决定：待审核
审核备注：
证据版本：2df35628246ecdbed5379bb463fb05d8932cefceeb77e52018a807f805e1e63b

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为观点/建议类文章，讨论低社会经济地位（SES）社区在AI医疗整合（患者门户、症状自查、照护协调平台）中面临的基础设施、认知与素养负担及信任障碍，并提出降低认知负荷、提升可及性与信任度的设计与实施指南。

纳入判断：属评论/建议类文章，讨论SES群体数字健康鸿沟并提出通用公平设计建议，未针对特定医学任务或算法开展公平性评测，缺乏亚组度量或偏倚机制证据；且仅摘要级证据，不能建议纳入。

限制：仅有摘要，无具体疾病或临床任务，无模型或数据集，无亚组指标、偏倚机制实验或缓解方法比较；结论为一般性公平AI建议，缺乏可核验的算法公平性测量证据。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：may inadvertently disadvantage low SES communities, while widening access disparities, exposure, and trust
- groups：design guidelines that support the needs of low-SES individuals
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42762121/)

## p-aa1d2c08ab2918b9678a

文章：[Artificial Intelligence in Thoracic Pathology and Biomarker Assessment: An IASLC Pathology Committee Review.](https://europepmc.org/article/MED/43064238)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

## p-6f63b3f380ed1aa84ab0

文章：[Perspective. Precision Nutrition at a Crossroads: From Biological Prediction to Contextual Implementation.](https://pubmed.ncbi.nlm.nih.gov/42994801/)

审核决定：待审核
审核备注：
证据版本：2a27101789d79ef4fbff561e4163b45e6770458bbc2a30e56fd59995449edbb2

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为精准营养观点文章，主张区分发现科学与干预科学，提出结合行为、社会、文化、经济和环境因素的情境化精准营养框架，并强调预测能力不等于临床效用、可扩展性与公平性。

纳入判断：观点文章且仅有摘要；未针对具体疾病或任务提供实质性算法公平性分析，公平性仅以“equity remains limited”泛泛提及，无亚组指标、机制或缓解评估，故排除。

限制：仅有摘要，无法核实全文是否包含具体疾病或亚组的算法公平性分析；摘要仅泛泛提及公平性有限。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42994801/)

## p-cb4228d020dc966ef78d

文章：[The future of follow-up: technology-enabled medical and developmental follow-up care for NICU graduates.](https://pubmed.ncbi.nlm.nih.gov/42009892/)

审核决定：待审核
审核备注：
证据版本：a5c56fbd0a8b08b478d4d121c8174d04d96892eed646ab10a73a9a35d2db7c0f

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该视角文章讨论NICU出院婴儿的技术赋能随访，强调AI、数字健康和连接设备在家庭教育、护理协调、远程监测及神经发育监测中的应用，并提出实施与公平建议。文章未评估具体算法，也未报告算法公平性分析。

纳入判断：摘要为视角文章，仅泛泛提及地理和社会经济不平等及公平建议，未评估具体医疗算法，也无算法公平性测量或详细分析，属偶然提及，不满足纳入标准。

限制：仅有摘要；未提供具体AI算法、公平性指标、亚组分析或缓解方法；公平仅作为服务可及性与实施建议出现。

建议分类：Not verified

证据：
- algorithm：
- evaluation：
- fairness：
- groups：geographic and socioeconomic inequities in access and outcomes
- medical：Premature infants are at higher risk of long-term clinical and developmental sequelae compared to their term counterparts.

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42009892/)

## p-e3df0dfe9963aaa731c7

文章：[Current research status of risk assessment models for oral squamous cell carcinoma based on microbiome databases.](https://europepmc.org/article/MED/43005677)

审核决定：待审核
审核备注：
证据版本：86c2c89d60015abcdb55cb2e7c74ca824413528f639a98418234560c07adbd3e

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文综述口腔鳞癌微生物组风险预测模型，梳理数据库、菌群标志物、传统统计/机器学习/深度学习及多模态整合，并讨论验证、混杂、批次效应与临床转化瓶颈。

纳入判断：聚焦OSCC微生物组风险模型而非算法公平性；公平性相关仅为人群异质性和混杂的零散提及，缺乏具体疾病场景下的公平性指标、机制或缓解分析，故不满足综述纳入的详细公平性条件。

限制：为叙述性综述，无原始实验；虽提及人群异质性与模型泛化，但未系统评估算法公平性、亚组差异指标或缓解策略。

建议分类：Not applicable

证据：
- algorithm：Machine learning algorithms, including random forest and extreme gradient boosting (XGBoost), have become cornerstone analytical tools
- evaluation：Quantitative summary of representative microbiome-based OSCC predictive models
- fairness：
- groups：matching (age, sex, and smoking), covariate adjustment in regression models, stratification by clinical subgroups
- medical：Oral squamous cell carcinoma (OSCC) represents the most prevalent head and neck malignancy

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13747251/fullTextXML)

## p-fb70d34452db872f1e30

文章：[AI-based augmentation of oncology clinical trials.](https://pubmed.ncbi.nlm.nih.gov/42567955/)

审核决定：待审核
审核备注：
证据版本：c4a52ea32779d3e5c632e79f508ce7dea6ffc4099e72dc68cf4d2baeebb7be04

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该综述讨论人工智能在肿瘤临床试验全生命周期中的应用，包括试验设计、患者招募与试验执行，并泛泛提及公平性、数据质量与监管问题。

纳入判断：该综述虽涉及肿瘤临床试验这一具体场景，但公平性仅属泛泛提及，缺少具体的算法公平性分析、亚组定义或实证评估，因此不足以纳入。

限制：仅有摘要，未见针对具体任务的公平性指标、亚组分析、偏差机制或缓解方法；公平性仅被笼统提及。

建议分类：Not verified

证据：
- algorithm：applications of AI across pre-trial design, trial conduct, and post-trial inference
- evaluation：
- fairness：
- groups：
- medical：Oncology clinical trials are often characterized by slow accrual

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42567955/)

## p-0b379f7f3d343436eaaa

文章：[[Research advances on the application of artificial intelligence in the warning and management of burn-related delirium].](https://pubmed.ncbi.nlm.nih.gov/42989545/)

审核决定：待审核
审核备注：
证据版本：67ed3263e3e65371f41ac000a9816b73fb885c2a01310fa40a48e24e6ade336e

模型建议：hold

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文综述人工智能在烧伤相关谵妄预警与管理中的应用，涵盖预测模型、多模态数据融合、可解释输出、多源数据采集、智能处理与决策支持，并讨论数据治理、算法公平性、临床整合及伦理监管等挑战。

纳入判断：该文为综述，明确烧伤相关谵妄这一具体任务，但公平性仅作为治理/伦理挑战一带而过；未给出定义群体、公平性测量或详细综合，且证据仅限摘要，暂不能判断全文是否存在所需详细分析。

限制：仅有摘要；摘要仅把算法公平性列为挑战，未提供具体任务下的公平性分析、亚组指标、偏差机制或缓解评估，需全文核实。

建议分类：Not verified

证据：
- algorithm：establishment of predictive models for burn-related delirium
- evaluation：
- fairness：data governance and algorithmic fairness
- groups：
- medical：Delirium in burn patients presented a prominent challenge in intensive care

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42989545/)

## p-803cd6bbdad8e1247ff4

文章：[Artificial Intelligence in Chronic Coronary Syndromes: Linking Cellular Pathways to Precision Risk Prediction.](https://pubmed.ncbi.nlm.nih.gov/43027368/)

审核决定：待审核
审核备注：
证据版本：b447eba6f68b43196609f779c86bf44c02e093bfcc4dead01113fa8daf779164

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该叙事综述讨论人工智能在慢性冠脉综合征中连接细胞通路与精准风险预测，涵盖斑块表型、无创缺血建模与多组学整合；公平性仅在结尾作为临床采用障碍之一被一句提及，未展开任何分析。

纳入判断：虽明确指向慢性冠脉综合征这一具体临床任务，但公平性只是障碍清单中的一次提及，没有亚组评估、机制阐释或缓解比较，属于偶然提及，按规则排除。

限制：仅有摘要，非原创研究；公平性仅一处泛泛列举性别、族裔、年龄与资源环境偏倚，缺少亚组指标、偏倚机制或缓解方法的具体讨论，无法证明存在实质性算法公平性分析。

建议分类：Not applicable

证据：
- algorithm：AI and machine learning may support a more mechanistic and individualised approach to CCS
- evaluation：
- fairness：
- groups：algorithmic bias across sex, ethnicity, age, and resource settings
- medical：Chronic coronary syndromes (CCSs) are no longer defined only by fixed stenosis

[分析原文](https://pubmed.ncbi.nlm.nih.gov/43027368/)

## p-0ef408fd609dad2f6516

文章：[Health Literacy and Communication in Stroke Prevention, Management, and Recovery: A Scientific Statement From the American Heart Association.](https://europepmc.org/article/MED/42877955)

审核决定：待审核
审核备注：
证据版本：1ab33625a9eb9a712cc89e66902c539ffe101787bb1d29d08249bfba500468ec

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：美国心脏协会科学声明，综述健康素养与沟通在卒中预防、治疗与康复全过程中的作用，强调护士主导的teach-back教育、二元心理教育及数字化支持干预，并呼吁关注认知/语言障碍、英语能力有限、社会经济弱势与数字素养不足人群的沟通公平性。

纳入判断：该文为卒中健康素养与沟通的科学声明，属综述/立场文件。虽明确卒中这一临床任务，但未评估任何AI/ML算法，公平性仅为泛泛的公平照护倡议（“minimize bias and ensure equity”），无亚组量化指标、偏倚机制或具体评测框架，未同时满足“具体任务+实质性算法公平性分析”两项条件，故排除。

限制：仅提供摘要，无任何AI/ML算法被评估，无亚组指标、偏倚测量或缓解方法；对人工智能与远程医疗仅一句泛泛提及“需严格评估以减少偏倚”，未给出卒中场景下的算法公平性分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：individuals with stroke-related cognitive or language impairments, limited English proficiency, socioeconomic disadvantage, or limited digital literacy
- medical：health literacy is strongly associated with functional outcomes and stroke-related morbidity

[分析原文](https://europepmc.org/article/MED/42877955)

## p-5b7aeb249d7ef6031eb8

文章：[Clinical, Immunological, Biochemical and Safety Outcomes of Eryxin (Reptilin) in Human Studies: A Systematic Review of Published and Grey Literature](https://europepmc.org/article/PPR/PPR1361599)

审核决定：待审核
审核备注：
证据版本：4b699fef1aace9b548fa029a1d8bd0f7e83c4400864c3bcc0f1a34ff321917ff

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文为蛇自体溶解物Eryxin（Reptilin）人体研究的系统综述，汇总22项非随机研究在临床、免疫、生化及安全性方面的结果，因混杂、报告不全和偏倚风险高，认为现有证据无法确立任何适应证的疗效，安全性亦不确定。

纳入判断：摘要为药物疗效与安全性的系统综述，未涉及任何AI/ML或算法评估，也无公平性/差异/编码/缓解或公平性测量问题，五项证据标准均不满足，属主题外文献。

限制：仅提供摘要，无全文；研究对象为药物而非AI/ML算法，全文未涉及算法公平性、亚组差异或偏见测量，与医学算法公平性主题无关。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://europepmc.org/article/PPR/PPR1361599)

## p-622c2ee72af5786411dd

文章：[Application of Artificial Intelligence (AI) in cancer symptom management for adult cancer survivors: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42603423/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-b1af80e58334a13852a7

文章：[Explainable Artificial Intelligence for Cognitive Workload Assessment: Methods, Evidence, and Human-Centered Evaluation](https://europepmc.org/article/PPR/PPR1372432)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

## p-03c4871fffd64213d701

文章：[Role of Telemedicine in Congenital Heart Disease Care Models in Low- and Middle-Income Countries: A Scientific Statement From the American Heart Association.](https://pubmed.ncbi.nlm.nih.gov/42831398/)

审核决定：待审核
审核备注：
证据版本：f44cc13d13112e24d792704c0e5c40546156abf55c84435c5790e8d232a6efa4

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

正式版本线索：[Role of Telemedicine in Congenital Heart Disease Care Models in Low‐ and Middle‐Income Countries: A Scientific Statement From the American Heart Association](https://doi.org/10.1161/jaha.126.054084)

中文概述：该文为AHA科学声明，综述中低收入国家先天性心脏病远程医疗模式，涵盖远程心电、超声、影像传输及AI辅助诊断与质控，强调改善可及性与公平性，但未开展算法公平性评估或亚组分析。

纳入判断：属远程医疗科学声明，虽涉及先天性心脏病这一具体任务，但仅泛泛提及AI工具与公平可及，未给出算法公平性分析、亚组指标或评估框架，不满足算法与公平性证据标准。

限制：仅有摘要，未提供具体AI算法、敏感属性定义、亚组指标或实证测量结果；公平性仅为一般性可及性论述，无法据此判定算法层面公平问题。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Congenital heart disease, a highly specialized field often centralized in urban centers

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42831398/)

## p-22eb0b7b819883505133

文章：[Vaginal microbiome composition and medically assisted reproduction outcomes: a systematic review and network meta-analysis of 2289 women across three WHO regions.](https://europepmc.org/article/MED/42885155)

审核决定：待审核
审核备注：
证据版本：6896eea9b8606695729a2c1c3f65c92a8adc3116ffeffa54703500a076ecb441

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：系统综述与网络荟萃分析比较阴道菌群社区状态类型（CST）与辅助生殖后妊娠结局的关联，纳入12项纵向研究、2289名女性；部分非L. crispatus CST与较低妊娠几率相关，但证据不足以支持临床常规CST检测。

纳入判断：该文评估阴道微生物组CST与辅助生殖妊娠结局的关联，属于临床系统综述/网络荟萃分析；全文未涉及AI/ML算法评估或算法公平性、差异或缓解问题，不满足算法与公平性核心标准。

限制：仅有摘要；研究为观察性系统综述，未涉及AI/ML算法、算法公平性、敏感分组或缓解措施；异质性、残余混杂及稀疏数据限制解释。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：Odds ratios (ORs) with 95% CIs were synthesized across CSTs using NMA.
- fairness：
- groups：
- medical：medically assisted reproduction (MAR), including IVF with or without ICSI, and IUI

[分析原文](https://europepmc.org/article/MED/42885155)

## p-325eff0bcdef03f3b45a

文章：[Recent advances in multiple sclerosis neurorehabilitation.](https://europepmc.org/article/MED/42929321)

审核决定：待审核
审核备注：
证据版本：4f0c09c58e934df27adf74c110e057b19cda0537d719fc5400917cc3aeae4b5d

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文为多发性硬化（MS）神经康复综述，概述多维筛查评估、数字技术（可穿戴、远程监测、AI辅助评估）、运动/认知/心理/职业康复及远程康复进展，并指出数字排斥与康复公平可及性问题，但未对具体算法开展公平性分析。

纳入判断：综述虽针对多发性硬化神经康复这一具体临床任务并提及AI辅助评估与康复公平可及，但摘要未显示针对具体算法的分组比较、公平性指标或测量评估，属偶然提及公平性，故排除。

限制：仅有摘要，无全文；未提供算法公平性的定义、亚组指标、偏倚机制或缓解方法评估，公平性仅作为一般性可及性问题被提及，无法核实其详细分析。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：Neurorehabilitation is a core component of comprehensive MS care, complementing pharmacological treatment.

[分析原文](https://europepmc.org/article/MED/42929321)

## p-58ea9d8fabcdaf9eda6d

文章：[Ethical Challenges in the Use of Artificial Intelligence for Psychiatric Patient Management: A Systematic Review](https://europepmc.org/article/PPR/PPR1366535)

审核决定：待审核
审核备注：
证据版本：2f7660463e6494a45b49c53652d215fdc236429c8a7290e75f235fb62edbb65b

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文系统综述14项研究，梳理精神科患者管理中人工智能应用面临的伦理挑战，包括隐私、监控、偏见、共情缺失与问责不清，并指出数据保护、透明度、人工监督和公平实施是接受AI的前提条件。

纳入判断：该文为伦理挑战综述，仅泛泛提及偏见与公平实施，未针对具体精神科任务提供实质性算法公平分析；无亚组指标或评估框架，摘要级证据亦不足以建议纳入。

限制：仅有摘要；未给出具体精神科疾病或预测任务、公平性指标、亚组分析或缓解方法；纳入证据多为认知调查，且主要来自高收入国家。

建议分类：Not applicable

证据：
- algorithm：This systematic review examines ethical challenges arising from the use of artificial intelligence (AI)
- evaluation：
- fairness：concerns about privacy, surveillance, bias, loss of empathy, and unclear accountability
- groups：
- medical：use of artificial intelligence (AI) in psychiatric patient management

[分析原文](https://europepmc.org/article/PPR/PPR1366535)

## p-6dc512fb49d7bb27a101

文章：[Factors associated with inequalities in antimicrobial-resistant bloodstream infections among socioeconomically disadvantaged populations in high-income countries: a systematic review protocol](https://europepmc.org/article/PPR/PPR1352179)

审核决定：待审核
审核备注：
证据版本：a0bbed0c8d653511340038071d1b7551b90db247117f5fc0bc9a39ad983724b2

模型建议：exclude

渠道核查：preprint；预印本不继承 CAS/CCF 等级，仅作为人工审核候选；未提供正式版本关联。

发现通道：recall

中文概述：该文为一项系统综述研究方案（PROSPERO注册），计划在OECD高收入国家人群中检索并综合与抗菌药物耐药血流感染（AMR BSI）及结局相关的社会经济剥夺、教育、族裔等健康不平等因素的观察性/干预/混合方法研究，采用PRISMA-P与PRISMA-E规范，并引入大语言模型辅助二次筛选。

纳入判断：属于流行病学健康不平等系统综述方案，研究问题为AMR BSI的社会经济与族裔差异，而非医学算法公平性；缺少受评估的AI/ML/算法以及算法公平性定义、测量或缓解评估，且方案阶段无实证结果，故不符合纳入标准。

限制：仅有摘要与方案文本，无任何结果、数据或偏倚评估结论；未涉及任何AI/ML模型作为受评对象，大语言模型仅用于文献筛选工具，未评价其公平性；未见算法层面的亚组指标、编码证据或缓解方法。

建议分类：Not applicable

证据：
- algorithm：
- evaluation：
- fairness：
- groups：factors associated with reported health disparities (e.g. deprivation score; education; ethnicity)
- medical：the burden of antimicrobial resistant (AMR) bloodstream infections (BSI) disproportionately affects populations

[分析原文](https://europepmc.org/article/PPR/PPR1352179)

## p-7f1d951b89c2475a87d3

文章：[Prognostic factors for cognitive intervention responsiveness in Parkinson's disease: a systematic review revealing inconsistent methodology and evidence.](https://pubmed.ncbi.nlm.nih.gov/42984867/)

审核决定：待审核
审核备注：
证据版本：f8fcb9a29c435ca7d6233eaad17042c7b00e15855953005e92529f123aecc333

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该系统综述汇总27项研究、835例帕金森病患者，考察认知干预反应性的预后因素和预测模型，发现基线认知较低与更大获益相关，但研究方法异质性大。

纳入判断：主题为帕金森病认知干预预后因素的系统综述，虽涉及预测模型和患者因素，但未提出或评估算法公平性、差异、编码或缓解问题，不满足公平性证据标准。

限制：仅有摘要；未报告算法公平性分析、亚组公平性指标、偏倚机制或缓解方法，无法判断其在医学算法公平性方面的贡献。

建议分类：Not applicable

证据：
- algorithm：prognostic factors and/or predictive models of responsiveness to cognitive interventions
- evaluation：
- fairness：
- groups：
- medical：cognitive interventions in PwPD

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42984867/)

## p-dfe423b65e59af94096b

文章：[Is More Perceived Empathy Better? Large Language Models, Communication, and Safety in Health Care.](https://europepmc.org/article/MED/43008223)

审核决定：待审核
审核备注：
证据版本：ea1bd0fdca7a18424d7e242219c8bc39e0b91a642d984d9e06ebed0b33cff173

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：该文是对一项LLM医患沟通共情能力系统综述的评论，指出AI生成回复在感知共情上优于医生，但强调研究多为模拟、异步、文本场景，缺乏随机试验、信任与安全性结局；主张在部署中加入本地验证、纵向审计、可读性与亚组差异审查、披露政策与监督机制。

纳入判断：虽涉及LLM医患沟通这一临床任务并提及亚组差异与健康素养公平风险，但属评论性文章，公平性论述为一般性治理与评估建议，缺少针对该任务的实质性公平分析（如亚组指标、机制或缓解方法比较），也无实测评估；按规则对仅有附带公平提及的评论应排除。摘要式之外的全文证据不足以支持suggest_include。

限制：全文为评论/观点文章，未提出新的评测设计、亚组指标或实测数据；公平性仅以“避免读者理解差距扩大”等一般性建议出现，未对特定任务给出实质性的算法公平分析与量化证据。

建议分类：Not applicable

证据：
- algorithm：large language model (LLM)–based tools in physician-patient communication
- evaluation：
- fairness：subgroup-level review to identify whether inaccuracies cluster by condition, language, age, disability
- groups：readability testing that includes low–health-literacy cohorts
- medical：communication as it actually unfolds in a clinical relationship

[分析原文](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13750628/fullTextXML)

## p-801228119b6cf272fa53

文章：[Potential and pitfalls of artificial intelligence to address disparities in epilepsy.](https://europepmc.org/article/MED/43064818)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

## p-22943fdfb12dc75e68da

文章：[Artificial intelligence in upper-limb, language and cognitive neurorehabilitation after stroke.](https://europepmc.org/article/MED/42929313)

审核决定：待审核
审核备注：
证据版本：1c77dcc1a303732041713f0fdbe7283d6d527befdb71fd6c977c5a50b6e792be

模型建议：exclude

渠道核查：eligible；精确匹配到 CAS 1/2 区期刊或 CCF A/B 主会记录。

发现通道：recall

中文概述：摘要综述AI在卒中后上肢、语言与认知神经康复中的研究现状，认为其在评估、个性化康复和扩大服务可及性方面有潜力，但尚未证明临床效用或优于其他数字康复手段，并提及小样本选择性数据集、隐私与公平性等关切，主张以伦理原则指导早期实施。

纳入判断：该文为综述，虽明确针对卒中神经康复这一具体临床任务，但对公平性仅作笼统提及（隐私与公平性关切、泛化的伦理建议），未提供亚组指标、偏差机制或评估框架等实质性算法公平性分析，不满足综述类纳入的双重条件；且仅有摘要证据，不满足纳入标准。

限制：仅有摘要：未给出具体数据集、结局指标、亚组结果或建模方法；公平性仅以“equity issues”一词带过，缺少机制、亚组度量或缓解方案的实质分析，无法判断全文是否含细致综述。

建议分类：Not verified

证据：
- algorithm：research into the use of AI has shown clear potential to enhance assessment
- evaluation：
- fairness：There remain concerns about small and selective datasets being used for modelling, privacy and equity issues
- groups：
- medical：upper-limb, language and cognitive neurorehabilitation research

[分析原文](https://europepmc.org/article/MED/42929313)

## p-e26f8e3e55f46fb001e5

文章：[Charting a human-Centered future: AI's promise and challenges for occupational therapy.](https://pubmed.ncbi.nlm.nih.gov/42762114/)

审核决定：待审核
审核备注：
证据版本：6b28e49c3f399d342f94da50ddb366aa37abe9e5319ff3abcaab1451bd2c0760

模型建议：exclude

渠道核查：pending；期刊或会议未在已核验的 CAS/CCF 注册表中精确匹配，保留待核验。

发现通道：recall

中文概述：该文为职业治疗领域的社论，讨论AI对职业治疗的科学出版、临床实践、教育与研究的影响，呼吁在AI开发与应用中坚持公平、可及、情境等专业价值，确保技术增进而非损害人类生活。

纳入判断：该文为社论，泛谈AI机遇、职业价值与公平可及等宏观议题，未指明具体疾病或临床任务，也未提供实质性算法公平性分析，属泛化伦理倡议类偶然提及，按规则排除。

限制：仅有摘要；未涉及具体疾病或临床任务，未提供任何算法公平性度量、分组指标、偏差机制或缓解方法等实质分析，也无实证评估。

建议分类：Not verified

证据：
- algorithm：
- evaluation：
- fairness：
- groups：
- medical：

[分析原文](https://pubmed.ncbi.nlm.nih.gov/42762114/)
