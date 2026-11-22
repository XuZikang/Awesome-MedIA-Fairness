# 医疗算法公平性文献摘要 · 2026-11-21

机器整理的候选与收录建议；未代表人工审核或实验复现。

候选库：341 篇；当日发现、更新或完成分析：215 篇。

已有有效中文分析：321 篇；待分析或缺少摘要证据：20 篇。

## 检索覆盖

- arxiv / 查询 4d95054412d0：1 条；完整
- arxiv / 查询 1d928560eb85：1 条；完整
- arxiv / 查询 1bb76ffa3406：0 条；完整
- arxiv / 查询 ab649b821460：2 条；完整
- arxiv / 查询 889f8ece294d：2 条；完整
- europepmc / 查询 d71eee65c043：2 条；完整
- europepmc / 查询 0013545bb3c4：5 条；完整
- europepmc / 查询 c227ae0068a5：1 条；完整
- europepmc / 查询 98f731ea147a：0 条；完整
- europepmc / 查询 f392a780813e：26 条；完整
- europepmc / 查询 4fbe2719fd72：12 条；完整
- pubmed / 查询 6d3220d57721：1 条；完整
- pubmed / 查询 a53b390db83d：3 条；完整
- pubmed / 查询 76fa0a7789bf：1 条；完整
- pubmed / 查询 4e705cd230bc：0 条；完整
- pubmed / 查询 12b1793035a0：31 条；完整
- pubmed / 查询 77caa6b8d3e4：16 条；完整

## 当日候选

### [Implications of Image-Level Duplication in Public Glaucoma Datasets.](https://europepmc.org/article/MED/43018943)

- 标识：`p-13cc881c6ffbf754dbd7`；发表：2026-11-12；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：待核验

该研究审计3个公开青光眼数据集，发现Harvard-GF与FairVision有1302眼匹配、1031眼为同一OCT volume，跨数据集分类AUC因泄漏升高0.12，且各种族亚组均出现膨胀，提示独立基准与公平性评估可能被高估。

限制：仅有摘要，缺少全文方法、亚组定义与样本量、公平性指标、代码/数据可用性等信息，无法确认详细公平性分析。

判断：该文为青光眼公开数据集重复审计，含记录链接和按种族亚组的性能膨胀测量，主题高度相关且摘要显示五项证据均具备；但仅有摘要，按规则不能建议纳入，需全文核实公平性分析细节与完整方法。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43018943)；模型：qoder-cn/dfmodel。

### [Applications of Fairness Training in Artificial Intelligence to Ophthalmic Disease Diagnosis using External Eye Photographs](https://europepmc.org/article/PPR/PPR1363752)

- 标识：`p-21b44eb38a70c944169c`；发表：2026-11-10；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Mitigation with Unverified Stage
- 状态：待核验

摘要报告利用40,687张外部眼照片开发深度学习与视觉语言模型，对威胁视力DR、晚期AMD和青光眼做二分类，并以ES-AUC评估性别、种族和族裔公平性，比较五种公平训练策略。报告称公平训练部分缩小差异并提升VTDR/AMD的AUC，但模型尚不适合临床部署。

限制：仅有摘要，无法核查五种公平训练策略的具体干预阶段、是否冻结基模型、亚组样本量、完整指标与代码/数据；亦无法判断全文是否包含更详细分析。摘要级证据不能建议纳入。

判断：摘要明确显示这是外部眼照片上的多病种分类与公平训练评估，直接相关；但仅有摘要，按规则不能据此suggest_include，且公平训练的具体阶段与完整结果无法核实，故暂hold。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1363752)；模型：qoder-cn/dfmodel。

Full-text access failed (ValueError); abstract retained.

### [FSD-Net: A Unified Skin-Tone-Aware Framework for Fair Skin Lesion Segmentation and Classification](https://europepmc.org/article/PPR/PPR1370450)

- 标识：`p-3daf0c4282bca4f685cf`；发表：2026-11-18；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、In-processing Mitigation
- 状态：待核验

FSD-Net在皮肤病变分割与分类两个阶段同时考虑肤色公平性：用连续肤色评分经FiLM调制ViT-B/16分割骨干，并用分割引导的ROI训练Swin-V2-Tiny分类器。在ISIC-2017/2018、PH2及HAM10000上报告Dice、准确率和Equalized Opportunity差距，并辅以消融、Bootstrap置信区间和McNemar检验。

限制：仅有摘要可用，缺少全文的方法细节、数据划分、公平性指标定义、基线配置及代码/数据可用性信息；无法独立核验框架各组件对公平性提升的贡献和结果稳健性。

判断：摘要显示该研究针对皮肤病变分割与分类评估肤色公平性，并报告分组指标、消融和统计检验，主题高度相关；但证据仅为摘要，按规则不能建议纳入，需全文核验后再定。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1370450)；模型：qoder-cn/dfmodel。

### [Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits](https://arxiv.org/abs/2611.23657)

- 标识：`p-52131ebbc4ad7c4a8714`；发表：2026-11-18；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：建议纳入，待审核

该文将固定模型的数值执行契约（FP64/FP32/TF32/FP8等）视为决策函数的一部分，在收入、就业、房贷和30天再入院任务上评估公平性审计结论的可复现性；提出审计稳定性协议，报告不同契约下统计量与通过/失败判定的范围。再入院任务按种族、性别和年龄分层，显示低精度部署可改变诊断性公平判定，但未证明FP8更公平。

限制：全文证据；临床仅一个公开糖尿病再入院数据集（1999–2008），4B模型在该任务近随机；多数改变判定的契约同时改变引擎、内核或权重，不能单独归因于算术精度；未观察临床部署或患者结局。

判断：文章明确以30天再入院风险预测为临床任务，审计多种模型并系统测量数值执行契约对人口学公平指标及审计判定的影响；包含种族/性别/年龄分层实证和稳定性协议，属于医学算法公平性评测方法贡献。

证据层级：full_text；[来源](https://arxiv.org/html/2611.23657v1)；模型：qoder-cn/dfmodel。

### [Reliable Skin-Tone Fairness in Dermatology AI: From Lesion-Level Leakage to Tone-Adaptive Learning](https://europepmc.org/article/PPR/PPR1345750)

- 标识：`p-53d198d32447f559a258`；发表：2026-10-20；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation
- 状态：待核验

提出面向皮肤镜与临床图像的色调自适应预处理流程，并建立按病灶分组、类别分层的评估协议，量化病灶级泄漏和肤色代理指标问题；在三个基准上报告深色皮肤敏感度提升，并发布泄漏审计工具。

限制：仅有摘要，无法核验全文方法细节、完整结果、消融统计及 leakaudit 实现；因此不能按纳入标准确认。

判断：摘要明确涉及皮肤色调公平性、三基准评估与预处理干预，五项标准均有摘要证据；但证据级别仅为摘要，无法核验全文，按规则不能建议纳入，故暂缓。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1345750)；模型：qoder-cn/dfmodel。

### [Governed Auditing of Hidden Failure Slice Discovery in Emergency Department Admission Models Agnostic to Sensitive Attributes](https://europepmc.org/article/PPR/PPR1363950)

- 标识：`p-802f852b1e8f331fe15d`；发表：2026-11-10；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation
- 状态：待核验

提出BASiC与ASAP，在急诊入院预测中利用临床规则和折外误差信号发现隐藏失败切片，并尝试样本加权修复。研究在Kaggle、RIPAS和NHAMCS数据上评估多种模型，发现切片发现较可靠，但修复未带来一致改善，且不建立人口统计学公平或临床有效性。

限制：仅摘要可用，无法核实全文是否包含受保护群体公平性分析、完整方法或代码；摘要明确不使用敏感人口学属性，且未证明人口统计学公平。

判断：摘要显示医学预测任务、多模型评估、失败切片发现与加权干预，但仅有摘要不能建议纳入；其属性无关审计与人口统计学公平的关系需全文确认。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1363950)；模型：qoder-cn/dfmodel。

### [Predicting Depression Risk Using Machine Learning Among Students](https://europepmc.org/article/PPR/PPR1362751)

- 标识：`p-8ba36d760ea51eb05928`；发表：2026-11-09；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

该研究基于27,900份学生问卷，比较逻辑回归、随机森林和XGBoost预测非临床抑郁风险，并进行性别公平性与SHAP/LIME可解释性分析；摘要称各模型准确率约84.5%–84.8%，性别差异较小。

限制：仅有摘要；摘要未报告公平性指标数值、数据划分、模型调参细节及完整方法，无法核实公平性评估的具体设计与结果稳健性。

判断：摘要显示该研究进行学生抑郁风险预测并对性别做公平性评估，但仅提供摘要，缺少具体指标和完整方法；按规则摘要级证据不能建议纳入，需全文核实。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1362751)；模型：qoder-cn/dfmodel。

### [Synthetic tabular healthcare data in health informatics: fixed-size substitution and incremental-value controls for predictive utility Application Paper](https://europepmc.org/article/PPR/PPR1358040)

- 标识：`p-8fc7d8cd62a109859e45`；发表：2026-11-04；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究构建合成表格医疗数据基准，在固定训练规模与增量价值两种设置下控制样本量和重复预测特征泄漏，评估高斯Copula、CTGAN、TVAE及三种分类器在糖尿病相关数据集上的预测效用，发现合成数据无普遍增益，并明确不涉及公平性结论。

限制：仅有摘要；未报告人口学分组、亚组指标、偏差机制或缓解评估，无法支持公平性审查。

判断：摘要聚焦合成数据预测效用与泄漏控制，虽涉及医疗预测建模和算法评估，但未提出或测量算法公平性问题，未定义受保护群体，公平性仅作为未验证事项被提及。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1358040)；模型：qoder-cn/dfmodel。

### [Causal-Weighted Machine Learning for RRT Prediction in Acute Kidney Injury: Development, External Validation, and Clinical Decision Support](https://europepmc.org/article/PPR/PPR1367120)

- 标识：`p-9bbed0421308d7921eb5`；发表：2026-11-13；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

该研究开发并外部验证了用于KDIGO 3期AKI患者48小时RRT启动预测的因果加权机器学习流程，采用堆叠集成与IPW元学习，并报告内部AUC 0.894、外部AUC 0.807；摘要还称公平性评估未发现具有临床意义的亚组差距，但未给出亚组定义或指标。

限制：仅有摘要；公平性仅一句结果性描述，未说明受保护属性、亚组划分、公平性指标、置信区间或具体差异，无法核验公平性评估的完整性与有效性。

判断：摘要显示该文为AKI-RRT预测的原创方法学与外部验证，并明确提及公平性评估及阴性亚组结果；但摘要未定义亚组/属性、未报告公平性指标或具体数值，且摘要级证据不足以支持纳入，需全文核实其公平性分析细节。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1367120)；模型：qoder-cn/dfmodel。

### [HIV-PrivFed: Privacy-Utility-Fairness-Aware Federated Learning for HIV Risk Stratification and Testing Prioritization Under Non-IID Clinical Heterogeneity.](https://europepmc.org/article/MED/43028461)

- 标识：`p-a4d951a2b8b867906d60`；发表：2026-10-30；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、EHR, Physiological Signals and Healthcare
- 状态：相关，待核实是否纳入

基于Sialon-II队列（13个欧洲城市MSM，13个自然客户端）开展水平联邦学习，比较十种传统分类器、集中式MLP及local-only/FedAvg/FedProx基线，提出差分隐私FedProx算法HIV-PrivFed，配备客户端级Rényi隐私核算与客户端级公平性审计（仅审计、不强制）。结果显示隐私预算远松于名义目标，客户端级估计不确定性高。

限制：仅见摘要：未报告任何客户端/亚组公平性数值，公平性仅审计未缓解；实际隐私预算（ε=22.1–224.1）无有效保证；队列规模小、无外部验证；摘要未说明代码或数据可得性，不能据此推断全文缺失。

判断：摘要明确给出HIV筛查临床任务、联邦模型实测评估、客户端级公平性审计及以13个城市客户端为分组，满足任务/算法/公平性/分组/实证五项要素；但仅有摘要级证据、未披露子组公平性结果且公平性未实施缓解，故不能建议纳入，按规则不作为suggest_include。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43028461)；模型：qoder-cn/dfmodel。

### [Design-based fairness monitoring for healthcare prediction with complex survey data.](https://europepmc.org/article/MED/42914067)

- 标识：`p-afe7ffeed3546c2df3d8`；发表：2026-10-22；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究提出基于复杂抽样设计的公平性监测框架，利用2015—2023年MEPS九轮数据，以随机森林预测高额医疗支出，并按性别、种族/民族和贫困状态评估人口均等与机会均等，估计设计校正的公平性差异及时间趋势。

限制：仅有摘要，无法核查全文的方法细节、敏感性分析、代码或数据可用性；摘要证据不足以建议纳入。

判断：摘要明确包含医疗支出预测、随机森林、公平性指标、受保护群体和设计校正的实证评估，符合五项标准；但证据级别仅为摘要，按规则不能建议纳入，需全文核实。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42914067)；模型：qoder-cn/dfmodel。

### [Explainable, Uncertainty-Aware Ensemble Learning for Brain Tumor Classification from MRI with a Simulated Fairness Audit](https://europepmc.org/article/PPR/PPR1365579)

- 标识：`p-c081b58879d4f9838b0c`；发表：2026-11-12；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

该研究构建了结合五种卷积网络和ViT的脑MRI肿瘤分类集成模型，评估校准、解释与不确定性，并用流行病学先验模拟年龄/性别标签进行公平性审计，报告各模型亚组差距较小且方向一致。

限制：仅见摘要，无法核实全文方法、代码与真实患者元数据；公平性标签为模拟生成，而非实际年龄/性别，亚组差距不能等同于真实临床差异。

判断：摘要明确报告脑MRI肿瘤分类及模拟年龄/性别公平性审计，但证据仅限摘要且亚组标签为流行病学先验模拟，无法确认真实患者层面的公平性评估，故暂缓纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1365579)；模型：qoder-cn/dfmodel。

### [Routine to Emergency: A Machine Learning Approach for Predicting ED Visits Among Patients with T2D](https://europepmc.org/article/PPR/PPR1358206)

- 标识：`p-cc9092de484d4c94f075`；发表：2026-11-04；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究利用EHR数据开发六种机器学习模型，预测2型糖尿病患者未来30/60/90天急诊就诊，并报告性别及种族/族裔亚组的判别与召回差异。摘要仅提供有限公平性结果，无法核实完整偏差分析。

限制：仅见摘要，缺少亚组样本量、公平性指标定义、阈值选择及置信区间等细节，无法评估公平性分析的严谨性与可复现性。

判断：摘要显示明确的T2D急诊预测任务、多种ML模型及按性别和种族/族裔的公平性评估，但证据仅限摘要，无法核实完整方法与公平性细节，故暂缓。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1358206)；模型：qoder-cn/dfmodel。

### [An Open, Reproducible Implementation of the CMS Hospital-Wide Readmission Measure on MIMIC-IV](https://europepmc.org/article/PPR/PPR1347611)

- 标识：`p-d5f34822605251a88ec8`；发表：2026-10-22；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：相关，待核实是否纳入

该文发布 CMS 医院全因再读入（HWR）指标的开放可复现实现：在 MIMIC-IV 上按计划性再读入算法与专科队列重建标签，使 30 天事件率由 17.6% 降至 15.9%（n=192,879），并公开编码表、Quan-Elixhauser 合并症编码与防泄漏特征规范，附校准基线模型（AUC 0.730），摘要称其做过亚组公平性与时间漂移评估。

限制：仅摘要层面：未给出任何亚组属性（种族、性别、年龄等）、公平性指标或亚组结果，也未说明公平性评估设计；无代码/数据链接证据。无法判断是否存在针对再读入任务的实质性公平性分析。

判断：属 EHR 临床预测任务的开放复现实现，摘要提到“亚组公平性评估”，但未定义分组、未报告任何亚组指标或公平性结论，公平性仅为评估清单中的一句提及；且证据仅限摘要，不能据此建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1347611)；模型：qoder-cn/dfmodel。

### [ECG foundation models share an age-related performance disparity that originates in the data, not the models](https://europepmc.org/article/PPR/PPR1357796)

- 标识：`p-e68fcceb7a02de0b9211`；发表：2026-11-02；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究在四个ECG基础模型、13个队列约540万份ECG上按年龄、性别和种族评估性能差异，发现差异主要集中于年龄并可在外部复现；未训练网络和经典特征模型也重现年龄差距，提示差异源于数据与任务而非预训练模型。

限制：仅提供摘要，缺少全文的方法细节、统计结果、代码与数据可用性信息及完整公平性分析；无法核验嵌入几何、缓解实验和外部验证的实施质量。

判断：摘要显示该研究涉及临床ECG任务、多个基础模型、明确的公平性差异评估及按年龄/性别/种族分层，并报告大规模实证结果，符合核心标准；但证据等级仅为摘要，按规则不能建议纳入，需全文核验后决定。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1357796)；模型：qoder-cn/dfmodel。

### [MelanoFusion: An Explainable and Uncertainty-Aware Hybrid CNN–Transformer Framework for Dermoscopic Melanoma Detection](https://europepmc.org/article/PPR/PPR1370178)

- 标识：`p-fd455cc2a36673f35d55`；发表：2026-11-19；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、In-processing Mitigation
- 状态：相关，待核实是否纳入

提出MelanoFusion混合CNN–Transformer框架用于皮肤镜黑色素瘤检测，结合可解释性、不确定性估计与公平导向表征学习；在HAM10000、ISIC 2018和PH²上评估，报告年龄组敏感性差异但性别无显著差异，并提示需外部验证。

限制：仅提供摘要，无法核验公平性指标细节、公平导向训练实现、统计检验及代码/数据；作者亦指出需外部验证与临床评估。

判断：摘要明确涉及皮肤镜黑色素瘤的年龄/性别亚组敏感性分析，属医学算法公平性相关研究；但证据仅为摘要，按规则不能建议收录，故列为related。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1370178)；模型：qoder-cn/dfmodel。

### [Deep Survival Analysis with Temporal Trajectory Embedding for Substandard Life Insurance Pricing: A DeepSurv Modeling Study of Type 2 Diabetes Mellitus](https://europepmc.org/article/PPR/PPR1360391)

- 标识：`p-12f4eff61a09eab3bddf`；发表：2026-11-06；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

该文以约188万份T2DM住院理赔记录构建DeepSurv定价框架，比较EM、GLM与Tweedie模型，并加入Elastic Net、LSTM、SHAP和Bootstrap稳健性检验；但仅在结论泛称提升定价公平性，未开展公平性分析。

限制：仅有摘要；未报告受保护属性、亚组指标、差异机制或公平性干预评估；公平性仅为结论性表述，无法判断全文是否包含相关分析。

判断：摘要仅在结论提及“改善公平性”，未定义群体或提供亚组/差异测量；属附带提及，且摘要级证据不足以建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1360391)；模型：qoder-cn/dfmodel。

### [A Multi-Model Framework for Explainable Sepsis Mortality Prediction With Dynamic Fairness and Drift Analysis.](https://europepmc.org/article/MED/43056270)

- 标识：`p-3f9a2ee2dec669d59e15`；发表：2026-11-19；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Mitigation with Unverified Stage、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究在MIMIC-IV上构建脓毒症死亡预测多模型框架，将公平性重新定义为动态生命周期属性，在15轮再训练与16个交叉子群中监测TPR、FPR、FOR差距，并开展eICU跨机构公平性审计与SHAP稳定性分析。

限制：仅有摘要，无法核查三种策略的干预阶段、统计与偏差控制细节及完整实验设计；按规则摘要级证据不能建议纳入。

判断：摘要包含临床预测任务、算法模型评估、明确公平性议题、交叉子群与实证测量，表面上符合五项标准，但证据层级仅为摘要，需全文复核后再定。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43056270)；模型：qoder-cn/dfmodel。

### [DRLCI: Dual-view Representation Learning Framework for Predicting Drug-Gene Interactions via Causal Intervention.](https://europepmc.org/article/MED/43013439)

- 标识：`p-009e12912fe734931786`；发表：2026-11-11；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

提出DRLCI双视图表示学习框架，用于预测药物-基因相互作用；通过关系感知图卷积、因果干预掩码和因果去偏对比损失抑制混淆因素，并融合医学先验文本，在DrugBank和DGIdb基准上报告最优性能。

限制：仅有摘要；未涉及算法公平性定义、受保护群体或亚组公平指标；所谓因果去偏针对硬负样本混淆，而非医疗算法公平性。

判断：摘要的医学任务和GNN方法明确，但公平性证据缺失：没有公平性/差异/编码/缓解研究问题，也没有定义群体或公平评估。因果去偏不等同于公平性分析，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43013439)；模型：qoder-cn/dfmodel。

### [DINOv3-SAM: Fusing Semantic and Anatomical Foundation Models for Robust Medical Image Classification.](https://europepmc.org/article/MED/42972189)

- 标识：`p-025d4680a20363b0f28f`；发表：2026-11-02；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

提出DINOv3-SAM双编码器框架，将自监督DINOv3的全局语义特征与冻结的SAM解剖感知特征空间对齐，经CBAM注意力精炼后用于儿科肺炎、心脏增大、RSNA肺炎、COVID-19胸片及皮肤病变分类，报告准确率与AUC提升并强调对数据集偏倚和跨域漂移的鲁棒性。

限制：仅有摘要，无法核查全文的公平性内容。文中未定义任何受保护人群或亚组，未报告亚组差异或公平性指标；"fair evaluation"指统一的分层训练/验证/测试协议，"dataset bias"指泛化鲁棒性，均不构成算法公平性证据。

判断：该文属通用多模态融合/鲁棒性分类方法，虽针对明确临床任务且经经验评估，但通篇未提出算法公平性、偏倚机制或分组差异问题，也没有任何受保护属性或亚组分析，属于仅泛泛提及"dataset bias"的鲁棒性工作，不符合公平性入选条件。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42972189)；模型：qoder-cn/dfmodel。

### [Multiview Integration for Robust Echocardiographic Embeddings: Accessible AI for Clinical Practice.](https://pubmed.ncbi.nlm.nih.gov/43050803/)

- 标识：`p-0aed599c7fa1f8e12a36`；发表：2026-11-18；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、In-processing Mitigation
- 状态：待核验

开发基于Transformer的多视角超声心动图编码器，将多段视频整合为研究级向量嵌入，并在21项二分类任务上评估；同时用对抗学习降低性别和种族捷径依赖，报告较强对抗权重下可预测性下降但临床性能受损。

限制：仅见摘要，无法核查对抗训练细节、公平性定义、亚组指标、统计方法与代码数据可用性；摘要未提供完整消融或外部验证。

判断：摘要显示明确的超声心动图临床任务、算法评估、性别/种族捷径公平性问题及实证测量，符合五项证据；但仅有摘要，不能据此建议纳入，需全文核验。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43050803/)；模型：qoder-cn/dfmodel。

### [Supporting Ergonomic Risk Assessment: An AI-driven Approach for Action Recognition Using Standard Video Recordings.](https://europepmc.org/article/MED/42925046)

- 标识：`p-0e20310c94fa66bd35f7`；发表：2026-10-23；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

提出并评估一种基于2D姿态与图卷积网络的视频动作识别方法，用于自动化OCRA工效学风险评估中的技术动作识别与计数；在37个制造场景数据上比较ST-GCN与2S-AGCN，准确率约60%。

限制：全文仅报告整体分类性能与基线比较，未按性别、年龄等群体分层，也未开展算法公平性、偏差机制或缓解效果分析；数据规模小且单中心，不能支持公平性结论。

判断：该文属于职业健康AI应用与方法评估，虽涉及工效学风险评估，但未提出算法公平性问题，未定义受保护群体或进行公平性测量；仅有隐私与不公平的泛泛提及，按附带提及规则排除。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13732331/fullTextXML)；模型：qoder-cn/dfmodel。

### [Radiology No-Show Calculator: A Social Determinants of Health-Enriched Machine Learning Prediction Model With Financial Analysis.](https://pubmed.ncbi.nlm.nih.gov/42660476/)

- 标识：`p-1582a8a2e3798f9bf7f2`；发表：2026-08-27；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究开发基于随机森林的放射科门诊失约预测模型，纳入区域剥夺指数等16个预测因子，并按人群患病率校准；报告AUC 0.760、ADI相关失约梯度和财务负担，提出针对高风险患者外展。

限制：仅摘要；未报告模型在各社会经济亚组的性能、公平性指标或缓解措施，无法判断全文是否有算法公平性评估；无代码或外部验证信息。

判断：摘要显示放射科失约预测与ADI梯度，但公平性主要为健康公平/财务表述，缺少模型亚组公平性测量；仅摘要无法确认全文分析，故暂缓。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42660476/)；模型：qoder-cn/dfmodel。

### [A preregistered simulation study provided evidence on the appropriate use of data-driven variable selection in descriptive multivariable regression modeling.](https://pubmed.ncbi.nlm.nih.gov/42486194/)

- 标识：`p-2076a6e307f6e08acb19`；发表：2026-07-23；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该预注册模拟研究比较流行病学描述性回归中的数据驱动变量选择方法（后退法与Lasso），评估变量选择率、模型选择率及回归系数偏倚，并提供方法选择决策框架；未涉及医学算法公平性、群体差异或公平性缓解。

限制：仅有摘要证据；主题为统计变量选择方法学，而非医学算法公平性研究。文中未定义敏感属性或受保护群体，也未报告亚组公平性指标、偏倚机制或缓解评估。

判断：文章评估回归变量选择方法的统计表现（TPR、FPR和系数偏倚），没有提出或测量算法公平性问题，也未定义受保护群体或进行公平性评估，因此不符合医学算法公平性纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42486194/)；模型：qoder-cn/dfmodel。

### [Computational Nutrition 2.0: From Static Models to Closed-Loop Agentic Systems for Personalized Nutrition.](https://pubmed.ncbi.nlm.nih.gov/42805435/)

- 标识：`p-220234c949e46cfa70a4`；发表：2026-09-28；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文为观点性文章，提出计算营养学2.0，主张以AI智能体推动个性化营养从静态模型走向闭环干预，覆盖代谢反应预测、营养因果推断、饮食相关疾病风险监测与营养政策模拟四个方向。

限制：仅有摘要，未提供具体方法、数据或实验；公平性仅在政策权衡中被附带提及一次，缺少亚组定义、公平性指标、编码证据或任何实证测量。

判断：属展望性评论：虽涉及营养健康任务与AI智能体，但未提出算法公平性研究问题，无群体定义、亚组发现或公平性评测，公平性仅为附带提及，且仅有摘要证据，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42805435/)；模型：qoder-cn/dfmodel。

### [Regional and national variation in donor and recipient characteristics, transplant practice, and outcomes after liver transplantation (the IMPROVEMENT collaborative): a multicentre cohort study.](https://europepmc.org/article/MED/42999582)

- 标识：`p-31cf3e898e1f39daf9dc`；发表：2026-10-29；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

IMPROVEMENT 多中心队列研究汇总 61 个中心、83 个病例序列、5218 例肝移植患者，覆盖五大洲，采用四步分析（世界地图、雷达图、笛卡尔图、混合效应预后模型）刻画供受体风险与风险缓解策略的区域差异，并建立 90 天、1 年、2 年死亡与并发症的预后算法，指出受者因素、冷缺血时间与中心体量是主要决定因素。

限制：全文为临床流行病学与预后建模研究：区域/国家差异属描述性结局比较，未定义算法公平性研究问题，未报告任何按人群分组的模型性能差异、偏倚机制或缓解方法比较；女性移植可及性仅在讨论中一句带过。

判断：具备医学任务（肝移植预后）与算法（混合效应预后模型），但全文的“差异/公平”讨论限于地区间医疗资源与服务可及性差异及结局描述，属医疗不平等而非算法公平性评估：无显式算法公平/偏倚问题、无亚组性能度量或缓解方法比较，五个判据中的 fairness 与 evaluation 均不成立，按规则排除而非作为相关文献推荐。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13743410/fullTextXML)；模型：qoder-cn/dfmodel。

### [BMR-Restormer: A transformer-based blind inpainting network for ultrasound marker removal.](https://pubmed.ncbi.nlm.nih.gov/42551183/)

- 标识：`p-3295b40be2839e3ffd5b`；发表：2026-07-25；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

提出 BMR-Restormer 盲修复网络，用于去除超声图像中烧录的人工标记（十字、文字、测量线），并评估标记对下游分类、分割、检测模型泛化性的影响，发现模型在含标记数据上训练后会过拟合伪特征，迁移到无标记图像时性能大幅下降。

限制：仅有摘要，未见全文方法细节、数据集构成与统计检验；研究关注标记伪影导致的伪特征过拟合，未涉及任何人群分组、敏感属性或亚组公平性指标，无法支撑算法公平性判断。

判断：该文属图像修复/鲁棒性研究：去除超声烧录标记并量化伪特征过拟合造成的性能下降，但未定义任何人口学或其他分组属性，没有亚组公平性度量、差异分析或公平性缓解方案；文中“bias”指伪相关捷径而非群体公平，属通用鲁棒性问题，不符合公平性准入标准，且证据仅为摘要。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42551183/)；模型：qoder-cn/dfmodel。

### [Improving Target-Adverse Event Association Prediction via Inverse Node Frequency Transformation to Mitigate Knowledge Graph Topological Bias](https://europepmc.org/article/PPR/PPR1373652)

- 标识：`p-3f6acf4e270b22ab1a5d`；发表：2026-11-20；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、Pre-processing Mitigation
- 状态：待核验

提出逆节点频率（INF）归一化方法，用于缓解生物医学知识图中因节点度数分布不均导致的拓扑偏倚（度偏倚），并以元路径特征为基础预测靶点-不良事件关联。结果显示INF提升了低度数靶点的召回率，并在外部未用于建模的关联集上优于两种基准，属知识图谱偏倚缓解类方法研究。

限制：仅有摘要级证据，未见方法细节、数据划分、统计检验或代码链接；所述偏倚为图拓扑/度数偏倚，摘要未涉及人群敏感属性或下游健康公平性分析。

判断：该文在药物安全任务中对图拓扑偏倚提出归一化缓解方法并给出低度数靶点的子群性能对比，符合偏倚机制与缓解的初步线索；但仅有摘要，无法确认其是否构成算法公平性问题的完整论证与评估设计，故暂持。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1373652)；模型：qoder-cn/dfmodel。

### [A Distributionally Robust Framework for Safe and Generalizable Utilization of Surrogate Markers](https://arxiv.org/abs/2611.18970)

- 标识：`p-410a2a1c61be26ff729a`；发表：2026-11-13；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

提出分布鲁棒框架评估替代终点：将跨治疗臂反事实依赖视为部分识别，通过最大化最坏情况解释方差学习替代标志物变换，并结合迁移学习与去偏机器学习处理协变量偏移。用模拟和CKD试验评估18个月GFR变化对两年GFR变化的替代性。

限制：全文未提出或评估算法公平性问题，未定义公平性群体、亚组差异或公平性指标；仅有临床替代终点效度与鲁棒性分析。

判断：该文满足临床任务、算法方法和实证评估，但核心是替代终点的部分识别与分布鲁棒估计，不是算法公平性、群体差异或缓解研究；无公平性定义、亚组比较或公平性测量，故排除。

证据层级：full_text；[来源](https://arxiv.org/html/2611.18970v1)；模型：qoder-cn/dfmodel。

### [Preoperative Mortality Risk Prediction and Equity Using Preoperative Score to Predict Postoperative Mortality in a Diverse US Surgical Population: Retrospective Cohort Study.](https://europepmc.org/article/MED/43050561)

- 标识：`p-46c871af6f5cd511e575`；发表：2026-11-18；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：建议纳入，待审核

该回顾性队列研究利用All of Us数据评估POSPOM术前死亡风险评分在17,262例手术患者中的判别与校准，并按种族/民族亚组描述30天和1年死亡差异；发现高危患者判别下降、黑人患者绝对死亡率更高但事件数少，提示需外部验证和重新校准。

限制：基于All of Us EHR数据，30天死亡仅12例，亚组分析为描述性且未做正式校准检验；未实施或比较缓解措施。

判断：评估POSPOM在多样化美国手术人群中的死亡预测及种族/民族亚组公平性，属任务特定算法公平审计；虽事件少且无缓解，仍符合纳入标准。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13781298/fullTextXML)；模型：qoder-cn/dfmodel。

### [ARBITER: retrieval-augmented generation for automated PROBAST+AI risk-of-bias assessment of HIV, HBV and HCV prediction models: a proof-of-concept validation study](https://europepmc.org/article/PPR/PPR1351930)

- 标识：`p-48b9e5d40beb02d005ae`；发表：2026-10-28；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

ARBITER 是一个基于检索增强生成（RAG，使用 Gemini 2.5 Pro）的工具，用于自动化完成 PROBAST+AI 偏倚风险评估：识别研究、区分建模与评价路径，并为每个信号问题给出分类判断及原文证据。在 10 项 HIV/HBV/HCV 预测模型研究上进行概念验证，与 Claude Sonnet 4.6 及人类统计专家对比，三者与专家共识均达到较高一致性（κ≈0.70–0.72）。

限制：仅有摘要，未见全文方法、提示词设计、样本构成与代码/数据可得性。评估对象是 PROBAST+AI 风险偏倚评定的一致性，不涉及任何人群分组、敏感属性或公平性指标，因此无法支撑算法公平性证据。样本仅 10 项研究，且其中 1 项用于流程迭代。

判断：该文属方法学/验证研究，任务是自动化风险偏倚评估而非算法公平性研究：摘要未提出任何公平性/差异性问题，未定义受保护人群或属性，也未测量亚组差异或实施偏倚缓解。风险偏倚（risk of bias）与算法公平性中的偏倚不同，故不满足公平性、分组两项核心标准，且非具名疾病下实质公平性综述，按规则排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1351930)；模型：qoder-cn/dfmodel。

### [Development and internal validation of a CSF-free machine-learning model to distinguish immune checkpoint inhibitor-induced encephalitis from HSV-1 and anti-LGI1 encephalitis](https://europepmc.org/article/PPR/PPR1354554)

- 标识：`p-4d243e183a986cc09be8`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于51例公开回顾性数据，构建并内部验证不含脑脊液特征的随机森林模型，用于区分免疫检查点抑制剂相关脑炎与HSV-1及抗LGI1脑炎，比较含或不含CSF、MRI特征时的判别力、校准与决策曲线表现，全程未涉及算法公平性分析。

限制：仅有摘要可查：样本量小（51例）、仅内部验证、校准差，且可能存在数据来源混杂。摘要未报告任何受保护属性、亚组比较或公平性测量，无法据此判断模型在不同人群中的差异表现。

判断：该文属脑炎鉴别诊断的机器学习模型开发与内部验证，具备临床任务、算法与实证评估，但未提出算法公平性或偏倚问题，也未定义受保护群体、开展亚组或公平性测量，不满足公平性相关判据，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1354554)；模型：qoder-cn/dfmodel。

### [Development and validation of early warning scores predicting 24 h mortality addressing intercurrent medical interventions in Denmark: a multicentre retrospective cohort study of 2·08 million hospital encounters.](https://pubmed.ncbi.nlm.nih.gov/42988715/)

- 标识：`p-515324d349beb4aea4b7`；发表：2026-11-05；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

摘要比较NEWS、简化NEWS、DEWS与XGB-EWS对24小时死亡的预测，使用倾向评分处理干预偏倚，并以净获益、AUC和校准评估，报告不同风险亚组的效用异质性。

限制：仅摘要；未报告按年龄、性别、种族等敏感属性的公平性指标或差异结果；“干预偏倚”指治疗混杂而非算法公平；摘要未提供代码或数据链接。

判断：研究是临床预测模型效用评估，虽提及亚组异质性和干预偏倚，但未提出或测量算法公平性/差异，也无可识别的敏感属性公平性分析；摘要证据不足以纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42988715/)；模型：qoder-cn/dfmodel。

### [Development and internal validation of a CSF-free machine-learning model to distinguish immune checkpoint inhibitor-induced encephalitis from HSV-1 and anti-LGI1 encephalitis](https://europepmc.org/article/PPR/PPR1355264)

- 标识：`p-66a0131f9ccb7890785d`；发表：2026-11-01；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

该摘要开发并内部验证一个不含脑脊液特征的随机森林模型，用于区分ICI相关脑炎与HSV-1及抗LGI1脑炎，报告AUC、校准和决策曲线等性能。

限制：仅有摘要，样本量51，缺乏外部验证；未报告任何公平性、亚组或敏感属性分析。

判断：研究聚焦诊断模型性能，未提出算法公平性问题，也未定义受保护群体或开展亚组/差异评估，故不属于医学算法公平性研究。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1355264)；模型：qoder-cn/dfmodel。

### [Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus](https://arxiv.org/abs/2611.22668)

- 标识：`p-67ee09e54a621a213502`；发表：2026-11-17；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、Post-processing Mitigation
- 状态：建议纳入，待审核

提出CHORD多视图去偏框架，通过多个表征视图提出类内分区，并在目标表征空间验证反转样本，无需组标注即可重训分类头；在CheXpert胸片二分类上报告WGA 71.43%，高于ERM的31.21%。

限制：医学证据仅限CheXpert单一胸片基准，且仅引用SubPopBench分组构造，原文未列明具体敏感属性或逐组公平性指标；方法为通用去偏框架，未见外部临床验证。

判断：文本明确在CheXpert胸片二分类上评估CHORD，使用SubPopBench分组并以WGA衡量，报告WGA 71.43%对ERM 31.21%，具备医学任务、算法、公平性、分组与实证五要素；虽为通用方法但有明确医学任务评估。

证据层级：full_text；[来源](https://arxiv.org/html/2611.22668v1)；模型：qoder-cn/dfmodel。

### [Antibiotic Choice for Community-Acquired Pneumonia in Children With Medical Complexity.](https://europepmc.org/article/MED/42838530)

- 标识：`p-72d2098ba0d9a6374d16`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该队列研究采用目标试验模拟与逆概率加权，比较儿童医学复杂（CMC）非重症社区获得性肺炎初始广谱与窄谱抗生素的结局。847例次住院中，广谱抗生素在至出院时间、进展为重症及30天再就诊方面与窄谱无显著差异，支持对多数CMC使用氨苄青霉素类。

限制：仅有摘要；研究为临床疗效比较，未涉及任何AI/ML算法，也未定义公平性概念、敏感属性或亚组差异测量；摘要未报告代码、数据或亚组结果。

判断：该文是抗生素选择的临床比较效果研究，使用倾向加权而非AI/ML模型，未评估算法公平性、偏见机制或缓解方法，缺乏本综述所需的五项证据，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42838530)；模型：qoder-cn/dfmodel。

### [A multimodal CT-based machine-learning model for differentiating pulmonary sarcomatoid carcinoma from conventional non-small cell lung cancer: an internally validated study](https://europepmc.org/article/PPR/PPR1348078)

- 标识：`p-7d6abfecd7636ea459d5`；发表：2026-10-22；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于三个中心的397例患者，比较临床-CT语义特征、影像组学与深度学习特征构建的六种模型，用于病理确诊前区分肺肉瘤样癌（PSC）与常规非小细胞肺癌；全融合模型AUROC 0.890，并分析采集参数异质性带来的残余混杂。

限制：仅摘要可得，无法核实全文的公平性分析。文中采集异质性属技术/站点混杂，未定义任何受保护人群属性，也未做亚组公平性指标或缓解措施评估。

判断：论文为PSC与c-NSCLC的CT多模态诊断模型开发与内部验证，虽具备临床任务、算法建模与实证评估，但缺少明确的算法公平性/偏倚问题及受保护群体定义或亚组发现方案；采集协议混杂属于稳健性与域偏移，不构成公平性研究，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1348078)；模型：qoder-cn/dfmodel。

### [Mediterranean Diet, Physical Activity, and Sleep in Endometriosis: An Age-Comparable Case-Control Study with Exploratory Machine Learning Discrimination.](https://pubmed.ncbi.nlm.nih.gov/43030256/)

- 标识：`p-871ab9f4cc09b5f81ad5`；发表：2026-10-31；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究为病例对照研究（177名女性，77例自报并经手术确诊的子宫内膜症），比较地中海饮食、体力活动、睡眠与症状指标，并用三种机器学习算法做交叉验证判别分析；最佳AUC-ROC为0.933，但限制于前置因素与饮食变量时仅0.67-0.73，作者认为判别主要反映并发症状而非营养因素。

限制：仅有摘要级证据；研究聚焦饮食、活动与症状的组间比较及判别性能，未涉及任何敏感属性分组、公平性指标、偏倚机制或缓解方法；年龄仅作为混杂因素校正，而非公平性分析维度。

判断：该文虽涉及子宫内膜症临床任务与机器学习算法评估，但通篇无算法公平性/差异/编码/缓解或公平性测量问题，也未定义公平性分组属性或亚组发现协议，仅有判别性能（AUC）报告，不符合纳入所需的五项证据标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43030256/)；模型：qoder-cn/dfmodel。

### [Self-report label bias in machine learning screening for undiagnosed diabetes: development, validation and offline on-device deployment of an interpretable HbA1c-anchored tool.](https://pubmed.ncbi.nlm.nih.gov/43033525/)

- 标识：`p-8e1089bbb872533b5f51`；发表：2026-11-10；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、Pre-processing Mitigation、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究基于NHANES与BRFSS数据，量化自报糖尿病诊断标签如何改变机器学习筛查模型优先识别人群的方式，显示自报标签部分编码了就医可及性；用正-未标记学习校正标签，并开发以HbA1c为锚点的可解释筛查工具，在相同转诊率下与指南规则比较敏感度并做离线部署验证。

限制：仅提供摘要级证据：亚组定义方式、公平性指标细节、标签校正方法的实现与部署评估均未展开；数据为单一调查周期的回顾性资料，外部验证样本小（388人）且需重新校准，缺乏前瞻性验证。

判断：摘要明确涉及标签偏倚（自报诊断编码就医可及性）、社会经济属性归因的比较分析以及经验性验证，五项标准在摘要层面均有对应证据；但按规则仅有摘要证据不能直接建议纳入，需获取全文核实亚组定义与公平性评估细节。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43033525/)；模型：qoder-cn/dfmodel。

### [Anthropometric and Psychological Variables Associated with Body Mass Index: A Sex-Stratified Evaluation of Students from a Romanian University.](https://pubmed.ncbi.nlm.nih.gov/43028626/)

- 标识：`p-923f4ac4a8b6eae7cf82`；发表：2026-10-24；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该横断面研究在445名大学生中分析颈围、BAI、指长比及心理变量与BMI分类的关联，并按性别分层建立回归与探索性ROC。颈围和BAI为主要相关指标，指长比具初步分类效用，心理指标无独立关联；未涉及算法公平性评估。

限制：仅有摘要；未报告算法公平性指标、亚组差异或缓解方法；样本为便利样本，阈值为内部探索性阈值，需外部验证。

判断：研究按性别分层分析BMI相关变量并做ROC，但未提出或测量算法公平性、差异、编码或缓解问题，故不属于医学算法公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43028626/)；模型：qoder-cn/dfmodel。

### [Learning from Maternal Mortality Confidential Enquiries: Sociodemographic Determinants Relevant to Equitable Guideline Development](https://europepmc.org/article/PPR/PPR1359271)

- 标识：`p-97c54bcea3ab95e0c708`；发表：2026-11-05；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该综述比较了16个高收入国家孕产妇死亡保密调查报告中社会人口学决定因素的报告差异，并据此制定国别公平清单以支持女性健康指南的制定与评估。全文未涉及任何AI/ML算法或算法公平性评估。

限制：仅有摘要；未列出具体社会人口学决定因素，无算法模型、亚组公平性指标或缓解方法比较，也未提供任何实证公平性测量结果。

判断：研究对象为孕产妇死亡监测报告与指南制定的公平清单，不存在被评估的AI/ML算法，也无算法公平性/差异测量或缓解实验；仅泛化地讨论监测报告中的公平议题，属偶然提及，按规则排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1359271)；模型：qoder-cn/dfmodel。

### [AI-powered radiology report simplification in Arabic: A prospective evaluation of patient-perceived understandability and clinical safety.](https://pubmed.ncbi.nlm.nih.gov/42546532/)

- 标识：`p-9d65abc11d11465e0b29`；发表：2026-08-01；发现：2026-11-14
- 主题：Clinical NLP and Foundation Models
- 状态：相关，待核实是否纳入

该研究前瞻性评估本地部署的两阶段大语言模型系统，将放射学报告简化为英语和阿拉伯语，报告患者可理解性及放射科医生判定的临床安全性，但未开展算法公平性分析。

限制：仅有摘要；未按语言、性别、年龄等分组比较公平性指标，也未评估偏倚机制或缓解措施；健康公平仅作为结论愿景提及。

判断：研究属临床NLP系统评估，涉及阿拉伯语患者可理解性与安全性，但未提出或测量算法公平性/差异，公平性为偶提，故列为相关。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42546532/)；模型：qoder-cn/dfmodel。

### [Association between patients’ knee posture and patient satisfaction in primary care consultations](https://europepmc.org/article/PPR/PPR1365698)

- 标识：`p-b1c2ba955b21e73bf64e`；发表：2026-11-12；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究探讨门诊咨询结束前30秒患者膝关节姿势与咨询后满意度的关联，203例患者中中立姿势组满意度高于伸展姿势组；属探索性观察研究，未涉及算法或算法公平性。

限制：证据仅为摘要，且为探索性观察研究；摘要未报告任何算法、敏感属性、亚组公平性指标或缓解措施。

判断：该研究分析膝关节姿势与门诊患者满意度的统计关联，未评估任何AI/ML算法，也未提出算法公平性、群体差异或公平性测量问题，不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1365698)；模型：qoder-cn/dfmodel。

### [AI-Based Prediction of Total Porosity Volume Fraction from 3D CT Volumes: A Volumetric Regression Approach](https://europepmc.org/article/PPR/PPR1370350)

- 标识：`p-b34d58a13643bfcc986f`；发表：2026-11-18；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

提出用带全局平均池化的3D CNN从含噪3D CT体积直接回归总孔隙体积分数，绕过体素分割；与Otsu阈值和随机森林基线比较，并分析合成数据中的捷径学习。

限制：仅提供摘要；研究对象为工业无损检测合成CT数据，不涉及临床任务、受保护群体或算法公平性评估；无法确认全文细节。

判断：该文是工业CT孔隙率回归方法，属于非医学无损检测；未提出算法公平性问题，未定义受保护群体或开展公平性测量，故不满足医学算法公平性纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1370350)；模型：qoder-cn/dfmodel。

### [When multi-institutional dataset aggregation masks shortcut-like behavior in Foundation Models for medical imaging.](https://pubmed.ncbi.nlm.nih.gov/42641372/)

- 标识：`p-b450c1e3be8d7e77257b`；发表：2026-08-22；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking、In-processing Mitigation
- 状态：待核验

该研究以乳腺X线摄影分类为任务，将预训练图像编码器（基础模型）作为特征提取器，在十个采集流程、人群与地区各异的队列上训练分类器，发现聚合异质数据会带来依赖数据集的失效模式，误差率、置信度与校准度在数据集间差异明显。表示层面可轻易恢复数据集身份而临床标签可分性较低，提示捷径式行为；测序向量分解显示任务信号多位于数据集对齐子空间。数据集对抗训练、最差组优化与平衡微调可缓解部分数据集聚差异，但常以总体性能下降为代价；探索性元数据分析还发现年龄相关的标签依赖性概率偏移。

限制：仅有摘要级证据：未见具体队列规模、划分方式、指标定义与统计检验细节，代码与数据可得性未提及；元数据探索（年龄）为探索性分析，未给出效应量；三种缓解方法的具体设置与冻结/微调范围不明，无法确认其是否真正固定基模型，因此干预阶段只能初步判断。

判断：摘要明确覆盖五项标准：乳腺X线摄影分类任务、以基础模型编码器为特征提取器、数据集层面的误差/校准差异与数据集身份可解码的编码证据、按数据集与地区划分的组别（并有年龄相关偏移）、以及在十个数据集上完成的实测与缓解实验。但证据等级为摘要，按规则摘要级证据不足以建议纳入，需全文核实指标、样本与缓解阶段后再定。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42641372/)；模型：qoder-cn/dfmodel。

### [A deep learning model for detection and staging of osteonecrosis of the femoral head on x-ray images: a retrospective, large-scale, multicentre study in China.](https://europepmc.org/article/MED/42934014)

- 标识：`p-b93a39c7c0676b99e9b3`；发表：2026-10-26；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

开发并多中心验证基于YOLOv8的X线髋部检测与分期模型OsteoAID，比较其与放射科及骨科医生的诊断表现，并以MRI为参照。

限制：仅有摘要；未报告按年龄、性别、种族、医院等群体的公平性分析，也无偏倚机制或缓解评估。

判断：摘要聚焦ONFH检测与分期的诊断性能及医生对比，未提出算法公平性问题，未定义敏感群体或开展亚组公平性评估，不满足纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42934014)；模型：qoder-cn/dfmodel。

### [Explainable Classification Models for Identifying Elevated Gastrointestinal Symptom Burden in Honduran Communities: A Cross-Sectional Study.](https://pubmed.ncbi.nlm.nih.gov/43028313/)

- 标识：`p-c4d939a39c87bfe230c4`；发表：2026-10-22；发现：2026-11-14
- 主题：待分类
- 状态：相关，待核实是否纳入

在洪都拉斯5省85个社区1838名12–49岁居民中，评估可解释的人口学与生活方式模型能否识别同时存在多种胃肠道症状负担；加入既往消化系统诊断后AUROC由0.663升至0.726，逻辑回归与复杂机器学习表现相当，并报告校准、决策曲线和亚组表现。

限制：仅摘要证据；未明确公平性属性、分组定义或公平性测量问题，仅有“亚组表现”的笼统表述，无法确认全文是否包含实质算法公平分析；亦无外部验证、代码或数据可用性信息。

判断：该文属于医学预测模型评估，但摘要未提出算法公平、差异、编码或缓解问题，也未定义受保护群体或公平性指标；仅有亚组表现的一般提及，且摘要级证据不足以建议纳入，故列为相关。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43028313/)；模型：qoder-cn/dfmodel。

### [Memory-guided mutual information optimization in retinal imaging for early stroke detection and subtyping.](https://europepmc.org/article/MED/43014078)

- 标识：`p-e325d3be42451c51b6cb`；发表：2026-11-09；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

提出 RetCEVD 框架，利用无创视网膜 OCTA 图像进行缺血性脑血管病（ICVD）辅助检测、病因亚型分型及症状状态分类，核心为记忆引导的互信息优化策略，在多中心 24,438 张图像上完成内部与外部验证并报告 AUC。

限制：仅有摘要：未报告代码、数据可得性、受试者人口学构成，也未涉及任何公平性/偏差分析、亚组指标或敏感属性，无法判断模型在不同人群中的差异表现。

判断：该文属原创方法学工作，但全文仅描述诊断性能与可解释性，未提出任何算法公平性、偏差机制、亚组比较或公平性度量问题，缺乏定义群体与公平性评估证据，故不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43014078)；模型：qoder-cn/dfmodel。

### [Multiparametric 0.4-T low-field MRI mapping for metabolic dysfunction-associated steatotic liver disease in rats.](https://europepmc.org/article/MED/43034251)

- 标识：`p-e7d4ce6f3482649fcced`；发表：2026-11-14；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

研究在90只MASLD大鼠中比较0.4-T MRI的T1、FcT1、T2、T2*和PDFF与全切片数字病理，并评估深度学习重建AIRS对T1定量的影响；结果显示各指标与脂肪、炎症、纤维化呈部分阶段依赖相关，AIRS可改变T1绝对值。

限制：全文为动物实验，仅评估MRI指标与病理相关性及AIRS重建的测量偏移；未定义算法公平性问题，未按敏感属性分组，也未进行差异或缓解分析。

判断：该研究评估低场MRI定量指标及深度学习重建对T1测量的影响，未提出或检验算法公平性问题，也未按敏感属性进行亚组比较，不属于医学算法公平性研究。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13769794/fullTextXML)；模型：qoder-cn/dfmodel。

### [Machine learning for maternal risk prediction in resource- constrained antenatal care: evidence-to-implementation gaps and implications for Sustainable Development Goal 3](https://europepmc.org/article/PPR/PPR1365530)

- 标识：`p-ebc11a06a333203c74b7`；发表：2026-11-12；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

该研究笔记梳理资源受限产前护理中孕产妇风险预测的机器学习证据，指出高准确率可能掩盖漏诊，主张在判别力之外同时评估校准、公平、工作流和前瞻性影响。

限制：仅有摘要；缺少具体公平性定义、受保护属性、亚组结果和缓解方法，公平仅作为评估维度被提及。

判断：摘要将“equity”和“subgroup assessment”作为实施评估清单或缺口一笔带过，未提供具体疾病场景下的亚组指标、机制或缓解分析；且仅有摘要，不能建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1365530)；模型：qoder-cn/dfmodel。

### [A Dual-Criterion Variable Inclusion Strategy for Improved Confounder Inclusion in Small-Sample Trauma Cohorts: An Empirical Methodological Study](https://europepmc.org/article/PPR/PPR1348111)

- 标识：`p-f352228a5c9bd18d0291`；发表：2026-10-22；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究在88例脑挫裂伤减压术后患者中提出双标准变量纳入策略，以改善小样本创伤队列的混杂因素纳入，比较ridge回归、随机森林及模型校准，发现该策略减少单阈值筛查的遗漏偏倚并影响危险因素识别。

限制：仅见摘要，无法核查全文方法细节、偏倚控制与统计假设；研究未涉及算法公平性、群体差异或缓解措施，且样本量小、单中心。

判断：该文关注小样本临床预测中的混杂变量筛选与模型性能，未提出或评估算法公平性问题，也无受保护群体、差异或缓解分析；不符合五项证据要求。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1348111)；模型：qoder-cn/dfmodel。

### [Causally Constrained and Uncertainty-Aware Cardiopulmonary Risk Prediction](https://arxiv.org/abs/2611.17819)

- 标识：`p-f6c51344bb4b7f0ff028`；发表：2026-11-13；发现：2026-11-21
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

提出CE-Agent两阶段心肺风险预测框架，将流行病学证据预先编译为因果约束，再拟合临床与胸部CT表型权重，并用闭式不确定性传播处理缺失输入；在NLST与MESA中评估判别、校准、跨医院与跨扫描仪泛化以及联合肺癌和心血管分诊。

限制：全文仅报告按医院、扫描仪及种族/民族分组的外部泛化与校准表现，未定义公平性目标、差异指标或任何缓解干预；亚组性能不等并不构成算法公平性证据。

判断：该文为心肺风险预测方法学研究，虽含种族/民族与扫描仪亚组泛化评估，但全文未提出或测量算法公平性、差异、编码或缓解问题，也未报告公平性指标；属于临床稳健性与域泛化研究，不符合公平性纳入标准。

证据层级：full_text；[来源](https://arxiv.org/html/2611.17819v1)；模型：qoder-cn/dfmodel。

### [Simulation-Based Development, Stress Testing, and External Physiological Benchmarking of a DKA Early-Warning Framework Intended for Future Nurse-Facing Evaluation.](https://pubmed.ncbi.nlm.nih.gov/43028810/)

- 标识：`p-fc980d34ff004464f5b8`；发表：2026-11-06；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究用两万条合成15小时DKA病程数据，对比验证冻结的BHB+趋势规则与XGBoost模型的灵敏度与误报率，并通过表型匹配的反事实生命体征、阈值网格和校准分析检验模拟器捷径，另用公开IOBP2数据做生理学外部基准，发现葡萄糖分布存在显著不匹配。

限制：仅有摘要，无全文方法、代码或数据链接细节；未涉及任何人群敏感属性；未报告按性别、种族、年龄等分组的表现差异；外部基准仅指向分布错配，不验证DKA预测或动力学。

判断：属模拟器构建偏差与外部生理分布错配研究（合成数据捷径、阈值网格、IOBP2基准），未提出算法公平性/差异问题，未定义任何人群子组或公平性指标，故不满足公平性与分组证据要求；其偏差机制为模拟器伪相关而非人群不平等。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43028810/)；模型：qoder-cn/dfmodel。

### [Hierarchical detection of neonatal brain pathologies using a two-stage deep learning framework from magnetic resonance imaging.](https://pubmed.ncbi.nlm.nih.gov/43031676/)

- 标识：`p-05c60193f5811117e901`；发表：2026-10-30；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究提出两阶段分层深度学习流程，基于新生儿T1/T2加权脑MRI，先用脑龄差筛查髓鞘化延迟，再用3-D ResNet-18进行正常、HIE与脑积水三分类，并报告阶段2 AUC为0.919。

限制：仅有摘要，缺少全文方法、代码和公平性分析；未报告人口学亚组、差异指标或缓解措施，无法评估算法公平性。

判断：摘要聚焦新生儿脑病理分层检测和模型性能，未涉及算法公平性、亚组差异、公平性指标或缓解方法，不满足公平性综述纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43031676/)；模型：qoder-cn/dfmodel。

### [Responsible Artificial Intelligence: Guiding Principles for Orthopaedic Surgery.](https://europepmc.org/article/MED/43037611)

- 标识：`p-11142b1729015cc61ea3`；发表：2026-11-16；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

本文为骨科领域负责任人工智能的指导原则类评论，提出透明与可解释、临床可靠性与价值导向、与人类价值对齐、算法公平、公平照护问责、临床专家监督六项原则，主张在肌肉骨骼照护中安全、公平地采用AI。全文仅在原则层面提及公平，未针对具体疾病或任务给出亚组指标、偏差机制或评估框架。

限制：仅有摘要，无具体骨科疾病或任务，无定义受保护群体、无亚组指标或实证测量结果，公平性仅作为六项原则之一被一句话提及，缺乏可核验的详细分析证据。

判断：属评论/指导原则类文献，仅泛泛提出公平原则与伦理治理建议，未命名具体骨科疾病或任务，也未提供实质性的算法公平分析（亚组指标、机制或评估框架），不满足评论类两项条件；且证据仅为摘要，不能据此建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43037611)；模型：qoder-cn/dfmodel。

### [SIGHT: A Methodological Appraisal Framework for Evaluating Large Language Models in Ophthalmology](https://arxiv.org/abs/2610.15958)

- 标识：`p-1d69c85a37b528600868`；发表：2026-10-11；发现：2026-11-14
- 主题：Clinical NLP and Foundation Models
- 状态：机器建议排除，待抽查

该文批判性综述眼科大语言模型评价研究，提出SIGHT五域二十项方法学评价框架，关注样本来源、盲法、对照公平性、配对数据处理与透明度，旨在提升研究内部有效性和临床相关性。

限制：仅摘要可见；无受保护属性、亚组指标、偏倚机制或缓解措施的具体信息；“fairness”为通用评价域，非算法公平性分析。

判断：摘要表明该文为眼科LLM评价的方法学框架，仅在框架域名称中出现“comparator fairness”，未提供算法公平性、群体差异或公平性实证测量；且仅摘要可见，按规则不能建议纳入。

证据层级：abstract；[来源](https://arxiv.org/abs/2610.15958)；模型：qoder-cn/dfmodel。

Full-text access failed (HTTPError); abstract retained.

### [Amino acid-based formula and &lt;i&gt;Clostridioides difficile&lt;/i&gt;-associated disease in infants: concerns regarding causal interpretation.](https://europepmc.org/article/MED/43018394)

- 标识：`p-1e7d50a645f4a3f54c29`；发表：2026-11-12；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

本文评论氨基酸配方喂养与婴儿艰难梭菌相关疾病关联研究，指出因果推断的混杂、事件数不足等方法学问题，并建议前瞻性研究设计；不涉及AI/ML或算法公平性。

限制：仅有摘要/评论文本，无AI或算法，也无子组公平性指标、机制或缓解评估；不能作为医学算法公平性证据。

判断：文章为儿科营养与感染领域评论，讨论AAF与CDAD关联的因果解释，未评估AI/ML算法，也未提出或测量算法公平性、子组差异或缓解方法，不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43018394)；模型：qoder-cn/dfmodel。

Full-text access failed (TimeoutError); abstract retained.

### [Between Obligations and Evidence: A Participatory Study of Translating the EU AI Act into Technical Requirements](https://arxiv.org/abs/2611.18439)

- 标识：`p-21e07c40e92ded8603f5`；发表：2026-11-13；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

该文通过32人参与式工作坊，围绕医疗疼痛估计、招聘与公共交通三个高风险场景，分析欧盟AI法案义务如何转化为技术需求、组织实践与合规证据，指出公平指标不能单独证明非歧视，并讨论监督、责任和部署变化导致证据失效。

限制：全文为定性工作坊主题分析；医疗疼痛估计仅为假设场景，未定义受保护群体，未报告亚组公平指标或实施医疗算法公平性测量，主要贡献在治理与证据有效性。

判断：文章属于AI法案合规的参与式治理研究，不是医疗算法公平性评估；虽提及疼痛估计场景和公平指标局限，但缺少定义群体与实证公平测量，未满足五项证据标准。

证据层级：full_text；[来源](https://arxiv.org/html/2611.18439v1)；模型：qoder-cn/dfmodel。

### [Healthcare providers' use and acceptance of translation technologies in multilingual healthcare settings: a cross-sectional study.](https://pubmed.ncbi.nlm.nih.gov/42919266/)

- 标识：`p-2f7dce3877d44026419f`；发表：2026-10-21；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

对443名医疗及心理社会服务提供者开展横断面调查，基于技术接受模型分析翻译技术使用与行为意向，发现感知有用性关联最强，并报告准确性、隐私及治理顾虑。

限制：仅有摘要，未说明翻译技术是否属AI/ML、具体工具与临床任务；无患者亚组公平性指标、偏倚机制或缓解评估；无法核验全文方法。

判断：该研究是翻译技术使用与接受度的横断面调查，仅一般性讨论语言障碍与公平照护；未评估具体医学AI/ML算法的公平性、亚组性能或偏倚机制，且仅有摘要，不能纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42919266/)；模型：qoder-cn/dfmodel。

### [Acute Stroke Classification Using Asymmetric Data Standardization and Orthogonal-Focal Loss Optimized CNN-ViT Cross-Attention Fusion: A Multicenter External Validation Study](https://arxiv.org/abs/2610.34529)

- 标识：`p-57d9615bd4c80bff0bd7`；发表：2026-10-25；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

提出一种用于急性卒中分型的CNN-ViT交叉注意力CAD系统，结合非对称预处理与正交焦点损失，并进行多中心外部验证；内部F1为95.48%，外部降至58–62%，报告硬件噪声相关域偏移及缺血性卒中敏感性偏低。

限制：仅基于摘要，未提供公平性/亚组分析、敏感属性定义或公平性指标；外部验证性能下降属于域偏移与稳健性问题，不能作为算法公平性证据。

判断：摘要聚焦卒中分型模型与跨中心泛化，未提出算法公平性问题，也未定义受保护群体或开展亚组公平性评估；仅报告域偏移和敏感性下降，按规则不足以纳入。

证据层级：abstract；[来源](https://arxiv.org/abs/2610.34529)；模型：qoder-cn/dfmodel。

Full-text access failed (HTTPError); abstract retained.

### [Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate](https://arxiv.org/abs/2611.22904)

- 标识：`p-62eefc78443f96579d03`；发表：2026-11-17；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、In-processing Mitigation
- 状态：建议纳入，待审核

该文审计小型临床联邦学习联盟中拜占庭鲁棒聚合的公平性，在3个FLamby数据集上比较8种聚合规则并运行54,214次实验。发现仅按客户端数量判断有效性会漏掉数据份额独裁；加权中位数、GeoMed与CC在单中心占比过半时崩溃；留出对照把性能下降分解为诚实数据损失与真实攻击损害；无权重规则会惩罚更新最异常的医院。

限制：证据为全文；仅3个数据集且n=4或6，模型多为线性或逻辑回归以及冻结特征，TCGA死亡样本少使区域指标噪声大；未按人口学属性评估公平性，并假设医院报告真实样本量。

判断：全文明确给出临床FL任务、8种聚合算法的实证审计、医院间影响与性能差异问题、医院分组及54,214次实证运行，五项标准均满足，故建议纳入。

证据层级：full_text；[来源](https://arxiv.org/html/2611.22904v1)；模型：qoder-cn/dfmodel。

### [Correcting historical bias in machine learning predictions of healthcare utilization in India.](https://europepmc.org/article/MED/43050464)

- 标识：`p-7abe2e1b40324a466501`；发表：2026-11-18；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：待核验

基于印度LASI 55,698名老年人数据，训练门诊和住院利用预测模型，比较全样本与排除未满足医疗需求子样本模型在不同社会经济与种姓亚组间的预测差异，并用SHAP和全国成本外推评估历史可及性差异的影响。

限制：仅有摘要，无法核查全文的模型设计、公平性指标、亚组分析细节、缓解措施及完整结果；不能确认代码或数据可用性。

判断：摘要显示该研究针对医疗利用预测开展亚组差异实证评估，具备算法、公平性问题、定义群体和测量证据；但仅有摘要，按规则不能建议纳入，需获取全文进一步核验。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43050464)；模型：qoder-cn/dfmodel。

Full-text access failed (TimeoutError); abstract retained.

### [Association between biological age acceleration and the risk of aortic valve stenosis: An observational epidemiologic and Mendelian randomization study.](https://pubmed.ncbi.nlm.nih.gov/42998401/)

- 标识：`p-92a449ec5369eaed3e6f`；发表：2026-11-07；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

研究基于RED-CARPET与ARIC队列及孟德尔随机化，评估KDM-BA和PhenoAge计算的生物学年龄加速与主动脉瓣狭窄风险的关联，发现BAA与AVS风险及严重程度相关，并提示KDM-BA加速可能具因果关联。

限制：全文为流行病学关联与孟德尔随机化研究，未提出或检验算法公平性问题；性别/种族仅作协变量或效应异质性亚组，无公平性指标、偏倚机制或缓解评估。

判断：该文研究生物学年龄加速与主动脉瓣狭窄的关联，虽使用年龄算法并做性别/种族亚组，但未围绕算法公平性、差异或缓解进行设计与测量，故不符合纳入标准。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13769574/fullTextXML)；模型：qoder-cn/dfmodel。

### [PVminerLLM: structured extraction of patient voice from patient-generated text using large language models.](https://europepmc.org/article/MED/42952888)

- 标识：`p-c1f95a81a24c991508ae`；发表：2026-10-27；发现：2026-11-14
- 主题：Clinical NLP and Foundation Models
- 状态：机器建议排除，待抽查

PVminerLLM 提出 PVminer 基准与一个监督微调的大语言模型，用于从患者生成文本中结构化抽取“患者声音”（如社会处境、就医参与等非临床信息），在代码、子代码与证据片段抽取上取得最高约 84%、81%、88% 的 F1，并声称小模型也可达到较好效果。

限制：仅有摘要。摘要只给出抽取任务的 F1 指标，没有子群定义、公平性度量、偏差机制分析或缓解方法；对“健康公平”仅有一句目的性表述，无任何实证公平性评估，也未提供数据或代码信息。

判断：该文是临床 NLP 信息抽取的模型与基准工作，属于原方法类，但公平性仅以“health equity”一句背景性提及出现，既未定义受保护群体/属性，也未设计公平性评测或偏差分析，五项准入标准中的公平性、分组与公平性测量均不成立；按规则属偶发提及，不作为相关文献推荐。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42952888)；模型：qoder-cn/dfmodel。

Full-text access failed (TimeoutError); abstract retained.

### [Association of Immunomodulatory Treatment with Long-Term Visual Outcomes in Behçet Uveitis: A Single-Center Retrospective Study.](https://europepmc.org/article/MED/43001002)

- 标识：`p-c2c763dae41b68b833ad`；发表：2026-11-09；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

单中心回顾性研究描述Behçet病相关葡萄膜炎的临床特征与治疗模式，并探索免疫调节治疗与长期视力结局的关联；未涉及人工智能算法或公平性分析。

限制：仅有摘要，样本量小（30例），为回顾性观察且存在混杂；全文不涉及算法、公平性、亚组公平性指标或缓解评估。

判断：研究评估免疫调节治疗与视力结局的临床关联，未评估任何AI/ML算法，也未提出公平性、偏倚或亚组差异问题；五项纳入标准均不满足。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43001002)；模型：qoder-cn/dfmodel。

### [Latent profiles of artificial intelligence ethical awareness and their association with professional identity among nursing interns: A multicentre cross-sectional study](https://europepmc.org/article/PPR/PPR1369288)

- 标识：`p-4e22d89fc1a2a51893ed`；发表：2026-11-17；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究对中国12家医院的550名护理实习生开展多中心横断面调查，采用潜在剖面分析基于AI伦理意识六个维度识别出三种意识类型，并比较其专业认同差异及与教育水平、AI熟悉度等因素的关联。

限制：仅有摘要，无全文方法、量表与统计细节；研究关注护理实习生AI伦理意识的潜在类别，未评估任何医疗AI算法的公平性或群体绩效差异，“算法公平”仅作为教育内容被提及。

判断：主题为护生AI伦理意识潜在剖面与专业认同的调查研究，未涉及对具体医疗AI/ML算法的公平性评估，也无敏感属性分组比较或偏见测量；“algorithmic fairness”仅在结论中作为伦理教育内容一笔带过，属于偶然提及，不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1369288)；模型：qoder-cn/dfmodel。

### [Advancing FAIR sharing for epidemiological, clinical and public health study data: the German National Research Data Infrastructure (NFDI4Health).](https://europepmc.org/article/MED/43037923)

- 标识：`p-85c646041c7ede02228d`；发表：2026-11-16；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该文介绍德国国家研究数据基础设施NFDI4Health的建设成果：通过健康研究枢纽、本地数据枢纽、FDPG门户、可互操作元数据模式、匿名化与合成数据工具、联邦分析框架等，提升流行病学、临床与公共卫生研究数据的FAIR（可发现、可访问、可互操作、可复用）共享水平。

限制：仅有摘要级证据；文中“FAIR”指数据管理原则，与算法公平性无关。摘要未提及对任何AI/ML算法进行亚组公平性评估、偏差测量或缓解实验。

判断：摘要聚焦健康数据的FAIR共享基础设施与元数据互操作，未涉及医疗算法公平性/偏倚问题，缺少定义的受保护群体或亚组发现协议，也无公平性实证评估。摘要中“AI support for metadata annotation”仅为元数据标注工具，并非被评估公平性的算法，故不满足纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43037923)；模型：qoder-cn/dfmodel。

### [Development and regional validation of a literacy-fair verbal cognitive screen for older adults in India.](https://europepmc.org/article/MED/43042671)

- 标识：`p-04210e1f154be8b67c44`；发表：2026-11-17；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking
- 状态：待核验

该研究在印度LASI-DAD队列（n=4096）中开发并验证完全口语化、无读写依赖的认知筛查模型Verbal-4，按识字水平分层比较AUC，并进行留一区域验证与临床CDR对照，报告不同识字组判别力相近且具独立预后信息。

限制：仅有摘要，缺少模型系数、公平性指标定义、缓解措施细节，也无代码或数据链接；按识字分组的公平性证据仅为单一亚组AUC对比，区域验证中判别力衰减原因未明。

判断：摘要显示研究针对识字相关测量偏倚开发并验证口语化痴呆筛查模型，并按识字水平报告分层AUC及留一区域验证，初步具备医学任务、算法评估、公平性问题、分组定义与实证评估五项要素；但证据仅为摘要，无法核实全文的公平性分析与亚组评估细节，故暂缓判断。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43042671)；模型：qoder-cn/dfmodel。

### [A Relational Framework for Artificial Intelligence-Assisted Shared Decision Making.](https://europepmc.org/article/MED/43028666)

- 标识：`p-0c8552b1982b0a8ff7f6`；发表：2026-10-28；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该定性框架综合文章提出AI辅助共享决策的关系框架，围绕AI输出的表面权威、可核验与可质疑性、偏好替代、不确定性与责任分散五项关系关切，转化为可观察的临床要求、临床测试与治理响应，并提出区分技术性能、决策过程、关系质量、公平、安全与治理结果的候选测量框架。

限制：仅摘要可获取；未报告具体疾病或临床任务、受保护群体定义、公平指标或任何实证测量，公平仅在候选测量框架中被概括提及，未展开机制、分组比较或缓解评估。

判断：摘要显示为AI辅助共享决策的通用关系与治理框架，仅将equity列为候选测量维度之一，缺少特定疾病或任务的算法公平分析、分组指标、偏差机制或缓解方法评估，也无算法公平的实证测量，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43028666)；模型：qoder-cn/dfmodel。

### [Improving the impact of medical student research through structured mentorship: a clinical research enterprise model.](https://europepmc.org/article/MED/42209435)

- 标识：`p-2ffcd2507b0c8b7fa267`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

本文介绍一个医学生临床研究企业式纵向导师制项目，报告2019—2025年的论文产出、引用和职业发展等结果，属于医学教育项目评估。文中仅笼统提及公平与人工智能工具使用，未涉及医疗算法公平性评估、偏倚机制或缓解方法。

限制：仅提供摘要，缺少完整方法、参与者特征和公平性相关分析；没有算法、分组属性、亚组指标或公平性实验证据。

判断：文章主题是医学生研究导师制与科研产出，不是医疗AI/算法公平性研究。公平仅作为教育培训可及性的泛泛目标出现，未评估算法偏倚、亚组差异或缓解措施。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42209435)；模型：qoder-cn/dfmodel。

### [Application of Explainable Machine Learning for Individualized Risk Stratification and Surgical Optimization in Geriatric Intertrochanteric Fractures.](https://pubmed.ncbi.nlm.nih.gov/42980212/)

- 标识：`p-4403cfa217b51b32b9c0`；发表：2026-11-03；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

该回顾性队列研究纳入628例股骨转子间骨折行头髓内钉固定的患者，用12个临床与影像变量构建随机森林模型预测内固定失败，并用SHAP分析内侧化进钉点与尖顶距（TAD）的非线性交互，发现内侧化进钉点在TAD超过25mm时具有缓冲效应（测试集AUC 0.877）。

限制：仅有摘要，无法核查模型细节、人群构成与亚组分析；文中未涉及任何公平性、亚组差异或偏倚测量内容，只有整体预测性能与生物力学解释。

判断：摘要聚焦股骨转子间骨折内固定失败的预测建模与SHAP可解释性分析，虽满足临床任务、算法评估与实证测量，但完全没有公平性、差异性、编码或缓解问题，也未定义受保护群体或亚组发现方案，属于与医学算法公平性无关的文献，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42980212/)；模型：qoder-cn/dfmodel。

### [Context is all you need: A causal framework for governing bias in clinical AI.](https://pubmed.ncbi.nlm.nih.gov/42993732/)

- 标识：`p-4d615fab90a24703edd1`；发表：2026-11-06；发现：2026-11-09
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking
- 状态：相关，待核实是否纳入

文章主张以因果与规范监督区分临床人工智能中临床合理与不合理的群体差异，提出六项标准、四种实现路径，以及兼顾临床敏感性与偏差降低的双向评估设想；未涉及具体疾病或实证实施。

限制：仅有摘要；属概念框架，未指明具体临床任务、队列或子组指标，所提标准与评估路径均未实施，无法核验。

判断：主题直接涉及算法公平，但为通用临床人工智能治理框架，未命名具体疾病或任务，且无已实施的实证或测量评估；摘要级证据不足以建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42993732/)；模型：qoder-cn/dfmodel。

### [Rethinking University Mental Health for the AI Era: From Crisis Response to Core Mission.](https://europepmc.org/article/MED/43013291)

- 标识：`p-99104d3f909768840511`；发表：2026-11-11；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

文章主张将大学生心理健康纳入大学核心使命，提出整合数字工具、分级照护与精准治疗算法的校园心理健康体系，并强调AI治理、安全与公平。

限制：仅有摘要；未提供具体算法公平性评估、亚组指标、偏差机制或缓解方法比较，公平仅作为治理原则被提及。

判断：该文为面向大学心理健康体系的评论/综述，未针对具体医学疾病或任务开展实质性算法公平性分析；公平与公平性仅出现在概括性治理建议中，缺少定义群体、测量或评估证据。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43013291)；模型：qoder-cn/dfmodel。

### [Building and Validating a Data-Governance Workflow for Artificial Intelligence-Based Tuberculosis Detection from Chest Radiographs, and Quantifying the Impact of Data Leakage.](https://europepmc.org/article/MED/42888308)

- 标识：`p-a036330c773f5ab14093`；发表：2026-10-16；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

提出七步数据治理流程（多源标准化、溯源管理、MD5/pHash/dHash 三重去重、患者级划分、不变性核查、肺分割、指纹版本冻结），在 46,410 张胸片、七个公开来源上量化去重缺失与随机划分造成的数据泄漏对 AUC 的影响，结论是泄漏量级依数据结构而定、必须被测量，治理流程使复用可验证。

限制：仅有摘要，未见全文方法与代码；文中不含任何公平性/亚组分析，未按人群属性分层报告性能；泄漏效应在三分类多源任务中不足 0.1 个百分点，主要见于单源探针任务，效应量有限。

判断：该文研究去重、患者级划分等数据治理与数据泄漏对 AUC 的虚高影响，属评测有效性与稳健性问题；摘要未提出任何算法公平性、偏倚机制、敏感属性分组或亚组指标问题，不满足公平性准则，故不纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42888308)；模型：qoder-cn/dfmodel。

### [Theoretical analysis of transfer learning for temporally dependent observations.](https://pubmed.ncbi.nlm.nih.gov/43023018/)

- 标识：`p-a3955dfee5639efddf72`；发表：2026-07-30；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

本文研究高维向量自回归模型下的迁移学习理论，提出两步迁移学习流程、辅助数据集的信息子集选择方法，以及两种用于参数推断的“去偏”技术，并在温和条件下建立理论性质，最后用模拟数据和EEG数据集检验经验表现。

限制：仅有摘要：所谓“debiasing”指统计推断中的偏差校正，与算法公平性无关；未见敏感属性、亚组分析或公平性度量，也未定义具体临床任务。

判断：该文为时间序列迁移学习的通用统计理论研究，摘要中的“去偏”是参数推断偏差校正而非公平性偏差；缺乏敏感属性分组、公平性度量或公平性评估，EEG仅作为示例数据，未构成医学算法公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43023018/)；模型：qoder-cn/dfmodel。

### [AI-Assisted Voice Analysis for Laryngeal Cancer: Primary Care Perspectives on Clinical Implementation](https://europepmc.org/article/PPR/PPR1371788)

- 标识：`p-a837a6597aee491abb27`；发表：2026-11-19；发现：2026-11-21
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

一项混合方法横断面研究，通过访谈（15人）与匿名问卷（16份）考察基层医生对持续性发声困难的处理方式，以及对语音人工智能用于喉癌风险分层的接受度。结果显示医生普遍将其视为决策支持而非替代临床判断，采纳取决于准确性、流程影响、监督、转诊路径及公平可及性等条件。

限制：仅为摘要级证据，样本量小且为描述性统计与主题分析，无算法模型、亚组指标或公平性测量；公平性仅作为实施条件被提及一次，缺乏对特定群体的定义或差异分析。

判断：该文为临床实施可行性与医生接受度的调查研究，虽涉及喉癌语音AI，但仅在结论中泛泛提及“equity、隐私与问责”，未定义受保护群体、未开展任何算法公平性测量或偏差机制分析，属于偶发提及公平性的文献，按规则排除而非列为相关。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1371788)；模型：qoder-cn/dfmodel。

### [Ethical guidelines for deploying artificial intelligence applications in the pathology field: Lessons learned from a prospective framework in a large tertiary care academic medical center.](https://pubmed.ncbi.nlm.nih.gov/42761742/)

- 标识：`p-a9324f28d8acd70d333c`；发表：2026-08-11；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement、Pre-processing Mitigation、In-processing Mitigation、Post-processing Mitigation
- 状态：机器建议排除，待抽查

文章讨论病理学AI中的年龄、性别、种族和族裔代表性偏差，提出覆盖治理、预处理、处理、部署和监测的伦理指南框架，强调公平使用与持续监测。

限制：仅见摘要；未给出具体病理AI任务、亚组指标、偏差测量结果或实证评估，也未见框架实施效果与代码数据信息。

判断：属伦理/治理指南类评论，仅泛称病理学领域，未命名具体疾病或AI任务，摘要也未提供任务特异性的详细公平性分析或实证测量；按规则排除此类泛化公平建议。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42761742/)；模型：qoder-cn/dfmodel。

### [AI alone will not transform healthcare: Learning Health Systems as the framework for responsible AI implementation.](https://europepmc.org/article/MED/43004359)

- 标识：`p-ae502679561d916dd517`；发表：2026-11-09；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

本文为评论文章，主张将医疗AI实施嵌入学习型健康系统（LHS），结合CFIR、ERIC、TEHAI等框架，强调持续评估、治理、子组监测与公平实施。引用美国医院调查指出AI采纳不均和偏倚评估不足，但未对具体临床任务开展算法公平性实证分析。

限制：仅评论/概念框架，无原始数据或实验；公平性讨论停留在系统层面的采纳差异、监测建议和治理清单，未提供具体疾病任务的子组指标、偏倚机制或缓解方法比较。

判断：文章类型为评论，虽提及AI偏倚评估和公平实施，但仅作一般性LHS/治理建议；未针对糖尿病视网膜病变或脓毒症等具体任务给出实质性算法公平性分析，也无实施的公平性测量评估，故排除。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13746506/fullTextXML)；模型：qoder-cn/dfmodel。

### [Background Bias Assessment and Mitigation in Plant Disease Detection Using EfficientNet-B0 with Image Processing](https://arxiv.org/abs/2611.00049)

- 标识：`p-af26ec6de648c002a857`；发表：2026-10-10；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

该文针对植物病害检测中 EfficientNet-B0 的背景捷径偏差，提出原图、仅叶片、仅背景三条件评估协议，并在 PlantVillage 上量化背景偏差系数，发现模型主要依赖叶片特征。属于农业视觉偏差评估，不涉及医学临床任务或受保护人群公平性。

限制：仅有摘要；未提供医学任务、临床数据或受保护群体/敏感属性定义；背景偏差不等于医疗算法中的群体公平性；未报告群体公平性指标或缓解效果。

判断：研究对象为植物病害检测，不属于 biomedical/clinical 任务；虽评估背景偏差并有三条件实验，但未涉及医疗算法、定义群体/敏感属性或群体公平性评估，不符合纳入标准。

证据层级：abstract；[来源](https://arxiv.org/abs/2611.00049)；模型：qoder-cn/dfmodel。

Full-text access failed (HTTPError); abstract retained.

### [Causal gradient intervention for debiased and evidence-grounded medical visual question answering.](https://pubmed.ncbi.nlm.nih.gov/42526079/)

- 标识：`p-b0b37535e71cc95770d9`；发表：2026-07-25；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement
- 状态：相关，待核实是否纳入

提出DE-CaGI因果梯度干预框架，用于医学视觉问答；通过辅助分支估计语言与视觉先验造成的捷径偏置梯度，在主干更新中抑制相关分量，并引入多任务证据监督与证据一致性约束，以提升答案准确性和视觉证据对齐。在VQA-RAD和SLAKE上验证。

限制：仅依据摘要，无法核查全文方法、代码与统计细节；研究针对语言/视觉先验和数据结构造成的捷径偏置，未涉及受保护人群属性或群体公平性指标。

判断：医学VQA任务与算法明确，并在VQA-RAD/SLAKE开展实证；但其偏置指捷径学习而非受保护群体公平，未定义敏感属性或公平性评估，故仅为相关研究，且摘要证据不能建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42526079/)；模型：qoder-cn/dfmodel。

### [Equipping the next generation: addressing the unmet need for artificial intelligence education at research performing organizations.](https://europepmc.org/article/MED/42888462)

- 标识：`p-bd98d28296dc8ae83062`；发表：2026-10-16；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

本文是一篇评论文章，基于对1200余名医学与生命科学学生及博士后的国际调查，指出生成式AI使用率高但缺乏正规培训与机构政策，并呼吁将AI素养纳入科研与临床教育，重审学术诚信框架，制定透明的负责任使用政策。文中仅在一般性建议层面提及识别幻觉与偏见、促进公平获取。

限制：仅有摘要层面证据。全文未涉及任何具体医学疾病或临床任务，也未对某个医学AI算法开展公平性测量、亚组比较或缓解方法验证；“bias”“equity”仅出现在通用教育政策建议中。

判断：该文为教育政策评论，焦点是科研机构中生成式AI素养与学术诚信治理。文中未界定具体临床/生物医学任务，也未评估任何算法的公平性（无亚组指标、无偏见机制分析、无实证测量），公平与偏见仅为泛泛的伦理建议，故不满足纳入所需的五项证据标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42888462)；模型：qoder-cn/dfmodel。

### [Is postoperative adjuvant therapy necessary for esophageal cancer patients with pathological complete response after neoadjuvant treatment?](https://pubmed.ncbi.nlm.nih.gov/42731259/)

- 标识：`p-c2d58d64ab882a71dc49`；发表：2026-09-10；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该回顾性队列研究纳入184例新辅助治疗后达病理完全缓解（pCR）的食管癌患者，采用IPTW比较术后辅助治疗与观察的生存差异，发现cT4a为独立预后危险因素，辅助治疗可降低并延迟复发，并提出按cT4a/cN分层选择辅助治疗的风险适应决策方案。

限制：仅有摘要，无全文方法学细节；研究为单中心回顾性队列，属临床疗效与预后分层分析，未涉及任何AI/ML模型的公平性评估、亚组公平性指标或偏倚机制。

判断：本文为食管癌pCR患者术后辅助治疗的临床预后研究，提出的“风险适应决策算法”是基于生存分析的临床规则，并非受评估的AI/ML系统；文中无算法公平性/偏倚/编码或缓解问题，也未定义敏感属性分组或公平性测量，五项证据标准中公平性、分组与公平性评估均不成立。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42731259/)；模型：qoder-cn/dfmodel。

### [Evidence of limited biases in probed language-based assessments.](https://europepmc.org/article/MED/43002526)

- 标识：`p-c3083ca58bc9a9905bcc`；发表：2026-11-09；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、Clinical NLP and Foundation Models
- 状态：待核验

该研究评估开放式心理健康自述经大语言模型嵌入加岭回归预测抑郁/焦虑严重度的公平性：1260名参与者的评估误差与性别、年龄、教育、就业、收入等社会人口学变量及语言特征关联有限，但症状越重评估偏差越大；对训练数据下采样可消除该偏差。

限制：仅有摘要，无法核实亚组样本量、统计检验细节、下采样等缓解策略的具体设计与效应量，也无法确认误差度量与临床可用性讨论；摘要中的“有限偏差”结论需全文佐证。

判断：摘要同时具备临床任务（抑郁/焦虑评估）、算法（LLM嵌入+岭回归）、明确公平性提问、受保护群体与实证测量五要素，并探索下采样缓解；但按规则仅摘要证据不足以建议纳入，需获取全文核实后判定。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43002526)；模型：qoder-cn/dfmodel。

### [C3E-RRG:Confounder-Aware Causal Evidence Coupling and Evolution for Chest X-Ray Report Generation.](https://europepmc.org/article/MED/42970651)

- 标识：`p-d62b2748ad6ed04dbe11`；发表：2026-11-02；发现：2026-11-09
- 主题：Bias Mechanisms and Measurement、In-processing Mitigation
- 状态：机器建议排除，待抽查

提出C3E-RRG，在胸片报告生成中融合语言先验与疾病共现以构建混杂变量，并通过跨模态证据一致耦合和双向因果演化抑制模板与共现引起的虚假相关；在IU-XRay和MIMIC-CXR上验证。

限制：仅有摘要；未定义敏感属性、人群亚组或公平性指标，文中bias指报告模板与疾病共现造成的混杂，不能证明人群间公平性差异。

判断：论文聚焦胸片报告生成的混杂因素与虚假相关，未涉及敏感属性、亚组比较或公平性评价，属于一般去偏/稳健性方法，不构成医学算法公平性研究。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42970651)；模型：qoder-cn/dfmodel。

### [Clinical AI in Canadian Community Hospitals: A Framework for Implementation Readiness.](https://europepmc.org/article/MED/42880210)

- 标识：`p-e91c09dd8b3e74599212`；发表：2026-10-15；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

提出加拿大社区医院临床AI实施准备框架，围绕情境有效性、社会技术工作流整合、人机依赖校准以及安全、公平与治理四个维度，通过模拟系统测试加以落实，并以CHARTwatch早期预警系统作为实践示例。

限制：仅有摘要；公平仅作为治理维度之一被提及，未针对具体临床任务报告亚组指标、偏倚机制或算法公平性测量，也未提供任何实证评估结果。

判断：摘要仅在实施准备框架中列出“equity”维度，属于泛泛的公平AI治理建议；未给出具体临床任务下的亚组分析、偏倚机制或公平性评估，按偶然提及规则排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42880210)；模型：qoder-cn/dfmodel。

### [Is it possible to vaccinate AI against bias? An exploratory study in epilepsy.](https://europepmc.org/article/MED/43014131)

- 标识：`p-ec7c0f5cb541d6dacee9`；发表：2026-11-10；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models、Mitigation with Unverified Stage
- 状态：待核验

该探索性概念验证研究在癫痫临床情景中测试提示指令能否减少六个大语言模型的诊断/治疗准确率差距。富裕与弱势复合画像在性别和社会描述上共同变化；结果按原评分规则重新计算，提示后汇总差距下降，但作者指出不能隔离社会经济偏倚或证明临床有效的去偏干预。

限制：仅提供摘要，无法核验完整方法、模型版本与全部运行；复合画像同时改变性别和社会描述，作者也明确不能隔离社会经济偏倚或确立临床有效去偏；摘要级证据不足以建议纳入。

判断：摘要显示其针对癫痫LLM诊断/治疗情景开展公平性测量和提示干预，并报告群体准确率差距，符合任务、算法、公平、群体和测量要点；但仅有摘要且作者承认无法隔离偏倚，无法核验全文细节，故保留待全文评估，不直接建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43014131)；模型：qoder-cn/dfmodel。

### [Large Language Models' Simulation of Patient Comprehension of Discharge Summaries: Multimodel Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42912964/)

- 标识：`p-ee8b2a7189a3d8b4887f`；发表：2026-10-22；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models
- 状态：待核验

该研究用4个当代LLM按教育、性别和医疗使用生成患者人设，模拟对出院小结的理解回答，并以模态绝对误差和序数距离比较其与99名人类参与者的对齐，考察各亚组公平性及思维链敏感性。

限制：仅有摘要，缺少全文方法、样本构成、统计检验、具体亚组数值及代码/数据信息，无法核验公平性评估的完整性和可复现性。

判断：摘要显示其评估LLM模拟不同患者群体回答的公平性，五项标准表面均满足；但证据仅为摘要，按规则不能建议纳入，需全文核验。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42912964/)；模型：qoder-cn/dfmodel。

### [Progressing From Association to Causation: Examining Prior Antibiotic Exposure and Antimicrobial Resistance Across Three US Health Systems Using Causal Machine Learning.](https://europepmc.org/article/MED/42878671)

- 标识：`p-ef01908a70510b22bc66`；发表：2026-10-15；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

利用双机器学习，在三个美国医疗系统的1,165,151次培养事件中估计既往90天抗生素暴露对同类耐药的因果效应，校正35个以上混杂因素，并用逆概率加权、E值、暴露窗口与剂量-反应敏感性分析及阴性对照进行稳健性验证；同时比较既往同类暴露者经验性治疗无效的比例。

限制：仅有摘要证据，无法确认全文是否含代码、数据或亚组分析；文中未定义任何公平性属性或亚组，机构间一致性属外部验证而非公平性差异评估。

判断：该研究以因果机器学习估计抗生素暴露与耐药的因果关系并支持处方优化，属因果推断与临床用药研究；未提出算法公平性/偏倚问题，也无按种族、性别、年龄或机构等群体的差异测量，混杂校正不等于公平性分析，故超出范围。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42878671)；模型：qoder-cn/dfmodel。

### [Crossing the Divide: From AI Awareness to AI Assurance in Nursing Administration.](https://europepmc.org/article/MED/43036953)

- 标识：`p-f1ccea6d3b9e79ddd33c`；发表：2026-11-16；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该文为护理管理视角的评论文章，主张把AI保障（治理、风险管理、持续监测）纳入护理领导职责，提出治理与问责、公平与偏倚缓解、临床性能与安全监测、透明与伦理、员工能力准备五个领导域，属政策与治理框架综述，未针对具体疾病或临床任务开展算法公平性分析或实证测量。

限制：仅有摘要：无具体疾病或临床任务、无亚组指标或偏倚机制分析、无数据集或实证测量；公平仅作为治理框架中的一项被列举，属泛化倡议，无法据此评估任何算法的公平性表现。

判断：文章为护理管理AI保障的评论/框架性论述，公平与偏倚缓解仅在领导域列表中被泛泛提及，未命名具体医学任务，也未提供亚组指标、偏倚机制、评估框架或缓解方法比较；无实证或详细的任务特异性综合，属偶发提及的治理类文献，且仅有摘要证据。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43036953)；模型：qoder-cn/dfmodel。

### [Deep Learning-based Semantic Segmentation of Dental Radiographs: Comparative Evaluation of PSPNet, DeepLabv3, UNet, and UNet++](https://arxiv.org/abs/2610.15061)

- 标识：`p-0a7ab584ceef7f910746`；发表：2026-10-10；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文在统一受控实验设置下比较 PSPNet、DeepLabv3、UNet 与 UNet++ 四种语义分割模型在 1269 张牙科X线片上的表现，考察图像尺寸与批大小的影响，并以 Dice、IoU、准确率、精确率及损失进行评价，UNet++ 取得最高 IoU 与 Dice。

限制：仅有摘要，无全文方法、代码或数据可得性信息；文中“fair”指公平受控的实验比较，未涉及任何人群、敏感属性或算法公平性分析，也未报告亚组指标。

判断：摘要显示该研究是牙科影像分割模型的性能对比，'fair'仅为实验条件控制之意；未定义受保护群体、未做亚组或差异测量，缺乏算法公平性问题与相应实证评估，属于偶然提及而非公平性研究。

证据层级：abstract；[来源](https://arxiv.org/abs/2610.15061)；模型：qoder-cn/dfmodel。

Full-text access failed (HTTPError); abstract retained.

### [Catalysing system reforms in Pakistan’s Healthcare and Health Professions Education: National Stakeholder priorities for strengthening policy and system Governance](https://europepmc.org/article/PPR/PPR1368269)

- 标识：`p-116d132a6a15a073e809`；发表：2026-11-16；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究通过2026年巴基斯坦健康与教育峰会的混合焦点小组讨论，汇集14名利益相关者对医学与口腔教育质量、治理监管、认证及卫生人力留存的看法，提出从投入型转向产出型认证、建立跨机构治理平台等改革建议。文中仅简要提及谨慎、有目的地整合人工智能，未涉及任何算法公平性评估。

限制：仅有摘要；定性政策研究，未评估任何AI/ML算法，无亚组指标、公平性度量或缓解实验；人工智能仅作为教育整合议题被提及。

判断：文章主题为巴基斯坦卫生专业教育与系统治理改革，属定性利益相关者研究；虽提及人工智能整合，但无算法被评估、无公平性/偏倚问题、无群体定义或实证测量，不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1368269)；模型：qoder-cn/dfmodel。

### [Direct Effects Multiplicative Inference (DEMI): causal prediction from pairwise clinical relationships, applied to antidepressant response.](https://europepmc.org/article/MED/42892463)

- 标识：`p-1423f020303a662753a5`；发表：2026-10-17；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

DEMI从All of Us提取4.3亿医学概念对关系，按时间顺序分解直接与间接效应并乘法聚合预测抗抑郁药应答；15种药物平均AUC 0.934，与逻辑回归0.935无显著差异。未评估公平性。

限制：仅摘要层面证据；缺少全文、代码或数据链接及任何按人群分组的公平性结果；不能据此推断完整论文没有相关分析。

判断：摘要仅报告DEMI与逻辑回归的AUC比较，未涉及算法公平性、差异、编码或缓解问题，也未定义受保护亚组；不满足公平性核心标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42892463)；模型：qoder-cn/dfmodel。

### [Connecting risk prediction to intervention: evidence from a randomized trial testing patient navigation and education to improve postpartum outcomes.](https://pubmed.ncbi.nlm.nih.gov/42705386/)

- 标识：`p-18c55d52c86dda3044c3`；发表：2026-09-07；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

该试点随机对照试验利用既往验证的产后医院使用风险计算器筛选高风险黑人个体，评估产后教育与患者导航干预的可行性和30天医院使用率；未评估算法公平性或偏倚。

限制：仅有摘要；研究聚焦干预可行性与临床结局，未报告算法公平性指标、亚组比较或偏倚分析，无法支持公平性评估。

判断：研究使用风险计算器招募高风险黑人个体并评估导航干预，但核心问题是可行性与临床效果，未提出或测量算法公平性问题；属偶然提及公平/公平照护，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42705386/)；模型：qoder-cn/dfmodel。

### [Anatomic Classifications and Functional Outcomes in Preaxial Polydactyly of the Hand.](https://pubmed.ncbi.nlm.nih.gov/42598942/)

- 标识：`p-1cf7f8e7a97808d0cb3c`；发表：2026-08-17；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究回顾性分析58例（59指）术前轴前多指的术后结局，比较Wassel-Flatt与JK解剖分类系统与JSSH、Rotterdam评分及再手术等结局的关联，并评估临时经关节K针固定的影响。全文为临床外科结局研究，未涉及人工智能或算法公平性。

限制：仅提供摘要，无全文、无代码或数据链接；研究本身不含AI/ML模型、亚组公平性指标或算法偏倚分析，也无任何算法公平性相关讨论。

判断：摘要聚焦多指畸形的解剖分类与手术结局比较，属于传统临床回顾性研究，未评估任何AI/ML算法，也未涉及算法公平性、偏倚或亚组差异度量，因此不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42598942/)；模型：qoder-cn/dfmodel。

### [Five-year risk of cardiovascular events in women with history of pregnancy complicated by fetal growth restriction.](https://europepmc.org/article/MED/43050674)

- 标识：`p-1de4b4c47fd32c7cf15f`；发表：2026-11-18；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该回顾性队列利用TriNetX数据评估胎儿生长受限与产后5年母亲心血管复合结局的关联，采用倾向评分匹配和Cox回归，未涉及AI/ML算法或算法公平性。

限制：仅有摘要；为观察性流行病学关联研究，未评估任何算法、亚组公平性指标或缓解措施。

判断：研究问题是FGR与心血管结局的流行病学关联，摘要未提及AI/ML模型、算法公平性/偏倚测量、受保护群体或公平性评估，不符合五项纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43050674)；模型：qoder-cn/dfmodel。

### [Age, tumor size, and therapy timing are associated with survival in primary spinal Ewing sarcoma: a nationwide analysis.](https://europepmc.org/article/MED/42928284)

- 标识：`p-1f518fcb9c579e3639fe`；发表：2026-10-26；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究利用国家癌症数据库分析原发性脊柱尤文肉瘤中年龄、肿瘤大小与治疗时机对生存的影响，训练五种机器学习生存模型，并用Extra Survival Trees和SHAP分析预后因素。

限制：仅有摘要；未提出算法公平性问题，未定义公平性保护属性，也未开展亚组公平性评估、偏倚机制或缓解分析；年龄及儿童/成人分组仅用于预后比较。

判断：摘要显示为脊柱尤文肉瘤预后与治疗时机研究，虽使用机器学习，但未涉及算法公平性、差异或缓解问题；年龄分组用于预后而非公平性评估，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42928284)；模型：qoder-cn/dfmodel。

### [Leveraging AI-ECG Technology for Early Notification and Tracking of AF Development (LATENT): A Randomized Controlled Trial.](https://pubmed.ncbi.nlm.nih.gov/42998297/)

- 标识：`p-263284ee8b9a724f7139`；发表：2026-11-07；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

LATENT为单中心、开放标签随机对照试验，评估AI-ECG风险分层引导的Holter监测能否提高新发房颤、房扑及前房颤心房表现的检出率。14 665名40–85岁无房颤史成人入组，主要复合终点为0.74% vs 0.48%（OR 1.54，P=0.046），作者自述结果统计学上脆弱、对1例事件重分类敏感。

限制：仅有摘要证据；未报告按性别、年龄、种族等敏感属性分层的检出率、误差或公平性指标；年龄与性别匹配仅用于减少确认偏倚，属研究设计而非公平性分析；无任何公平性测量或缓解方法，无法据此判断算法公平性。

判断：该研究是AI-ECG临床有效性的随机对照试验，满足临床任务与AI算法两项，但未提出任何算法公平性、差异、编码、缓解或公平性测量问题，也未定义敏感属性群体或开展亚组公平性分析；按基线AI风险分层的交互作用属临床效应异质性而非公平性分析，故不满足公平性、群体与公平性评估标准，予以排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42998297/)；模型：qoder-cn/dfmodel。

### [Digital twin control framework uncovers individualized cross-scale links between functional connectivity deviations, communication impairment, and molecular mechanisms in autism.](https://pubmed.ncbi.nlm.nih.gov/42918437/)

- 标识：`p-28fd16540d52d28aa2c6`；发表：2026-10-23；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究提出基于深度对比学习的数字孪生对照框架，量化自闭症个体的功能连接偏差，并将其与ADOS沟通评分及转录组、神经递质、线粒体等跨尺度机制关联。

限制：仅有摘要；未定义公平性敏感属性或亚组，未开展差异、编码、缓解或公平性指标评估；数字孪生对照用于疾病效应解耦，并非公平性反事实定义。

判断：研究聚焦自闭症个体化神经机制，虽使用AI并做实证关联，但未提出算法公平性问题、敏感群体或公平性评估，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42918437/)；模型：qoder-cn/dfmodel。

### [Confronting the Twin Divides: Data Bias and Infrastructure Gaps in AI-Driven Nutrition for the Global South.](https://pubmed.ncbi.nlm.nih.gov/42988168/)

- 标识：`p-2e0706f35cfba2dd0a08`；发表：2026-11-05；发现：2026-11-09
- 主题：Bias Mechanisms and Measurement
- 状态：待核验

评论讨论全球南方AI营养应用中的数据偏差与基础设施差距，提及FRANI应用及营养不良模型临床使用不足，呼吁在部署前加强本地数据主权、基础设施和治理。

限制：仅摘要；缺少方法、分组结果、定量评估与全文细节，不能确认是否满足详细公平性分析要求。

判断：摘要为观点评论，虽点名营养不良与食物识别，但仅有泛化的数据偏差与基础设施论述，未展示分组指标或具体公平性评估；仅摘要不足以判断全文，故暂缓。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42988168/)；模型：qoder-cn/dfmodel。

### [Prediction of Systemic Lupus Erythematosus from Genotype and Gene-Expression Data: Batch Correction and Leakage-Free Evaluation](https://europepmc.org/article/PPR/PPR1349594)

- 标识：`p-3d223ee6ca3da41000e6`；发表：2026-10-23；发现：2026-11-14
- 主题：待分类
- 状态：相关，待核实是否纳入

该研究利用30个候选单核苷酸多态性与6个基因表达数据集预测系统性红斑狼疮。采用均值型批次校正，并在每个训练折内重新估计预处理与建模以避免数据泄漏，按个体划分折；以ROC-AUC、PR-AUC和MCC及标签置换检验评估。表达模型AUC达0.837至0.915，但仅用研究标签即可达0.857，显示批次与疾病标签强混杂，留出整项研究时性能明显下降。

限制：仅提供摘要：未见以种族、性别、年龄或社会经济地位等受保护人群为分组的公平性指标、偏倚机制分析或缓解方法。年龄与性别仅作为单核苷酸多态性模型的协变量，批次与研究间差异属于泛化与混杂问题，摘要未将其构建为算法公平性问题，也无代码或数据可用性信息。

判断：摘要明确涉及疾病预测的机器学习建模与严格的无泄漏交叉验证，对医学算法评估方法学有参考价值；但全文未提出算法公平性、群体差异或编码偏倚问题，性别与年龄仅作为预测协变量，研究间批次混杂属站点泛化问题，不能单独构成公平性证据，故不满足纳入标准中的公平性与分组两项，不推荐纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1349594)；模型：qoder-cn/dfmodel。

### [It’s about time: Specifying time zero for target trial emulation in psychological research](https://europepmc.org/article/PPR/PPR1363496)

- 标识：`p-408fcf2c00db10ff8789`；发表：2026-11-10；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文是面向心理学研究的目标试验模拟（TTE）教程，重点讨论"时间零点"这一常被忽视的基石概念。作者系统枚举时间零点各组成部分的排列组合，说明其错位会引入选择偏倚、治疗后混杂、治疗依赖的合格性变化与不死时间偏倚，并提出决策框架与实践建议，以工作场所AI使用与员工倦怠为例进行演示。

限制：仅有摘要，缺少全文与具体分析细节；文中AI使用仅为暴露示例，未涉及医学影像或临床预测算法，也未报告任何算法的公平性评估、亚组指标或缓解方法。

判断：摘要内容为观察性研究因果推断设计（TTE与时间零点对齐）的通用方法学教程，非医学算法公平性研究：没有临床AI/ML算法被评估，没有受保护属性分组、差异度量或公平性定义，也未开展实证测量，不符合纳入的五项证据标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1363496)；模型：qoder-cn/dfmodel。

### [Adoption and perception of artificial intelligence by corresponding authors in orthopaedic research: A global cross-sectional study.](https://pubmed.ncbi.nlm.nih.gov/41825826/)

- 标识：`p-4aa4395b22cef533ddeb`；发表：2026-03-11；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该横断面调查评估骨科研究通讯作者对生成式AI的使用、态度、培训需求与披露实践，并按职业阶段和性别分析未来使用意愿。结果显示使用广泛但披露不足，男性性别与更积极的未来使用感知独立相关。

限制：仅有摘要；研究对象为作者态度与出版实践，未评估具体医学算法、临床任务或公平性指标，不能支持算法公平性纳入。

判断：主题为骨科研究者对生成式AI的认知与披露调查；虽提及AI偏见担忧及性别差异，但非医学算法公平性研究，缺少临床任务、算法系统、公平性测量或缓解评估，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/41825826/)；模型：qoder-cn/dfmodel。

### [Association between Alzheimer's disease and related dementias and postoperative outcomes after geriatric hip fracture surgery.](https://europepmc.org/article/MED/43013143)

- 标识：`p-4af28d0a37e706d529ca`；发表：2026-11-11；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

回顾性队列研究，纳入3312例65岁以上髋部骨折手术患者，按电子病历记录的ADRD状态分组，用多因素回归分析ADRD与术后并发症、ICU入住、再入院及1年死亡率的关系，发现ADRD独立关联更差结局。

限制：仅摘要可及；研究为临床流行病学关联分析，未涉及任何AI/ML算法、模型编码或算法公平性评估；ADRD为临床暴露变量而非受保护的公平性属性，也未开展亚组公平性度量。

判断：该文评估痴呆与髋部骨折术后结局的临床关联，属传统观察性研究，既无被评估的AI/ML算法，也无算法公平性/偏倚/缓解问题，不满足algorithm与fairness两项核心准入条件。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43013143)；模型：qoder-cn/dfmodel。

### [International Consensus on Artificial Intelligence in Undergraduate Dental Student Assessment: A Two-Round Modified Delphi and Live Consensus Study](https://europepmc.org/article/PPR/PPR1359981)

- 标识：`p-4f82f9f44262ebd27f40`；发表：2026-11-04；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究通过两轮改良德尔菲法及现场共识投票，形成本科牙科学生评估中使用生成式人工智能的国际共识原则与评估形式分类建议，强调治理、披露、问责、数据保护与AI素养，但未评估任何具体算法。

限制：仅有摘要；属于牙科教育评估的治理共识，非临床或影像算法研究。公平性仅以“equity”一词在意见归纳中附带提及，未定义受保护群体、未报告亚组指标或偏差测量。

判断：该文为牙科教育评估中AI使用治理的德尔菲共识，缺乏被评估的医学AI/算法、明确的算法公平性研究问题、受保护群体定义及实证公平性评估；公平性仅为附带提及，属incidental mention，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1359981)；模型：qoder-cn/dfmodel。

### [It’s about time: Specifying time zero for target trial emulation in psychological research](https://europepmc.org/article/PPR/PPR1363497)

- 标识：`p-58c16252ff091a586ebd`；发表：2026-11-10；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

摘要介绍目标试验模拟（TTE）及“时间零点”在心理学观察性因果研究中的设计作用，讨论时间零点错位导致的偏倚并提出决策框架，以工作场所AI使用与员工倦怠为例。未涉及医学算法公平性、受保护群体或实证公平评估。

限制：仅依据摘要；文章为因果推断教程，未提供医学算法、公平性指标、群体比较或实证测量，无法作为医学算法公平性研究纳入。

判断：摘要聚焦心理学观察性研究的TTE时间零点与因果偏倚，虽提及工作场所AI，但未评估医学算法，也无公平性、群体或实证公平测量，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1363497)；模型：qoder-cn/dfmodel。

### [Longitudinal AI-based home-cage monitoring of locomotor aging in C57BL/6J mice: An exploratory pilot study.](https://pubmed.ncbi.nlm.nih.gov/43052603/)

- 标识：`p-61addd093647a7caaf49`；发表：2026-11-18；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

该探索性先导研究利用AI家庭笼监测系统（DOME）对C57BL/6J小鼠连续行为记录长达9个月，筛选出四项跨队列一致性较高的运动学指标，并按性别归一化以处理雌雄二态性，进而构建候选的运动源性行为衰弱指数（bFI），并在27月龄小鼠中初步观察到其与临床衰弱指数（CFI）的正相关。

限制：仅有摘要，缺少方法、统计与亚组分析细节；样本仅20只小鼠、4个笼具（4个独立实验单元），作者自述需更大规模重复队列验证；未报告任何算法公平性指标、亚组性能差异或缓解方法的定量评估。

判断：该研究属临床前动物行为表型研究，文中出现的队列特异性偏倚与性别二态性归一化属于批次效应与生理差异处理，未构成针对医学算法的公平性、差异性、编码或缓解问题的界定与测量，也无亚组公平性指标或缓解方法比较，属偶然提及，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43052603/)；模型：qoder-cn/dfmodel。

### [Medical leadership between motivation and organisational support: findings from a contemporary survey.](https://pubmed.ncbi.nlm.nih.gov/42814092/)

- 标识：`p-6e502862f36dba96cf40`；发表：2026-10-28；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文报告一项国际横断面问卷调查，分析临床与非临床医疗领导者在领导动机、组织支持（受保护时间、决策支持、共享治理）方面的差距，并将累积支持缺失与感知领导影响力和压力/倦怠关联，提出“动机—支持缺口”框架。

限制：仅有摘要；为自愿参与、滚雪球抽样的横断面自报调查（143人，76%来自意大利），无客观治理或绩效指标。未评估任何AI/ML算法，也未开展算法公平性测量；公平与AI仅作为背景性表述出现。

判断：主题为医疗领导力与组织支持调查，非医学算法公平性研究。文中未评估AI/ML算法，无明确公平性/差异问题、受保护群体定义或亚组公平性测量；仅有泛化的公平与AI决策支持背景提及，不满足纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42814092/)；模型：qoder-cn/dfmodel。

### [Formation of calcium oxalate kidney stones is related to consumption of some ultra-processed foods: a case-control study.](https://pubmed.ncbi.nlm.nih.gov/42470774/)

- 标识：`p-71348eabce0902da8421`；发表：2026-06-23；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究为德黑兰开展的病例对照研究（366人），用147项食物频率问卷和NOVA分类评估超加工食品摄入与草酸钙肾结石的关联，采用多因素logistic回归。结果显示甜食类摄入与结石风险升高相关，乳制品摄入与风险降低相关，但总超加工食品摄入无显著关联。

限制：仅有摘要，缺少完整方法、食物分类细节与偏倚控制信息；作者自述存在回忆偏倚，且结果为关联性而非因果。全文未涉及任何算法、模型或公平性分析。

判断：本文是膳食因素与肾结石的流行病学病例对照研究，使用传统统计回归，不涉及人工智能/机器学习算法，也无算法公平性、偏倚机制或亚组性能评估问题，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42470774/)；模型：qoder-cn/dfmodel。

### [SGLT2 Inhibitors and Risk of Postmenopausal Bleeding in Women: An Active-Comparator, New-User Cohort Study.](https://europepmc.org/article/MED/42957436)

- 标识：`p-743354216635218b0792`；发表：2026-10-29；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究为药物流行病学队列分析，利用 All of Us 数据比较 55-90 岁女性新使用 SGLT2 抑制剂与 DPP-4 抑制剂后绝经后出血风险，采用倾向评分匹配与 Cox/Poisson 模型；结果显示风险无显著升高（HR 1.14，95%CI 0.70-1.84）。

限制：仅有摘要，无全文；研究对象为药物安全性而非算法；未涉及任何 AI/ML 模型、公平性指标、受保护亚组比较或偏倚机制分析，无法提供算法公平性证据。

判断：该文是药物不良事件的安全性队列研究，虽按女性人群分析，但未评估任何 AI/ML 算法，也无算法公平性、亚组差异或缓解措施问题，属于非算法公平性文献，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42957436)；模型：qoder-cn/dfmodel。

### [Toward equitable fidelity measurement of evidence-based psychosocial interventions.](https://europepmc.org/article/MED/42956225)

- 标识：`p-90e758f61454cf309cc5`；发表：2026-11-01；发现：2026-11-09
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

摘要讨论心理社会循证干预中临床医生保真度（fidelity）测量的公平性问题：观察性保真度编码成本高、在资源匮乏环境中很少使用，且编码方案源自以白人、中产为主的临床试验人群。作者基于健康公平实施框架提出考量，并介绍标准化病人、片段编码和AI自动评分等探索，但未报告算法公平性的实证评估。

限制：仅获取摘要，无全文；摘要未给出任何子组指标、评估设计或实证结果，AI自动评分仅作为“在研工作”被一笔带过，无法确认文中是否存在针对算法系统的公平性分析。

判断：该文属评论/展望，讨论的是保真度测量工具本身的公平性考量与实施科学问题，并未评估某一AI/ML算法的公平性；摘要缺乏算法被评估、子组实证测量等证据，属公平性偶提及的评论，按规则排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42956225)；模型：qoder-cn/dfmodel。

### [Circulating miRNA profiling identifies hsa-miR-23a-3p and a three-miRNA signature associated with serous ovarian cancer](https://europepmc.org/article/PPR/PPR1373555)

- 标识：`p-9248ffc4421b28b6931d`；发表：2026-11-20；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

研究比较卵巢癌患者与对照血浆中8种miRNA，发现hsa-miR-23a-3p及三-miRNA逻辑回归模型具中等区分度，并报告交叉验证后性能下降及样本来源/技术变异等混杂因素。

限制：摘要仅报告病例对照生物标志物性能与内部验证，未涉及算法公平性、亚组差异、敏感属性或缓解措施，无法评估公平性贡献。

判断：研究为卵巢癌循环miRNA生物标志物区分病例与对照，未提出或评估算法公平性、亚组差异、敏感属性或缓解措施，仅有ROC/AUC性能，不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1373555)；模型：qoder-cn/dfmodel。

### [Treatment intensity and survival benefit among older adults with glioblastoma: A population-based analysis.](https://pubmed.ncbi.nlm.nih.gov/42710195/)

- 标识：`p-a11377379ca4050b6b0d`；发表：2026-09-07；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于SEER数据库（2000-2020）回顾性分析21,206例≥65岁胶质母细胞瘤患者，描述手术、放疗与化疗联合治疗强度的年龄趋势，并用中位生存期和24个月限制平均生存时间（ΔRMST0-24）评估各年龄层的绝对生存获益，发现高龄与接受三联治疗概率降低相关，但强化治疗在各年龄层均与更长生存相关。

限制：仅有摘要，无AI/ML模型、无算法公平性指标或缓解方法；年龄分层属临床预后分析，且作者自述存在未测量混杂与永生时间偏倚。

判断：该文为基于登记数据库的流行病学队列研究，评估年龄与治疗强度及生存关系，未涉及任何AI/ML算法被评估，也无算法公平性、偏倚编码或缓解问题；年龄分层不构成算法公平性研究，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42710195/)；模型：qoder-cn/dfmodel。

### [Systemic ethics framework for artificial intelligence in nursing and healthcare.](https://pubmed.ncbi.nlm.nih.gov/42989488/)

- 标识：`p-a13199f8b00c3ef3f702`；发表：2026-11-05；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

该文通过整合综述提出护理与医疗AI的系统性伦理框架，归纳规范基础、治理问责、信任透明、数据正义与公平、生命周期伦理等八个概念轴，并构建微观—中观—宏观多层次模型，强调问责安排、人类监督与制度支持。

限制：仅摘要可见；未提供具体疾病或临床任务，也未报告算法公平性定义、亚组指标、偏差测量或缓解评估；数据正义与公平仅作为伦理轴被泛述。

判断：属护理与医疗AI伦理框架综述，虽提及数据正义与公平，但缺少具体临床任务及实质性算法公平性分析（无亚组指标、偏差机制或评估框架），属泛化伦理建议与偶然提及，故排除；摘要级证据亦不足以支持纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42989488/)；模型：qoder-cn/dfmodel。

### [Evaluation of chromosome-level structural variation for acute myocardial infarction risk prediction](https://europepmc.org/article/PPR/PPR1362124)

- 标识：`p-aa065ed711d05a970047`；发表：2026-11-09；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究利用 All of Us 队列中对性别、自报种族和年龄做 1:1 匹配的 3290 例样本，将染色体级别结构变异（全基因组 128 个片段的 LRR 分布统计矩）输入随机森林，进行急性心肌梗死风险预测。10 折交叉验证平均 AUC 仅 0.529，与打乱标签对照（0.491）及随机水平无法区分，结论为宏观结构变异不能解释 AMI 的缺失遗传力。

限制：仅有摘要，未提供完整方法、代码与数据获取信息；未报告任何亚组性能、差异或公平性指标。人口学匹配仅作为混杂控制手段，未构成算法公平性评估。

判断：该文虽为医学（AMI 预测）算法评估，但对性别、种族、年龄做 1:1 匹配仅为消除人口学混杂，用于验证预测信号是否为零，未提出任何公平性、差异测量、群体编码或缓解问题，也无亚组公平性指标。属人口学变量参与的一般预测性能评估，不满足公平性标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1362124)；模型：qoder-cn/dfmodel。

Full-text access failed (ValueError); abstract retained.

### [Efficacy and Safety of Stent-Assisted Coiling Versus Coiling Alone for Ruptured Multilobed Aneurysms: A Multicenter Study.](https://pubmed.ncbi.nlm.nih.gov/42974369/)

- 标识：`p-b1770139d184f1002ae3`；发表：2026-09-03；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

多中心前瞻性队列比较支架辅助栓塞与单纯栓塞治疗破裂多叶颅内动脉瘤的安全性和疗效，采用重叠权重及双稳健回归分析。研究未涉及AI/ML算法评估或算法公平性问题。

限制：仅有摘要；为观察性临床比较效果研究，未报告算法、敏感属性、亚组公平性或公平性指标分析。

判断：该文评估两种血管内治疗方式的安全性与疗效，不涉及AI/ML算法，也未提出或测量算法公平性问题，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42974369/)；模型：qoder-cn/dfmodel。

### [Analisi dell’appropriatezza prescrittiva ed evoluzione digitale: integrazione tra ricetta dematerializzata, intelligenza artificiale e manuale Rao.](https://europepmc.org/article/MED/42979883)

- 标识：`p-b1f1c2e8dcbc74c8d6c7`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该摘要介绍意大利马尔凯大区利用 NotebookLM 分析 36,465 份去物质化处方与 RAO 优先标准的符合性，发现 30% 处方不一致且异常集中于少数开方者，属于处方适当性数字审计，并非医疗算法公平性研究。

限制：仅有摘要；未提供算法公平性定义、受保护群体、亚组指标或公平性评估结果。文中“healthcare equity”仅为泛泛政策表述，不能作为算法公平性证据。

判断：摘要描述的是处方适当性审计，公平仅以“ensuring healthcare equity” incidental 提及；缺乏明确的算法公平/差异问题、群体定义及公平性测量，且摘要证据不足以建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42979883)；模型：qoder-cn/dfmodel。

### [Oxidation over omega-3: Reinterpreting the paradoxical link between fish oil supplements and accelerated cognitive decline.](https://pubmed.ncbi.nlm.nih.gov/42612547/)

- 标识：`p-be1ec4309a4ce2fb4aa3`；发表：2026-08-18；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文为致编辑信，评论一项观察性研究：鱼油补充与认知加速下降相关，并由FDG-PET低代谢介导。作者指出四点方法学局限（暴露错分、残余混杂、机制过度推断、情境依赖），并建议血清EPA+DHA剂量建模、负对照敏感性分析、部分容积校正FDG中介分析等改进。全文未涉及任何AI/ML算法或算法公平性评估。

限制：仅有信件摘要级文本；属营养流行病学方法学批评，未涉及算法模型、亚组公平性指标、偏差机制测量或任何实证性公平性评估，也未定义受保护属性或分组比较。

判断：该信评论的是鱼油补充与认知下降的观察性关联及其错分、混杂等统计方法学问题，未评估任何AI/ML算法，也未提出算法公平性、子群差异、编码偏差或缓解措施问题；算法、公平性、分组与实证测量四项标准均不满足，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42612547/)；模型：qoder-cn/dfmodel。

### [MRCP-derived radiomics features associated with biliary dilation: a multi-step feature reduction, multivariable regression, and diagnostic classification study.](https://pubmed.ncbi.nlm.nih.gov/42138743/)

- 标识：`p-c481c3634d23e0326c99`；发表：2026-05-15；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于MRCP影像提取三维CBD radiomics特征，经ICC可重复性、低方差、相关性、FDR与Cliff's delta多步降维，纳入年龄、性别和胆囊切除状态的多变量回归，并用随机森林等三种分类器做胆管扩张诊断分类，另在6-10 mm临界管径亚组做探索性分析。

限制：仅有摘要，无全文、代码或外部验证细节。文中仅将年龄、性别作为回归混杂因素校正，未定义公平性群体、未报告亚组性能差异、偏倚机制或缓解方法。

判断：摘要显示为胆管扩张的radiomics诊断分类研究，仅把年龄、性别、胆囊切除史作为混杂变量调整，未提出任何算法公平性/差异/编码或缓解问题，也未按敏感属性报告亚组指标，属公平性偶提之外的无关工作。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42138743/)；模型：qoder-cn/dfmodel。

### [Comparing Lightweight Models for Physician-Consensus Pharyngitis Classification from Primary-Care Smartphone Images.](https://europepmc.org/article/MED/43028421)

- 标识：`p-c52d73c3e19f9160643a`；发表：2026-10-28；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement
- 状态：相关，待核实是否纳入

该研究在PGUPharyngitis智能手机咽部图像数据集上比较五种轻量级模型（四种CNN与MobileViT-XS）预测医师共识的细菌性/非细菌性咽炎标签，用五折患者级交叉验证评估PR-AUC与AUROC并考察计算效率。结果显示模型区分度中等，且采集设备与标签相关，设备混杂无法排除。

限制：仅有摘要：未提供全文、代码或数据链接；无任何按设备（如三星/小米）分层的模型性能或公平性指标，也未报告校准、阈值公平性或缓解措施，因此无法确认真实公平性分析。

判断：属于医学影像（临床摄影）算法评估，报告了采集设备与标签的分布差异（9.2% vs 26.9%）及设备单变量基线，提示设备混杂这一偏倚机制；但全文未提出算法公平性问题，也未做亚组公平性度量。且证据仅限摘要，不能建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43028421)；模型：qoder-cn/dfmodel。

### [Cross-cohort analyses of OLFML2B cellular distribution and stromal associations in gastric adenocarcinoma.](https://pubmed.ncbi.nlm.nih.gov/43040151/)

- 标识：`p-c7d769f27ffccb863361`；发表：2026-11-17；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究整合五个队列的批量、单细胞、空间和蛋白质组数据，分析OLFML2B在胃腺癌中的细胞分布及其与成纤维细胞、ECM、TGF-β程序的相关性，并考察PD-1治疗队列中的反应关联；未涉及算法公平性。

限制：仅有摘要，缺少全文方法、代码和数据细节；研究属于分子生物标志物分析，未定义受保护群体、公平性指标或缓解方法，无法支持纳入。

判断：摘要聚焦OLFML2B在胃腺癌中的表达与细胞分布，采用队列和统计比较，但未评估AI/ML算法，也未提出算法公平性、差异、编码或缓解问题；无受保护群体或公平性测量，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43040151/)；模型：qoder-cn/dfmodel。

### [Association of objectively measured physical activity with incident spinal stenosis in a Fitbit-linked cohort from the All of Us Research Program.](https://europepmc.org/article/MED/43050913)

- 标识：`p-d577bfdc715f5d3350d6`；发表：2026-11-18；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

利用 All of Us 研究项目中 Fitbit 可穿戴设备数据与电子健康记录链接的回顾性队列（48,709 人、161,900 人年），以时变 Cox 比例风险模型评估客观测量的日均步数与活跃分钟数与新发椎管狭窄（颈段、腰段）的关联，发现步数较高者椎管狭窄风险较低（HR 0.84）。

限制：仅有摘要，无全文及代码或数据链接；该研究为暴露与结局的流行病学关联分析，未构建或评估任何临床决策算法，未开展亚组公平性度量、偏倚机制或缓解方法分析；race、sex 等仅作为混杂因素校正。

判断：研究主题为可穿戴设备测量的体力活动与新发椎管狭窄的流行病学关联，不属于医学算法公平性研究：没有待评估的 AI/ML 算法，也无算法公平性、差异、编码、缓解或公平性度量问题，更无按群体分层的性能比较。文中对 race、sex、education 的调整属混杂控制，不构成公平性证据，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43050913)；模型：qoder-cn/dfmodel。

### [EXPRESS: Brain Age Gap from Non-Contrast CT Is Independently Associated with Functional Outcome after Acute Ischemic Stroke.](https://europepmc.org/article/MED/43015642)

- 标识：`p-d5df31f2d791fe9c70ba`；发表：2026-11-11；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于1,173例急性缺血性卒中患者的前瞻性多中心队列，用深度学习从对侧非增强CT估计脑年龄，定义BrainAGE（预测年龄减实际年龄），并分析其与90天功能结局的关联。结果显示BrainAGE较高与更差功能结局独立相关，但判别力提升有限。

限制：仅有摘要，缺少模型结构、训练验证细节与代码数据信息；未涉及任何算法公平性、亚组差异或偏倚评估，性别仅作为回归协变量。

判断：属预后生物标志物关联研究：虽使用深度学习与CT影像，但全文未提出算法公平性/差异/编码/缓解或公平性度量问题，仅将性别作为调整协变量，不满足fairness与groups证据要求，且为摘要级证据，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43015642)；模型：qoder-cn/dfmodel。

### [Association of Cumulative Pharmacist Interventions and Interprofessional Adherence With Survival Among Patients Requiring Pharmacotherapeutic Optimization in a Pediatric Intensive Care Unit: A Retrospective Time-Dependent Cohort Study.](https://europepmc.org/article/MED/43000161)

- 标识：`p-e6d3c6428f1e2c8de26d`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该回顾性队列研究纳入565例儿科重症监护病房（PICU）患者，采用含时变暴露的扩展Cox比例风险模型，评估累计药师干预数及跨专业团队依从性与PICU内生存的关系，并按PIM-2校正基线严重度，报告总体死亡率11.9%、干预接受率72.2%。

限制：仅有摘要证据；研究为观察性药物管理/结局关联分析，未涉及任何AI/ML模型，也未提出算法公平性、亚组差异或偏倚机制问题；无代码、数据或公平性评价细节。

判断：该文研究药师干预与PICU生存的流行病学关联，属临床药物管理与结局评价，既未评估AI/ML算法，也未涉及算法公平性、敏感属性分组或亚组公平性测量，不符合纳入标准中的算法公平性要求，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43000161)；模型：qoder-cn/dfmodel。

### [Tenecteplase vs Alteplase in Basilar Artery Occlusion Treated with Endovascular Thrombectomy: A Propensity Score-Matched Analysis of 90- and 180-Day Outcomes.](https://europepmc.org/article/MED/42217837)

- 标识：`p-e9bbb6c62205518a6b32`；发表：2026-11-19；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究利用TriNetX回顾性队列（553例基底动脉闭塞行血管内取栓患者），通过倾向性评分匹配比较替奈普酶与阿替普酶桥接溶栓在90天和180天的出血、死亡、功能依赖及康复利用等结局，未发现显著差异，仅康复利用信号在多重检验校正后消失。

限制：仅有摘要，无全文方法、代码或补充材料；研究为药物比较有效性分析，未涉及任何AI/ML模型、算法公平性指标、亚组公平性评测或偏差机制；倾向性评分匹配属于混杂控制而非算法公平性干预。

判断：该文是两种溶栓药物的临床比较有效性研究，无AI/机器学习或算法被评估，也无算法公平性/偏倚/编码差异或公平性度量问题；人群分层仅为混杂调整，不构成敏感属性的公平性评估，故不满足算法公平性纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42217837)；模型：qoder-cn/dfmodel。

### [Artificial intelligence, health literacy, and sex and gender specific medicine: navigating the new paradigm in the physician-patient relationship.](https://europepmc.org/article/MED/42979871)

- 标识：`p-ea3b2e02ee0a3aa3db56`；发表：2026-11-01；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

该文为观点/评论性文章，讨论生成式AI、健康素养与性别特异医学对医患关系与临床实践的影响，泛泛指出训练数据偏倚会损害女性与少数群体的诊断适宜性，并呼吁公众提升数字健康素养、医生提升"算法素养"，未针对具体疾病或临床任务开展公平性分析或实证测量。

限制：仅摘要可用；未命名具体疾病或临床任务，未报告亚组指标、偏倚机制分析、评测框架或缓解方法比较，属泛泛的公平AI倡议与教育呼吁。

判断：属评论/观点文章，虽提及训练数据偏倚与公平，但未指明具体医学疾病或任务，也无实质性的算法公平分析（亚组指标、机制、框架或缓解比较）与实证评估，属附带提及型文献，不符合纳入条件。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42979871)；模型：qoder-cn/dfmodel。

### [Morphology-based selvester QRS score for phenotyping acute heart failure in patients with native left bundle branch block.](https://pubmed.ncbi.nlm.nih.gov/42721639/)

- 标识：`p-f2b6a21e012418a77837`；发表：2026-09-10；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该摘要评估Selvester QRS评分在伴原生左束支传导阻滞的急性心衰患者中区分HFrEF、HFmrEF、HFpEF和RHF的诊断表现，报告SQS与超声参数相关且对HFrEF区分中等。未涉及AI/算法公平性、敏感人群比较或缓解措施。

限制：仅有摘要；单中心回顾性研究；无公平性指标、敏感属性分组、偏倚机制或缓解评估；无代码/数据可用性信息。

判断：临床ECG评分诊断研究，虽评估算法性能，但未提出或测量算法公平性/差异，缺乏敏感属性分组与公平性评价，故不属于医学算法公平性范围。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42721639/)；模型：qoder-cn/dfmodel。

### [Association of C-reactive protein to albumin ratio with progression of CKD and all-cause mortality in diabetic CKD.](https://pubmed.ncbi.nlm.nih.gov/42412363/)

- 标识：`p-f497b8eb950e521f7701`；发表：2026-07-07；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究在231例糖尿病合并慢性肾脏病患者中评估C反应蛋白/白蛋白比值（CAR）与CKD进展及全因死亡的关联，采用Kaplan-Meier、Cox回归、限制性立方样条及SHAP机器学习分析，发现CAR为独立预后因子并可提升风险预测效能。

限制：摘要层面证据，仅涉及单中心回顾性预后建模；按年龄、性别、BMI的亚组分析用于检验关联稳健性，未涉及任何算法公平性、组间差异或偏倚机制分析。

判断：研究为CAR生物标志物的预后关联与预测增量分析，虽使用SHAP机器学习方法，但未提出算法公平性/差异/编码/缓解或公平性度量问题，亚组分析仅验证关联一致性而非公平性评估，故不属医学算法公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42412363/)；模型：qoder-cn/dfmodel。

### [Clinical and sociodemographic predictors of AI use for mental health among college students.](https://pubmed.ncbi.nlm.nih.gov/42217639/)

- 标识：`p-faa1ff8cf33578158f1a`；发表：2026-05-29；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

基于2024-2025年Healthy Minds Study两所美国高校675名学生的横截面数据，用层次logistic回归分析大学生将生成式AI用于心理健康支持的临床与社会人口学预测因素，发现重度抑郁、重度焦虑、自杀倾向及亚裔身份与更高使用几率相关，并提示边缘群体使用未受监管AI工具的比例偏高。

限制：仅有摘要，缺乏样本抽样细节、量表与建模协变量说明；横截面设计无法推断因果；仅两所院校，外部效度有限。全文未评估任何AI/ML算法本身，也未提出或实施算法公平性指标与缓解方法，缺乏可核验的代码或数据信息。

判断：该研究把生成式AI使用当作被解释的行为结局，用回归描述使用者的人口学差异，并未评估任何医疗AI算法的公平性（无亚组性能指标、编码偏差或缓解方法）。虽有分组比较与实证测量，但缺少“被评估算法”与“算法公平性/偏倚问题”两项核心要件，属于AI使用行为的流行病学描述而非医疗算法公平性研究，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42217639/)；模型：qoder-cn/dfmodel。

### [Association Between MIA3 and Coronary Collateral Circulation Formation in Patients with Chronic Total Occlusion](https://europepmc.org/article/PPR/PPR1354723)

- 标识：`p-ff7c424314366178daee`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究纳入489例冠状动脉慢性完全闭塞（CTO）患者，检测血浆MIA3与VEGFA水平，按Rentrop分级分为侧支循环良好组与不良组，采用多因素logistic回归、ROC曲线及NRI/IDI评估MIA3对良好侧支形成的预测价值，并开展临床亚组与交互分析。

限制：仅有摘要，缺少样本构成、模型校准与外部验证细节；亚组分析基于血脂异常等临床特征，未涉及任何算法公平性、群体差异或偏倚测量，也无代码或数据可用性信息。

判断：该文为CTO患者生物标志物MIA3与侧支循环形成的临床关联及预测效能研究，虽使用回归与ROC/NRI/IDI评估，但未提出算法公平性、偏倚机制或缓解措施问题，亚组分析针对血脂异常而非受保护属性，不满足公平性核心判据。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1354723)；模型：qoder-cn/dfmodel。

### [Critical Validation of Deep Learning-Based Cervical Vertebral Fracture Detection on Computed Tomography Localizer Radiographs.](https://europepmc.org/article/MED/42970201)

- 标识：`p-1346d065a32670a53db3`；发表：2026-11-02；发现：2026-11-09
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

该研究在346例创伤患者的CT定位片上评估深度学习颈椎骨折检测，比较全图二分类与先定位颈椎再分类的两步流程，并用置换检验、遮挡测试、Grad-CAM、混杂因素分析及按解剖部位的亚组分析检验模型有效性，发现全图模型虽PR-AUC更高，但并不主要依赖骨折区域，属于典型捷径学习案例。

限制：仅有摘要可查；所谓亚组分析仅按解剖骨折位置划分，未涉及任何敏感属性、人群分组或公平性指标，也未报告组间差异或缓解干预，无法据此判断算法公平性。

判断：该文聚焦模型有效性与捷径学习（混杂/伪相关线索），亚组仅为解剖部位而非敏感属性，未提出算法公平性、差异或编码问题，也无公平性度量或缓解方法，按规则不足以纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42970201)；模型：qoder-cn/dfmodel。

### [Ethical Decision-Making in Nursing Management: Comparing Nurse Managers and Generative Artificial Intelligence](https://europepmc.org/article/PPR/PPR1359832)

- 标识：`p-2a813b12a1e170b90af2`；发表：2026-11-05；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

探索性研究，比较西班牙某公立大学医院护理管理者的伦理决策与三种生成式AI模型在相同管理情景下的回答一致性和重复稳定性。结果显示总体一致性相近，但模型在拒绝执行与知情同意等情景上系统性偏离人类众数；作者强调稳定性、专业一致性与伦理正当性是三个独立问题，不主张临床有效性。

限制：仅有摘要，无全文方法与数据；未定义任何患者群体或敏感属性，未做亚组公平性指标分析；“公平”仅作为伦理决策选项出现，并非算法公平性研究；也未涉及临床任务或疾病结局。

判断：该文考察生成式AI在护理管理伦理决策中的一致性与稳定性，属于人机一致性/治理研究。文中“fairness-related actions”仅指伦理决策内容，未提出算法公平性问题，未定义受保护群体或亚组发现协议，也未实施公平性测量评估，属于偶然提及公平，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1359832)；模型：qoder-cn/dfmodel。

### [Concurrent cognitive, behavioral and systemic physiological features mark preclinical Alzheimer’s disease](https://europepmc.org/article/PPR/PPR1354470)

- 标识：`p-2d4258f545c1b26784f5`；发表：2026-10-30；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究纳入644名自报认知正常的老年人，以血浆p-tau217界定临床前阿尔茨海默病亚组，描述其认知、行为及生理特征，并构建概念验证AI分类器整合多域临床数据，较单独认知筛查提高p-tau217高风险个体识别。

限制：仅有摘要，缺乏算法细节、亚组性能及敏感属性分析；未报告公平性、差异或缓解评估，不能支持医学算法公平性纳入。

判断：摘要聚焦临床前AD多域表型与p-tau217分类器，未提出或评估算法公平性、亚组差异或敏感属性；仅具临床相关性，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1354470)；模型：qoder-cn/dfmodel。

### [Clinical and molecular characteristics associated with megakaryocytic dysplasia in patients with myelodysplastic syndromes.](https://pubmed.ncbi.nlm.nih.gov/43043920/)

- 标识：`p-35e6e11c24cb884c5eeb`；发表：2026-11-17；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

研究169例骨髓增生异常综合征患者，比较伴或不伴巨核细胞发育异常者的临床、细胞遗传学及突变特征，发现EZH2突变是唯一独立相关因素。该研究为临床-分子关联分析，未涉及AI/ML算法或算法公平性。

限制：仅有摘要，缺少全文方法学细节与外部验证信息；且内容与算法公平性无关。

判断：摘要聚焦骨髓增生异常综合征中巨核细胞发育异常的临床与分子关联，无AI/ML算法被评估，也未涉及公平性、差异、编码或缓解问题及受保护群体，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43043920/)；模型：qoder-cn/dfmodel。

### [Early Catheter Ablation for Patients With Atrial Fibrillation and a Stroke History: A Target Trial Emulation Analysis.](https://pubmed.ncbi.nlm.nih.gov/42821842/)

- 标识：`p-481a4db85e5cf700e6a2`；发表：2026-10-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究采用目标试验模拟（克隆-删失-加权法）比较房颤合并缺血性卒中患者早期导管消融与药物治疗的长期结局，纳入6家中心431例患者，报告MACE、再住院、死亡及mRS/AD8功能认知结局的关联，属观察性因果效应估计研究。

限制：仅有摘要，无全文；研究未涉及AI/ML模型或算法公平性评估，仅以性别比例等形式描述人群构成，未见任何亚组公平性指标、偏倚机制或缓解方法。

判断：该文为房颤卒中亚组导管消融疗效的目标试验模拟分析，属临床比较效果研究；未评估任何AI/ML算法，也未提出算法公平性/差异/编码/缓解或公平性测量问题，虽有临床任务与经验评估，但不满足算法与公平性两项准则。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42821842/)；模型：qoder-cn/dfmodel。

### [Value-Based Care in Neurosurgery: Results from Maryland’s Global Budget Revenue Program](https://europepmc.org/article/PPR/PPR1344342)

- 标识：`p-596a0bc151428ccc8ae7`；发表：2026-10-18；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究评估马里兰全球预算收入模型对垂体手术费用、住院时长、再入院及不同保险和年龄患者构成的影响，报告费用下降与低收入患者可及性改善，但未涉及AI/ML算法或算法公平性。

限制：仅有摘要；无AI/ML算法，也无算法公平性评估；属于支付政策回顾性研究，不能支持纳入。

判断：摘要仅评估支付政策与手术结局及可及性，未评估AI/ML算法，也未进行算法公平性测量；健康公平提及不构成算法公平研究。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1344342)；模型：qoder-cn/dfmodel。

### [How to tackle inequities in bereavement support for ethnically diverse communities: a national qualitative study using experience-based co-design.](https://pubmed.ncbi.nlm.nih.gov/42902353/)

- 标识：`p-7d86f34b5b0505602795`；发表：2026-10-21；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该全国定性研究通过访谈、焦点小组和共创工作坊，识别族裔多元群体在丧亲支持获取上的障碍与促进因素，提出文化安全照护、反种族主义实践和社区合作建议，并形成逻辑模型。研究未涉及AI/ML算法或算法公平性评估。

限制：仅摘要；无算法、模型、数据集或代码信息，也未报告算法公平性指标或缓解方法，无法判断医学算法公平性贡献。

判断：摘要显示为丧亲支持服务的定性公平性研究，未评估任何AI/ML算法或算法公平性指标，不属于医学算法公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42902353/)；模型：qoder-cn/dfmodel。

### [Clinical equipoise as inclusion criterion to control for confounding in observational studies.](https://pubmed.ncbi.nlm.nih.gov/42854534/)

- 标识：`p-875da7d10afd9f30ec2b`；发表：2026-10-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究以专家治疗推荐分歧作为临床均势代理，评估不同分歧层级下肱骨近端骨折治疗组基线可比性，发现更严格纳入标准可改善组间平衡但减少样本量。研究不涉及医学AI/ML算法或算法公平性评估。

限制：仅有摘要；未报告AI/ML模型、算法公平性指标、受保护亚组或公平性干预与评估。

判断：研究关注观察性研究中的混杂控制与纳入标准，未评估医学算法，也未提出或测量算法公平性/偏倚问题，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42854534/)；模型：qoder-cn/dfmodel。

### [Propensity Score Matching Unmasks Core Predictors of Psychosis Conversion in Clinical High-Risk Individuals.](https://pubmed.ncbi.nlm.nih.gov/42960986/)

- 标识：`p-9a0944cda37da259a878`；发表：2026-10-27；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究在920例临床高危精神病(CHR-P)个体中随访3年，使用倾向性评分匹配(PSM)平衡年龄、性别、教育程度及6个认知域等混杂因素，再以多因素logistic回归与ROC分析识别精神病转化的独立预测因子。PSM后模型AUC由0.685升至0.808，GAF下降率单项准确率约73%，作者据此强调早期精神病预测中需控制认知与人口学混杂。

限制：仅有摘要，无全文方法细节、代码或数据链接。PSM仅用于消除混杂以提升预后预测准确性，未涉及任何敏感属性亚组的算法公平性定义、差异度量或偏倚缓解设计，也未报告分组公平性指标。

判断：该文是临床预后预测建模研究，以倾向性评分匹配控制认知与人口学混杂并提升AUC，属于统计混杂校正而非算法公平性问题：未定义受保护群体、未测量亚组性能差异、未讨论编码偏倚或缓解方法。摘要亦无公平性相关词句，故不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42960986/)；模型：qoder-cn/dfmodel。

### [Extracapsular and joint-dominant hand and wrist MRI patterns in psoriatic and rheumatoid arthritis: an exploratory case-control study.](https://pubmed.ncbi.nlm.nih.gov/42978735/)

- 标识：`p-9ea0a6100ead36f59229`；发表：2026-10-20；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该探索性病例对照研究比较41例银屑病关节炎与41例类风湿关节炎患者手/腕3.0T MRI的预设影像学特征，发现关节囊外软组织炎症、附着点相关特征更支持PsA，而关节积液、腕部滑膜炎与骨侵蚀更支持RA，并报告了读者间与读者内一致性系数。

限制：仅有摘要；未涉及任何算法或AI模型，也未按年龄、性别等属性进行亚组公平性比较；年龄与性别仅作为校正混杂因素进入回归模型；样本量小、无外部验证，结论本身声明需独立验证。

判断：研究为PsA与RA的MRI影像模式诊断学比较，采用Firth校正logistic回归仅作统计校正，未评估任何AI/ML算法的公平性、偏倚机制或缓解方法，也无亚组差异指标或公平性度量，不符合纳入所需的算法公平性证据标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42978735/)；模型：qoder-cn/dfmodel。

### [The C-reactive protein to lymphocyte ratio and 28-day mortality in critically ill patients with sepsis: a retrospective propensity score-matched cohort study.](https://pubmed.ncbi.nlm.nih.gov/43011466/)

- 标识：`p-a8215224fac5c572c2b3`；发表：2026-11-11；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

基于MIMIC-IV的回顾性倾向评分匹配队列，评估脓毒症患者C反应蛋白/淋巴细胞比与28天及长期全因死亡率的关联和预测价值；未涉及算法公平性、偏倚机制或缓解评估。

限制：仅有摘要；未报告公平性指标、受保护属性或算法偏倚分析；常规亚组与交互分析不能替代算法公平性评估。

判断：研究聚焦脓毒症生物标志物预后关联，虽使用回归与ROC评估，但无AI/ML公平性、差异或缓解问题，亦无定义公平群体，故不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43011466/)；模型：qoder-cn/dfmodel。

### [Development and validation of a cuff size prediction model for pediatric blood pressure measurement outside the office.](https://pubmed.ncbi.nlm.nih.gov/42207271/)

- 标识：`p-ba6fa6408cc8bbe26dd7`；发表：2026-05-28；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

基于NHANES数据开发线性回归模型，用年龄、性别、身高、体重等EHR变量预测儿童中臂围以确定动态血压监测袖带尺寸，并在儿科高血压门诊107人外部验证；报告预测一致性（⍴c=0.94）与袖带尺寸符合率（83.2%）。

限制：仅有摘要级证据；全文的方法细节、代码与数据可用性未知。摘要未报告任何按性别、年龄、种族等亚组的性能比较或公平性度量。

判断：该文属预测模型开发与外部验证，评估的是整体预测精度与袖带尺寸一致性；虽将性别作为预测变量，但未提出问题化的算法公平性/差异问题，无亚组分层指标、偏倚机制或缓解方法，按规则排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42207271/)；模型：qoder-cn/dfmodel。

### [Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models](https://arxiv.org/abs/2611.21215)

- 标识：`p-c953684f67e297ff37a6`；发表：2026-11-16；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

Open-fMIND 构建并发布大规模开放 fMRI 分区时间序列语料，覆盖 322 项 OpenNeuro 研究、11,379 名受试者，支持脑基础模型自监督预训练，并在 HCP-YA、ABIDE、ADHD-200 上评估下游预测性能。

限制：全文未定义公平性目标或报告按年龄、性别、站点等亚组的模型性能差异；人群覆盖和站点/运动效应仅为数据质量或使用注意事项，且无公平性缓解方法。

判断：该文是开放 fMRI 预训练语料与下游评测，虽涉及诊断/认知预测和年龄性别覆盖，但未提出或检验算法公平性、亚组差异或缓解问题，不符合公平性研究纳入标准。

证据层级：full_text；[来源](https://arxiv.org/html/2611.21215v1)；模型：qoder-cn/dfmodel。

### [Artificial Intelligence Applications in General Surgery in the United States of America: A Bibliometric Analysis.](https://pubmed.ncbi.nlm.nih.gov/42104780/)

- 标识：`p-d329a221375326aba663`；发表：2026-05-09；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文是对美国普外科人工智能研究的文献计量分析，纳入2020—2025年59篇文献，统计作者、主题、期刊、国别与资助分布，采用H指数、AIS、布拉德福德定律及泊松/负二项回归等指标，发现研究集中于手术流程识别与临床决策支持，且资金更倾向临床可落地的应用。

限制：仅提供摘要，无全文方法、数据或代码信息。文中未涉及任何算法公平性指标、亚组比较或偏倚机制分析，仅在结论中以一句泛泛的“公平导向”建议收尾，属偶发提及。

判断：文献计量学研究，虽涉及普外科AI临床应用，但核心问题是研究产出与资助格局，未评估任何算法的公平性、亚组差异或偏倚机制；结论中“equity-focused AI development”仅为泛泛的公平AI建议，缺乏亚组指标、机制或缓解方法的具体分析，不满足公平性标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42104780/)；模型：qoder-cn/dfmodel。

### [Same day discharge following bimaxillary osteotomy surgery a single center retrospective study.](https://pubmed.ncbi.nlm.nih.gov/42993311/)

- 标识：`p-d6abeded64d1a68e9115`；发表：2026-11-06；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

该回顾性队列描述80例双颌截骨术患者同日出院与留院过夜的并发症记录，报告未调整混杂因素的比例差异，未涉及人工智能、算法公平性或受保护群体分析。

限制：仅提供摘要；研究为单中心回顾性、非随机、未调整混杂的临床可行性观察，无算法或公平性证据。

判断：研究比较双颌截骨术后的出院安排与并发症，未评估AI/ML算法，也未进行算法公平性、偏倚机制或亚组公平性分析，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42993311/)；模型：qoder-cn/dfmodel。

### [Racial Composition and Single-Input Dominance in the First Hospice Special Focus Program Cohort.](https://pubmed.ncbi.nlm.nih.gov/42895138/)

- 标识：`p-e2c8854d96deaa4b99ad`；发表：2026-10-19；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：相关，待核实是否纳入

该研究审计美国临终关怀特别关注项目（SFP）的复合质量算法：对2024年11月CMS目录中7115家临终关怀机构做横断面分析，用逻辑回归检验入选与机构规模、患者种族构成及独立质量指标（HVLDL）的关系，并对50家入选机构的复合评分做标准化输入分解。结果显示入选与黑人患者比例显著相关，且48/50家入选机构的评分恶化主要由单一输入驱动，提示算法可能不成比例地影响服务黑人患者的机构。

限制：仅有摘要，缺少完整抽样、变量定义、模型设定与敏感性分析细节；为观察性横断面分析，不能推断因果；仅基于单一批次50家入选机构，且该项目2025年因诉讼暂停，外部适用性与时间稳定性有限。

判断：摘要明确评估联邦临终关怀监督复合算法入选结果与患者种族构成的关联，含7115家机构的实证测量与评分输入分解，五项标准均有摘要证据；但依据仅摘要不得建议纳入的规则，定为related而非suggest_include。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42895138/)；模型：qoder-cn/dfmodel。

### [Good Enough to Sequence: Fluorometry-Guided Salvage of Low-Volume and Compromised Paediatric DNA in Custom Amplicon Next-Generation Sequencing.](https://pubmed.ncbi.nlm.nih.gov/43028320/)

- 标识：`p-f773c3a00472650dfad3`；发表：2026-10-22；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于314例儿童样本，比较Qubit与Nanoquant定量及A260/280质量分组对定制扩增子NGS建库产量、测序深度与覆盖度质控指标的影响，并提出约20 ng/µL的输入阈值以降低建库失败风险。属实验室样本质量控制方法学，不涉及AI算法评估或算法公平性分析。

限制：仅有摘要证据；分组依据为DNA浓度与纯度，而非人群或敏感属性；全文是否含其他分析无法从摘要判定，但摘要中未见任何算法公平性、偏倚测量或缓解评估。

判断：研究内容为测序前DNA定量与质量控制的实验室方法学，虽含建库失败的ROC/逻辑回归预测，但未评估任何AI/ML算法的公平性或偏倚，也未定义人口学亚组或公平性指标，不满足医学算法公平性研究的入选标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43028320/)；模型：qoder-cn/dfmodel。

### [Artificial intelligence in chronic kidney disease care: An integrative review of outcomes and sociotechnical factors.](https://europepmc.org/article/MED/43057074)

- 标识：`p-0ef43e765130077b006e`；发表：2026-11-13；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该整合综述梳理CKD照护中AI技术的临床使用结局及社会技术因素，纳入25项研究，报告患者结局、照护流程、资源使用及社会技术报告不均，并指出公平性等报告不足。未开展CKD场景下的算法公平性分析。

限制：仅有摘要；公平性仅作为社会技术报告维度被一句带过，缺少亚组指标、偏差机制或公平性评估框架；无法据此判断全文是否有更详细公平性分析。

判断：该综述虽聚焦CKD中AI的临床结局，但公平性仅作为报告维度偶然提及，未提供具体的算法公平性分析、亚组评估或机制研究，按要求应排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43057074)；模型：qoder-cn/dfmodel。

### [Density Peak Clustering: A Systematic Survey of Methods, Applications, Challenges, and Future Research Directions](https://europepmc.org/article/PPR/PPR1352750)

- 标识：`p-21c05110656354a438ee`；发表：2026-10-27；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

这是一篇关于密度峰值聚类（DPC）的系统性综述，梳理2014年以来的方法演进、八大方法族（自适应邻域与密度估计、图与流形建模、自动确定簇数、分配与不确定性、表示学习、隐私/联邦/增量计算、可扩展执行、采样与优化等辅助策略）及其适用假设与计算代价，并列举医疗、网络安全、遥感、交通等领域应用，最后提出面向鲁棒、可解释、公平、隐私保护等方向的未来研究议题。

限制：仅有摘要，未见正文与实验细节；摘要中“healthcare”仅为泛化应用领域列举，未给出具体疾病或临床任务，也未提供任何子群指标、偏倚机制或缓解方法的实质分析，“fairness-aware”仅出现在未来方向罗列中。证据不足以判定其属于医学算法公平性研究。

判断：该文为通用聚类算法（DPC）综述，医学仅作为应用领域之一被顺带提及，未指明任何具体疾病或临床任务；公平性仅在结尾未来方向中以“fairness-aware”一笔带过，属于偶发提及，缺少针对具体医学情境的子群度量、偏倚机制或缓解比较等实质性分析，故不纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1352750)；模型：qoder-cn/dfmodel。

### [Machine Learning Validation Pipelines: From Tabular Benchmarking to Conformal Calibration and Execution-Grounded Agentic Testing](https://europepmc.org/article/PPR/PPR1370333)

- 标识：`p-280deca54061942c17e6`；发表：2026-11-18；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Post-processing Mitigation
- 状态：机器建议排除，待抽查

提出五层机器学习验证流程，涵盖基准测试与泄漏防护、可解释性审计、共形校准、部署前门控及执行级多智能体验证，并以金融ML元分析和临床分诊等高风险场景说明失败模式。

限制：仅摘要级证据；无法核实全文是否包含具体临床任务的公平性分析；可见元分析聚焦金融ML，临床分诊仅为示例。

判断：摘要仅在临床分诊等高风险场景中泛泛提及，未针对具体医学任务分析公平性；公平审计与少数群体覆盖结果未与临床亚组或医学评价关联，且为摘要级证据，不能建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1370333)；模型：qoder-cn/dfmodel。

### [What Factors Influence Hospital Admission for Mandible Fractures in Emergency Departments Across the United States?](https://pubmed.ncbi.nlm.nih.gov/42235594/)

- 标识：`p-2929aa6bb236b998782c`；发表：2026-05-21；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

基于2022年全国急诊样本的回顾性队列，分析下颌骨骨折患者入院及费用的生物、情境和社会经济预测因素。结果显示男性、多发骨折、合并中面部骨折和枪伤与入院相关，无保险患者入院可能性较低。

限制：仅有摘要；研究使用多变量 logistic 模型识别入院预测因素，并非评估 AI/ML 算法的公平性，也未报告分组模型性能、偏倚机制或缓解措施。

判断：该文有临床任务、分组和统计分析，但核心不是算法公平性；仅在结论泛泛提及“improve equity”，属于偶然提及，按规则排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42235594/)；模型：qoder-cn/dfmodel。

### [Promoting Just Culture: Implementing a Medication Error Reporting Process in Nursing Education.](https://pubmed.ncbi.nlm.nih.gov/42089774/)

- 标识：`p-442a05aaacc8e4189c99`；发表：2026-05-06；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

护理教育中的用药错误报告质量改进项目：培训临床教师使用标准化报告流程（事件上报系统、复盘工具、学生行为分类算法、第二受害者支持），比较培训前后的教师调查结果，教师处理用药错误的信心显著提升，并称促进公平。全文未涉及AI/ML算法或算法公平性分析。

限制：仅有摘要；无算法模型、无受保护群体定义、无亚组或公平性指标；公平仅在结论处被提及一次；无代码或数据链接信息。

判断：该文为护理教育中用药错误上报流程的质量改进项目，文中“算法”指人工分类学生行为的流程，并非AI/ML模型；公平/公正文化仅作为管理理念被提及一次，缺少明确的受保护属性、亚组比较与公平性测量，属于偶然提及，不符合纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42089774/)；模型：qoder-cn/dfmodel。

### [Toward Clinically Trustworthy Deep Learning in Cardiology: A Unified Mathematical Synthesis of Representation, Optimization, and Reliability.](https://europepmc.org/article/MED/43028492)

- 标识：`p-4ba526797d8b268917d7`；发表：2026-11-02；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该系统综述基于79篇文献，从统一的数学视角梳理心脏病学可信深度学习中的表示学习、优化、不确定性、鲁棒性、公平性、可解释性与泛化，并提出概念性审计框架；作者强调相关指标仅具理论性，并非实际临床指标。

限制：仅见摘要；公平性只在可信性概念列举中出现，未见具体心血管疾病或任务下的亚组指标、偏倚机制、评测设计或缓解方法；作者自述所提指标纯属理论。

判断：该文是心脏病学可信深度学习的宽泛系统综述，公平性仅作为概念之一被附带提及，未提供特定疾病或任务的实质性算法公平性分析；按综述入选规则不予推荐，且摘要级证据不足以建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43028492)；模型：qoder-cn/dfmodel。

### [Contribution of artificial intelligence research to the development of inclusive applications for people with disabilities: A scoping review (2015-2025).](https://europepmc.org/article/MED/42879324)

- 标识：`p-5ff397bb1086a10ff761`；发表：2026-10-15；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

该文为2015—2025年范围综述，检索四个数据库并纳入93项健康AI研究，考察其对残障人士包容性应用的支持程度。约60%研究提及公平，但仅12.9%落实具体措施（如工具适配、样本多样性），6.5%让残障人士参与共同设计或验证，并指出算法偏见与数据代表性不足等问题。

限制：仅提供摘要，无全文方法、亚组指标或任务细节；综述横跨运动、感官、认知、沟通与心理社会等多类残障，未锚定具体疾病或临床任务，公平性分析停留在措施计数与宏观公平倡导层面，无法判定是否满足综述纳入条件。

判断：主题虽涉及健康AI中的算法偏见与残障群体，但这是覆盖多类残障的泛化公平综述：未命名具体疾病或临床任务，也未在该情境下给出亚组指标、偏见机制或缓解方法比较等细致公平分析，且仅12.9%研究落实公平措施，属泛化公平倡导型综述，按规则排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42879324)；模型：qoder-cn/dfmodel。

### [Advancing Equitable and Trustworthy AI in Breast Cancer Detection Through Interpretable Deep Learning](https://europepmc.org/article/PPR/PPR1361567)

- 标识：`p-6c2d4e6ce2f485ff83ff`；发表：2026-11-06；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：待核验

该文为PRISMA系统综述，聚焦乳腺癌钼靶筛查中深度学习模型的公平性与人口学偏倚，提出解释图“reasoning bias”及多指标热图偏倚评估框架，并指出种族、年龄和乳腺密度交叉亚组证据不足。

限制：仅有摘要，无法核验全文是否实际提供细粒度亚组指标、偏倚机制分析或综述结果；该文为综述并主要提出未来研究框架，非原始实证评估。

判断：摘要明确为乳腺癌钼靶深度学习公平性系统综述，涉及种族、年龄和乳腺密度亚组及解释偏倚；但证据仅限摘要，无法确认全文是否具备实质性、细粒度的公平性综合分析，故暂缓而非建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1361567)；模型：qoder-cn/dfmodel。

### [Trustworthiness Evaluation of Medical Vision-Language Models: A Scoping Review and a Proposed Minimum Evaluation Checklist.](https://europepmc.org/article/MED/42933376)

- 标识：`p-8133fbf008b01c6049b4`；发表：2026-10-26；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking
- 状态：机器建议排除，待抽查

该范围综述系统梳理医学视觉-语言模型的可信度评估实践，提出八项最低可信度评估清单（MiTEC）并做回溯打分：稳健性11/29、幻觉7/29，而公平性与可解释性各仅4/29（13.8%），亚组分析、形式化校准与图像依赖对照均少见。

限制：仅有摘要可查：公平性只是可信度八个维度之一，未指明具体疾病或影像任务，也未给出亚组定义、公平性指标或偏差机制的具体分析，因此无法核验其公平性综合的深度。

判断：该文为可信度（含稳健性、幻觉、公平性等八个维度）范围综述，公平性仅以“4/29（13.8%）”的计数形式出现，未命名具体医学疾病或任务，也没有该场景下实质性的算法公平性分析（如亚组指标、机制或缓解方法比较），属于附带提及；且仅有摘要证据，不满足综述纳入所需的两项条件。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42933376)；模型：qoder-cn/dfmodel。

### [Explainable and Trustworthy AI for Diabetic Retinopathy: A Systematic Review and Diagnostic Meta-analysis](https://europepmc.org/article/PPR/PPR1350140)

- 标识：`p-9830d51967755c683818`；发表：2026-10-26；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

该文为糖尿病视网膜病变（DR）可解释与可信AI的系统综述和诊断Meta分析，汇总10项研究的诊断性能，并讨论可解释性、校准、不确定性、泛化、公平性、隐私和部署证据。

限制：仅有摘要；未见具体亚组公平性指标、敏感属性定义、偏倚机制或缓解方法比较，无法核验全文是否包含详细的DR公平性分析。

判断：摘要明确DR任务和AI评估，但公平性仅作为可信AI维度被笼统提及（亚组公平性有限及建议），缺乏具体亚组证据；仅摘要不足以判断全文是否有详细公平性综合，故暂缓而非纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1350140)；模型：qoder-cn/dfmodel。

### [Artificial Intelligence in Neglected Tropical Diseases: Current Applications, Challenges, and Opportunities](https://europepmc.org/article/PPR/PPR1371479)

- 标识：`p-b739156d3045cfb0e9ce`；发表：2026-11-19；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该文是对AI应用于被忽视热带病（NTDs）的系统综述，纳入289项研究，涵盖诊断、预后、监测、暴发预测、治疗监测与药物发现，指出外部验证、前瞻性评估及数据治理、可解释性、公平性等方面存在不足。

限制：仅有摘要可读；全文的公平性分析无法核实。摘要中公平性仅作为部署考量之一被列举，未给出具体疾病或任务的亚组指标、偏倚机制或缓解方法比较。

判断：此为系统综述，摘要未指明具体NTD疾病或任务，且公平性仅在“数据治理、健康系统整合、可解释性、公平性、可解释性”清单中一带而过，缺乏针对该场景的实质性算法公平性分析（亚组指标、机制或评估框架），符合偶然提及类文献的排除条件。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1371479)；模型：qoder-cn/dfmodel。

### [Protocol for Conducting a Scoping Review on The Use of AI in Automated Scoring of Short-Answer Questions in Medical Education](https://europepmc.org/article/PPR/PPR1346575)

- 标识：`p-cc8d5c0e4ff2868dbbd2`；发表：2026-10-21；发现：2026-11-14
- 主题：Clinical NLP and Foundation Models
- 状态：机器建议排除，待抽查

该文是一篇范围综述方案，计划梳理医学教育中AI自动评分简答题的模型、评分性能、信效度及公平性比较，采用JBI方法和PCC框架，纳入2015年以来的实证研究。摘要未报告任何已完成的公平性分析或结果。

限制：仅有摘要，且为研究方案；未给出具体疾病/临床任务、受保护群体、公平性指标或实证结果，无法评估其公平性证据。

判断：仅为范围综述方案，未提供具体临床任务或实质性公平性分析；全文仅将公平性列为待考察维度，且未定义受保护群体或实施评估，不满足纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1346575)；模型：qoder-cn/dfmodel。

### [Beyond scales: Artificial intelligence, language, and behavior in suicide risk modeling-a narrative review.](https://europepmc.org/article/MED/43035089)

- 标识：`p-ee87c34c3078786f90ec`；发表：2026-11-15；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该叙述性综述总结人工智能在自杀想法与行为预测中的多模态应用，涵盖电子健康记录与理赔数据、临床文本自然语言处理、语音与面部行为信号、神经影像及被动传感，并讨论判别与校准、外部验证、类别不平衡和部署伦理，仅泛泛提及算法偏见与公平。

限制：仅获得摘要，无法核实全文是否包含具体亚组指标、偏见机制或公平性评估与缓解方法；摘要中公平仅作为伦理与实施挑战列出，证据不足以支持纳入。

判断：文章为自杀风险人工智能的叙述性综述。摘要虽提及算法偏见与公平，但未针对该临床任务提供具体公平分析、亚组指标、偏见机制或评估/缓解框架，属于偶然提及，未满足详细公平性分析条件。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43035089)；模型：qoder-cn/dfmodel。

### [Beyond AUROC: External Validation, Calibration, and Explainability of Machine Learning Models for 30-Day Hospital Readmission Using Electronic Health Records—A Rapid Systematic Review](https://europepmc.org/article/PPR/PPR1346087)

- 标识：`p-fb55a16fedc7a47752c1`；发表：2026-10-20；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、EHR, Physiological Signals and Healthcare
- 状态：待核验

该快速系统综述评估EHR 30天再入院预测模型的验证、校准、可解释性与亚组公平性报告情况，发现公平性分析仅占4.5%，并提出超越AUROC的最小评估集。

限制：仅摘要；无法确认全文是否对7项公平性分析研究给出亚组指标、偏倚机制或具体评估框架；摘要未定义受保护属性。

判断：综述明确针对EHR 30天再入院预测并报告公平性分析仅7项(4.5%)；但摘要只给出报告率，未提供亚组指标、机制或具体公平性框架，也未定义分组属性，故不能建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1346087)；模型：qoder-cn/dfmodel。

### [Etiology and Anatomical Level of Lower-Limb Amputations in Two Iranian Referral Hospitals: A Retrospective Record-Based Study.](https://pubmed.ncbi.nlm.nih.gov/42940562/)

- 标识：`p-1f719bc172ff6ac3b1d8`；发表：2026-10-19；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

回顾性分析伊朗两家医院229例下肢截肢记录，描述创伤、血管病和感染等病因及截肢平面，并发现年龄与医院差异；未涉及AI/ML模型或算法公平性评估。

限制：仅有摘要；研究为临床流行病学描述，未报告任何模型、亚组公平性指标或缓解措施。

判断：研究使用ICD编码规则重建病因并比较医院间差异，但未评估AI/ML算法，也无算法公平性、偏倚或缓解问题，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42940562/)；模型：qoder-cn/dfmodel。

### [Exploring Racial Bias in Rating Facial Attractiveness Among Artificial Intelligence Platforms.](https://europepmc.org/article/MED/42906598)

- 标识：`p-2511def0b4e92255227b`；发表：2026-10-21；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

研究用五个商业AI面部分吸引力评分平台，对Black、White、Latino、Asian四组各30张标准化女性图像打分，发现White组平均分最高(8.18)、Black组最低(6.91)，组间及平台间差异显著，提示评分可能偏向Eurocentric面部特征。

限制：仅有摘要：缺少平台版本、图像标准化流程、统计模型与效应量细节；刺激为AI生成的库存图而非真实患者照片，未评估对临床决策或患者结局的下游影响。

判断：摘要明确报告了种族分组、多平台评分对比与显著性检验，属于任务特异的算法公平性审计，五项证据均可满足；但证据等级仅为摘要，无法核实全文方法学细节，按规则不得直接建议纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42906598)；模型：qoder-cn/dfmodel。

### [The Ethics of Autonomous Clinical AI: Shifting From Model Accuracy to Model Impact.](https://pubmed.ncbi.nlm.nih.gov/42913471/)

- 标识：`p-5e14e8326ab1970479b8`；发表：2026-10-23；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文为观点/评论文章，主张自主临床AI的伦理评估应从模型准确率转向完整诊疗路径结局，并转述Nichol等人的九项试验建议，包括预设亚组表现、随访照护与模型变更等义务。全文未针对任何具体疾病或临床任务提供实质性的算法公平性分析，也无亚组指标或实证测量。

限制：仅有摘要级证据：未指明具体疾病或临床任务，无亚组公平性指标、偏倚机制或缓解方法比较，也无实证测量结果；摘要未说明全文是否含这些内容，但摘要本身不足以支持纳入。

判断：属评论/观点类文章，仅笼统提出伦理治理与“亚组表现”义务等一般性建议，既未指明具体医学疾病或任务，也未提供该情境下的实质性公平性分析（亚组指标、机制或评估框架），且无实证/测量评估，符合附带提及类排除标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42913471/)；模型：qoder-cn/dfmodel。

### [Evaluating four consumer artificial intelligence chatbots on smartphone dermatology images: diagnostic accuracy, the contribution of clinical context, and skin-tone equity](https://europepmc.org/article/PPR/PPR1365867)

- 标识：`p-79ee704c380a3242315c`；发表：2026-11-12；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models
- 状态：待核验

该研究在3,005例SCIN智能手机皮肤图像上评估四款消费级AI聊天机器人，比较单图、多图、图像加临床背景及纯文本四种条件下的诊断准确率，并按Fitzpatrick肤色分层检验公平性，发现表现最好的模型存在浅色与深色皮肤间的准确率差异。

限制：仅有摘要证据，缺少全文方法细节、模型版本与提示设置、统计方案及代码或数据可用性信息；无法核实完整评估设计与公平性分析的细节。

判断：摘要显示这是皮肤科诊断任务，实际测评了四款聊天机器人，并在Fitzpatrick肤色分层下报告准确率差异，五项标准均有摘要支持；但证据层级仅为摘要，按规则不能suggest_include，需获取全文核实后决定。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1365867)；模型：qoder-cn/dfmodel。

### [Comparative evaluation of training strategies using partially labelled datasets for segmentation of white matter hyperintensities and stroke lesions in FLAIR MRI.](https://pubmed.ncbi.nlm.nih.gov/42659784/)

- 标识：`p-941651f4cc3f2fc37b20`；发表：2026-08-24；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究在FLAIR MRI上比较六种利用部分标注数据训练联合白质高信号（WMH）与缺血性卒中病灶（ISL）分割模型的策略，汇总2052例MRI体数据，发现伪标签策略效果最佳，可稳定分割WMH并检出多数FLAIR阳性ISL。

限制：仅有摘要，缺乏各策略的详细方法与统计结果；未涉及任何人群分组、公平性指标或偏差分析，也未报告代码与数据获取方式。

判断：摘要聚焦部分标注数据下的分割训练策略比较，属方法学与性能评估；全文未涉及算法公平性、亚组差异、敏感属性或缓解措施，仅为普通性能研究，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42659784/)；模型：qoder-cn/dfmodel。

### [AI-Supported Semiquantitative CT Characterization of COVID-19 Pneumonia Across SARS-CoV-2 Wild-Type, Alpha, and Delta Variants and Its Association with Clinical Parameters.](https://europepmc.org/article/MED/43028567)

- 标识：`p-a27cbdea53664651a807`；发表：2026-11-09；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该回顾性单中心研究使用AI CT肺炎分析原型对255例COVID-19患者的肺部阴影进行半自动定量，比较野生型、Alpha和Delta变异组的CT衰减、体积及COVID-19概率，并分析其与临床和实验室参数的相关性。

限制：研究仅按病毒变异分组，未涉及种族、性别、年龄等敏感属性或算法公平性指标，也未评估偏倚机制、差异表现或缓解方法，因此不满足算法公平性纳入标准。

判断：研究虽使用AI算法并比较不同病毒变异组的定量输出，但未提出算法公平性、差异或编码问题，也未按敏感属性进行公平性测量，核心公平性证据缺失。

证据层级：full_text；[来源](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13762066/fullTextXML)；模型：qoder-cn/dfmodel。

### [A Qualitative Study of African Americans' Experiences with Healthcare: Developing Cultural Competency Training for Cancer Care.](https://pubmed.ncbi.nlm.nih.gov/42995326/)

- 标识：`p-a633a59806919d28b53e`；发表：2026-11-07；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

研究通过30名非洲裔美国人半结构访谈，探讨癌症照护中的就医可及性、文化观念与种族偏见经历，并据此开发文化胜任力模拟教育模块。

限制：仅有摘要，且为社区定性访谈与教育需求开发，未涉及AI/ML算法、数据集或算法公平性测量。

判断：虽涉及癌症照护中的种族偏见与健康差异，但研究对象是文化胜任力培训，未评估任何AI/ML算法或算法公平性，故不满足算法与公平性核心标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42995326/)；模型：qoder-cn/dfmodel。

### [Impact of Unrestricted Artificial Intelligence Scribe Deployment in a Single Health System on Clinician Workload and Productivity : A Quality Improvement Study.](https://europepmc.org/article/MED/42932880)

- 标识：`p-d4ccac7ce879b6812b7a`；发表：2026-10-27；发现：2026-11-14
- 主题：Clinical NLP and Foundation Models、EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

该研究为单家医疗系统的回顾性质量改进研究，采用中断时间序列分析，评估902名门诊临床医生启用环境AI病历记录助手（Heidi）后文档负担的变化，并按使用强度（未使用者、低使用者、高使用者）分组比较。结果显示启用后记录活跃时间小幅下降、病历长度增加，且高使用者变化更明显；当日与工作时间外病历完成率及wRVU均无差异。

限制：仅有摘要，缺少全文方法、亚组定义与补充材料；观察性设计存在未测量混杂，且无法区分AI生成与医生撰写的病历。文中未按患者或临床医生的敏感属性开展算法公平性分析。

判断：研究评估AI病历记录助手对临床文档工作量与效率的影响，患者人口学特征仅作为混杂因素调整，未提出算法公平性、群体差异或编码偏倚问题，也未按敏感属性做亚组公平性度量。虽属医学任务并有实证评估，但缺少公平性核心要素，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42932880)；模型：qoder-cn/dfmodel。

### [Translation and Cross-Cultural Adaptation of the Chronic Rhinosinusitis Control Test for Global Use.](https://pubmed.ncbi.nlm.nih.gov/42262654/)

- 标识：`p-014d28297e30dc61bb6f`；发表：2026-06-09；发现：2026-11-14
- 主题：Clinical NLP and Foundation Models
- 状态：机器建议排除，待抽查

该研究采用生成式人工智能（ChatGPT、Copilot、Perplexity 等大语言模型）与人工语言学家协作的混合流程，将慢性鼻窦炎控制测试（CRCT）翻译并跨文化适配为37种语言，并对各步骤译文的准确性与有效性进行定性与定量评估，作者称此举可促进数据公平。

限制：仅有摘要：未定义任何受保护群体或亚组，未报告公平性/差异性指标、偏倚测量或缓解方法；“data equity”只是泛泛表述，缺乏针对算法公平性的实证分析。

判断：本文是患者报告结局量表的翻译与跨文化适配研究，属语言验证工作。虽使用大语言模型并提及“data equity”，但未提出算法公平性/差异性问题，未定义群体属性，也未开展公平性测量，不满足公平性与群体两条证据标准，属偶然提及公平的文献，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42262654/)；模型：qoder-cn/dfmodel。

### [Fluorescence Encoding-Enabled Multiplexed Droplet Digital Recombinase Polymerase Amplification-CRISPR/Cas12a Assay for Rapid Screening of Lower Respiratory Tract Infection-Associated Bacterial Pathogens.](https://pubmed.ncbi.nlm.nih.gov/42937587/)

- 标识：`p-0f29043f64118c8a4f09`；发表：2026-10-27；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文提出荧光编码多重液滴数字RPA-CRISPR/Cas12a检测平台，结合机器学习解码，实现下呼吸道感染相关细菌病原体多重定量，并用临床样本验证与培养结果的一致性。

限制：仅提供摘要，缺少方法细节与公平性相关分组、差异或缓解分析；所述“编码”为荧光信号编码，并非人口学属性编码。

判断：研究为病原体核酸检测方法学开发，虽使用机器学习解码并开展临床一致性验证，但未提出算法公平性问题，也无群体定义、亚组比较或偏差测量，故不属于医学算法公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42937587/)；模型：qoder-cn/dfmodel。

### [Association of bilingual language use with brain age: MRI evidence from bilinguals, translators, and interpreters.](https://pubmed.ncbi.nlm.nih.gov/43041269/)

- 标识：`p-102f2c250012d5cd6b69`；发表：2026-11-09；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

研究用六个预训练脑龄模型比较105名捷克语-英语双语者（非专业双语者、笔译和同传）的年龄校正脑龄差，未发现经FDR校正的组间差异；结果强调脑龄推断对模型选择和年龄偏差校正敏感。

限制：证据仅来自摘要，未提供完整模型与统计细节；研究问题是双语经验与脑龄差异，不包含算法公平性评估。

判断：研究评估双语职业经验与MRI脑龄差距的关联，虽使用预训练模型并比较组间差异，但未提出算法公平性、偏倚机制、敏感属性差异或缓解问题，属于非公平性神经影像研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43041269/)；模型：qoder-cn/dfmodel。

### [Longitudinal pre-diagnostic blood samples predict osteoporosis risk.](https://pubmed.ncbi.nlm.nih.gov/42871651/)

- 标识：`p-15ed546d8e15d79fd402`；发表：2026-09-22；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于丹麦献血者队列的538份纵向血浆代谢组样本（99例prediagnostic骨质疏松患者与99名匹配对照），比较横断面与纵向建模的预测性能：纵向LASSO轨迹模型AUC为0.67–0.76，优于横断面的0.57–0.63，最佳模型独立验证AUC为0.70。全文摘要未涉及算法公平性、亚组差异或偏差机制的分析。

限制：仅有标题与摘要，缺少全文方法、代码与数据细节；匹配对照未按敏感属性分组，无任何亚组公平性指标、偏差机制或缓解实验证据。

判断：医学任务与机器学习模型（LASSO、随机森林）明确，但研究目标是提高骨质疏松预测的纵向采样信息量，未提出或测量任何算法公平性问题：无受保护群体定义、无亚组性能比较、无偏差或缓解分析，属于公平性偶提之外的普通预测建模研究，不满足纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42871651/)；模型：qoder-cn/dfmodel。

### [Worldwide survey on artificial intelligence in occupational therapy.](https://pubmed.ncbi.nlm.nih.gov/42585570/)

- 标识：`p-16d932da8047442b4c63`；发表：2026-08-12；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

摘要报告了一项全球职业治疗师调查，了解其对人工智能的知识、使用情况和态度；研究未评估具体算法、群体公平性指标或缓解措施。

限制：仅有摘要，缺少问卷细节、亚组公平性指标和算法层面评估；公平仅作为定性主题出现。

判断：该文是职业治疗中人工智能应用态度调查，未涉及具体AI/ML算法评估、明确受保护群体或公平性测量，且证据级别仅为摘要，不满足纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42585570/)；模型：qoder-cn/dfmodel。

### [Excessive Weight Loss with Zepbound Is Associated with Higher Rates of Adverse Events, Electrolyte Imbalances, and Hospitalization than Moderate Weight Loss](https://europepmc.org/article/PPR/PPR1346607)

- 标识：`p-2857d68b3a9af48583e2`；发表：2026-10-21；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究利用去标识化EHR比较Zepbound首年减重≥30%与5%-15%者的不良事件，发现过度减重与更高不良事件、住院及电解质异常相关；LLM仅用于事件提取，未评估算法公平性。

限制：摘要仅提供观察性药物安全性比较，未涉及医疗AI/ML算法的公平性、敏感属性或亚组公平性测量；不能作为算法公平性证据。

判断：研究为Zepbound减重幅度的药物安全性观察分析，使用EHR和LLM提取不良事件，但未评估算法公平性，也未定义敏感属性或公平性亚组，故不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1346607)；模型：qoder-cn/dfmodel。

### [Continual learning in oncology AI: A framework for safe clinical translation.](https://pubmed.ncbi.nlm.nih.gov/43063946/)

- 标识：`p-28adaf06b29241ce8db3`；发表：2026-11-20；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking
- 状态：机器建议排除，待抽查

该文综述肿瘤学AI中的持续学习方法，讨论灾难性遗忘、校准与重训等转化障碍，并提出包含亚组安全、校准稳定性等六项安全转化标准。公平性仅作为持续学习临床转化的一项风险被提及。

限制：仅有摘要，无法核实全文是否针对具体疾病或任务提供详细的公平性分析；摘要未给出具体亚组指标、实验或代码信息。

判断：该文为持续学习综述，虽提及代表性不足人群的隐性退化和亚组安全，但未命名具体疾病或任务，也未提供该场景的详细算法公平性分析，属于附带性提及，按规则排除；摘要级证据也不能建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43063946/)；模型：qoder-cn/dfmodel。

### [Nursing, Artificial Intelligence, and the Algorithmic Time Machine: Safeguarding Techno-Temporal Justice for Person-Centred Care.](https://europepmc.org/article/MED/42952232)

- 标识：`p-29e9e0f870fc81357c24`；发表：2026-10-28；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

论文提出“算法时间机器”与“技术-时间正义”概念，讨论AI如何通过分类、预测、推荐和压缩重塑护理时间与护士能动性，并主张以时间敏感框架评估AI是否支持公平、人性化、以人为中心的照护。

限制：仅摘要；属概念/话语性论文，未针对具体疾病或临床任务，无算法、数据、亚组指标或实证公平性评估，无法核验详细公平分析。

判断：文章讨论护理时间与AI治理概念，未建立具体医学任务，也未提供算法公平性测量、亚组比较或缓解评估，属一般性伦理/公平倡议，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42952232)；模型：qoder-cn/dfmodel。

### [Decision-to-Delivery Interval and Perinatal Outcomes Following Emergency Cesarean Section in Southern Ethiopia](https://europepmc.org/article/PPR/PPR1340265)

- 标识：`p-2a0b7223fe49d5fe9cd3`；发表：2026-10-15；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究为埃塞俄比亚某医院急诊剖宫产决策至分娩间期（DDI）的横断面调查，纳入284例产妇，用描述统计与二元logistic回归分析DDI延长（&gt;30分钟）的相关因素及其与围产结局（如1分钟Apgar评分）的关联。

限制：仅有摘要，无全文方法与数据细节；研究为单中心观察性设计，未涉及任何AI/ML模型、算法公平性定义、群体公平性指标或偏倚缓解措施，也没有算法层面的评估。

判断：研究主题为急诊剖宫产时间间期与围产结局的临床流行病学分析，全文不含AI/ML算法，也不存在算法公平性、群体差异测量或缓解问题；虽提及既往剖宫产等因素，但属临床危险因素而非公平性分组分析，故不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1340265)；模型：qoder-cn/dfmodel。

### [Navigating barriers: The journey of women surgeons in Türkiye Across decades.](https://pubmed.ncbi.nlm.nih.gov/42648007/)

- 标识：`p-3646728625d955d7bac3`；发表：2026-07-29；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

文章为土耳其女性外科医生职业历程的视角评论，描述历史先驱、性别刻板印象、骚扰与晋升障碍，以及机构改革建议。未涉及医学人工智能算法、模型公平性评估或缓解方法。

限制：仅有摘要，且主题为外科人力资源与性别不平等，不含AI/ML算法、亚组性能比较、公平性指标或实证算法评估。

判断：该文为外科领域性别平等视角评论；虽提及女性代表性不足和偏见，但没有评估任何医学算法、模型或算法公平性指标，属于医疗队伍不平等而非算法公平研究，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42648007/)；模型：qoder-cn/dfmodel。

### [Relapse of ANCA-Associated Vasculitis With Kidney Involvement: A Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/43044903/)

- 标识：`p-517e6927ff88a49bc260`；发表：2026-11-17；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究为法国多中心回顾性队列，分析ANCA相关性血管炎肾受累患者的复发模式、危险因素及复发与肾衰竭/死亡的关联，并评估现有复发风险评分的区分度；未涉及算法公平性、亚组差异或偏倚缓解。

限制：仅有摘要，无法核查全文方法、亚组分析或公平性指标；摘要未报告任何按人群属性分层的算法公平性评估或偏倚干预。

判断：研究聚焦临床复发预测与风险评分区分度，未提出或评估算法公平性问题，缺少定义群体、亚组发现或公平性测量，不符合医学算法公平性范围。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/43044903/)；模型：qoder-cn/dfmodel。

### [How did data sharing evolve in the decade since the FAIR Principles?](https://arxiv.org/abs/2611.20319)

- 标识：`p-636203d18db253767e77`；发表：2026-11-15；发现：2026-11-21
- 主题：待分类
- 状态：机器建议排除，待抽查

对2011–2025年PMC开放获取子集680余万篇生物医学论文进行纵向分析，提取数据可用性声明、仓储链接与JATS4R合规性，并考察学科、地区、资助方、开放获取层级及作者性别相关的数据共享差异。

限制：证据为全文，但研究属科研数据共享与开放科学计量，并非医疗算法或临床任务；性别由姓名推断，且未涉及算法公平性评估或缓解。

判断：本文分析生物医学文献的数据可用性声明与FAIR实践，按性别、地区等描述数据共享差异，但未评估任何医疗AI/算法，也未提出算法公平性测量、偏倚机制或缓解问题，故排除。

证据层级：full_text；[来源](https://arxiv.org/html/2611.20319v1)；模型：qoder-cn/dfmodel。

### [Real-time peri-operative data integration and clinical decision support: an open interoperable platform for patient data.](https://pubmed.ncbi.nlm.nih.gov/42298974/)

- 标识：`p-750bf3589b72386d1cf9`；发表：2026-06-15；发现：2026-11-14
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

介绍一个开放、可互操作的围手术期数据平台，基于 Apache Kafka 实时整合监护仪、注射泵、呼吸机、脑电与检验数据，采用本地存储与匿名化治理；自2019年已收录118915名患者、77张手术室或重症监护床位的波形与数值数据，支持实时临床决策与多中心研究。

限制：仅有摘要，未提供算法模型细节、公平性指标或亚组比较；结尾的“clinical equity”属泛化表述，不足以构成算法公平性研究证据。

判断：该文为数据平台与基础设施工程报告，未评估任何人工智能或机器学习算法的公平性，未定义受保护群体或开展亚组比较，也无差异、偏倚编码或缓解方法的实证测量；仅在结论中泛泛提及临床公平，属偶然提及，按规则排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42298974/)；模型：qoder-cn/dfmodel。

### [Identifying patients at elevated risk of stroke after transcarotid artery revascularization.](https://pubmed.ncbi.nlm.nih.gov/42323112/)

- 标识：`p-7a7241c81548105604e8`；发表：2026-06-20；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

利用VQI数据（61,111例TCAR）以CART和随机森林识别院内卒中相关因素，并按症状状态、P2Y12依从性和支架数量分组，报告调整后卒中风险差异。

限制：仅有摘要，无法核实全文；研究聚焦卒中风险因素，无公平性定义、敏感属性分组或偏倚/缓解评估。

判断：研究为TCAR术后卒中风险因素分析，使用CART/随机森林但未提出或评估算法公平性，未按敏感属性或公平指标进行亚组比较。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42323112/)；模型：qoder-cn/dfmodel。

### [Green AI for Telehealth.](https://europepmc.org/article/MED/42969789)

- 标识：`p-7b736b8d23744e060972`；发表：2026-11-02；发现：2026-11-09
- 主题：待分类
- 状态：机器建议排除，待抽查

文章讨论加拿大远程医疗中的绿色AI，提出IoT-fog-cloud资源感知架构，并主张评估临床性能、资源使用、组织适配与可持续性，同时将公平可及列为负责任AI的考量之一。

限制：仅有摘要；未给出具体疾病或临床任务、具体AI算法、亚组定义或公平性指标，也没有实施的实证评估。公平性仅泛泛提及。

判断：摘要属于远程医疗绿色AI的泛论，仅一次提及公平可及，没有具体医学任务下的算法公平性分析、亚组指标或实证测量，按附带提及规则排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42969789)；模型：qoder-cn/dfmodel。

### [Prognostic Factors for Survival in ICI-Treated NSCLC: An Umbrella Review of Evidence Certainty and Clinical Relevance.](https://europepmc.org/article/MED/43033040)

- 标识：`p-85640a44163a7e495a79`；发表：2026-11-14；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement（规则建议）
- 状态：待模型分析／人工核验

### [Artificial Intelligence in Longevity Research: From Molecular Clocks to Interventional Geroscience](https://europepmc.org/article/PPR/PPR1357971)

- 标识：`p-873f8add702e04deb02e`；发表：2026-11-03；发现：2026-11-14
- 主题：Bias Mechanisms and Measurement
- 状态：机器建议排除，待抽查

叙述性综述梳理AI衰老时钟（表观基因组、蛋白质组、视网膜、心电、MRI等）在年龄估计、预后关联、干预反应与替代终点验证四类属性上的证据，提出证据阶梯与转化链，并指出校准报告不足与因果推断缺口。

限制：仅有摘要；未见针对具体任务报告的亚组公平性指标、偏倚机制分析或缓解方法比较，公平性仅以“祖源与社会因素混杂”一句泛化带过，无可引用证据片段。

判断：该文为叙述性综述，虽涉及AI衰老时钟这一任务，但公平性仅泛化提及（祖源与社会因素混杂），未提供具体情境下的亚组度量、偏倚机制或缓解比较，属偶然提及；且仅有摘要，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1357971)；模型：qoder-cn/dfmodel。

### [Retinal imaging for cerebrovascular risk stratification: evidence, limitations, and practical thresholds for the ophthalmologist.](https://pubmed.ncbi.nlm.nih.gov/42390572/)

- 标识：`p-883b35cbccb829e5d82d`；发表：2026-07-02；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该叙述性综述评估视网膜影像（眼底、血管几何、OCT/OCTA及AI oculomics）用于脑血管风险分层的证据成熟度与临床转化局限，并提出面向眼科医生的模式化框架。

限制：仅有摘要；未报告算法公平性、亚组比较、偏倚机制或缓解方法，也无具体公平性评测指标、数据或结果。

判断：文章虽涉及视网膜AI与脑血管风险，但未提出算法公平性问题，缺少定义群体、亚组测量或公平性分析，故排除。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42390572/)；模型：qoder-cn/dfmodel。

### [Detecting Language-Related Disparities in Spiritual Care Using Artificial Intelligence.](https://pubmed.ncbi.nlm.nih.gov/42902576/)

- 标识：`p-8c77e8f6e91acd395a98`；发表：2026-10-20；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该摘要报告一项基于电子健康记录的研究，使用自然语言处理识别灵性照护文档，并用逻辑回归分析患者语言与正式灵性照护获取及时间的关系，发现非英语使用者获取率更低、支持更晚。

限制：仅见摘要，缺少模型构建、验证、亚组性能及算法公平性评估细节；研究关注的是照护获取差异，而非AI系统本身的公平性。

判断：研究用NLP测量语言相关灵性照护获取差异，属于医疗不平等观察，未评估AI/ML算法在不同群体中的公平性、编码或缓解措施；且仅有摘要，不能建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42902576/)；模型：qoder-cn/dfmodel。

### [A multinational pharmacoepidemiology atlas of prescription medication associations with all-cause mortality across six population cohorts](https://europepmc.org/article/PPR/PPR1367355)

- 标识：`p-9320409dfec5a4ff0cd3`；发表：2026-11-13；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究在英、美、芬兰、香港和日本六个队列（893万人、14.9亿条处方）中，用时依Cox模型筛查处方药与全因死亡的关联，发现VZV疫苗、阿托伐醌-氯胍等少数药物呈负相关，并提示健康使用者偏倚不能完全解释VZV疫苗信号。

限制：仅有摘要；未涉及任何算法公平性、亚组差异、敏感属性或缓解方法的分析，社会经济因素仅作为混杂调整变量出现。

判断：本文为药物流行病学关联筛查研究，虽具临床任务与统计建模，但不存在明确的算法公平性/偏倚问题、受保护群体划分或公平性评测，仅将社会经济因素作为混杂变量调整，属于无关的偶然提及，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1367355)；模型：qoder-cn/dfmodel。

### [Participation in an integrated telemedicine and psychological counseling program and psychological outcomes in patients with HCC: a multicenter retrospective cohort study.](https://europepmc.org/article/MED/42955103)

- 标识：`p-9d5bd94b760b9bad9a79`；发表：2026-10-28；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究评估HCC患者参与整合远程医疗与心理咨询项目的累计程度与12个月心理结局的关联，发现较高参与度与抑郁、焦虑、睡眠和痛苦评分较好相关，但疾病特异性生活质量较低；为多中心回顾性队列，非算法公平性研究。

限制：仅有摘要；未涉及AI/ML算法、公平性定义、受保护群体或亚组公平性评估；不能据此判断算法偏倚或缓解效果。

判断：该文为HCC远程医疗/心理咨询参与度与心理结局的临床队列研究，未评估任何AI/ML算法的公平性、偏倚机制、亚组差异或缓解措施，故不符合纳入标准。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42955103)；模型：qoder-cn/dfmodel。

### [Modifications of diagnosis-related group payment for hospital care: a systematic review](https://europepmc.org/article/PPR/PPR1351285)

- 标识：`p-9ebb0211c5729745c2dd`；发表：2026-10-27；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

系统综述评估DRG支付方式修改（主要为捆绑支付）对患者结局、质量、利用、成本和公平性的影响；发现捆绑支付与较低住院总费用相关，但公平性证据有限。该文不属于医学AI/ML算法公平性研究。

限制：仅有摘要；未涉及AI/ML算法或算法公平性评估，公平性仅作为支付政策结局之一被笼统提及，证据有限。

判断：文章评估DRG支付改革而非医学AI/ML算法；仅笼统提及公平性证据有限，缺乏针对特定疾病或任务的算法公平性分析，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1351285)；模型：qoder-cn/dfmodel。

### [Attitudes Towards Risks and Benefits of Using Generative Artificial Intelligence (GenAI) for African American Family Members of a Person with Dementia.](https://europepmc.org/article/MED/43041993)

- 标识：`p-a3bb94685f1bec630254`；发表：2026-11-14；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking（规则建议）
- 状态：待模型分析／人工核验

### [Health Care Delays, Mental Health Care, and Discrimination among US Sexual and Gender Minority Adults: Intersectional Analysis of State-level Policies.](https://europepmc.org/article/MED/42913961)

- 标识：`p-a5f1ff2ceb89d9e47906`；发表：2026-10-22；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

研究分析美国性与性别少数成年人中，州级政策包容性与就医延迟、心理健康服务使用和医疗歧视的关联，采用交叉性多层分析；未评估任何AI/ML算法或算法公平性。

限制：仅有摘要；非算法研究，无模型、预测任务或算法公平性评价，无法支持医学算法公平性纳入。

判断：该文为健康服务与政策公平性流行病学研究，未涉及AI/ML算法、其公平性测量或缓解，故不符合算法公平性范围。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42913961)；模型：qoder-cn/dfmodel。

### [Feasibility and equity in the assessment of parent-child interactions: Lessons from three approaches.](https://europepmc.org/article/MED/42956222)

- 标识：`p-a74fb8515fa29c366d7b`；发表：2026-11-01；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文比较三种亲子互动观察与编码方法（视频会议实时编码、智能手机App结合AI支持编码、可穿戴设备家庭自然情境录像）的可行性、成本、生态效度与公平可及性，并讨论临床与伦理影响，样本量分别为114、27、27。

限制：仅有摘要：未提供任何算法层面的分组公平性指标、偏差测量或缓解实验；'equity'主要指参与可及性与多样性，而非模型公平性评估。

判断：摘要聚焦亲子互动观察方法的可行性、成本与参与公平性，属发展心理学评估方法比较；虽提及AI支持编码，但未构成对AI/ML算法的公平性/偏倚测量问题，也无疾病或临床任务及分组算法性能比较，属偶然提及公平性的非算法公平研究。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42956222)；模型：qoder-cn/dfmodel。

Full-text access failed (HTTPError); abstract retained.

### [Prognostic prediction models for psoriatic arthritis in psoriasis: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42312903/)

- 标识：`p-c26def1ad664f90b88d2`；发表：2026-06-18；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该系统综述纳入15项研究、490个预后模型，评估银屑病患者发生银屑病关节炎的风险预测模型之预测性能、偏倚风险与报告质量；摘要未涉及算法公平性、亚组差异或缓解措施。

限制：仅有摘要，未提供全文；未报告公平性/亚组分析、敏感属性定义或模型代码/数据可用性，无法进一步核验。

判断：该综述虽针对银屑病关节炎这一具体临床任务，但摘要只评估预测性能、偏倚风险和报告质量，没有算法公平性、亚组差异或缓解分析，不满足综述纳入所需的详细公平性证据。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42312903/)；模型：qoder-cn/dfmodel。

### [The Prevalence and Clinical Characteristics of Atrial Fibrillation and Reflux Esophagitis Among Individuals Undergoing Health Checkups.](https://europepmc.org/article/MED/42875209)

- 标识：`p-ca3d70e3725b143a1044`；发表：2026-10-15；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究为健康体检人群的横断面流行病学分析，纳入5205名接受胃镜检查的成年人，考察房颤与反流性食管炎的关联；结果显示房颤组食管炎患病率更高，但多因素logistic回归校正性别、年龄等因素后关联不再独立，提示由共同混杂因素解释。

限制：仅提供摘要，无法核查全文方法与数据；研究不涉及任何AI/机器学习模型，也不涉及算法公平性、亚组差异或偏倚评估，仅有性别、年龄等临床协变量调整。

判断：该文为房颤与反流性食管炎的临床流行病学关联研究，全文摘要未见AI/算法被评估，也未提出算法公平性、差异或测量问题，仅有常规流行病学混杂校正；不满足医学任务之外的算法与公平性判据，故排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42875209)；模型：qoder-cn/dfmodel。

### [Digital Transformation of Rehabilitation Care: A Systems-Based Narrative Review and Conceptual Framework for Connected, Intelligent, and Hybrid Rehabilitation.](https://europepmc.org/article/MED/43028647)

- 标识：`p-cdb91e4a7fe04fb245d1`；发表：2026-10-26；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该文为康复领域数字化（远程监测、人工智能、居家与混合照护）的叙事综述，提出由互联、智能、混合三类能力构成的系统框架，并强调互操作性、数据治理、公平与持续评估等社会技术条件。

限制：仅提供摘要：无具体疾病或康复任务的公平性分析，无亚组指标、偏倚机制或缓解方法比较；“equity”仅出现在治理条件清单中一次，属附带提及。

判断：综述未针对特定疾病或康复任务提供实质性算法公平性分析（无亚组指标、机制或评估框架），公平仅作治理要素附带提及，按规则属附带提及类，排除。

证据层级：abstract；[来源](https://europepmc.org/article/MED/43028647)；模型：qoder-cn/dfmodel。

### [Artificial Intelligence as a Catalyst for Value-Based Care in Vascular Disease.](https://europepmc.org/article/MED/43035227)

- 标识：`p-cf956d481a5b46de9c2b`；发表：2026-11-15；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [reFLASH: a proof-of-concept meta-analytic framework to validate surrogate endpoints in the absence of randomized clinical trial data.](https://pubmed.ncbi.nlm.nih.gov/42641770/)

- 标识：`p-d336159d7b8908016928`；发表：2026-08-25；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

提出 reFLASH 元分析框架：将 12 项滤泡性淋巴瘤随机试验拆分为单臂试验并重新配对，用 IPTW 模拟随机化，评估 30 个月完全缓解对无进展生存期的替代终点效度。属于肿瘤学统计方法研究，不涉及医学算法公平性。

限制：仅有摘要；研究聚焦替代终点验证与配对策略稳健性，未报告公平性定义、受保护群体、亚组差异或偏倚测量。

判断：该文虽评估一种统计建模框架并报告经验结果，但未提出或测量医学算法公平性、群体差异、编码偏倚或缓解措施，不符合公平性研究纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42641770/)；模型：qoder-cn/dfmodel。

### [Predicting PANSS symptoms in schizophrenia spectrum disorders using speech only: an international, multi-centre, computational secondary analysis across multiple languages.](https://pubmed.ncbi.nlm.nih.gov/42991136/)

- 标识：`p-dfd76ee4553e36909d88`；发表：2026-10-28；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：待核验

该国际多中心计算二次分析汇总10国453例精神分裂症谱系障碍患者的语音，将录音切分为6664段，比较16种算法预测8个PANSS条目，并按年龄、性别、教育程度和症状严重度做偏倚检查。预训练多语言嵌入表现最佳；除男性N4准确率较低外，未见年龄、性别或教育偏倚，但高症状严重度下性能下降。

限制：仅摘要证据：未提供偏倚检查的具体分层指标、效应量、阈值、置信区间或任何缓解措施，无法核验公平性分析深度；也未报告代码或数据。

判断：摘要显示明确的临床任务、算法评估、按年龄/性别/教育/症状严重度的偏倚检查及RMSE实证结果，符合入选标准；但证据仅限摘要，无法核验详细公平性方法与结果，按规则不能suggest_include，暂予hold。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42991136/)；模型：qoder-cn/dfmodel。

### [Short- Versus Long-Course Radiation in Total Neoadjuvant Therapy for Locally Advanced Rectal Cancer: A Propensity-Matched National Cancer Database Analysis.](https://pubmed.ncbi.nlm.nih.gov/42598830/)

- 标识：`p-ef2c73c3a8803f2d0255`；发表：2026-08-14；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究利用国家癌症数据库比较局部晚期直肠癌全程新辅助治疗中长程与短程放疗的总生存及病理结局；倾向评分匹配后生存无差异，长程组淋巴结降期率较高。未涉及AI/ML算法或公平性分析。

限制：仅有摘要，无法评估全文细节；且摘要显示为治疗方式比较，不含算法公平性、受保护群体差异或缓解措施分析。

判断：摘要为直肠癌长/短程放疗的倾向评分匹配比较，未评估AI/ML算法、公平性、受保护群体或差异指标，不符合医学算法公平性纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42598830/)；模型：qoder-cn/dfmodel。

### [Orbital morphometry on computed tomography for sex estimation: A systematic review and meta-analysis.](https://pubmed.ncbi.nlm.nih.gov/43057131/)

- 标识：`p-f0405d6bf007e5f2b22c`；发表：2026-11-19；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation（规则建议）
- 状态：待模型分析／人工核验

### [Striving for Equity in Cystic Fibrosis Research: Perspectives from Black and Hispanic/ Latino(a) Individuals with CF.](https://pubmed.ncbi.nlm.nih.gov/42896705/)

- 标识：`p-fa3ca2ed93703292ee6b`；发表：2026-10-19；发现：2026-11-14
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究通过半结构化访谈，探讨黑人及西班牙裔/拉丁裔囊性纤维化患者对临床研究的看法、参与障碍与促进因素，并提出以社区支持和信息透明为核心的纳入改进方案。研究聚焦临床研究代表性不足的社会文化因素，未涉及任何算法或AI模型。

限制：仅有摘要，缺少访谈提纲、编码框架与完整主题细节；研究本身不含算法、数据集或模型评估，无法提供算法公平性证据。

判断：研究主题为囊性纤维化临床研究参与的健康公平与定性访谈，不涉及任何AI/ML算法、模型编码差异或算法公平性评估，属于健康差异研究而非医学算法公平性研究，故不纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42896705/)；模型：qoder-cn/dfmodel。

### [Smoking and dementia risk: an updated systematic review and meta-analysis of 61 prospective cohort studies and implications for tobacco control.](https://pubmed.ncbi.nlm.nih.gov/43034842/)

- 标识：`p-2308c78840b3881bc14d`；发表：2026-11-07；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation（规则建议）
- 状态：待模型分析／人工核验

### [Machine learning-based risk prediction of hepatocellular carcinoma in patients with chronic hepatitis B: current evidence and future directions.](https://europepmc.org/article/MED/43064890)

- 标识：`p-b7ac23993de63dc9a3e9`；发表：2026-11-20；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706)

- 标识：`p-220173ecbe71aeffc6a2`；发表：2026-11-10；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、Clinical NLP and Foundation Models、EHR, Physiological Signals and Healthcare（规则建议）
- 状态：待模型分析／人工核验

### [Data-centric, robust, and explainable multimodal deep learning for clinical decision support: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42667902/)

- 标识：`p-2dc7893202614a28f741`；发表：2026-08-26；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [AI-generated patient instructions as safety-critical communication: a provisional evidence-informed framework for clinical deployment.](https://pubmed.ncbi.nlm.nih.gov/42607431/)

- 标识：`p-31dd08c87fcdfb2c9189`；发表：2026-08-17；发现：2026-11-21
- 主题：Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [Application of geospatial technologies in mental health research: A scoping review of progress and future directions.](https://europepmc.org/article/MED/43042965)

- 标识：`p-496be92504999e54331b`；发表：2026-11-17；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement（规则建议）
- 状态：待模型分析／人工核验

### [In-context learning for medical artificial intelligence.](https://pubmed.ncbi.nlm.nih.gov/43008739/)

- 标识：`p-62e5a416316a8b47bef5`；发表：2026-11-10；发现：2026-11-14
- 主题：Fairness Evaluation and Benchmarking、Pre-processing Mitigation、In-processing Mitigation、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [Bias and equity in large language model-based applications for health care: a scoping review.](https://europepmc.org/article/MED/43052083)

- 标识：`p-aca067eb1061051f9b86`；发表：2026-11-18；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [Intelligent immunotherapy: AI-driven optimization of CAR-T therapy in hematologic malignancies.](https://pubmed.ncbi.nlm.nih.gov/42904142/)

- 标识：`p-d3566a29f4f70f84cac4`；发表：2026-10-12；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [Artificial Intelligence in Thoracic Pathology and Biomarker Assessment: An IASLC Pathology Committee Review.](https://europepmc.org/article/MED/43064238)

- 标识：`p-aa1d2c08ab2918b9678a`；发表：2026-11-20；发现：2026-11-21
- 主题：Pre-processing Mitigation、In-processing Mitigation、Clinical NLP and Foundation Models（规则建议）
- 状态：待模型分析／人工核验

### [Application of Artificial Intelligence (AI) in cancer symptom management for adult cancer survivors: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42603423/)

- 标识：`p-622c2ee72af5786411dd`；发表：2026-08-15；发现：2026-11-21
- 主题：Pre-processing Mitigation、EHR, Physiological Signals and Healthcare（规则建议）
- 状态：待模型分析／人工核验

### [Explainable Artificial Intelligence for Cognitive Workload Assessment: Methods, Evidence, and Human-Centered Evaluation](https://europepmc.org/article/PPR/PPR1372432)

- 标识：`p-b1af80e58334a13852a7`；发表：2026-11-18；发现：2026-11-21
- 主题：Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare（规则建议）
- 状态：待模型分析／人工核验

### [Potential and pitfalls of artificial intelligence to address disparities in epilepsy.](https://europepmc.org/article/MED/43064818)

- 标识：`p-801228119b6cf272fa53`；发表：2026-11-20；发现：2026-11-21
- 主题：Fairness Evaluation and Benchmarking、EHR, Physiological Signals and Healthcare（规则建议）
- 状态：待模型分析／人工核验
