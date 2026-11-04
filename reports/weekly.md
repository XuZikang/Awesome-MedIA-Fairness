# 文献候选七日汇总 · 2026-10-29—2026-11-04

主题为规则建议或机器分析结果；候选不等同于正式收录。

## Bias Mechanisms and Measurement

- [The Role of Artificial Intelligence in PET Imaging.](https://pubmed.ncbi.nlm.nih.gov/42957403/) · 相关综述／资源 · `p-103ada15cebbb7f64a8f`
  该文综述AI在PET成像临床流程中的应用，包括自动预约与协议、深度学习重建、病灶检测及大语言模型报告，并讨论算法偏倚、数据漂移和监管等实施挑战。
- [BiasLab: A multilingual dual-framing framework for LLM bias measurement, applied to workplace and HR contexts.](https://pubmed.ncbi.nlm.nih.gov/42434887/) · 相关综述／资源 · `p-2ace6f04876029d3419e`
  BiasLab 提出多语言双框架提示对方法，配合随机包装扰动、固定选项约束与极性对齐打分，量化 LLM 在六个职场/HR 议题（性别领导力、就业空档、年龄招聘等）上的方向性输出偏好；对十个模型、十二种语言生成 43,200 条回答，发现一致的方向偏好与“拒斥强于赞同”的不对称模式。
- [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215) · 建议纳入，待审核 · `p-2fcb4e34b5f7daab4c8d`
  研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。
- [AI-Driven Multiomics Biomarkers for Precision Oncology: Navigating the Translational Gap and Regulatory Hurdles.](https://pubmed.ncbi.nlm.nih.gov/42560117/) · 相关综述／资源 · `p-3afb8c155e44c9705fd1`
  该文为精准肿瘤学多组学AI生物标志物的综述，梳理从数据生成、整合、标志物发现、验证到监管落地的五阶段路线，并提及异质性、可重复性、算法偏倚与伦理监管等转化障碍。
- [A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering](https://arxiv.org/abs/2611.00298) · 建议纳入，待审核 · `p-3d7d2c77176c61d55abc`
  提出 MICF 框架，将反事实公平约束重述为 Transformer 激活层面的分析与干预：用激活补丁定位敏感属性相关层，分解直接与间接效应，并在推理时通过激活转向降低种族偏差；在 UTICalc 临床预测和 COMPAS 表格任务上评估。
- [Fairness Metrics based on the AUC in Clinical Predictive AI](https://arxiv.org/abs/2611.05222) · 建议纳入，待审核 · `p-5903974910ebbe7950d2`
  该文系统分析临床预测模型中八种基于AUC的公平性指标，阐明AUC不可折叠性对指标解释的影响，并以EuroSCORE II为例用模拟展示亚组与跨组AUC差异，建议报告完整AUC矩阵并优先采用组内AUC parity。
- [MRI radiomics for predicting pathological complete response in breast cancer: a systematic review of current evidence and limitations.](https://pubmed.ncbi.nlm.nih.gov/42541995/) · 相关综述／资源 · `p-5f6af5fefa6890d56a13`
  该系统综述汇总35项MRI影像组学预测乳腺癌新辅助治疗病理完全缓解（pCR）的研究，采用METRICS评分与改良QUADAS-2框架评估方法学质量、偏倚风险及亚组表现，报告合并AUC 0.813，并指出样本量普遍不足、外部验证少见、亚组分析仅占14%，限制了公平性能的评估。
- [Ethical and legal challenges of integrating artificial intelligence into paediatric surgery.](https://pubmed.ncbi.nlm.nih.gov/41725549/) · 相关综述／资源 · `p-747c407c5696b151b802`
  该叙述性综述梳理将AI（影像、机器人辅助、早期风险预测）整合进儿科手术的伦理与法律挑战，涵盖敏感儿科数据保护、知情同意、算法偏见缓解、自适应系统责任界定与监管协调，并提出联邦学习、模型卡、绩效审计等治理建议。
- [Editorial Commentary: Calling Balls and Strikes: For Artificial Intelligence Models to Accurately Predict Rotator Cuff Retear, We Must Carefully Define the Strike Zone.](https://pubmed.ncbi.nlm.nih.gov/42701888/) · 相关综述／资源 · `p-ab58f18226651ba5545c`
  该编辑评论指出，深度学习可用于肩袖修复后早期再撕裂预测，但单术者训练数据会引入偏倚变异，标注主观性也会影响模型可信度；临床落地需关注预处理、泛化性、公平性与治理。
- [Public evaluations of AI-mediated healthcare when considering people with diverse access and support needs: a mixed-methods survey.](https://pubmed.ncbi.nlm.nih.gov/42472498/) · 相关综述／资源 · `p-ceb7d989076bafad0d24`
  一项混合方法问卷研究（N=1151，其中117人作答开放式问题），考察受访者在考虑“获取与支持需求多样的人群”时如何评价AI介导的医疗服务。量化部分结合贝叶斯回归、验证性因子分析与相关分析，质性部分用编码本主题分析归纳出四个主题，其中包含对“不公平分类”的担忧。
- [AI algorithms and external validation: promises, pitfalls, and a practical blueprint.](https://pubmed.ncbi.nlm.nih.gov/42961821/) · 相关综述／资源 · `p-cf9833bc80232d798aba`
  文章提出临床AI外部验证的实践蓝图，强调预注册、多中心代表性队列、避免患者与时间重叠、校准和净获益评估、预设亚组与公平性审计，并连接部署后漂移监测和模型更新。
- [Responsible AI for Acute Stroke Management.](https://pubmed.ncbi.nlm.nih.gov/42751787/) · 相关综述／资源 · `p-e63a02248d4e14119359`
  该综述梳理急性卒中管理中人工智能的可解释性与公平性研究，涵盖大血管闭塞检测、ASPECTS评分与功能预后预测，指出后验解释方法缺乏验证、公平性评估因人口学元数据不足与缺少卒中专用公平标准而少见，并呼吁建立联合评估可解释性、公平性与泛化性的统一框架。
- [Using Generative AI for Behavioural Research Effectively and Responsibly: a BR-UK Statement](https://europepmc.org/article/PPR/PPR1351821) · 相关综述／资源 · `p-ecc70724990e28b4c271`
  该文是BR-UK关于行为研究中有效且负责任使用生成式AI的开放声明，提出伦理诚信、人类在环、严格评估和多方协同四项主张，并为七类利益相关者提供建议与工具。
- [Transforming one health antimicrobial resistance surveillance in resource-limited countries (RLCs): From point-of-care diagnostics to AI-driven decision support.](https://pubmed.ncbi.nlm.nih.gov/42810525/) · 相关综述／资源 · `p-064ee08a8e0905727f10`
  综述讨论资源有限地区抗菌耐药监测从即时诊断到AI决策支持的演进，涵盖机器学习用于耐药检测、处方与暴发预测，并提及算法偏倚、公平部署及实施挑战。
- [Governing Artificial Intelligence in University Mental Health Services: A Population Health Intelligence Framework for Preventing Algorithmic Stratification](https://europepmc.org/article/PPR/PPR1352995) · 相关综述／资源 · `p-2c91ef57a53bcafa21e4`
  提出面向大学心理健康服务的SAFE-STUDENT治理框架，基于人群健康智能（PHI）视角，识别隐私与监控张力、学生发展阶段、数字原住民假设的公平影响、机构照护责任与学生自主权四大挑战，给出11项原则及跨七个PHI阶段的实施指标与利益相关方指引，旨在防止算法分层。
- [Artificial Intelligence-Based Assessment of Pathologic Response to Neoadjuvant Chemoimmunotherapy in Non-Small Cell Lung Cancer: An International Multicenter Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/42715648/) · 相关综述／资源 · `p-2e9873c464054f991ee6`
  该研究开发基于AI的%RVT自动评分方法，用于评估非小细胞肺癌新辅助化疗免疫治疗后的病理缓解，并在内部及中国、德国、西班牙三个外部多中心队列共135例患者中与专家共识对比：MPR分类合并准确率91%、AUC≥0.95，并对不一致病例进行算法误差来源分析。
- [AI integration for transforming care of patients with liver diseases.](https://europepmc.org/article/MED/42957964) · 相关综述／资源 · `p-41c2f5e12d24a76bab3e`
  该文综述人工智能在肝病诊断、风险分层、临床优先级和肝移植中的应用，指出传统评分可能造成漏诊并跨人口学亚组引入偏倚，同时讨论可解释性、泛化性和临床整合等挑战。
- [Assessing Variability in ChatGPT Responses: A Case Study on Simulating Online User Inputs.](https://pubmed.ncbi.nlm.nih.gov/40298212/) · 待核验 · `p-90cc3b587e16a8a6abd1`
  研究用结构化提问模拟首次交互，测试ChatGPT 3.5与4.0在种族、性别和性取向等社会变量下的HIV咨询回答差异，发现部分群体获得的建议较不全面，提示潜在偏见。
- [The application of artificial intelligence in healthcare practice: A mapping review of systematic reviews.](https://pubmed.ncbi.nlm.nih.gov/42492159/) · 相关综述／资源 · `p-9be6ed0d8b3a561dd390`
  该文为医疗AI系统综述的映射综述，汇总368篇综述，覆盖影像、EHR、诊断预后治疗等应用，并报告隐私、准确性、数据与算法偏倚及可解释性等伦理关注；未开展具体算法的公平性测量或缓解评估。
- [Risk-Oriented Differentiated Governance for Ambiguous Information.](https://pubmed.ncbi.nlm.nih.gov/42973283/) · 待分析／证据不足 · `p-ca8d7d03e55f918b8e65`
- [Artificial intelligence, work, and structural inequality: Why human-centric AI requires institutional architecture, not just ethics.](https://pubmed.ncbi.nlm.nih.gov/42550915/) · 相关综述／资源 · `p-d393349a30ba59457dea`
  文章为制度与政策分析，主张AI嵌入劳动市场、移民治理与社会保护后，单靠伦理框架不足，需以制度架构、可争议机制和可执行监督来应对结构性不平等。
- [Responsible AI in Academic Research: A Systematic Review of Ethical Principles, Challenges, and Future Directions](https://europepmc.org/article/PPR/PPR1356467) · 相关综述／资源 · `p-d3fdee71565e6c28bc07`
  该文按PRISMA 2020系统综述2015至2025年学术研究中负责任AI的伦理原则、挑战与治理建议，归纳算法偏见、数据治理与透明性等议题，并提出五原则对应五阶段的整合框架。
- [The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.](https://pubmed.ncbi.nlm.nih.gov/42447641/) · 待核验 · `p-645868c25d38e8ad956f`
  该研究基于PIC与MIMIC-IV重症监护数据，评估成人或年长儿数据训练的机器学习死亡预测模型在低龄儿科患者中的迁移差距，发现判别力下降与校准恶化，并比较目标域重训练与仅校准更新的缓解效果。
- [Deep Learning for Cervical Cytology Screening: Methods, Algorithms, Challenges and Prospects](https://arxiv.org/abs/2611.01730) · 相关综述／资源 · `p-79db3e55e911174329df`
  本文综述宫颈细胞学筛查的深度学习进展，按数据尺度、任务和监督方式分类，比较数据集与模型性能，并讨论临床转化、可信AI及公平性缺口。
- [Patient attitudes toward artificial intelligence-driven dermatology.](https://pubmed.ncbi.nlm.nih.gov/42969910/) · 相关综述／资源 · `p-ca287a15e23f038adaf1`
  该文系统综述患者对皮肤科人工智能的态度，发现患者有条件支持，但更倾向由皮肤科医生监督的AI；信任受临床问责、解释与不确定性说明、隐私保护及跨肤色性能可靠性影响，并建议按肤色、诊断和诊疗场景分层评估与报告。
- [Subgroup deployment-readiness audit of calibration and clinical utility in perioperative infection prediction.](https://pubmed.ncbi.nlm.nih.gov/42962674/) · 待核验 · `p-cd61ff429b4e8948cce1`
  摘要报告对围手术期术后感染预测模型开展亚组部署就绪审计，按性别、年龄及生理储备代理分层，评估判别力、校准、阈值误差与决策曲线净获益，并比较通用与分组重校准及去除过采样的影响。
- [Can You See It? Diagnostic Blind Spots in Pigmented Skin: A Review of the Literature in Plastic Surgery and Burns.](https://pubmed.ncbi.nlm.nih.gov/42748034/) · 相关综述／资源 · `p-2d408dda7b908686a6ac`
  该叙述性综述综合塑料外科与烧伤领域因肤色不同而产生的诊断盲点，涵盖临床评估、彩色摄影、浅层与深层成像及人工智能，指出深色皮肤验证不足和AI性能分层，呼吁按肤色分层验证并更新培训。
- [Sex, gender and artificial intelligence in cardiovascular medicine 4.0.](https://pubmed.ncbi.nlm.nih.gov/42721913/) · 相关综述／资源 · `p-719d950501ac09bbdb7d`
  该文为心血管医学人工智能中性别与性别偏倚的框架性论文，梳理六类相互作用的偏倚机制，讨论机器学习中二元性别分层的认识论风险，并提出包含性别感知临床提示工程、三阶段负责任人工智能互动模型以及数据治理、算法设计、临床教育与监管议程的操作框架。
- [Skin color representation in orthopedic literature.](https://pubmed.ncbi.nlm.nih.gov/42975702/) · 相关综述／资源 · `p-fda1af6a735d35a7ab7d`
  研究用GPT-4o流程分析14种开放获取骨科期刊的40,674幅图，在2,025幅含皮肤图中发现浅肤色占65.6%、深肤色仅4.8%，相对人群基准显著不足。

## Clinical NLP and Foundation Models

- [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215) · 建议纳入，待审核 · `p-2fcb4e34b5f7daab4c8d`
  研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。
- [Artificial intelligence-driven pharmacovigilance: transforming signal detection, real-world drug safety monitoring, and regulatory decision-making.](https://pubmed.ncbi.nlm.nih.gov/42975625/) · 相关综述／资源 · `p-4271f40bb01045bc8aab`
  本文为药物警戒领域的AI应用综述，梳理机器学习、深度学习、自然语言处理在不良事件检测、文献挖掘、信号优先级排序以及EHR和社交媒体数据分析中的应用，并讨论大语言模型、联邦学习、区块链、数字孪生与IoT等新兴技术；同时指出可解释性、数据质量、网络安全、算法偏倚与监管验证等落地障碍。
- [Technology Matters: Emerging technologies in clinical informatics to support child and adolescent mental healthcare safety.](https://pubmed.ncbi.nlm.nih.gov/41937617/) · 相关综述／资源 · `p-791ad6693c5fab805032`
  该文概述电子健康记录在儿童青少年精神卫生安全中的应用，涵盖精神药物安全、自伤风险与限制性措施监测，并讨论预警疲劳、实施差异及高风险青少年检测中的算法偏倚等挑战。
- [Artificial intelligence in medical education: a narrative review across four functional domains.](https://pubmed.ncbi.nlm.nih.gov/42574942/) · 相关综述／资源 · `p-a71fdd3bd3bf63d2ba2a`
  该叙事综述按四个功能域总结医学教育中的AI应用，涵盖教学与内容生成、模拟训练、评估与学习分析、诊断推理，强调监督实施、透明报告和公平关切，但未开展算法公平性实证评估。
- [Assessing Variability in ChatGPT Responses: A Case Study on Simulating Online User Inputs.](https://pubmed.ncbi.nlm.nih.gov/40298212/) · 待核验 · `p-90cc3b587e16a8a6abd1`
  研究用结构化提问模拟首次交互，测试ChatGPT 3.5与4.0在种族、性别和性取向等社会变量下的HIV咨询回答差异，发现部分群体获得的建议较不全面，提示潜在偏见。
- [Artificial Intelligence in Dietary Management and Nutritional Interventions: A Narrative Review of Current Evidence, Applications, and Translational Challenges.](https://europepmc.org/article/MED/42970338) · 相关综述／资源 · `p-f729e9411f9f1a7cc891`
  该叙述性综述总结AI在饮食评估、精准营养、餐后血糖预测和LLM饮食咨询中的应用，并讨论外部验证不足、算法偏见、隐私与监管等转化挑战。
- [Deep Learning for Cervical Cytology Screening: Methods, Algorithms, Challenges and Prospects](https://arxiv.org/abs/2611.01730) · 相关综述／资源 · `p-79db3e55e911174329df`
  本文综述宫颈细胞学筛查的深度学习进展，按数据尺度、任务和监督方式分类，比较数据集与模型性能，并讨论临床转化、可信AI及公平性缺口。
- [Sex, gender and artificial intelligence in cardiovascular medicine 4.0.](https://pubmed.ncbi.nlm.nih.gov/42721913/) · 相关综述／资源 · `p-719d950501ac09bbdb7d`
  该文为心血管医学人工智能中性别与性别偏倚的框架性论文，梳理六类相互作用的偏倚机制，讨论机器学习中二元性别分层的认识论风险，并提出包含性别感知临床提示工程、三阶段负责任人工智能互动模型以及数据治理、算法设计、临床教育与监管议程的操作框架。

## EHR, Physiological Signals and Healthcare

- [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215) · 建议纳入，待审核 · `p-2fcb4e34b5f7daab4c8d`
  研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。
- [A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering](https://arxiv.org/abs/2611.00298) · 建议纳入，待审核 · `p-3d7d2c77176c61d55abc`
  提出 MICF 框架，将反事实公平约束重述为 Transformer 激活层面的分析与干预：用激活补丁定位敏感属性相关层，分解直接与间接效应，并在推理时通过激活转向降低种族偏差；在 UTICalc 临床预测和 COMPAS 表格任务上评估。
- [Artificial intelligence-driven pharmacovigilance: transforming signal detection, real-world drug safety monitoring, and regulatory decision-making.](https://pubmed.ncbi.nlm.nih.gov/42975625/) · 相关综述／资源 · `p-4271f40bb01045bc8aab`
  本文为药物警戒领域的AI应用综述，梳理机器学习、深度学习、自然语言处理在不良事件检测、文献挖掘、信号优先级排序以及EHR和社交媒体数据分析中的应用，并讨论大语言模型、联邦学习、区块链、数字孪生与IoT等新兴技术；同时指出可解释性、数据质量、网络安全、算法偏倚与监管验证等落地障碍。
- [Technology Matters: Emerging technologies in clinical informatics to support child and adolescent mental healthcare safety.](https://pubmed.ncbi.nlm.nih.gov/41937617/) · 相关综述／资源 · `p-791ad6693c5fab805032`
  该文概述电子健康记录在儿童青少年精神卫生安全中的应用，涵盖精神药物安全、自伤风险与限制性措施监测，并讨论预警疲劳、实施差异及高风险青少年检测中的算法偏倚等挑战。
- [Toward multimodal physiological assessment of clinical performance in simulation-based medical education: a machine learning approach.](https://europepmc.org/article/MED/42955499) · 相关综述／资源 · `p-bbc3b6330d6af062be13`
  该研究用 Empatica E4 腕带同步采集皮肤电、心率与皮温等多模态生理信号，结合遗传算法特征选择与神经网络，对高保真模拟教学中医师评定的“新手/胜任”表现分级进行二分类，内部验证平衡准确率约 84-85%，属生理信号驱动的教育评估模型。
- [Artificial intelligence-based nurse scheduling in healthcare: A scoping review of functional features and empirical outcomes.](https://pubmed.ncbi.nlm.nih.gov/42600237/) · 相关综述／资源 · `p-d39e326704b43f57948f`
  该文为AI护士排班的范围综述，梳理11项研究的算法类型、功能特征及组织、员工和患者层面实证结局，指出系统层研究较重视自动化、护士偏好与公平建模，但实时性、医院系统集成和真实世界评价仍有限。
- [The symbiotic shift: How AI is reshaping rehabilitation and the future of work.](https://pubmed.ncbi.nlm.nih.gov/42804281/) · 相关综述／资源 · `p-f51c76f9a365032f9da6`
  本文为结构化文献综述，论述人工智能在康复与重返工作场景中的“共生式”应用：临床康复中的个体化治疗、计算机视觉动作分析与预后预测，重返工作流程中的功能能力评估与岗位辅导，以及面向残障或慢性病人群的包容性就业支持，并强调隐私、算法偏见与公平可及等伦理要求。
- [Investigating Patient Trust and Intention to Act in AI-Supported Clinical Decisions: Cross-Sectional Survey.](https://pubmed.ncbi.nlm.nih.gov/42970578/) · 相关综述／资源 · `p-fafce843d0071edb38ce`
  摘要报告一项美国1185名成人的横断面调查，比较医生单独、医生加风险计算器、医生加AI风险预测三种推荐来源下患者的行动意愿、信任与偏好，并考察社会人口学特征的影响。研究未针对模型开展算法公平性评估。
- [Explainable Machine Learning for 30-Day Hospital Readmission Risk Prediction in Patients with Diabetes: A Comparative Analysis of Model Performance and Algorithmic Fairness](https://europepmc.org/article/PPR/PPR1351995) · 待核验 · `p-2ffe88b3f5427706252d`
  该摘要描述利用机器学习预测糖尿病患者30天再入院风险，拟作为辅助工具帮助识别需额外随访或出院指导的高风险患者；摘要仅给出背景与目标，未报告数据、模型细节或结果。
- [AI integration for transforming care of patients with liver diseases.](https://europepmc.org/article/MED/42957964) · 相关综述／资源 · `p-41c2f5e12d24a76bab3e`
  该文综述人工智能在肝病诊断、风险分层、临床优先级和肝移植中的应用，指出传统评分可能造成漏诊并跨人口学亚组引入偏倚，同时讨论可解释性、泛化性和临床整合等挑战。
- [A clinical decision support system for ECG diagnosis: Surpassing commercial standards through dual-stream feature fusion.](https://pubmed.ncbi.nlm.nih.gov/42667695/) · 机器建议排除，待抽查 · `p-2e2b2ef426e2412e7968`
  提出双流信号融合架构，将原始12导联心电波形与148项专家工程特征结合，在PTB-XL测试集上对比Marquette 12SL商业标准，报告Macro F1及心肌梗死敏感性提升，并分析特征重要性。
- [The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.](https://pubmed.ncbi.nlm.nih.gov/42447641/) · 待核验 · `p-645868c25d38e8ad956f`
  该研究基于PIC与MIMIC-IV重症监护数据，评估成人或年长儿数据训练的机器学习死亡预测模型在低龄儿科患者中的迁移差距，发现判别力下降与校准恶化，并比较目标域重训练与仅校准更新的缓解效果。
- [Subgroup deployment-readiness audit of calibration and clinical utility in perioperative infection prediction.](https://pubmed.ncbi.nlm.nih.gov/42962674/) · 待核验 · `p-cd61ff429b4e8948cce1`
  摘要报告对围手术期术后感染预测模型开展亚组部署就绪审计，按性别、年龄及生理储备代理分层，评估判别力、校准、阈值误差与决策曲线净获益，并比较通用与分组重校准及去除过采样的影响。

## Fairness Evaluation and Benchmarking

- [BiasLab: A multilingual dual-framing framework for LLM bias measurement, applied to workplace and HR contexts.](https://pubmed.ncbi.nlm.nih.gov/42434887/) · 相关综述／资源 · `p-2ace6f04876029d3419e`
  BiasLab 提出多语言双框架提示对方法，配合随机包装扰动、固定选项约束与极性对齐打分，量化 LLM 在六个职场/HR 议题（性别领导力、就业空档、年龄招聘等）上的方向性输出偏好；对十个模型、十二种语言生成 43,200 条回答，发现一致的方向偏好与“拒斥强于赞同”的不对称模式。
- [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215) · 建议纳入，待审核 · `p-2fcb4e34b5f7daab4c8d`
  研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。
- [A Scoping Review of Artificial Intelligence and Machine Learning for Spatio-temporal Infectious Disease Forecasting](https://europepmc.org/article/PPR/PPR1356097) · 相关综述／资源 · `p-39172eeeef221e79bbcc`
  该文为时空传染病预测AI/ML的范围综述，纳入93项研究，总结模型、误差指标、外部验证、代码共享及公平性分析等评估缺口，指出仅1项研究开展公平性分析。
- [Fairness Metrics based on the AUC in Clinical Predictive AI](https://arxiv.org/abs/2611.05222) · 建议纳入，待审核 · `p-5903974910ebbe7950d2`
  该文系统分析临床预测模型中八种基于AUC的公平性指标，阐明AUC不可折叠性对指标解释的影响，并以EuroSCORE II为例用模拟展示亚组与跨组AUC差异，建议报告完整AUC矩阵并优先采用组内AUC parity。
- [Responsible Credit-Line Increase: A Fairness-Aware, Explainable, and Governed Machine-Learning Framework for Socio-Technical Lending Systems](https://europepmc.org/article/PPR/PPR1353923) · 机器建议排除，待抽查 · `p-59d12037c0f5cd6ad9d2`
  提出面向信贷额度主动上调（CLI）的公平性感知、可解释且可治理的机器学习框架：在组合预期损失预算与显式公平容忍度下最大化增量利润，将问题归约为经校准、可审计的阈值策略，并在不改变已验证模型的前提下做群体级重校准以控制差异影响。评估基于6万账户的合成组合，并在一公开信贷基准上复核。
- [MRI radiomics for predicting pathological complete response in breast cancer: a systematic review of current evidence and limitations.](https://pubmed.ncbi.nlm.nih.gov/42541995/) · 相关综述／资源 · `p-5f6af5fefa6890d56a13`
  该系统综述汇总35项MRI影像组学预测乳腺癌新辅助治疗病理完全缓解（pCR）的研究，采用METRICS评分与改良QUADAS-2框架评估方法学质量、偏倚风险及亚组表现，报告合并AUC 0.813，并指出样本量普遍不足、外部验证少见、亚组分析仅占14%，限制了公平性能的评估。
- [Artificial intelligence in medical education: a narrative review across four functional domains.](https://pubmed.ncbi.nlm.nih.gov/42574942/) · 相关综述／资源 · `p-a71fdd3bd3bf63d2ba2a`
  该叙事综述按四个功能域总结医学教育中的AI应用，涵盖教学与内容生成、模拟训练、评估与学习分析、诊断推理，强调监督实施、透明报告和公平关切，但未开展算法公平性实证评估。
- [AI algorithms and external validation: promises, pitfalls, and a practical blueprint.](https://pubmed.ncbi.nlm.nih.gov/42961821/) · 相关综述／资源 · `p-cf9833bc80232d798aba`
  文章提出临床AI外部验证的实践蓝图，强调预注册、多中心代表性队列、避免患者与时间重叠、校准和净获益评估、预设亚组与公平性审计，并连接部署后漂移监测和模型更新。
- [Responsible AI for Acute Stroke Management.](https://pubmed.ncbi.nlm.nih.gov/42751787/) · 相关综述／资源 · `p-e63a02248d4e14119359`
  该综述梳理急性卒中管理中人工智能的可解释性与公平性研究，涵盖大血管闭塞检测、ASPECTS评分与功能预后预测，指出后验解释方法缺乏验证、公平性评估因人口学元数据不足与缺少卒中专用公平标准而少见，并呼吁建立联合评估可解释性、公平性与泛化性的统一框架。
- [Interpretable models for scRNA-seq data embedding with multi-scale structure preservation.](https://europepmc.org/article/MED/42950829) · 待核验 · `p-e76f08abf1081b362cba`
  摘要提出ViScore评分框架与ViVAE深度嵌入模型，用于单细胞转录组数据的多尺度结构保持与可解释降维，并称评分框架兼顾可扩展性与公平性。
- [Navigating the cultural iceberg: Addressing algorithmic bias, hallucination, and semantic flattening in AI-assisted qualitative thematic analysis.](https://pubmed.ncbi.nlm.nih.gov/42721502/) · 待分析／证据不足 · `p-11a0ba65de9fc94bbcd8`
- [Assessing Variability in ChatGPT Responses: A Case Study on Simulating Online User Inputs.](https://pubmed.ncbi.nlm.nih.gov/40298212/) · 待核验 · `p-90cc3b587e16a8a6abd1`
  研究用结构化提问模拟首次交互，测试ChatGPT 3.5与4.0在种族、性别和性取向等社会变量下的HIV咨询回答差异，发现部分群体获得的建议较不全面，提示潜在偏见。
- [Risk-Oriented Differentiated Governance for Ambiguous Information.](https://pubmed.ncbi.nlm.nih.gov/42973283/) · 待分析／证据不足 · `p-ca8d7d03e55f918b8e65`
- [Fairness-Aware Design for Contextual Experiments: Guaranteeing Reliability and Equity in Heterogeneous Subgroups](https://arxiv.org/abs/2611.01867) · 待核验 · `p-cb6eb929d7f879132fb0`
  提出F-CTSD算法，在异质亚组情境实验中兼顾子组公平与样本效率，给出公平-效率权衡、样本复杂度及治疗效应估计的理论保证，并在数值实验中报告子组公平违规下降4.95%。
- [The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.](https://pubmed.ncbi.nlm.nih.gov/42447641/) · 待核验 · `p-645868c25d38e8ad956f`
  该研究基于PIC与MIMIC-IV重症监护数据，评估成人或年长儿数据训练的机器学习死亡预测模型在低龄儿科患者中的迁移差距，发现判别力下降与校准恶化，并比较目标域重训练与仅校准更新的缓解效果。
- [Deep Learning for Cervical Cytology Screening: Methods, Algorithms, Challenges and Prospects](https://arxiv.org/abs/2611.01730) · 相关综述／资源 · `p-79db3e55e911174329df`
  本文综述宫颈细胞学筛查的深度学习进展，按数据尺度、任务和监督方式分类，比较数据集与模型性能，并讨论临床转化、可信AI及公平性缺口。
- [Patient attitudes toward artificial intelligence-driven dermatology.](https://pubmed.ncbi.nlm.nih.gov/42969910/) · 相关综述／资源 · `p-ca287a15e23f038adaf1`
  该文系统综述患者对皮肤科人工智能的态度，发现患者有条件支持，但更倾向由皮肤科医生监督的AI；信任受临床问责、解释与不确定性说明、隐私保护及跨肤色性能可靠性影响，并建议按肤色、诊断和诊疗场景分层评估与报告。
- [Subgroup deployment-readiness audit of calibration and clinical utility in perioperative infection prediction.](https://pubmed.ncbi.nlm.nih.gov/42962674/) · 待核验 · `p-cd61ff429b4e8948cce1`
  摘要报告对围手术期术后感染预测模型开展亚组部署就绪审计，按性别、年龄及生理储备代理分层，评估判别力、校准、阈值误差与决策曲线净获益，并比较通用与分组重校准及去除过采样的影响。
- [Can You See It? Diagnostic Blind Spots in Pigmented Skin: A Review of the Literature in Plastic Surgery and Burns.](https://pubmed.ncbi.nlm.nih.gov/42748034/) · 相关综述／资源 · `p-2d408dda7b908686a6ac`
  该叙述性综述综合塑料外科与烧伤领域因肤色不同而产生的诊断盲点，涵盖临床评估、彩色摄影、浅层与深层成像及人工智能，指出深色皮肤验证不足和AI性能分层，呼吁按肤色分层验证并更新培训。
- [Skin color representation in orthopedic literature.](https://pubmed.ncbi.nlm.nih.gov/42975702/) · 相关综述／资源 · `p-fda1af6a735d35a7ab7d`
  研究用GPT-4o流程分析14种开放获取骨科期刊的40,674幅图，在2,025幅含皮肤图中发现浅肤色占65.6%、深肤色仅4.8%，相对人群基准显著不足。

## In-processing Mitigation

- [A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering](https://arxiv.org/abs/2611.00298) · 建议纳入，待审核 · `p-3d7d2c77176c61d55abc`
  提出 MICF 框架，将反事实公平约束重述为 Transformer 激活层面的分析与干预：用激活补丁定位敏感属性相关层，分解直接与间接效应，并在推理时通过激活转向降低种族偏差；在 UTICalc 临床预测和 COMPAS 表格任务上评估。
- [The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.](https://pubmed.ncbi.nlm.nih.gov/42447641/) · 待核验 · `p-645868c25d38e8ad956f`
  该研究基于PIC与MIMIC-IV重症监护数据，评估成人或年长儿数据训练的机器学习死亡预测模型在低龄儿科患者中的迁移差距，发现判别力下降与校准恶化，并比较目标域重训练与仅校准更新的缓解效果。

## Mitigation with Unverified Stage

- [Governing Artificial Intelligence in University Mental Health Services: A Population Health Intelligence Framework for Preventing Algorithmic Stratification](https://europepmc.org/article/PPR/PPR1352995) · 相关综述／资源 · `p-2c91ef57a53bcafa21e4`
  提出面向大学心理健康服务的SAFE-STUDENT治理框架，基于人群健康智能（PHI）视角，识别隐私与监控张力、学生发展阶段、数字原住民假设的公平影响、机构照护责任与学生自主权四大挑战，给出11项原则及跨七个PHI阶段的实施指标与利益相关方指引，旨在防止算法分层。

## Post-processing Mitigation

- [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215) · 建议纳入，待审核 · `p-2fcb4e34b5f7daab4c8d`
  研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。
- [Responsible Credit-Line Increase: A Fairness-Aware, Explainable, and Governed Machine-Learning Framework for Socio-Technical Lending Systems](https://europepmc.org/article/PPR/PPR1353923) · 机器建议排除，待抽查 · `p-59d12037c0f5cd6ad9d2`
  提出面向信贷额度主动上调（CLI）的公平性感知、可解释且可治理的机器学习框架：在组合预期损失预算与显式公平容忍度下最大化增量利润，将问题归约为经校准、可审计的阈值策略，并在不改变已验证模型的前提下做群体级重校准以控制差异影响。评估基于6万账户的合成组合，并在一公开信贷基准上复核。
- [The pediatric transfer gap: How adult-ICU-trained machine-learning models degrade on pediatric intensive care patients.](https://pubmed.ncbi.nlm.nih.gov/42447641/) · 待核验 · `p-645868c25d38e8ad956f`
  该研究基于PIC与MIMIC-IV重症监护数据，评估成人或年长儿数据训练的机器学习死亡预测模型在低龄儿科患者中的迁移差距，发现判别力下降与校准恶化，并比较目标域重训练与仅校准更新的缓解效果。
- [Subgroup deployment-readiness audit of calibration and clinical utility in perioperative infection prediction.](https://pubmed.ncbi.nlm.nih.gov/42962674/) · 待核验 · `p-cd61ff429b4e8948cce1`
  摘要报告对围手术期术后感染预测模型开展亚组部署就绪审计，按性别、年龄及生理储备代理分层，评估判别力、校准、阈值误差与决策曲线净获益，并比较通用与分组重校准及去除过采样的影响。

## Pre-processing Mitigation

- [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215) · 建议纳入，待审核 · `p-2fcb4e34b5f7daab4c8d`
  研究临床多智能体大模型中的“差异洗白”：在120例MIMIC-IV急诊病例、5个模型家族×4种聚合拓扑及种族/性别反事实替换下，所有配置均未消除差异；事后公平指令与人口学遮蔽无效，自我去偏反而扩大差距；让各智能体看到不同人口学版本并汇聚可将差异降低67%–94%。

## 待分类

- [Rethinking Intellectual Property in the Age of Generative AI: Ethics, Rights and Accountability](https://europepmc.org/article/PPR/PPR1356304) · 相关综述／资源 · `p-104fdea547833123c665`
  文章以同意、补偿、署名与问责四轴框架分析生成式AI知识产权伦理，比较专利、诉讼、和解及创作者调查，并提出分层治理模型。
- [Precision Lipid Management in the Era of Biotechnology and Artificial Intelligence: From Gene Editing to Smart Drug Delivery.](https://pubmed.ncbi.nlm.nih.gov/42599575/) · 相关综述／资源 · `p-1607ccec012a87a0fdca`
  该叙述性综述讨论高脂血症精准管理中基因编辑、PCSK9抗体、纳米递送与人工智能辅助治疗优化等新兴策略，强调转化成熟度、临床适用性与监管问题，仅把算法偏倚、公平实施列为转化障碍之一，未开展算法公平性评估。
- [Governing artificial intelligence in Australian healthcare organisations - a qualitative study of staff perspectives.](https://europepmc.org/article/MED/42906928) · 相关综述／资源 · `p-3e7581d5cf989529b639`
  该定性研究访谈澳大利亚某医疗机构的23名工作人员，归纳AI治理的五个组织域：风险评估、基础设施与数据、伦理、能力与文化、治理结构，强调生命周期监督与公平透明。
- [Artificial intelligence in dedicated forensic-science journals: A bibliometric and science-mapping analysis (1991-2026).](https://pubmed.ncbi.nlm.nih.gov/42617285/) · 相关综述／资源 · `p-5c95d2dbcd135df1a0e0`
  对1991–2026年法医科学专门期刊中的人工智能文献进行文献计量与科学图谱分析，纳入1127篇文献，刻画其增长、国家分布与主题结构，并统计外部验证、校准、可采性、对抗安全以及偏见/公平等术语在题录中的出现比例。
- [Institutional Governance Authenticity and Student Responses to Artificial Intelligence Assessment Guidelines in Higher Education](https://europepmc.org/article/PPR/PPR1353709) · 机器建议排除，待抽查 · `p-07c67a5b12c0019428e7`
  文章讨论高校生成式AI评估指南的“制度真实性”，基于程序正义与中性化理论提出研究议程，关注公平感知、道德中性化与合规意向，非医学算法公平研究。
- [A longitudinal case study of practice and policy gaps in responsible AI adoption across Ukrainian higher education from 2023 to 2025](https://europepmc.org/article/PPR/PPR1352081) · 机器建议排除，待抽查 · `p-2d3bf73fccc4912dddf5`
  该文基于乌克兰高校2023年与2024年两次教师问卷调查，构建“实践—政策”保真度矩阵，将问卷条目映射到欧盟可信AI七项原则及学术诚信这一补充维度，并比较2023—2025年乌克兰高校负责任AI采纳与国家政策之间的差距。
- [Artificial intelligence integration in allied health professions: A comprehensive review of educational, research, and clinical applications.](https://pubmed.ncbi.nlm.nih.gov/42865081/) · 相关综述／资源 · `p-3e28ee0d19df84b9f3d4`
  综述七类联合健康专业中AI在教育、研究和临床的应用，报告诊断准确性、工作流程效率与决策支持等趋势，并提及隐私、算法偏见、自动化依赖和公平可及性等实施挑战。
- [Creative Assignments and Who Gets Left Behind: A Systematic Review of Inclusion Readiness in Generative AI Teaching Practices in Business and Technology Higher Education](https://europepmc.org/article/PPR/PPR1352692) · 机器建议排除，待抽查 · `p-4cdbb2df2923fd9ce2c7`
  该综述按PRISMA筛查191项研究，审计生成式AI教学作业在可及性、公平性、伦理与残障包容方面的准备度，并构建0–5包容准备度指数；结果显示免费访问、非AI替代和残障支持等措施很少。
- [Sources of Risk in AI Systems Revisited: FCAIR-O, a Faceted Causal Framework and Lightweight Ontology for Risk Management and Assurance](https://europepmc.org/article/PPR/PPR1352914) · 相关综述／资源 · `p-84cbd12dbfc944d49f87`
  提出FCAIR-O：面向AI风险管理的分面因果本体与概念框架，将公平等属性重新分配至因果、伤害、控制、证据或规范角色；以Uber Tempe等案例说明框架，但明确不构成实证验证。
- [The Age of AI Strategic Decision-Making: The Business Analytics in the Corporate Divisions as the Competitive Advantage](https://europepmc.org/article/PPR/PPR1353951) · 机器建议排除，待抽查 · `p-f2c8f82e8af197e219f9`
  本文为综述性研究，基于近十年的学术文献、行业报告与从业者案例，探讨企业如何用人工智能与业务分析提升营销、财务、人力资源与运营等职能的决策质量与速度，并指出数据孤岛、遗留系统、数据质量与人才等障碍，以及隐私、算法偏见、透明度与合规等治理议题。
- [Algorithmic Bias Concerns and Acceptance of AI Supported Legal Decision Making in Bangladesh](https://europepmc.org/article/PPR/PPR1352698) · 机器建议排除，待抽查 · `p-f65a2a15eb4c53ba6488`
  该研究基于385名孟加拉国法律AI调查受访者，报告86.8%担忧训练数据偏见、82.3%支持定期审计、85.2%支持复核或申诉权；偏见担忧与感知有用性相关很弱（ρ=.075）。研究整合技术接受与程序正义框架，提出审计、人工复核与可申诉机制建议。
- [Comment on "Artificial Intelligence in Health Care: A Rallying Cry for Critical Clinical Research and Ethical Thinking".](https://pubmed.ncbi.nlm.nih.gov/42727424/) · 待分析／证据不足 · `p-7f1b929f13b08962e27b`
