# 医疗算法公平性文献摘要 · 2026-11-04

机器整理的候选与收录建议；未代表人工审核或实验复现。

候选库：56 篇；当日发现、更新或完成分析：56 篇。

已有有效中文分析：54 篇；待分析或缺少摘要证据：2 篇。

## 检索覆盖

- arxiv / 查询 4744eb3faccd：5 条；完整
- arxiv / 查询 42b91404506f：0 条；完整
- europepmc / 查询 249ba7c65421：19 条；完整
- europepmc / 查询 b614de0bf8b6：0 条；完整
- pubmed / 查询 29bd77c2182f：34 条；完整
- pubmed / 查询 d4312ff2e61d：3 条；完整

## 当日候选

### [The Role of Artificial Intelligence in PET Imaging.](https://pubmed.ncbi.nlm.nih.gov/42957403/)

- 标识：`p-103ada15cebbb7f64a8f`；发表：2026-09-29；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该文综述AI在PET成像临床流程中的应用，包括自动预约与协议、深度学习重建、病灶检测及大语言模型报告，并讨论算法偏倚、数据漂移和监管等实施挑战。

限制：仅有摘要，属综述；未提供明确受保护群体、亚组分析或实证公平性评估，无法验证方法细节与结果。

判断：PET医学影像AI综述，摘要仅泛提算法偏倚等挑战，未定义敏感群体或开展实证公平性评估；按综述归为相关。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42957403/)；模型：qoder-cn/dfmodel。

### [Rethinking Intellectual Property in the Age of Generative AI: Ethics, Rights and Accountability](https://europepmc.org/article/PPR/PPR1356304)

- 标识：`p-104fdea547833123c665`；发表：2026-11-03；发现：2026-11-04
- 主题：待分类
- 状态：相关综述／资源

文章以同意、补偿、署名与问责四轴框架分析生成式AI知识产权伦理，比较专利、诉讼、和解及创作者调查，并提出分层治理模型。

限制：摘要仅呈现二手数据、法律案例与调查结果，未开展医学算法公平性测量；不能据此推断临床效用或代码数据可用性。

判断：文章属生成式AI知识产权与伦理治理讨论，虽提及算法偏见审计，但无医学/临床任务、具体算法评估或敏感群体公平性实证测量，故不宜纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1356304)；模型：qoder-cn/dfmodel。

### [Precision Lipid Management in the Era of Biotechnology and Artificial Intelligence: From Gene Editing to Smart Drug Delivery.](https://pubmed.ncbi.nlm.nih.gov/42599575/)

- 标识：`p-1607ccec012a87a0fdca`；发表：2026-08-14；发现：2026-11-04
- 主题：待分类
- 状态：相关综述／资源

该叙述性综述讨论高脂血症精准管理中基因编辑、PCSK9抗体、纳米递送与人工智能辅助治疗优化等新兴策略，强调转化成熟度、临床适用性与监管问题，仅把算法偏倚、公平实施列为转化障碍之一，未开展算法公平性评估。

限制：仅有摘要，无全文方法与结果细节；摘要未体现具体算法、数据集或亚组公平性分析，“算法偏倚”仅为泛泛列举，不能据此判断全文是否含公平性内容。

判断：摘要为叙述性综述，提及AI驱动的预测与治疗优化，但未提出或检验明确的算法公平性/差异问题，也无分组定义与实证测量评估，不满足五项证据标准；属与公平性主题相关的综述类文献。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42599575/)；模型：qoder-cn/dfmodel。

### [BiasLab: A multilingual dual-framing framework for LLM bias measurement, applied to workplace and HR contexts.](https://pubmed.ncbi.nlm.nih.gov/42434887/)

- 标识：`p-2ace6f04876029d3419e`；发表：2026-07-11；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：相关综述／资源

BiasLab 提出多语言双框架提示对方法，配合随机包装扰动、固定选项约束与极性对齐打分，量化 LLM 在六个职场/HR 议题（性别领导力、就业空档、年龄招聘等）上的方向性输出偏好；对十个模型、十二种语言生成 43,200 条回答，发现一致的方向偏好与“拒斥强于赞同”的不对称模式。

限制：仅见摘要，未见代码、数据或完整方法细节；评估场景为职场与 HR，而非临床或生物医学任务，医疗相关性未建立；偏好是否构成公平意义上的偏差被作者称为依赖议题，未做下游决策影响分析。

判断：该文是 LLM 方向性偏见的多语言测量框架，具备明确属性（性别、年龄）与大规模实证评估，属公平性评测方法学，可作为相关参考；但任务为 HR/职场语境，未涉及任何临床、EHR、影像或生理信号任务，医疗证据标准未满足，故不作为纳入建议。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42434887/)；模型：qoder-cn/dfmodel。

### [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215)

- 标识：`p-2fcb4e34b5f7daab4c8d`；发表：2026-10-28；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、Post-processing Mitigation、Clinical NLP and Foundation Models、EHR, Physiological Signals and Healthcare
- 状态：建议纳入，待审核

研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。

限制：证据来自单一急诊来源、120例及每格3个种子，部分结果为描述性点估计；仅使用源数据中存在的种族类别和二分类性别，未覆盖交叉身份；团队为同模型五实例；多样化视角集成属于沙盒审计性缓解，未做临床验证。

判断：全文报告了临床多智能体LLM的公平性实证审计与缓解：包含急诊分诊任务、模型与拓扑评估、种族和性别反事实组以及20格实证测量，满足五项纳入标准。

证据层级：full_text；[来源](https://arxiv.org/html/2610.38215v1)；模型：qoder-cn/dfmodel。

### [A Scoping Review of Artificial Intelligence and Machine Learning for Spatio-temporal Infectious Disease Forecasting](https://europepmc.org/article/PPR/PPR1356097)

- 标识：`p-39172eeeef221e79bbcc`；发表：2026-11-03；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking
- 状态：相关综述／资源

该文为时空传染病预测AI/ML的范围综述，纳入93项研究，总结模型、误差指标、外部验证、代码共享及公平性分析等评估缺口，指出仅1项研究开展公平性分析。

限制：仅有摘要，且为范围综述，未开展原始公平性实证评估；公平性仅作为文献缺口提及，未定义敏感属性或亚组，无法支持纳入。

判断：摘要显示其为传染病预测方法学范围综述，虽指出公平性分析与公平性评估不足，但未实施针对特定群体的算法公平性测量或缓解，属于相关综述而非符合五项证据标准的研究。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1356097)；模型：qoder-cn/dfmodel。

### [AI-Driven Multiomics Biomarkers for Precision Oncology: Navigating the Translational Gap and Regulatory Hurdles.](https://pubmed.ncbi.nlm.nih.gov/42560117/)

- 标识：`p-3afb8c155e44c9705fd1`；发表：2026-08-06；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该文为精准肿瘤学多组学AI生物标志物的综述，梳理从数据生成、整合、标志物发现、验证到监管落地的五阶段路线，并提及异质性、可重复性、算法偏倚与伦理监管等转化障碍。

限制：仅有摘要，且为综述；未提供原始实证或公平性测量，未定义受保护群体或亚组，也未验证具体缓解措施或临床获益。

判断：摘要显示文章综述多组学与AI在精准肿瘤学中的转化，并笼统提及算法偏倚，但无实证公平性评估、群体定义或方法实施；按规则属相关综述而非可纳入的公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42560117/)；模型：qoder-cn/dfmodel。

### [A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering](https://arxiv.org/abs/2611.00298)

- 标识：`p-3d7d2c77176c61d55abc`；发表：2026-10-30；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、In-processing Mitigation、EHR, Physiological Signals and Healthcare
- 状态：建议纳入，待审核

提出 MICF 框架，将反事实公平约束重述为 Transformer 激活层面的分析与干预：用激活补丁定位敏感属性相关层，分解直接与间接效应，并在推理时通过激活转向降低种族偏差；在 UTICalc 临床预测和 COMPAS 表格任务上评估。

限制：仅覆盖 TabPFN、两个表格任务和二元种族属性，主要优化总效应；部分转向设置伴随准确率下降，作者也强调结果不构成通用公平性保证或临床部署依据。

判断：全文包含临床 UTI 预测任务、TabPFN 算法、反事实公平问题、种族敏感属性和实证测量，五个纳入证据均具备，故建议纳入。

证据层级：full_text；[来源](https://arxiv.org/html/2611.00298v1)；模型：qoder-cn/dfmodel。

### [Governing artificial intelligence in Australian healthcare organisations - a qualitative study of staff perspectives.](https://europepmc.org/article/MED/42906928)

- 标识：`p-3e7581d5cf989529b639`；发表：2026-11-01；发现：2026-11-04
- 主题：待分类
- 状态：相关综述／资源

该定性研究访谈澳大利亚某医疗机构的23名工作人员，归纳AI治理的五个组织域：风险评估、基础设施与数据、伦理、能力与文化、治理结构，强调生命周期监督与公平透明。

限制：仅有摘要；为员工观点定性研究，未评估具体AI/ML算法，未定义受保护群体或开展公平性测量；不能据此推断算法性能差异或临床获益。

判断：属医疗AI治理与伦理的视角研究，提及公平但非算法公平性实证评估，缺乏临床任务、具体算法、群体定义和测量，故列为相关。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42906928)；模型：qoder-cn/dfmodel。

### [Artificial intelligence-driven pharmacovigilance: transforming signal detection, real-world drug safety monitoring, and regulatory decision-making.](https://pubmed.ncbi.nlm.nih.gov/42975625/)

- 标识：`p-4271f40bb01045bc8aab`；发表：2026-11-03；发现：2026-11-04
- 主题：Clinical NLP and Foundation Models、EHR, Physiological Signals and Healthcare
- 状态：相关综述／资源

本文为药物警戒领域的AI应用综述，梳理机器学习、深度学习、自然语言处理在不良事件检测、文献挖掘、信号优先级排序以及EHR和社交媒体数据分析中的应用，并讨论大语言模型、联邦学习、区块链、数字孪生与IoT等新兴技术；同时指出可解释性、数据质量、网络安全、算法偏倚与监管验证等落地障碍。

限制：仅提供摘要，属综述性总结，未给出原始实证数据或代码与数据来源；未界定受保护人群或敏感属性，未开展算法公平性测量或缓解实验；算法偏倚仅作为实施挑战被列举，缺乏编码证据与性能差异分析。

判断：摘要显示该文为综述，涉及不良事件检测这一生物医学任务及机器学习等方法，并提及算法偏倚，但未定义受保护群体、未设计亚组发现协议，也未实施任何公平性实证或测量评估，不满足纳入所需的五项证据要求；按综述类文献归为相关。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42975625/)；模型：qoder-cn/dfmodel。

### [Fairness Metrics based on the AUC in Clinical Predictive AI](https://arxiv.org/abs/2611.05222)

- 标识：`p-5903974910ebbe7950d2`；发表：2026-11-03；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：建议纳入，待审核

该文系统分析临床预测模型中八种基于AUC的公平性指标，阐明AUC不可折叠性对指标解释的影响，并以EuroSCORE II为例用模拟展示亚组与跨组AUC差异，建议报告完整AUC矩阵并优先采用组内AUC parity。

限制：证据主要来自方法学分析与EuroSCORE II模拟，仅涉及二分类结局和男女两个亚组；未评估真实世界多中心数据的公平性，也未深入验证校准公平性及干预效果。

判断：该文针对临床预测AI的AUC公平性指标开展正式分析与模拟测量，明确以性别定义亚组并比较组内/跨组差异，满足临床任务、算法评估、公平性问题和实证评价五项标准。

证据层级：full_text；[来源](https://arxiv.org/html/2611.05222v1)；模型：qoder-cn/dfmodel。

### [Responsible Credit-Line Increase: A Fairness-Aware, Explainable, and Governed Machine-Learning Framework for Socio-Technical Lending Systems](https://europepmc.org/article/PPR/PPR1353923)

- 标识：`p-59d12037c0f5cd6ad9d2`；发表：2026-10-30；发现：2026-11-04
- 主题：Post-processing Mitigation、Fairness Evaluation and Benchmarking
- 状态：机器建议排除，待抽查

提出面向信贷额度主动上调（CLI）的公平性感知、可解释且可治理的机器学习框架：在组合预期损失预算与显式公平容忍度下最大化增量利润，将问题归约为经校准、可审计的阈值策略，并在不改变已验证模型的前提下做群体级重校准以控制差异影响。评估基于6万账户的合成组合，并在一公开信贷基准上复核。

限制：仅有摘要级证据，未说明代码或数据可得性；实验数据为合成信贷组合与公开信贷基准，任务与场景均属金融信贷，不涉及任何生物医学或临床数据、影像、病历或信号，超出本综述的医学算法范围。

判断：摘要显示研究对象为消费信贷额度上调决策，属金融风控场景，缺少生物医学/临床任务这一必要条件；其余算法、公平性、受保护群体与实证评估虽具备，但领域不符，故判为范围外。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1353923)；模型：qoder-cn/dfmodel。

### [Artificial intelligence in dedicated forensic-science journals: A bibliometric and science-mapping analysis (1991-2026).](https://pubmed.ncbi.nlm.nih.gov/42617285/)

- 标识：`p-5c95d2dbcd135df1a0e0`；发表：2026-08-18；发现：2026-11-04
- 主题：待分类
- 状态：相关综述／资源

对1991–2026年法医科学专门期刊中的人工智能文献进行文献计量与科学图谱分析，纳入1127篇文献，刻画其增长、国家分布与主题结构，并统计外部验证、校准、可采性、对抗安全以及偏见/公平等术语在题录中的出现比例。

限制：仅有摘要，未见数据、代码或检索细节；偏见/公平仅以标题、摘要、关键词中的词汇计数呈现，无法证明任何算法存在或不存在下游性能差异。

判断：该文属文献计量/科学图谱综述，只统计偏见与公平（1.9%）等术语的可见度，未针对具体算法开展公平性测量，也未定义受保护群体或子群发现方案，不属临床/生物医学任务的公平性实证评估。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42617285/)；模型：qoder-cn/dfmodel。

### [MRI radiomics for predicting pathological complete response in breast cancer: a systematic review of current evidence and limitations.](https://pubmed.ncbi.nlm.nih.gov/42541995/)

- 标识：`p-5f6af5fefa6890d56a13`；发表：2026-07-27；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：相关综述／资源

该系统综述汇总35项MRI影像组学预测乳腺癌新辅助治疗病理完全缓解（pCR）的研究，采用METRICS评分与改良QUADAS-2框架评估方法学质量、偏倚风险及亚组表现，报告合并AUC 0.813，并指出样本量普遍不足、外部验证少见、亚组分析仅占14%，限制了公平性能的评估。

限制：证据仅为摘要：未给出具体敏感属性、各亚组样本量或公平性量化指标，也未呈现检索、合并及各研究偏倚评定细节；该文为二次研究，未实施模型训练或公平性干预，无法据此判断全文是否缺失代码或临床验证。

判断：摘要显示这是对MRI影像组学pCR预测模型的系统综述，涉及公平性能、人口学报告与亚组分析，属算法公平性评价范畴；但为综述性二次研究，未定义具体受保护属性，也未自行实施实证公平性测量，且仅有摘要，故列为相关而非纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42541995/)；模型：qoder-cn/dfmodel。

### [Ethical and legal challenges of integrating artificial intelligence into paediatric surgery.](https://pubmed.ncbi.nlm.nih.gov/41725549/)

- 标识：`p-747c407c5696b151b802`；发表：2026-02-23；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该叙述性综述梳理将AI（影像、机器人辅助、早期风险预测）整合进儿科手术的伦理与法律挑战，涵盖敏感儿科数据保护、知情同意、算法偏见缓解、自适应系统责任界定与监管协调，并提出联邦学习、模型卡、绩效审计等治理建议。

限制：仅有摘要，属叙述性综述与伦理法律分析，未报告具体算法、队列或分组公平性测量结果，也无代码或数据链接；不能据此推断全文缺乏相关内容。

判断：摘要显示为2015-2025年文献与监管指南的叙述性综述，仅定性提出“缓解算法偏见”等治理议题，未实施任何算法公平性实证测量或分组评估，按规则归为相关综述而非可纳入研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/41725549/)；模型：qoder-cn/dfmodel。

### [Technology Matters: Emerging technologies in clinical informatics to support child and adolescent mental healthcare safety.](https://pubmed.ncbi.nlm.nih.gov/41937617/)

- 标识：`p-791ad6693c5fab805032`；发表：2026-04-06；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare、Clinical NLP and Foundation Models
- 状态：相关综述／资源

该文概述电子健康记录在儿童青少年精神卫生安全中的应用，涵盖精神药物安全、自伤风险与限制性措施监测，并讨论预警疲劳、实施差异及高风险青少年检测中的算法偏倚等挑战。

限制：仅有摘要，属综述/观点性文章；未评估具体AI/ML算法，未定义受保护群体，也未开展公平性实证测量或干预。

判断：文章讨论EHR与AI在儿童精神卫生安全中的前景和算法偏倚风险，但无具体算法评估、群体定义或实证公平性评价，故作为相关背景文献而非可纳入研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/41937617/)；模型：qoder-cn/dfmodel。

### [Artificial intelligence in medical education: a narrative review across four functional domains.](https://pubmed.ncbi.nlm.nih.gov/42574942/)

- 标识：`p-a71fdd3bd3bf63d2ba2a`；发表：2026-08-10；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Clinical NLP and Foundation Models
- 状态：相关综述／资源

该叙事综述按四个功能域总结医学教育中的AI应用，涵盖教学与内容生成、模拟训练、评估与学习分析、诊断推理，强调监督实施、透明报告和公平关切，但未开展算法公平性实证评估。

限制：仅有摘要，未提供全文方法、纳入研究细节或公平性分析；摘要未报告敏感属性、分组比较、公平性指标、代码或数据链接。

判断：该文是医学教育AI应用的叙事综述，仅将公平性列为评估关切，未提出算法公平、差异、编码、缓解或公平测量问题，也未定义敏感群体或开展实证公平评估，故归为相关综述。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42574942/)；模型：qoder-cn/dfmodel。

### [Editorial Commentary: Calling Balls and Strikes: For Artificial Intelligence Models to Accurately Predict Rotator Cuff Retear, We Must Carefully Define the Strike Zone.](https://pubmed.ncbi.nlm.nih.gov/42701888/)

- 标识：`p-ab58f18226651ba5545c`；发表：2026-09-06；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该编辑评论指出，深度学习可用于肩袖修复后早期再撕裂预测，但单术者训练数据会引入偏倚变异，标注主观性也会影响模型可信度；临床落地需关注预处理、泛化性、公平性与治理。

限制：仅有摘要和评论性文本，无方法、样本、分组或结果数据；不能据此判断全文是否包含代码、数据集或临床验证。

判断：本文为编辑评论，讨论肩袖修复后 retear 预测中的迁移学习、单术者数据偏倚与公平性治理；未定义受保护群体，也未实施公平性测量或实证评估，故仅归为相关。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42701888/)；模型：qoder-cn/dfmodel。

### [Toward multimodal physiological assessment of clinical performance in simulation-based medical education: a machine learning approach.](https://europepmc.org/article/MED/42955499)

- 标识：`p-bbc3b6330d6af062be13`；发表：2026-10-29；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare
- 状态：相关综述／资源

该研究用 Empatica E4 腕带同步采集皮肤电、心率与皮温等多模态生理信号，结合遗传算法特征选择与神经网络，对高保真模拟教学中医师评定的“新手/胜任”表现分级进行二分类，内部验证平衡准确率约 84-85%，属生理信号驱动的教育评估模型。

限制：仅有摘要：未报告代码或数据可用性；无任何分组公平性指标、亚组分析或偏差测量，公平性仅在结论中列为未来工作；评分类标签效度与跨机构泛化性未验证；无法据此判断全文是否另有分析。

判断：纳入生理信号并用机器学习分类临床模拟表现，属生物医学算法评估，但研究问题是分类性能与不平衡稳健性，未定义受保护群体、未做亚组或偏差测量，公平性仅作为后续工作提及，不满足公平性问题的证据要求。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42955499)；模型：qoder-cn/dfmodel。

### [Public evaluations of AI-mediated healthcare when considering people with diverse access and support needs: a mixed-methods survey.](https://pubmed.ncbi.nlm.nih.gov/42472498/)

- 标识：`p-ceb7d989076bafad0d24`；发表：2026-07-17；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

一项混合方法问卷研究（N=1151，其中117人作答开放式问题），考察受访者在考虑“获取与支持需求多样的人群”时如何评价AI介导的医疗服务。量化部分结合贝叶斯回归、验证性因子分析与相关分析，质性部分用编码本主题分析归纳出四个主题，其中包含对“不公平分类”的担忧。

限制：仅有摘要，未涉及具体AI系统、模型或数据集；未报告算法层面的公平性指标或亚组性能比较；质性材料为受访者主观担忧，不构成对算法偏见的测量；摘要未提及代码或数据可用性，故无法判断全文。

判断：该文为公众态度问卷研究，讨论AI医疗的可及性、责任与公平担忧（含“不公平分类”主题），但未评估具体算法、未对定义群体开展公平性测量，仅属医疗AI公平议题的相关背景文献，不满足五项纳入证据标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42472498/)；模型：qoder-cn/dfmodel。

### [AI algorithms and external validation: promises, pitfalls, and a practical blueprint.](https://pubmed.ncbi.nlm.nih.gov/42961821/)

- 标识：`p-cf9833bc80232d798aba`；发表：2026-10-30；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：相关综述／资源

文章提出临床AI外部验证的实践蓝图，强调预注册、多中心代表性队列、避免患者与时间重叠、校准和净获益评估、预设亚组与公平性审计，并连接部署后漂移监测和模型更新。

限制：仅有摘要，属方法学蓝图/观点性文本；未报告实际数据、敏感属性定义、亚组发现协议或经验性公平性测量结果，无法验证公平性收益。

判断：讨论临床AI外部验证并明确提及亚组差异和公平性审计，但摘要级方法框架未定义受保护群体，也未实施经验性公平性评估，不满足纳入的五项证据标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42961821/)；模型：qoder-cn/dfmodel。

### [Artificial intelligence-based nurse scheduling in healthcare: A scoping review of functional features and empirical outcomes.](https://pubmed.ncbi.nlm.nih.gov/42600237/)

- 标识：`p-d39e326704b43f57948f`；发表：2026-08-03；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare
- 状态：相关综述／资源

该文为AI护士排班的范围综述，梳理11项研究的算法类型、功能特征及组织、员工和患者层面实证结局，指出系统层研究较重视自动化、护士偏好与公平建模，但实时性、医院系统集成和真实世界评价仍有限。

限制：仅有摘要，无法核查全文方法、纳入研究细节及公平性测量；公平仅作为排班功能被提及，未定义敏感群体或开展亚组/偏差实证评估；综述不能提供原始干预证据。

判断：属AI护士排班范围综述，涉及医疗运营算法及公平功能描述，但无明确敏感属性分组或公平性实证测量，且摘要级证据不能建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42600237/)；模型：qoder-cn/dfmodel。

### [Responsible AI for Acute Stroke Management.](https://pubmed.ncbi.nlm.nih.gov/42751787/)

- 标识：`p-e63a02248d4e14119359`；发表：2026-09-17；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking
- 状态：相关综述／资源

该综述梳理急性卒中管理中人工智能的可解释性与公平性研究，涵盖大血管闭塞检测、ASPECTS评分与功能预后预测，指出后验解释方法缺乏验证、公平性评估因人口学元数据不足与缺少卒中专用公平标准而少见，并呼吁建立联合评估可解释性、公平性与泛化性的统一框架。

限制：仅摘要可及，无法核查全文方法、数据与结果；本文为文献综述，未开展作者自身的实证测量或干预实验，故不能作为原创公平性证据。

判断：摘要显示其为综述性文章，系统总结卒中AI中的算法偏见与公平评估缺口，符合算法公平议题但无原始实证评估，且仅有摘要证据，故列为相关而非纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42751787/)；模型：qoder-cn/dfmodel。

### [Interpretable models for scRNA-seq data embedding with multi-scale structure preservation.](https://europepmc.org/article/MED/42950829)

- 标识：`p-e76f08abf1081b362cba`；发表：2026-10-28；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

摘要提出ViScore评分框架与ViVAE深度嵌入模型，用于单细胞转录组数据的多尺度结构保持与可解释降维，并称评分框架兼顾可扩展性与公平性。

限制：仅有摘要；未给出敏感属性、受保护群体、公平性指标定义或分组结果，无法核验公平性实证；需全文确认。

判断：摘要仅笼统提及评分框架关注公平性，未建立明确的算法公平性测量问题或分组证据；摘要级证据不足以纳入，需全文核验。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42950829)；模型：qoder-cn/dfmodel。

### [Using Generative AI for Behavioural Research Effectively and Responsibly: a BR-UK Statement](https://europepmc.org/article/PPR/PPR1351821)

- 标识：`p-ecc70724990e28b4c271`；发表：2026-10-28；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该文是BR-UK关于行为研究中有效且负责任使用生成式AI的开放声明，提出伦理诚信、人类在环、严格评估和多方协同四项主张，并为七类利益相关者提供建议与工具。

限制：仅有摘要，未报告具体医学或临床任务、被评估算法、分组公平性指标或实证测量；属伦理与政策声明，不能支持纳入证据。

判断：属伦理和政策声明，仅泛提算法偏见风险；缺少生物医学任务、具体AI算法公平性评估、受保护群体或实证测量，五项标准均未满足，且摘要不足以纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1351821)；模型：qoder-cn/dfmodel。

### [The symbiotic shift: How AI is reshaping rehabilitation and the future of work.](https://pubmed.ncbi.nlm.nih.gov/42804281/)

- 标识：`p-f51c76f9a365032f9da6`；发表：2026-09-28；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare
- 状态：相关综述／资源

本文为结构化文献综述，论述人工智能在康复与重返工作场景中的“共生式”应用：临床康复中的个体化治疗、计算机视觉动作分析与预后预测，重返工作流程中的功能能力评估与岗位辅导，以及面向残障或慢性病人群的包容性就业支持，并强调隐私、算法偏见与公平可及等伦理要求。

限制：仅有摘要，未见具体算法、数据集、代码或实证测量；算法偏见仅作为伦理议题被列举，未提出公平性研究问题、未定义受保护属性下的分组比较，也无任何缓解或评测实验。

判断：该文属观点/综述类，虽涉及康复与职业健康中的AI及算法偏见伦理，但未评估具体算法、未开展公平性测量或分组比较，也无实证评测，依规则归为相关文献而非可纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42804281/)；模型：qoder-cn/dfmodel。

### [Investigating Patient Trust and Intention to Act in AI-Supported Clinical Decisions: Cross-Sectional Survey.](https://pubmed.ncbi.nlm.nih.gov/42970578/)

- 标识：`p-fafce843d0071edb38ce`；发表：2026-11-02；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare
- 状态：相关综述／资源

摘要报告一项美国1185名成人的横断面调查，比较医生单独、医生加风险计算器、医生加AI风险预测三种推荐来源下患者的行动意愿、信任与偏好，并考察社会人口学特征的影响。研究未针对模型开展算法公平性评估。

限制：仅有摘要；未报告受保护属性分层的模型性能或任何公平性度量；“公平”仅作为定性反馈主题出现，无法核实全文的方法、数据与亚组结果。

判断：该研究调查患者对AI临床决策支持的态度与部分社会人口学差异，属患者认知层面研究；缺少明确的算法公平性、偏倚编码或缓解问题，也未实施公平性测量，故判为相关而非纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42970578/)；模型：qoder-cn/dfmodel。

### [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/)

- 标识：`p-064ee08a8e0905727f10`；发表：2026-09-29；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

综述讨论资源有限地区抗菌耐药监测从即时诊断到AI决策支持的演进，涵盖机器学习用于耐药检测、处方与暴发预测，并提及算法偏倚、公平部署及实施挑战。

限制：仅为摘要层面的综述，未提供具体算法、数据集、公平性测量或实证评估，也未定义敏感属性或报告代码与临床验证。

判断：文章为AMR监测综述，虽提及算法偏倚与公平部署，但无明确公平性研究问题、分组评估或实证测量；摘要级证据不足以纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42810525/)；模型：qoder-cn/dfmodel。

### [Institutional Governance Authenticity and Student Responses to Artificial Intelligence Assessment Guidelines in Higher Education](https://europepmc.org/article/PPR/PPR1353709)

- 标识：`p-07c67a5b12c0019428e7`；发表：2026-10-30；发现：2026-11-04
- 主题：待分类
- 状态：机器建议排除，待抽查

文章讨论高校生成式AI评估指南的“制度真实性”，基于程序正义与中性化理论提出研究议程，关注公平感知、道德中性化与合规意向，非医学算法公平研究。

限制：仅提供摘要，未报告医学任务、算法公平性测量或实证结果；研究对象为高等教育政策，属范围外。

判断：摘要显示为高等教育AI评估政策研究议程，无生物医学/临床任务与AI算法公平性实证评估，故不纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1353709)；模型：qoder-cn/dfmodel。

### [Navigating the cultural iceberg: Addressing algorithmic bias, hallucination, and semantic flattening in AI-assisted qualitative thematic analysis.](https://pubmed.ncbi.nlm.nih.gov/42721502/)

- 标识：`p-11a0ba65de9fc94bbcd8`；发表：2026-09-08；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking（规则建议）
- 状态：待模型分析／人工核验

### [Governing Artificial Intelligence in University Mental Health Services: A Population Health Intelligence Framework for Preventing Algorithmic Stratification](https://europepmc.org/article/PPR/PPR1352995)

- 标识：`p-2c91ef57a53bcafa21e4`；发表：2026-10-29；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、Mitigation with Unverified Stage
- 状态：相关综述／资源

提出面向大学心理健康服务的SAFE-STUDENT治理框架，基于人群健康智能（PHI）视角，识别隐私与监控张力、学生发展阶段、数字原住民假设的公平影响、机构照护责任与学生自主权四大挑战，给出11项原则及跨七个PHI阶段的实施指标与利益相关方指引，旨在防止算法分层。

限制：仅有摘要可查，属概念性文献综述与框架构建，未实现或评估任何具体算法，未定义受保护属性或亚组发现协议，也未报告实证测量结果；作者自述需三阶段研究议程进行实证验证。

判断：该文讨论AI心理健康工具可能造成的算法分层，涉及公平治理议题，但为概念性治理框架，缺少被评估的具体算法、明确的群体/属性定义与实证测量评估，不满足五条证据标准，故列为相关文献而非纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1352995)；模型：qoder-cn/dfmodel。

### [A longitudinal case study of practice and policy gaps in responsible AI adoption across Ukrainian higher education from 2023 to 2025](https://europepmc.org/article/PPR/PPR1352081)

- 标识：`p-2d3bf73fccc4912dddf5`；发表：2026-10-28；发现：2026-11-04
- 主题：待分类
- 状态：机器建议排除，待抽查

该文基于乌克兰高校2023年与2024年两次教师问卷调查，构建“实践—政策”保真度矩阵，将问卷条目映射到欧盟可信AI七项原则及学术诚信这一补充维度，并比较2023—2025年乌克兰高校负责任AI采纳与国家政策之间的差距。

限制：仅有摘要，未见具体方法、代码或数据；研究对象为高等教育机构的GenAI使用与治理政策，不涉及临床任务、医疗算法或患者群体，也未开展任何模型层面的公平性评测。

判断：研究主题是乌克兰高校生成式AI采纳与政策治理的纵向案例研究，缺乏生物医学/临床任务与被评估的AI算法，不满足医学算法公平性纳入标准。文中虽提及“多样性、非歧视与公平”原则，但仅为政策维度映射，并非对算法的偏差、编码或缓解进行实证测量。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1352081)；模型：qoder-cn/dfmodel。

### [Artificial Intelligence-Based Assessment of Pathologic Response to Neoadjuvant Chemoimmunotherapy in Non-Small Cell Lung Cancer: An International Multicenter Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/42715648/)

- 标识：`p-2e9873c464054f991ee6`；发表：2026-09-05；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该研究开发基于AI的%RVT自动评分方法，用于评估非小细胞肺癌新辅助化疗免疫治疗后的病理缓解，并在内部及中国、德国、西班牙三个外部多中心队列共135例患者中与专家共识对比：MPR分类合并准确率91%、AUC≥0.95，并对不一致病例进行算法误差来源分析。

限制：仅有结构化摘要，未见代码或数据共享信息；未定义任何敏感人群属性（种族、性别、社会经济地位等），也未报告分组性能差异。文中“算法偏倚”排查仅指向误差来源（间质代表性不足、非肿瘤成分误判），不构成基于群体的公平性评估。

判断：属病理影像AI算法的实证评估，包含一致性、准确度与AUC等测量，并提及对不一致病例的算法偏倚排查，故与偏倚测量相关；但全文未定义受保护属性或亚组发现方案，缺少分组公平性指标，组别与公平性证据不成立，且仅为摘要级证据，故不能建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42715648/)；模型：qoder-cn/dfmodel。

### [Explainable Machine Learning for 30-Day Hospital Readmission Risk Prediction in Patients with Diabetes: A Comparative Analysis of Model Performance and Algorithmic Fairness](https://europepmc.org/article/PPR/PPR1351995)

- 标识：`p-2ffe88b3f5427706252d`；发表：2026-10-28；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare
- 状态：待核验

该摘要描述利用机器学习预测糖尿病患者30天再入院风险，拟作为辅助工具帮助识别需额外随访或出院指导的高风险患者；摘要仅给出背景与目标，未报告数据、模型细节或结果。

限制：仅有摘要，缺少数据来源、模型方法、评价指标与结果；正文未出现公平性分析内容，标题中的公平性比较无法核实，也不能推断临床获益或代码数据可用性。

判断：摘要确立糖尿病再入院预测的临床机器学习任务，并提及低收入、少数族裔等属性；但正文未报告公平性测量或实证评价，摘要级证据不足以建议纳入，故暂置。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1351995)；模型：qoder-cn/dfmodel。

### [Artificial intelligence integration in allied health professions: A comprehensive review of educational, research, and clinical applications.](https://pubmed.ncbi.nlm.nih.gov/42865081/)

- 标识：`p-3e28ee0d19df84b9f3d4`；发表：2026-10-12；发现：2026-11-04
- 主题：待分类
- 状态：相关综述／资源

综述七类联合健康专业中AI在教育、研究和临床的应用，报告诊断准确性、工作流程效率与决策支持等趋势，并提及隐私、算法偏见、自动化依赖和公平可及性等实施挑战。

限制：仅基于摘要，属结构化文献综述；未报告具体算法、受保护群体、公平性比较或实证测量，亦无全文方法与结果。

判断：文章为联合健康AI应用综述，仅在实施挑战中提及算法偏见与公平可及性，未提出明确公平性问题、群体定义或实证评估，故列为相关而非纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42865081/)；模型：qoder-cn/dfmodel。

### [AI integration for transforming care of patients with liver diseases.](https://europepmc.org/article/MED/42957964)

- 标识：`p-41c2f5e12d24a76bab3e`；发表：2026-10-29；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare
- 状态：相关综述／资源

该文综述人工智能在肝病诊断、风险分层、临床优先级和肝移植中的应用，指出传统评分可能造成漏诊并跨人口学亚组引入偏倚，同时讨论可解释性、泛化性和临床整合等挑战。

限制：仅有摘要，属综述而非原始实证研究；未定义具体人口学分组，也未报告任何公平性测量或缓解评估。

判断：摘要明确为肝病AI综述，虽提及算法偏倚和人口学亚组，但未开展可核验的公平性实证评估，且属综述，故仅判为相关。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42957964)；模型：qoder-cn/dfmodel。

### [Creative Assignments and Who Gets Left Behind: A Systematic Review of Inclusion Readiness in Generative AI Teaching Practices in Business and Technology Higher Education](https://europepmc.org/article/PPR/PPR1352692)

- 标识：`p-4cdbb2df2923fd9ce2c7`；发表：2026-10-28；发现：2026-11-04
- 主题：待分类
- 状态：机器建议排除，待抽查

该综述按PRISMA筛查191项研究，审计生成式AI教学作业在可及性、公平性、伦理与残障包容方面的准备度，并构建0–5包容准备度指数；结果显示免费访问、非AI替代和残障支持等措施很少。

限制：仅有摘要，未提供全文方法、编码细节或原始数据；研究对象为高等教育生成式AI教学，非临床算法或医疗人群，不能支持医学算法公平性结论。

判断：该文是商科与技术高等教育中生成式AI教学作业的系统综述，聚焦教学包容性与可及性，不涉及生物医学或临床任务，也未评估医疗算法的公平性。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1352692)；模型：qoder-cn/dfmodel。

### [Sources of Risk in AI Systems Revisited: FCAIR-O, a Faceted Causal Framework and Lightweight Ontology for Risk Management and Assurance](https://europepmc.org/article/PPR/PPR1352914)

- 标识：`p-84cbd12dbfc944d49f87`；发表：2026-10-29；发现：2026-11-04
- 主题：待分类
- 状态：相关综述／资源

提出FCAIR-O：面向AI风险管理的分面因果本体与概念框架，将公平等属性重新分配至因果、伤害、控制、证据或规范角色；以Uber Tempe等案例说明框架，但明确不构成实证验证。

限制：仅见摘要；为概念综合与本体构建，未提供医学场景、算法公平性测量或实证评估，公平仅作为风险属性被重新归类。

判断：摘要显示其为通用AI风险本体与理论框架，非医学算法公平性实证研究；不满足医学任务、算法评估、公平性问题和实证评价等纳入标准，且摘要证据不能建议纳入，故列为相关。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1352914)；模型：qoder-cn/dfmodel。

### [Assessing Variability in ChatGPT Responses: A Case Study on Simulating Online User Inputs.](https://pubmed.ncbi.nlm.nih.gov/40298212/)

- 标识：`p-90cc3b587e16a8a6abd1`；发表：2025-04-29；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models
- 状态：待核验

研究用结构化提问模拟首次交互，测试ChatGPT 3.5与4.0在种族、性别和性取向等社会变量下的HIV咨询回答差异，发现部分群体获得的建议较不全面，提示潜在偏见。

限制：仅有摘要，无法核实全文的提示设计、样本量、统计方法与结果稳健性，也未说明代码或数据是否公开，因此不足以支持纳入。

判断：摘要显示对ChatGPT的HIV建议按种族、性别和性取向进行结构化测试并报告差异，但证据仅为摘要，按规则不能suggest_include，宜暂缓。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/40298212/)；模型：qoder-cn/dfmodel。

### [The application of artificial intelligence in healthcare practice: A mapping review of systematic reviews.](https://pubmed.ncbi.nlm.nih.gov/42492159/)

- 标识：`p-9be6ed0d8b3a561dd390`；发表：2026-07-18；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该文为医疗AI系统综述的映射综述，汇总368篇综述，覆盖影像、EHR、诊断预后治疗等应用，并报告隐私、准确性、数据与算法偏倚及可解释性等伦理关注；未开展具体算法的公平性测量或缓解评估。

限制：所供仅为摘要，且文章本身是综述的综述；未报告具体算法、群体定义、公平性指标或实证公平性评估，不能据此判断任何模型的临床获益或公平性改善。

判断：摘要明确其为医疗AI系统综述的映射综述，仅将数据与算法偏倚列为伦理主题之一；未提出可检验的公平性问题、定义群体或进行算法公平性测量/缓解评估，故不满足纳入标准，仅属相关综述。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42492159/)；模型：qoder-cn/dfmodel。

### [Risk-Oriented Differentiated Governance for Ambiguous Information.](https://pubmed.ncbi.nlm.nih.gov/42973283/)

- 标识：`p-ca8d7d03e55f918b8e65`；发表：2026；发现：2026-11-04
- 主题：待分类
- 状态：机器建议排除，待抽查

提出面向模糊信息的风险导向分层治理框架，结合语义不确定性与传播特征构建风险函数，划分风险等级并模拟差异化治理策略，讨论公平与伦理。

限制：仅摘要级证据，未报告临床验证、代码或数据；主题为生成式AI虚假信息治理，非医疗算法公平性研究，摘要中的公平仅作伦理讨论。

判断：未涉及任何生物医学或临床任务、患者数据或医疗AI算法；公平仅作为治理策略的伦理讨论，没有明确的算法公平性测量或分组差异评估，且仅有摘要不足以纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42973283/)；模型：qoder-cn/dfmodel。

### [Fairness-Aware Design for Contextual Experiments: Guaranteeing Reliability and Equity in Heterogeneous Subgroups](https://arxiv.org/abs/2611.01867)

- 标识：`p-cb6eb929d7f879132fb0`；发表：2026-11-01；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking
- 状态：待核验

提出F-CTSD算法，在异质亚组情境实验中兼顾子组公平与样本效率，给出公平-效率权衡、样本复杂度及治疗效应估计的理论保证，并在数值实验中报告子组公平违规下降4.95%。

限制：仅有摘要；未说明具体医疗场景、数据集、敏感属性或亚组定义及完整实验设置；4.95%改善缺乏细节。

判断：摘要仅描述通用情境实验设计算法，未确立具体临床任务或敏感属性分组；仅摘要证据不足以建议纳入，需全文核验。

证据层级：abstract；[来源](https://arxiv.org/abs/2611.01867)；模型：qoder-cn/dfmodel。

Full-text access failed (HTTPError); abstract retained.

### [Artificial intelligence, work, and structural inequality: Why human-centric AI requires institutional architecture, not just ethics.](https://pubmed.ncbi.nlm.nih.gov/42550915/)

- 标识：`p-d393349a30ba59457dea`；发表：2026-08-04；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

文章为制度与政策分析，主张AI嵌入劳动市场、移民治理与社会保护后，单靠伦理框架不足，需以制度架构、可争议机制和可执行监督来应对结构性不平等。

限制：仅见摘要；属概念/政策论述，非生物医学临床研究，未定义敏感群体，亦无算法公平性实证测量或干预评估。

判断：文章讨论算法决策与结构性不平等，属一般公平、伦理与治理视角；但无临床任务、明确群体和实证测量，不能按纳入标准建议收录。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42550915/)；模型：qoder-cn/dfmodel。

### [Responsible AI in Academic Research: A Systematic Review of Ethical Principles, Challenges, and Future Directions](https://europepmc.org/article/PPR/PPR1356467)

- 标识：`p-d3fdee71565e6c28bc07`；发表：2026-11-03；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement
- 状态：相关综述／资源

该文按PRISMA 2020系统综述2015至2025年学术研究中负责任AI的伦理原则、挑战与治理建议，归纳算法偏见、数据治理与透明性等议题，并提出五原则对应五阶段的整合框架。

限制：仅见摘要；属学术研究伦理与治理综述，非临床场景；未呈现具体AI算法评估、敏感属性分组或公平性实证测量，不能据此推断干预效果或临床获益。

判断：摘要显示其系统综述学术研究中负责任AI的伦理原则与挑战，涉及算法偏见，但未针对医学AI算法开展公平性分组评价或实证测量；作为伦理综述仅属相关，摘要亦不足以支持纳入。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1356467)；模型：qoder-cn/dfmodel。

### [The Age of AI Strategic Decision-Making: The Business Analytics in the Corporate Divisions as the Competitive Advantage](https://europepmc.org/article/PPR/PPR1353951)

- 标识：`p-f2c8f82e8af197e219f9`；发表：2026-10-30；发现：2026-11-04
- 主题：待分类
- 状态：机器建议排除，待抽查

本文为综述性研究，基于近十年的学术文献、行业报告与从业者案例，探讨企业如何用人工智能与业务分析提升营销、财务、人力资源与运营等职能的决策质量与速度，并指出数据孤岛、遗留系统、数据质量与人才等障碍，以及隐私、算法偏见、透明度与合规等治理议题。

限制：仅有摘要，无方法细节、数据集、评价指标或结果数值；全文未涉及任何临床或生物医学任务，也未对具体算法开展公平性测量；摘要提到算法偏见仅属治理层面的泛泛讨论，不能据此推断论文缺少相关实证。

判断：主题为企业战略决策与业务分析的文献综述，缺少生物医学/临床任务，也未对具体AI/算法开展显式的公平性、偏倚或缓解评估，且无群体定义与实证测量，不符合纳入所需的五项证据标准。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1353951)；模型：qoder-cn/dfmodel。

### [Algorithmic Bias Concerns and Acceptance of AI Supported Legal Decision Making in Bangladesh](https://europepmc.org/article/PPR/PPR1352698)

- 标识：`p-f65a2a15eb4c53ba6488`；发表：2026-10-28；发现：2026-11-04
- 主题：待分类
- 状态：机器建议排除，待抽查

该研究基于385名孟加拉国法律AI调查受访者，报告86.8%担忧训练数据偏见、82.3%支持定期审计、85.2%支持复核或申诉权；偏见担忧与感知有用性相关很弱（ρ=.075）。研究整合技术接受与程序正义框架，提出审计、人工复核与可申诉机制建议。

限制：仅摘要级证据。研究场景为法律决策支持而非临床或生物医学；为自报告态度调查，未评估任何具体算法，无分组性能或编码测量，作者亦指出其不能证明系统公平性或因果效应。

判断：研究属法律AI的公众态度调查，缺乏生物医学/临床任务、被评估的具体AI算法以及分组公平性实证测量，五项证据标准均未满足，超出本综述范围。

证据层级：abstract；[来源](https://europepmc.org/article/PPR/PPR1352698)；模型：qoder-cn/dfmodel。

### [Artificial Intelligence in Dietary Management and Nutritional Interventions: A Narrative Review of Current Evidence, Applications, and Translational Challenges.](https://europepmc.org/article/MED/42970338)

- 标识：`p-f729e9411f9f1a7cc891`；发表：2026-11-02；发现：2026-11-04
- 主题：Clinical NLP and Foundation Models
- 状态：相关综述／资源

该叙述性综述总结AI在饮食评估、精准营养、餐后血糖预测和LLM饮食咨询中的应用，并讨论外部验证不足、算法偏见、隐私与监管等转化挑战。

限制：仅有摘要，未提供全文方法、数据/代码或公平性评估细节；摘要中的算法偏见仅为一般性障碍描述，不能证明全文缺乏相关分析。

判断：摘要明确为叙述性综述，仅泛泛提及算法偏见与公平治理，未定义敏感群体，也未实施公平性测量；按标准应标为相关而非纳入。

证据层级：abstract；[来源](https://europepmc.org/article/MED/42970338)；模型：qoder-cn/dfmodel。

### [A clinical decision support system for ECG diagnosis: Surpassing commercial standards through dual-stream feature fusion.](https://pubmed.ncbi.nlm.nih.gov/42667695/)

- 标识：`p-2e2b2ef426e2412e7968`；发表：2026-08-18；发现：2026-11-04
- 主题：EHR, Physiological Signals and Healthcare
- 状态：机器建议排除，待抽查

提出双流信号融合架构，将原始12导联心电波形与148项专家工程特征结合，在PTB-XL测试集上对比Marquette 12SL商业标准，报告Macro F1及心肌梗死敏感性提升，并分析特征重要性。

限制：仅为摘要；未设置公平性、亚组或敏感属性分析，也未说明代码、数据链接及外部多中心验证；“多样化全球人群”仅为愿景。

判断：该文是心电诊断AI与商业标准的准确率基准研究，未提出算法公平性、差异、编码或缓解问题，也未定义受保护群体或亚组发现流程，故不属于公平性研究。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42667695/)；模型：qoder-cn/dfmodel。

### [The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.](https://pubmed.ncbi.nlm.nih.gov/42447641/)

- 标识：`p-645868c25d38e8ad956f`；发表：2026-07-09；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、In-processing Mitigation、Post-processing Mitigation、EHR, Physiological Signals and Healthcare
- 状态：待核验

该研究基于PIC与MIMIC-IV重症监护数据，评估成人或年长儿数据训练的机器学习死亡预测模型在低龄儿科患者中的迁移差距，发现判别力下降与校准恶化，并比较目标域重训练与仅校准更新的缓解效果。

限制：仅摘要可用，未提供代码/数据链接，也未核实全文的方法细节、统计分析与临床验证；公平性框架和干预阶段需全文确认。

判断：摘要报告了按年龄分组的性能与校准差异，并实施重训练/校准干预，满足五项证据要点；但证据级别为摘要，不能据此建议纳入，需全文核验。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42447641/)；模型：qoder-cn/dfmodel。

### [Deep Learning for Cervical Cytology Screening: Methods, Algorithms, Challenges and Prospects](https://arxiv.org/abs/2611.01730)

- 标识：`p-79db3e55e911174329df`；发表：2026-11-01；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Clinical NLP and Foundation Models
- 状态：相关综述／资源

本文综述宫颈细胞学筛查的深度学习进展，按数据尺度、任务和监督方式分类，比较数据集与模型性能，并讨论临床转化、可信AI及公平性缺口。

限制：证据来自叙述性综述全文；公平性讨论停留在年龄、HPV状态、扫描仪和地区等亚组差异未被量化及报告建议，未提供原始数据上的公平性测量、缓解或基准实验，无法支持纳入。

判断：文章是宫颈细胞学影像深度学习综述，明确提及公平性/亚组报告缺口，但没有实施公平性测量、缓解或基准评估，符合相关综述而非可纳入的实证研究。

证据层级：full_text；[来源](https://arxiv.org/html/2611.01730v1)；模型：qoder-cn/dfmodel。

### [Patient attitudes toward artificial intelligence-driven dermatology.](https://pubmed.ncbi.nlm.nih.gov/42969910/)

- 标识：`p-ca287a15e23f038adaf1`；发表：2026-11-02；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement
- 状态：相关综述／资源

该文系统综述患者对皮肤科人工智能的态度，发现患者有条件支持，但更倾向由皮肤科医生监督的AI；信任受临床问责、解释与不确定性说明、隐私保护及跨肤色性能可靠性影响，并建议按肤色、诊断和诊疗场景分层评估与报告。

限制：仅有摘要；属患者态度系统综述，未提供算法性能、偏倚测量、干预实施或临床验证的原始实证。

判断：文章讨论皮肤科AI信任及跨肤色性能公平问题，但核心是患者态度综述，不是算法公平性实证评估；且仅有摘要，不能建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42969910/)；模型：qoder-cn/dfmodel。

### [Subgroup deployment-readiness audit of calibration and clinical utility in perioperative infection prediction.](https://pubmed.ncbi.nlm.nih.gov/42962674/)

- 标识：`p-cd61ff429b4e8948cce1`；发表：2026-10-30；发现：2026-11-04
- 主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Post-processing Mitigation、EHR, Physiological Signals and Healthcare
- 状态：待核验

摘要报告对围手术期术后感染预测模型开展亚组部署就绪审计，按性别、年龄及生理储备代理分层，评估判别力、校准、阈值误差与决策曲线净获益，并比较通用与分组重校准及去除过采样的影响。

限制：仅有摘要，无全文、代码或数据链接可核验；事件数有限，生理储备非衰弱层仅六例事件不可估计；二〇一八年以前感染编码基本缺失，患病率相关结论受限；尚无前瞻性验证。

判断：仅摘要证据不足以满足全文五项标准，无法核验模型细节、缓解阶段与完整评估，故暂缓而非纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42962674/)；模型：qoder-cn/dfmodel。

### [Can You See It? Diagnostic Blind Spots in Pigmented Skin: A Review of the Literature in Plastic Surgery and Burns.](https://pubmed.ncbi.nlm.nih.gov/42748034/)

- 标识：`p-2d408dda7b908686a6ac`；发表：2026-09-16；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking
- 状态：相关综述／资源

该叙述性综述综合塑料外科与烧伤领域因肤色不同而产生的诊断盲点，涵盖临床评估、彩色摄影、浅层与深层成像及人工智能，指出深色皮肤验证不足和AI性能分层，呼吁按肤色分层验证并更新培训。

限制：仅有摘要，无法核查全文、检索策略与偏倚评估细节；作为叙述性综述，未提供原始实证或算法公平性测量，AI相关结论仅为二手汇总。

判断：文章属叙述性综述，涉及肤色相关诊断偏倚并提及AI性能分层，但无原始算法公平性实证评估，故定为related。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42748034/)；模型：qoder-cn/dfmodel。

### [Sex, gender and artificial intelligence in cardiovascular medicine 4.0.](https://pubmed.ncbi.nlm.nih.gov/42721913/)

- 标识：`p-719d950501ac09bbdb7d`；发表：2026-08-29；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、Clinical NLP and Foundation Models
- 状态：相关综述／资源

该文为心血管医学人工智能中性别与性别偏倚的框架性论文，梳理六类相互作用的偏倚机制，讨论机器学习中二元性别分层的认识论风险，并提出包含性别感知临床提示工程、三阶段负责任人工智能互动模型以及数据治理、算法设计、临床教育与监管议程的操作框架。

限制：仅有摘要可查，未呈现具体数据集、模型、分组比较或任何量化偏倚测量；亦无干预实施与效果验证，属概念框架与立场性论述。

判断：摘要明确涉及心血管人工智能的性别偏倚机制与治理框架，属算法公平性相关议题；但缺乏已实施的经验性评估与测量，不满足五项证据标准中的评估一项，故列为相关文献而非建议纳入。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42721913/)；模型：qoder-cn/dfmodel。

### [Skin color representation in orthopedic literature.](https://pubmed.ncbi.nlm.nih.gov/42975702/)

- 标识：`p-fda1af6a735d35a7ab7d`；发表：2026-11-03；发现：2026-11-04
- 主题：Bias Mechanisms and Measurement、Fairness Evaluation and Benchmarking
- 状态：相关综述／资源

研究用GPT-4o流程分析14种开放获取骨科期刊的40,674幅图，在2,025幅含皮肤图中发现浅肤色占65.6%、深肤色仅4.8%，相对人群基准显著不足。

限制：仅摘要可用；该研究审计骨科文献图像的肤色代表性，GPT-4o是标注工具而非被评估的临床算法；摘要未提供全文方法、代码或数据链接，无法确认临床验证或算法公平性评估。

判断：摘要显示其为骨科教育图像肤色代表性审计，使用GPT-4o作测量工具；虽有肤色分组和经验统计，但未评估临床AI/ML算法的公平性，且仅有摘要证据，故不满足纳入标准。

证据层级：abstract；[来源](https://pubmed.ncbi.nlm.nih.gov/42975702/)；模型：qoder-cn/dfmodel。

### [Comment on "Artificial Intelligence in Health Care: A Rallying Cry for Critical Clinical Research and Ethical Thinking".](https://pubmed.ncbi.nlm.nih.gov/42727424/)

- 标识：`p-7f1b929f13b08962e27b`；发表：2026-07-15；发现：2026-11-04
- 主题：待分类（规则建议）
- 状态：待模型分析／人工核验
