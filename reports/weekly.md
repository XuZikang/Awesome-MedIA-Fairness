# 文献候选七日汇总 · 2026-11-15—2026-11-21

主题为规则建议或机器分析结果；候选不等同于正式收录。

## Bias Mechanisms and Measurement

- [Implications of Image-Level Duplication in Public Glaucoma Datasets.](https://europepmc.org/article/MED/43018943) · 待核验 · `p-13cc881c6ffbf754dbd7`
  该研究审计3个公开青光眼数据集，发现Harvard-GF与FairVision有1302眼匹配、1031眼为同一OCT volume，跨数据集分类AUC因泄漏升高0.12，且各种族亚组均出现膨胀，提示独立基准与公平性评估可能被高估。
- [Applications of Fairness Training in Artificial Intelligence to Ophthalmic Disease Diagnosis using External Eye Photographs](https://europepmc.org/article/PPR/PPR1363752) · 待核验 · `p-21b44eb38a70c944169c`
  摘要报告利用40,687张外部眼照片开发深度学习与视觉语言模型，对威胁视力DR、晚期AMD和青光眼做二分类，并以ES-AUC评估性别、种族和族裔公平性，比较五种公平训练策略。报告称公平训练部分缩小差异并提升VTDR/AMD的AUC，但模型尚不适合临床部署。
- [FSD-Net: A Unified Skin-Tone-Aware Framework for Fair Skin Lesion Segmentation and Classification](https://europepmc.org/article/PPR/PPR1370450) · 待核验 · `p-3daf0c4282bca4f685cf`
  FSD-Net在皮肤病变分割与分类两个阶段同时考虑肤色公平性：用连续肤色评分经FiLM调制ViT-B/16分割骨干，并用分割引导的ROI训练Swin-V2-Tiny分类器。在ISIC-2017/2018、PH2及HAM10000上报告Dice、准确率和Equalized Opportunity差距，并辅以消融、Bootstrap置信区间和McNemar检验。
- [Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits](https://arxiv.org/abs/2611.23657) · 建议纳入，待审核 · `p-52131ebbc4ad7c4a8714`
  该文将固定模型的数值执行契约（FP64/FP32/TF32/FP8等）视为决策函数的一部分，在收入、就业、房贷和30天再入院任务上评估公平性审计结论的可复现性；提出审计稳定性协议，报告不同契约下统计量与通过/失败判定的范围。再入院任务按种族、性别和年龄分层，显示低精度部署可改变诊断性公平判定，但未证明FP8更公平。
- [Reliable Skin-Tone Fairness in Dermatology AI: From Lesion-Level Leakage to Tone-Adaptive Learning](https://europepmc.org/article/PPR/PPR1345750) · 待核验 · `p-53d198d32447f559a258`
  提出面向皮肤镜与临床图像的色调自适应预处理流程，并建立按病灶分组、类别分层的评估协议，量化病灶级泄漏和肤色代理指标问题；在三个基准上报告深色皮肤敏感度提升，并发布泄漏审计工具。
- [Governed Auditing of Hidden Failure Slice Discovery in Emergency Department Admission Models Agnostic to Sensitive Attributes](https://europepmc.org/article/PPR/PPR1363950) · 待核验 · `p-802f852b1e8f331fe15d`
  提出BASiC与ASAP，在急诊入院预测中利用临床规则和折外误差信号发现隐藏失败切片，并尝试样本加权修复。研究在Kaggle、RIPAS和NHAMCS数据上评估多种模型，发现切片发现较可靠，但修复未带来一致改善，且不建立人口统计学公平或临床有效性。
- [Design-based fairness monitoring for healthcare prediction with complex survey data.](https://europepmc.org/article/MED/42914067) · 待核验 · `p-afe7ffeed3546c2df3d8`
  该研究提出基于复杂抽样设计的公平性监测框架，利用2015—2023年MEPS九轮数据，以随机森林预测高额医疗支出，并按性别、种族/民族和贫困状态评估人口均等与机会均等，估计设计校正的公平性差异及时间趋势。
- [ECG foundation models share an age-related performance disparity that originates in the data, not the models](https://europepmc.org/article/PPR/PPR1357796) · 待核验 · `p-e68fcceb7a02de0b9211`
  该研究在四个ECG基础模型、13个队列约540万份ECG上按年龄、性别和种族评估性能差异，发现差异主要集中于年龄并可在外部复现；未训练网络和经典特征模型也重现年龄差距，提示差异源于数据与任务而非预训练模型。
- [MelanoFusion: An Explainable and Uncertainty-Aware Hybrid CNN–Transformer Framework for Dermoscopic Melanoma Detection](https://europepmc.org/article/PPR/PPR1370178) · 相关，待核实是否纳入 · `p-fd455cc2a36673f35d55`
  提出MelanoFusion混合CNN–Transformer框架用于皮肤镜黑色素瘤检测，结合可解释性、不确定性估计与公平导向表征学习；在HAM10000、ISIC 2018和PH²上评估，报告年龄组敏感性差异但性别无显著差异，并提示需外部验证。
- [A Multi-Model Framework for Explainable Sepsis Mortality Prediction With Dynamic Fairness and Drift Analysis.](https://europepmc.org/article/MED/43056270) · 待核验 · `p-3f9a2ee2dec669d59e15`
  该研究在MIMIC-IV上构建脓毒症死亡预测多模型框架，将公平性重新定义为动态生命周期属性，在15轮再训练与16个交叉子群中监测TPR、FPR、FOR差距，并开展eICU跨机构公平性审计与SHAP稳定性分析。
- [Multiview Integration for Robust Echocardiographic Embeddings: Accessible AI for Clinical Practice.](https://pubmed.ncbi.nlm.nih.gov/43050803/) · 待核验 · `p-0aed599c7fa1f8e12a36`
  开发基于Transformer的多视角超声心动图编码器，将多段视频整合为研究级向量嵌入，并在21项二分类任务上评估；同时用对抗学习降低性别和种族捷径依赖，报告较强对抗权重下可预测性下降但临床性能受损。
- [Radiology No-Show Calculator: A Social Determinants of Health-Enriched Machine Learning Prediction Model With Financial Analysis.](https://pubmed.ncbi.nlm.nih.gov/42660476/) · 待核验 · `p-1582a8a2e3798f9bf7f2`
  该研究开发基于随机森林的放射科门诊失约预测模型，纳入区域剥夺指数等16个预测因子，并按人群患病率校准；报告AUC 0.760、ADI相关失约梯度和财务负担，提出针对高风险患者外展。
- [BMR-Restormer: A transformer-based blind inpainting network for ultrasound marker removal.](https://pubmed.ncbi.nlm.nih.gov/42551183/) · 机器建议排除，待抽查 · `p-3295b40be2839e3ffd5b`
  提出 BMR-Restormer 盲修复网络，用于去除超声图像中烧录的人工标记（十字、文字、测量线），并评估标记对下游分类、分割、检测模型泛化性的影响，发现模型在含标记数据上训练后会过拟合伪特征，迁移到无标记图像时性能大幅下降。
- [Improving Target-Adverse Event Association Prediction via Inverse Node Frequency Transformation to Mitigate Knowledge Graph Topological Bias](https://europepmc.org/article/PPR/PPR1373652) · 待核验 · `p-3f6acf4e270b22ab1a5d`
  提出逆节点频率（INF）归一化方法，用于缓解生物医学知识图中因节点度数分布不均导致的拓扑偏倚（度偏倚），并以元路径特征为基础预测靶点-不良事件关联。结果显示INF提升了低度数靶点的召回率，并在外部未用于建模的关联集上优于两种基准，属知识图谱偏倚缓解类方法研究。
- [Preoperative Mortality Risk Prediction and Equity Using Preoperative Score to Predict Postoperative Mortality in a Diverse US Surgical Population: Retrospective Cohort Study.](https://europepmc.org/article/MED/43050561) · 建议纳入，待审核 · `p-46c871af6f5cd511e575`
  该回顾性队列研究利用All of Us数据评估POSPOM术前死亡风险评分在17,262例手术患者中的判别与校准，并按种族/民族亚组描述30天和1年死亡差异；发现高危患者判别下降、黑人患者绝对死亡率更高但事件数少，提示需外部验证和重新校准。
- [Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus](https://arxiv.org/abs/2611.22668) · 建议纳入，待审核 · `p-67ee09e54a621a213502`
  提出CHORD多视图去偏框架，通过多个表征视图提出类内分区，并在目标表征空间验证反转样本，无需组标注即可重训分类头；在CheXpert胸片二分类上报告WGA 71.43%，高于ERM的31.21%。
- [Self-report label bias in machine learning screening for undiagnosed diabetes: development, validation and offline on-device deployment of an interpretable HbA1c-anchored tool.](https://pubmed.ncbi.nlm.nih.gov/43033525/) · 待核验 · `p-8e1089bbb872533b5f51`
  该研究基于NHANES与BRFSS数据，量化自报糖尿病诊断标签如何改变机器学习筛查模型优先识别人群的方式，显示自报标签部分编码了就医可及性；用正-未标记学习校正标签，并开发以HbA1c为锚点的可解释筛查工具，在相同转诊率下与指南规则比较敏感度并做离线部署验证。
- [When multi-institutional dataset aggregation masks shortcut-like behavior in Foundation Models for medical imaging.](https://pubmed.ncbi.nlm.nih.gov/42641372/) · 待核验 · `p-b450c1e3be8d7e77257b`
  该研究以乳腺X线摄影分类为任务，将预训练图像编码器（基础模型）作为特征提取器，在十个采集流程、人群与地区各异的队列上训练分类器，发现聚合异质数据会带来依赖数据集的失效模式，误差率、置信度与校准度在数据集间差异明显。表示层面可轻易恢复数据集身份而临床标签可分性较低，提示捷径式行为；测序向量分解显示任务信号多位于数据集对齐子空间。数据集对抗训练、最差组优化与平衡微调可缓解部分数据集聚差异，但常以总体性能下降为代价；探索性元数据分析还发现年龄相关的标签依赖性概率偏移。
- [Between Obligations and Evidence: A Participatory Study of Translating the EU AI Act into Technical Requirements](https://arxiv.org/abs/2611.18439) · 机器建议排除，待抽查 · `p-21e07c40e92ded8603f5`
  该文通过32人参与式工作坊，围绕医疗疼痛估计、招聘与公共交通三个高风险场景，分析欧盟AI法案义务如何转化为技术需求、组织实践与合规证据，指出公平指标不能单独证明非歧视，并讨论监督、责任和部署变化导致证据失效。
- [Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate](https://arxiv.org/abs/2611.22904) · 建议纳入，待审核 · `p-62eefc78443f96579d03`
  该文审计小型临床联邦学习联盟中拜占庭鲁棒聚合的公平性，在3个FLamby数据集上比较8种聚合规则并运行54,214次实验。发现仅按客户端数量判断有效性会漏掉数据份额独裁；加权中位数、GeoMed与CC在单中心占比过半时崩溃；留出对照把性能下降分解为诚实数据损失与真实攻击损害；无权重规则会惩罚更新最异常的医院。
- [Correcting historical bias in machine learning predictions of healthcare utilization in India.](https://europepmc.org/article/MED/43050464) · 待核验 · `p-7abe2e1b40324a466501`
  基于印度LASI 55,698名老年人数据，训练门诊和住院利用预测模型，比较全样本与排除未满足医疗需求子样本模型在不同社会经济与种姓亚组间的预测差异，并用SHAP和全国成本外推评估历史可及性差异的影响。
- [Development and regional validation of a literacy-fair verbal cognitive screen for older adults in India.](https://europepmc.org/article/MED/43042671) · 待核验 · `p-04210e1f154be8b67c44`
  该研究在印度LASI-DAD队列（n=4096）中开发并验证完全口语化、无读写依赖的认知筛查模型Verbal-4，按识字水平分层比较AUC，并进行留一区域验证与临床CDR对照，报告不同识字组判别力相近且具独立预后信息。
- [Context is all you need: A causal framework for governing bias in clinical AI.](https://pubmed.ncbi.nlm.nih.gov/42993732/) · 相关，待核实是否纳入 · `p-4d615fab90a24703edd1`
  文章主张以因果与规范监督区分临床人工智能中临床合理与不合理的群体差异，提出六项标准、四种实现路径，以及兼顾临床敏感性与偏差降低的双向评估设想；未涉及具体疾病或实证实施。
- [Ethical guidelines for deploying artificial intelligence applications in the pathology field: Lessons learned from a prospective framework in a large tertiary care academic medical center.](https://pubmed.ncbi.nlm.nih.gov/42761742/) · 机器建议排除，待抽查 · `p-a9324f28d8acd70d333c`
  文章讨论病理学AI中的年龄、性别、种族和族裔代表性偏差，提出覆盖治理、预处理、处理、部署和监测的伦理指南框架，强调公平使用与持续监测。
- [AI alone will not transform healthcare: Learning Health Systems as the framework for responsible AI implementation.](https://europepmc.org/article/MED/43004359) · 机器建议排除，待抽查 · `p-ae502679561d916dd517`
  本文为评论文章，主张将医疗AI实施嵌入学习型健康系统（LHS），结合CFIR、ERIC、TEHAI等框架，强调持续评估、治理、子组监测与公平实施。引用美国医院调查指出AI采纳不均和偏倚评估不足，但未对具体临床任务开展算法公平性实证分析。
- [Causal gradient intervention for debiased and evidence-grounded medical visual question answering.](https://pubmed.ncbi.nlm.nih.gov/42526079/) · 相关，待核实是否纳入 · `p-b0b37535e71cc95770d9`
  提出DE-CaGI因果梯度干预框架，用于医学视觉问答；通过辅助分支估计语言与视觉先验造成的捷径偏置梯度，在主干更新中抑制相关分量，并引入多任务证据监督与证据一致性约束，以提升答案准确性和视觉证据对齐。在VQA-RAD和SLAKE上验证。
- [Evidence of limited biases in probed language-based assessments.](https://europepmc.org/article/MED/43002526) · 待核验 · `p-c3083ca58bc9a9905bcc`
  该研究评估开放式心理健康自述经大语言模型嵌入加岭回归预测抑郁/焦虑严重度的公平性：1260名参与者的评估误差与性别、年龄、教育、就业、收入等社会人口学变量及语言特征关联有限，但症状越重评估偏差越大；对训练数据下采样可消除该偏差。
- [C3E-RRG:Confounder-Aware Causal Evidence Coupling and Evolution for Chest X-Ray Report Generation.](https://europepmc.org/article/MED/42970651) · 机器建议排除，待抽查 · `p-d62b2748ad6ed04dbe11`
  提出C3E-RRG，在胸片报告生成中融合语言先验与疾病共现以构建混杂变量，并通过跨模态证据一致耦合和双向因果演化抑制模板与共现引起的虚假相关；在IU-XRay和MIMIC-CXR上验证。
- [Is it possible to vaccinate AI against bias? An exploratory study in epilepsy.](https://europepmc.org/article/MED/43014131) · 待核验 · `p-ec7c0f5cb541d6dacee9`
  该探索性概念验证研究在癫痫临床情景中测试提示指令能否减少六个大语言模型的诊断/治疗准确率差距。富裕与弱势复合画像在性别和社会描述上共同变化；结果按原评分规则重新计算，提示后汇总差距下降，但作者指出不能隔离社会经济偏倚或证明临床有效的去偏干预。
- [Large Language Models' Simulation of Patient Comprehension of Discharge Summaries: Multimodel Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42912964/) · 待核验 · `p-ee8b2a7189a3d8b4887f`
  该研究用4个当代LLM按教育、性别和医疗使用生成患者人设，模拟对出院小结的理解回答，并以模态绝对误差和序数距离比较其与99名人类参与者的对齐，考察各亚组公平性及思维链敏感性。
- [Confronting the Twin Divides: Data Bias and Infrastructure Gaps in AI-Driven Nutrition for the Global South.](https://pubmed.ncbi.nlm.nih.gov/42988168/) · 待核验 · `p-2e0706f35cfba2dd0a08`
  评论讨论全球南方AI营养应用中的数据偏差与基础设施差距，提及FRANI应用及营养不良模型临床使用不足，呼吁在部署前加强本地数据主权、基础设施和治理。
- [Longitudinal AI-based home-cage monitoring of locomotor aging in C57BL/6J mice: An exploratory pilot study.](https://pubmed.ncbi.nlm.nih.gov/43052603/) · 机器建议排除，待抽查 · `p-61addd093647a7caaf49`
  该探索性先导研究利用AI家庭笼监测系统（DOME）对C57BL/6J小鼠连续行为记录长达9个月，筛选出四项跨队列一致性较高的运动学指标，并按性别归一化以处理雌雄二态性，进而构建候选的运动源性行为衰弱指数（bFI），并在27月龄小鼠中初步观察到其与临床衰弱指数（CFI）的正相关。
- [Toward equitable fidelity measurement of evidence-based psychosocial interventions.](https://europepmc.org/article/MED/42956225) · 机器建议排除，待抽查 · `p-90e758f61454cf309cc5`
  摘要讨论心理社会循证干预中临床医生保真度（fidelity）测量的公平性问题：观察性保真度编码成本高、在资源匮乏环境中很少使用，且编码方案源自以白人、中产为主的临床试验人群。作者基于健康公平实施框架提出考量，并介绍标准化病人、片段编码和AI自动评分等探索，但未报告算法公平性的实证评估。
- [Comparing Lightweight Models for Physician-Consensus Pharyngitis Classification from Primary-Care Smartphone Images.](https://europepmc.org/article/MED/43028421) · 相关，待核实是否纳入 · `p-c52d73c3e19f9160643a`
  该研究在PGUPharyngitis智能手机咽部图像数据集上比较五种轻量级模型（四种CNN与MobileViT-XS）预测医师共识的细菌性/非细菌性咽炎标签，用五折患者级交叉验证评估PR-AUC与AUROC并考察计算效率。结果显示模型区分度中等，且采集设备与标签相关，设备混杂无法排除。
- [Artificial intelligence, health literacy, and sex and gender specific medicine: navigating the new paradigm in the physician-patient relationship.](https://europepmc.org/article/MED/42979871) · 机器建议排除，待抽查 · `p-ea3b2e02ee0a3aa3db56`
  该文为观点/评论性文章，讨论生成式AI、健康素养与性别特异医学对医患关系与临床实践的影响，泛泛指出训练数据偏倚会损害女性与少数群体的诊断适宜性，并呼吁公众提升数字健康素养、医生提升"算法素养"，未针对具体疾病或临床任务开展公平性分析或实证测量。
- [Critical Validation of Deep Learning-Based Cervical Vertebral Fracture Detection on Computed Tomography Localizer Radiographs.](https://europepmc.org/article/MED/42970201) · 机器建议排除，待抽查 · `p-1346d065a32670a53db3`
  该研究在346例创伤患者的CT定位片上评估深度学习颈椎骨折检测，比较全图二分类与先定位颈椎再分类的两步流程，并用置换检验、遮挡测试、Grad-CAM、混杂因素分析及按解剖部位的亚组分析检验模型有效性，发现全图模型虽PR-AUC更高，但并不主要依赖骨折区域，属于典型捷径学习案例。
- [Racial Composition and Single-Input Dominance in the First Hospice Special Focus Program Cohort.](https://pubmed.ncbi.nlm.nih.gov/42895138/) · 相关，待核实是否纳入 · `p-e2c8854d96deaa4b99ad`
  该研究审计美国临终关怀特别关注项目（SFP）的复合质量算法：对2024年11月CMS目录中7115家临终关怀机构做横断面分析，用逻辑回归检验入选与机构规模、患者种族构成及独立质量指标（HVLDL）的关系，并对50家入选机构的复合评分做标准化输入分解。结果显示入选与黑人患者比例显著相关，且48/50家入选机构的评分恶化主要由单一输入驱动，提示算法可能不成比例地影响服务黑人患者的机构。
- [Machine Learning Validation Pipelines: From Tabular Benchmarking to Conformal Calibration and Execution-Grounded Agentic Testing](https://europepmc.org/article/PPR/PPR1370333) · 机器建议排除，待抽查 · `p-280deca54061942c17e6`
  提出五层机器学习验证流程，涵盖基准测试与泄漏防护、可解释性审计、共形校准、部署前门控及执行级多智能体验证，并以金融ML元分析和临床分诊等高风险场景说明失败模式。
- [Contribution of artificial intelligence research to the development of inclusive applications for people with disabilities: A scoping review (2015-2025).](https://europepmc.org/article/MED/42879324) · 机器建议排除，待抽查 · `p-5ff397bb1086a10ff761`
  该文为2015—2025年范围综述，检索四个数据库并纳入93项健康AI研究，考察其对残障人士包容性应用的支持程度。约60%研究提及公平，但仅12.9%落实具体措施（如工具适配、样本多样性），6.5%让残障人士参与共同设计或验证，并指出算法偏见与数据代表性不足等问题。
- [Advancing Equitable and Trustworthy AI in Breast Cancer Detection Through Interpretable Deep Learning](https://europepmc.org/article/PPR/PPR1361567) · 待核验 · `p-6c2d4e6ce2f485ff83ff`
  该文为PRISMA系统综述，聚焦乳腺癌钼靶筛查中深度学习模型的公平性与人口学偏倚，提出解释图“reasoning bias”及多指标热图偏倚评估框架，并指出种族、年龄和乳腺密度交叉亚组证据不足。
- [Evaluating four consumer artificial intelligence chatbots on smartphone dermatology images: diagnostic accuracy, the contribution of clinical context, and skin-tone equity](https://europepmc.org/article/PPR/PPR1365867) · 待核验 · `p-79ee704c380a3242315c`
  该研究在3,005例SCIN智能手机皮肤图像上评估四款消费级AI聊天机器人，比较单图、多图、图像加临床背景及纯文本四种条件下的诊断准确率，并按Fitzpatrick肤色分层检验公平性，发现表现最好的模型存在浅色与深色皮肤间的准确率差异。
- [Continual learning in oncology AI: A framework for safe clinical translation.](https://pubmed.ncbi.nlm.nih.gov/43063946/) · 机器建议排除，待抽查 · `p-28adaf06b29241ce8db3`
  该文综述肿瘤学AI中的持续学习方法，讨论灾难性遗忘、校准与重训等转化障碍，并提出包含亚组安全、校准稳定性等六项安全转化标准。公平性仅作为持续学习临床转化的一项风险被提及。
- [Prognostic Factors for Survival in ICI-Treated NSCLC: An Umbrella Review of Evidence Certainty and Clinical Relevance.](https://europepmc.org/article/MED/43033040) · 待分析／证据不足 · `p-85640a44163a7e495a79`
- [Artificial Intelligence in Longevity Research: From Molecular Clocks to Interventional Geroscience](https://europepmc.org/article/PPR/PPR1357971) · 机器建议排除，待抽查 · `p-873f8add702e04deb02e`
  叙述性综述梳理AI衰老时钟（表观基因组、蛋白质组、视网膜、心电、MRI等）在年龄估计、预后关联、干预反应与替代终点验证四类属性上的证据，提出证据阶梯与转化链，并指出校准报告不足与因果推断缺口。
- [Artificial Intelligence as a Catalyst for Value-Based Care in Vascular Disease.](https://europepmc.org/article/MED/43035227) · 待分析／证据不足 · `p-cf956d481a5b46de9c2b`
- [Predicting PANSS symptoms in schizophrenia spectrum disorders using speech only: an international, multi-centre, computational secondary analysis across multiple languages.](https://pubmed.ncbi.nlm.nih.gov/42991136/) · 待核验 · `p-dfd76ee4553e36909d88`
  该国际多中心计算二次分析汇总10国453例精神分裂症谱系障碍患者的语音，将录音切分为6664段，比较16种算法预测8个PANSS条目，并按年龄、性别、教育程度和症状严重度做偏倚检查。预训练多语言嵌入表现最佳；除男性N4准确率较低外，未见年龄、性别或教育偏倚，但高症状严重度下性能下降。
- [Orbital morphometry on computed tomography for sex estimation: A systematic review and meta-analysis.](https://pubmed.ncbi.nlm.nih.gov/43057131/) · 待分析／证据不足 · `p-f0405d6bf007e5f2b22c`
- [Smoking and dementia risk: an updated systematic review and meta-analysis of 61 prospective cohort studies and implications for tobacco control.](https://pubmed.ncbi.nlm.nih.gov/43034842/) · 待分析／证据不足 · `p-2308c78840b3881bc14d`
- [Machine learning-based risk prediction of hepatocellular carcinoma in patients with chronic hepatitis B: current evidence and future directions.](https://europepmc.org/article/MED/43064890) · 待分析／证据不足 · `p-b7ac23993de63dc9a3e9`
- [Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706) · 待分析／证据不足 · `p-220173ecbe71aeffc6a2`
- [Data-centric, robust, and explainable multimodal deep learning for clinical decision support: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42667902/) · 待分析／证据不足 · `p-2dc7893202614a28f741`
- [Application of geospatial technologies in mental health research: A scoping review of progress and future directions.](https://europepmc.org/article/MED/43042965) · 待分析／证据不足 · `p-496be92504999e54331b`
- [Intelligent immunotherapy: AI-driven optimization of CAR-T therapy in hematologic malignancies.](https://pubmed.ncbi.nlm.nih.gov/42904142/) · 待分析／证据不足 · `p-d3566a29f4f70f84cac4`
- [Explainable Artificial Intelligence for Cognitive Workload Assessment: Methods, Evidence, and Human-Centered Evaluation](https://europepmc.org/article/PPR/PPR1372432) · 待分析／证据不足 · `p-b1af80e58334a13852a7`

## Clinical NLP and Foundation Models

- [AI-powered radiology report simplification in Arabic: A prospective evaluation of patient-perceived understandability and clinical safety.](https://pubmed.ncbi.nlm.nih.gov/42546532/) · 相关，待核实是否纳入 · `p-9d65abc11d11465e0b29`
  该研究前瞻性评估本地部署的两阶段大语言模型系统，将放射学报告简化为英语和阿拉伯语，报告患者可理解性及放射科医生判定的临床安全性，但未开展算法公平性分析。
- [SIGHT: A Methodological Appraisal Framework for Evaluating Large Language Models in Ophthalmology](https://arxiv.org/abs/2610.15958) · 机器建议排除，待抽查 · `p-1d69c85a37b528600868`
  该文批判性综述眼科大语言模型评价研究，提出SIGHT五域二十项方法学评价框架，关注样本来源、盲法、对照公平性、配对数据处理与透明度，旨在提升研究内部有效性和临床相关性。
- [PVminerLLM: structured extraction of patient voice from patient-generated text using large language models.](https://europepmc.org/article/MED/42952888) · 机器建议排除，待抽查 · `p-c1f95a81a24c991508ae`
  PVminerLLM 提出 PVminer 基准与一个监督微调的大语言模型，用于从患者生成文本中结构化抽取“患者声音”（如社会处境、就医参与等非临床信息），在代码、子代码与证据片段抽取上取得最高约 84%、81%、88% 的 F1，并声称小模型也可达到较好效果。
- [Evidence of limited biases in probed language-based assessments.](https://europepmc.org/article/MED/43002526) · 待核验 · `p-c3083ca58bc9a9905bcc`
  该研究评估开放式心理健康自述经大语言模型嵌入加岭回归预测抑郁/焦虑严重度的公平性：1260名参与者的评估误差与性别、年龄、教育、就业、收入等社会人口学变量及语言特征关联有限，但症状越重评估偏差越大；对训练数据下采样可消除该偏差。
- [Is it possible to vaccinate AI against bias? An exploratory study in epilepsy.](https://europepmc.org/article/MED/43014131) · 待核验 · `p-ec7c0f5cb541d6dacee9`
  该探索性概念验证研究在癫痫临床情景中测试提示指令能否减少六个大语言模型的诊断/治疗准确率差距。富裕与弱势复合画像在性别和社会描述上共同变化；结果按原评分规则重新计算，提示后汇总差距下降，但作者指出不能隔离社会经济偏倚或证明临床有效的去偏干预。
- [Large Language Models' Simulation of Patient Comprehension of Discharge Summaries: Multimodel Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42912964/) · 待核验 · `p-ee8b2a7189a3d8b4887f`
  该研究用4个当代LLM按教育、性别和医疗使用生成患者人设，模拟对出院小结的理解回答，并以模态绝对误差和序数距离比较其与99名人类参与者的对齐，考察各亚组公平性及思维链敏感性。
- [Protocol for Conducting a Scoping Review on The Use of AI in Automated Scoring of Short-Answer Questions in Medical Education](https://europepmc.org/article/PPR/PPR1346575) · 机器建议排除，待抽查 · `p-cc8d5c0e4ff2868dbbd2`
  该文是一篇范围综述方案，计划梳理医学教育中AI自动评分简答题的模型、评分性能、信效度及公平性比较，采用JBI方法和PCC框架，纳入2015年以来的实证研究。摘要未报告任何已完成的公平性分析或结果。
- [Evaluating four consumer artificial intelligence chatbots on smartphone dermatology images: diagnostic accuracy, the contribution of clinical context, and skin-tone equity](https://europepmc.org/article/PPR/PPR1365867) · 待核验 · `p-79ee704c380a3242315c`
  该研究在3,005例SCIN智能手机皮肤图像上评估四款消费级AI聊天机器人，比较单图、多图、图像加临床背景及纯文本四种条件下的诊断准确率，并按Fitzpatrick肤色分层检验公平性，发现表现最好的模型存在浅色与深色皮肤间的准确率差异。
- [Impact of Unrestricted Artificial Intelligence Scribe Deployment in a Single Health System on Clinician Workload and Productivity : A Quality Improvement Study.](https://europepmc.org/article/MED/42932880) · 机器建议排除，待抽查 · `p-d4ccac7ce879b6812b7a`
  该研究为单家医疗系统的回顾性质量改进研究，采用中断时间序列分析，评估902名门诊临床医生启用环境AI病历记录助手（Heidi）后文档负担的变化，并按使用强度（未使用者、低使用者、高使用者）分组比较。结果显示启用后记录活跃时间小幅下降、病历长度增加，且高使用者变化更明显；当日与工作时间外病历完成率及wRVU均无差异。
- [Translation and Cross-Cultural Adaptation of the Chronic Rhinosinusitis Control Test for Global Use.](https://pubmed.ncbi.nlm.nih.gov/42262654/) · 机器建议排除，待抽查 · `p-014d28297e30dc61bb6f`
  该研究采用生成式人工智能（ChatGPT、Copilot、Perplexity 等大语言模型）与人工语言学家协作的混合流程，将慢性鼻窦炎控制测试（CRCT）翻译并跨文化适配为37种语言，并对各步骤译文的准确性与有效性进行定性与定量评估，作者称此举可促进数据公平。
- [Artificial Intelligence as a Catalyst for Value-Based Care in Vascular Disease.](https://europepmc.org/article/MED/43035227) · 待分析／证据不足 · `p-cf956d481a5b46de9c2b`
- [Machine learning-based risk prediction of hepatocellular carcinoma in patients with chronic hepatitis B: current evidence and future directions.](https://europepmc.org/article/MED/43064890) · 待分析／证据不足 · `p-b7ac23993de63dc9a3e9`
- [Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706) · 待分析／证据不足 · `p-220173ecbe71aeffc6a2`
- [Data-centric, robust, and explainable multimodal deep learning for clinical decision support: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42667902/) · 待分析／证据不足 · `p-2dc7893202614a28f741`
- [AI-generated patient instructions as safety-critical communication: a provisional evidence-informed framework for clinical deployment.](https://pubmed.ncbi.nlm.nih.gov/42607431/) · 待分析／证据不足 · `p-31dd08c87fcdfb2c9189`
- [In-context learning for medical artificial intelligence.](https://pubmed.ncbi.nlm.nih.gov/43008739/) · 待分析／证据不足 · `p-62e5a416316a8b47bef5`
- [Bias and equity in large language model-based applications for health care: a scoping review.](https://europepmc.org/article/MED/43052083) · 待分析／证据不足 · `p-aca067eb1061051f9b86`
- [Intelligent immunotherapy: AI-driven optimization of CAR-T therapy in hematologic malignancies.](https://pubmed.ncbi.nlm.nih.gov/42904142/) · 待分析／证据不足 · `p-d3566a29f4f70f84cac4`
- [Artificial Intelligence in Thoracic Pathology and Biomarker Assessment: An IASLC Pathology Committee Review.](https://europepmc.org/article/MED/43064238) · 待分析／证据不足 · `p-aa1d2c08ab2918b9678a`

## EHR, Physiological Signals and Healthcare

- [HIV-PrivFed: Privacy-Utility-Fairness-Aware Federated Learning for HIV Risk Stratification and Testing Prioritization Under Non-IID Clinical Heterogeneity.](https://europepmc.org/article/MED/43028461) · 相关，待核实是否纳入 · `p-a4d951a2b8b867906d60`
  基于Sialon-II队列（13个欧洲城市MSM，13个自然客户端）开展水平联邦学习，比较十种传统分类器、集中式MLP及local-only/FedAvg/FedProx基线，提出差分隐私FedProx算法HIV-PrivFed，配备客户端级Rényi隐私核算与客户端级公平性审计（仅审计、不强制）。结果显示隐私预算远松于名义目标，客户端级估计不确定性高。
- [Design-based fairness monitoring for healthcare prediction with complex survey data.](https://europepmc.org/article/MED/42914067) · 待核验 · `p-afe7ffeed3546c2df3d8`
  该研究提出基于复杂抽样设计的公平性监测框架，利用2015—2023年MEPS九轮数据，以随机森林预测高额医疗支出，并按性别、种族/民族和贫困状态评估人口均等与机会均等，估计设计校正的公平性差异及时间趋势。
- [Routine to Emergency: A Machine Learning Approach for Predicting ED Visits Among Patients with T2D](https://europepmc.org/article/PPR/PPR1358206) · 待核验 · `p-cc9092de484d4c94f075`
  该研究利用EHR数据开发六种机器学习模型，预测2型糖尿病患者未来30/60/90天急诊就诊，并报告性别及种族/族裔亚组的判别与召回差异。摘要仅提供有限公平性结果，无法核实完整偏差分析。
- [An Open, Reproducible Implementation of the CMS Hospital-Wide Readmission Measure on MIMIC-IV](https://europepmc.org/article/PPR/PPR1347611) · 相关，待核实是否纳入 · `p-d5f34822605251a88ec8`
  该文发布 CMS 医院全因再读入（HWR）指标的开放可复现实现：在 MIMIC-IV 上按计划性再读入算法与专科队列重建标签，使 30 天事件率由 17.6% 降至 15.9%（n=192,879），并公开编码表、Quan-Elixhauser 合并症编码与防泄漏特征规范，附校准基线模型（AUC 0.730），摘要称其做过亚组公平性与时间漂移评估。
- [ECG foundation models share an age-related performance disparity that originates in the data, not the models](https://europepmc.org/article/PPR/PPR1357796) · 待核验 · `p-e68fcceb7a02de0b9211`
  该研究在四个ECG基础模型、13个队列约540万份ECG上按年龄、性别和种族评估性能差异，发现差异主要集中于年龄并可在外部复现；未训练网络和经典特征模型也重现年龄差距，提示差异源于数据与任务而非预训练模型。
- [Deep Survival Analysis with Temporal Trajectory Embedding for Substandard Life Insurance Pricing: A DeepSurv Modeling Study of Type 2 Diabetes Mellitus](https://europepmc.org/article/PPR/PPR1360391) · 机器建议排除，待抽查 · `p-12f4eff61a09eab3bddf`
  该文以约188万份T2DM住院理赔记录构建DeepSurv定价框架，比较EM、GLM与Tweedie模型，并加入Elastic Net、LSTM、SHAP和Bootstrap稳健性检验；但仅在结论泛称提升定价公平性，未开展公平性分析。
- [A Multi-Model Framework for Explainable Sepsis Mortality Prediction With Dynamic Fairness and Drift Analysis.](https://europepmc.org/article/MED/43056270) · 待核验 · `p-3f9a2ee2dec669d59e15`
  该研究在MIMIC-IV上构建脓毒症死亡预测多模型框架，将公平性重新定义为动态生命周期属性，在15轮再训练与16个交叉子群中监测TPR、FPR、FOR差距，并开展eICU跨机构公平性审计与SHAP稳定性分析。
- [Radiology No-Show Calculator: A Social Determinants of Health-Enriched Machine Learning Prediction Model With Financial Analysis.](https://pubmed.ncbi.nlm.nih.gov/42660476/) · 待核验 · `p-1582a8a2e3798f9bf7f2`
  该研究开发基于随机森林的放射科门诊失约预测模型，纳入区域剥夺指数等16个预测因子，并按人群患病率校准；报告AUC 0.760、ADI相关失约梯度和财务负担，提出针对高风险患者外展。
- [Development and internal validation of a CSF-free machine-learning model to distinguish immune checkpoint inhibitor-induced encephalitis from HSV-1 and anti-LGI1 encephalitis](https://europepmc.org/article/PPR/PPR1355264) · 机器建议排除，待抽查 · `p-66a0131f9ccb7890785d`
  该摘要开发并内部验证一个不含脑脊液特征的随机森林模型，用于区分ICI相关脑炎与HSV-1及抗LGI1脑炎，报告AUC、校准和决策曲线等性能。
- [Self-report label bias in machine learning screening for undiagnosed diabetes: development, validation and offline on-device deployment of an interpretable HbA1c-anchored tool.](https://pubmed.ncbi.nlm.nih.gov/43033525/) · 待核验 · `p-8e1089bbb872533b5f51`
  该研究基于NHANES与BRFSS数据，量化自报糖尿病诊断标签如何改变机器学习筛查模型优先识别人群的方式，显示自报标签部分编码了就医可及性；用正-未标记学习校正标签，并开发以HbA1c为锚点的可解释筛查工具，在相同转诊率下与指南规则比较敏感度并做离线部署验证。
- [Machine learning for maternal risk prediction in resource- constrained antenatal care: evidence-to-implementation gaps and implications for Sustainable Development Goal 3](https://europepmc.org/article/PPR/PPR1365530) · 机器建议排除，待抽查 · `p-ebc11a06a333203c74b7`
  该研究笔记梳理资源受限产前护理中孕产妇风险预测的机器学习证据，指出高准确率可能掩盖漏诊，主张在判别力之外同时评估校准、公平、工作流和前瞻性影响。
- [Causally Constrained and Uncertainty-Aware Cardiopulmonary Risk Prediction](https://arxiv.org/abs/2611.17819) · 机器建议排除，待抽查 · `p-f6c51344bb4b7f0ff028`
  提出CE-Agent两阶段心肺风险预测框架，将流行病学证据预先编译为因果约束，再拟合临床与胸部CT表型权重，并用闭式不确定性传播处理缺失输入；在NLST与MESA中评估判别、校准、跨医院与跨扫描仪泛化以及联合肺癌和心血管分诊。
- [Correcting historical bias in machine learning predictions of healthcare utilization in India.](https://europepmc.org/article/MED/43050464) · 待核验 · `p-7abe2e1b40324a466501`
  基于印度LASI 55,698名老年人数据，训练门诊和住院利用预测模型，比较全样本与排除未满足医疗需求子样本模型在不同社会经济与种姓亚组间的预测差异，并用SHAP和全国成本外推评估历史可及性差异的影响。
- [AI-Assisted Voice Analysis for Laryngeal Cancer: Primary Care Perspectives on Clinical Implementation](https://europepmc.org/article/PPR/PPR1371788) · 机器建议排除，待抽查 · `p-a837a6597aee491abb27`
  一项混合方法横断面研究，通过访谈（15人）与匿名问卷（16份）考察基层医生对持续性发声困难的处理方式，以及对语音人工智能用于喉癌风险分层的接受度。结果显示医生普遍将其视为决策支持而非替代临床判断，采纳取决于准确性、流程影响、监督、转诊路径及公平可及性等条件。
- [AI alone will not transform healthcare: Learning Health Systems as the framework for responsible AI implementation.](https://europepmc.org/article/MED/43004359) · 机器建议排除，待抽查 · `p-ae502679561d916dd517`
  本文为评论文章，主张将医疗AI实施嵌入学习型健康系统（LHS），结合CFIR、ERIC、TEHAI等框架，强调持续评估、治理、子组监测与公平实施。引用美国医院调查指出AI采纳不均和偏倚评估不足，但未对具体临床任务开展算法公平性实证分析。
- [Clinical AI in Canadian Community Hospitals: A Framework for Implementation Readiness.](https://europepmc.org/article/MED/42880210) · 机器建议排除，待抽查 · `p-e91c09dd8b3e74599212`
  提出加拿大社区医院临床AI实施准备框架，围绕情境有效性、社会技术工作流整合、人机依赖校准以及安全、公平与治理四个维度，通过模拟系统测试加以落实，并以CHARTwatch早期预警系统作为实践示例。
- [Progressing From Association to Causation: Examining Prior Antibiotic Exposure and Antimicrobial Resistance Across Three US Health Systems Using Causal Machine Learning.](https://europepmc.org/article/MED/42878671) · 机器建议排除，待抽查 · `p-ef01908a70510b22bc66`
  利用双机器学习，在三个美国医疗系统的1,165,151次培养事件中估计既往90天抗生素暴露对同类耐药的因果效应，校正35个以上混杂因素，并用逆概率加权、E值、暴露窗口与剂量-反应敏感性分析及阴性对照进行稳健性验证；同时比较既往同类暴露者经验性治疗无效的比例。
- [Connecting risk prediction to intervention: evidence from a randomized trial testing patient navigation and education to improve postpartum outcomes.](https://pubmed.ncbi.nlm.nih.gov/42705386/) · 机器建议排除，待抽查 · `p-18c55d52c86dda3044c3`
  该试点随机对照试验利用既往验证的产后医院使用风险计算器筛选高风险黑人个体，评估产后教育与患者导航干预的可行性和30天医院使用率；未评估算法公平性或偏倚。
- [Racial Composition and Single-Input Dominance in the First Hospice Special Focus Program Cohort.](https://pubmed.ncbi.nlm.nih.gov/42895138/) · 相关，待核实是否纳入 · `p-e2c8854d96deaa4b99ad`
  该研究审计美国临终关怀特别关注项目（SFP）的复合质量算法：对2024年11月CMS目录中7115家临终关怀机构做横断面分析，用逻辑回归检验入选与机构规模、患者种族构成及独立质量指标（HVLDL）的关系，并对50家入选机构的复合评分做标准化输入分解。结果显示入选与黑人患者比例显著相关，且48/50家入选机构的评分恶化主要由单一输入驱动，提示算法可能不成比例地影响服务黑人患者的机构。
- [Beyond AUROC: External Validation, Calibration, and Explainability of Machine Learning Models for 30-Day Hospital Readmission Using Electronic Health Records—A Rapid Systematic Review](https://europepmc.org/article/PPR/PPR1346087) · 待核验 · `p-fb55a16fedc7a47752c1`
  该快速系统综述评估EHR 30天再入院预测模型的验证、校准、可解释性与亚组公平性报告情况，发现公平性分析仅占4.5%，并提出超越AUROC的最小评估集。
- [Impact of Unrestricted Artificial Intelligence Scribe Deployment in a Single Health System on Clinician Workload and Productivity : A Quality Improvement Study.](https://europepmc.org/article/MED/42932880) · 机器建议排除，待抽查 · `p-d4ccac7ce879b6812b7a`
  该研究为单家医疗系统的回顾性质量改进研究，采用中断时间序列分析，评估902名门诊临床医生启用环境AI病历记录助手（Heidi）后文档负担的变化，并按使用强度（未使用者、低使用者、高使用者）分组比较。结果显示启用后记录活跃时间小幅下降、病历长度增加，且高使用者变化更明显；当日与工作时间外病历完成率及wRVU均无差异。
- [Real-time peri-operative data integration and clinical decision support: an open interoperable platform for patient data.](https://pubmed.ncbi.nlm.nih.gov/42298974/) · 机器建议排除，待抽查 · `p-750bf3589b72386d1cf9`
  介绍一个开放、可互操作的围手术期数据平台，基于 Apache Kafka 实时整合监护仪、注射泵、呼吸机、脑电与检验数据，采用本地存储与匿名化治理；自2019年已收录118915名患者、77张手术室或重症监护床位的波形与数值数据，支持实时临床决策与多中心研究。
- [Predicting PANSS symptoms in schizophrenia spectrum disorders using speech only: an international, multi-centre, computational secondary analysis across multiple languages.](https://pubmed.ncbi.nlm.nih.gov/42991136/) · 待核验 · `p-dfd76ee4553e36909d88`
  该国际多中心计算二次分析汇总10国453例精神分裂症谱系障碍患者的语音，将录音切分为6664段，比较16种算法预测8个PANSS条目，并按年龄、性别、教育程度和症状严重度做偏倚检查。预训练多语言嵌入表现最佳；除男性N4准确率较低外，未见年龄、性别或教育偏倚，但高症状严重度下性能下降。
- [Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706) · 待分析／证据不足 · `p-220173ecbe71aeffc6a2`
- [Application of Artificial Intelligence (AI) in cancer symptom management for adult cancer survivors: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42603423/) · 待分析／证据不足 · `p-622c2ee72af5786411dd`
- [Explainable Artificial Intelligence for Cognitive Workload Assessment: Methods, Evidence, and Human-Centered Evaluation](https://europepmc.org/article/PPR/PPR1372432) · 待分析／证据不足 · `p-b1af80e58334a13852a7`
- [Potential and pitfalls of artificial intelligence to address disparities in epilepsy.](https://europepmc.org/article/MED/43064818) · 待分析／证据不足 · `p-801228119b6cf272fa53`

## Fairness Evaluation and Benchmarking

- [Implications of Image-Level Duplication in Public Glaucoma Datasets.](https://europepmc.org/article/MED/43018943) · 待核验 · `p-13cc881c6ffbf754dbd7`
  该研究审计3个公开青光眼数据集，发现Harvard-GF与FairVision有1302眼匹配、1031眼为同一OCT volume，跨数据集分类AUC因泄漏升高0.12，且各种族亚组均出现膨胀，提示独立基准与公平性评估可能被高估。
- [Applications of Fairness Training in Artificial Intelligence to Ophthalmic Disease Diagnosis using External Eye Photographs](https://europepmc.org/article/PPR/PPR1363752) · 待核验 · `p-21b44eb38a70c944169c`
  摘要报告利用40,687张外部眼照片开发深度学习与视觉语言模型，对威胁视力DR、晚期AMD和青光眼做二分类，并以ES-AUC评估性别、种族和族裔公平性，比较五种公平训练策略。报告称公平训练部分缩小差异并提升VTDR/AMD的AUC，但模型尚不适合临床部署。
- [FSD-Net: A Unified Skin-Tone-Aware Framework for Fair Skin Lesion Segmentation and Classification](https://europepmc.org/article/PPR/PPR1370450) · 待核验 · `p-3daf0c4282bca4f685cf`
  FSD-Net在皮肤病变分割与分类两个阶段同时考虑肤色公平性：用连续肤色评分经FiLM调制ViT-B/16分割骨干，并用分割引导的ROI训练Swin-V2-Tiny分类器。在ISIC-2017/2018、PH2及HAM10000上报告Dice、准确率和Equalized Opportunity差距，并辅以消融、Bootstrap置信区间和McNemar检验。
- [Same Model, Different People: Numerical Execution Contracts and the Reproducibility of Fairness Audits](https://arxiv.org/abs/2611.23657) · 建议纳入，待审核 · `p-52131ebbc4ad7c4a8714`
  该文将固定模型的数值执行契约（FP64/FP32/TF32/FP8等）视为决策函数的一部分，在收入、就业、房贷和30天再入院任务上评估公平性审计结论的可复现性；提出审计稳定性协议，报告不同契约下统计量与通过/失败判定的范围。再入院任务按种族、性别和年龄分层，显示低精度部署可改变诊断性公平判定，但未证明FP8更公平。
- [Reliable Skin-Tone Fairness in Dermatology AI: From Lesion-Level Leakage to Tone-Adaptive Learning](https://europepmc.org/article/PPR/PPR1345750) · 待核验 · `p-53d198d32447f559a258`
  提出面向皮肤镜与临床图像的色调自适应预处理流程，并建立按病灶分组、类别分层的评估协议，量化病灶级泄漏和肤色代理指标问题；在三个基准上报告深色皮肤敏感度提升，并发布泄漏审计工具。
- [Governed Auditing of Hidden Failure Slice Discovery in Emergency Department Admission Models Agnostic to Sensitive Attributes](https://europepmc.org/article/PPR/PPR1363950) · 待核验 · `p-802f852b1e8f331fe15d`
  提出BASiC与ASAP，在急诊入院预测中利用临床规则和折外误差信号发现隐藏失败切片，并尝试样本加权修复。研究在Kaggle、RIPAS和NHAMCS数据上评估多种模型，发现切片发现较可靠，但修复未带来一致改善，且不建立人口统计学公平或临床有效性。
- [Predicting Depression Risk Using Machine Learning Among Students](https://europepmc.org/article/PPR/PPR1362751) · 待核验 · `p-8ba36d760ea51eb05928`
  该研究基于27,900份学生问卷，比较逻辑回归、随机森林和XGBoost预测非临床抑郁风险，并进行性别公平性与SHAP/LIME可解释性分析；摘要称各模型准确率约84.5%–84.8%，性别差异较小。
- [Causal-Weighted Machine Learning for RRT Prediction in Acute Kidney Injury: Development, External Validation, and Clinical Decision Support](https://europepmc.org/article/PPR/PPR1367120) · 待核验 · `p-9bbed0421308d7921eb5`
  该研究开发并外部验证了用于KDIGO 3期AKI患者48小时RRT启动预测的因果加权机器学习流程，采用堆叠集成与IPW元学习，并报告内部AUC 0.894、外部AUC 0.807；摘要还称公平性评估未发现具有临床意义的亚组差距，但未给出亚组定义或指标。
- [HIV-PrivFed: Privacy-Utility-Fairness-Aware Federated Learning for HIV Risk Stratification and Testing Prioritization Under Non-IID Clinical Heterogeneity.](https://europepmc.org/article/MED/43028461) · 相关，待核实是否纳入 · `p-a4d951a2b8b867906d60`
  基于Sialon-II队列（13个欧洲城市MSM，13个自然客户端）开展水平联邦学习，比较十种传统分类器、集中式MLP及local-only/FedAvg/FedProx基线，提出差分隐私FedProx算法HIV-PrivFed，配备客户端级Rényi隐私核算与客户端级公平性审计（仅审计、不强制）。结果显示隐私预算远松于名义目标，客户端级估计不确定性高。
- [Design-based fairness monitoring for healthcare prediction with complex survey data.](https://europepmc.org/article/MED/42914067) · 待核验 · `p-afe7ffeed3546c2df3d8`
  该研究提出基于复杂抽样设计的公平性监测框架，利用2015—2023年MEPS九轮数据，以随机森林预测高额医疗支出，并按性别、种族/民族和贫困状态评估人口均等与机会均等，估计设计校正的公平性差异及时间趋势。
- [Explainable, Uncertainty-Aware Ensemble Learning for Brain Tumor Classification from MRI with a Simulated Fairness Audit](https://europepmc.org/article/PPR/PPR1365579) · 待核验 · `p-c081b58879d4f9838b0c`
  该研究构建了结合五种卷积网络和ViT的脑MRI肿瘤分类集成模型，评估校准、解释与不确定性，并用流行病学先验模拟年龄/性别标签进行公平性审计，报告各模型亚组差距较小且方向一致。
- [Routine to Emergency: A Machine Learning Approach for Predicting ED Visits Among Patients with T2D](https://europepmc.org/article/PPR/PPR1358206) · 待核验 · `p-cc9092de484d4c94f075`
  该研究利用EHR数据开发六种机器学习模型，预测2型糖尿病患者未来30/60/90天急诊就诊，并报告性别及种族/族裔亚组的判别与召回差异。摘要仅提供有限公平性结果，无法核实完整偏差分析。
- [ECG foundation models share an age-related performance disparity that originates in the data, not the models](https://europepmc.org/article/PPR/PPR1357796) · 待核验 · `p-e68fcceb7a02de0b9211`
  该研究在四个ECG基础模型、13个队列约540万份ECG上按年龄、性别和种族评估性能差异，发现差异主要集中于年龄并可在外部复现；未训练网络和经典特征模型也重现年龄差距，提示差异源于数据与任务而非预训练模型。
- [MelanoFusion: An Explainable and Uncertainty-Aware Hybrid CNN–Transformer Framework for Dermoscopic Melanoma Detection](https://europepmc.org/article/PPR/PPR1370178) · 相关，待核实是否纳入 · `p-fd455cc2a36673f35d55`
  提出MelanoFusion混合CNN–Transformer框架用于皮肤镜黑色素瘤检测，结合可解释性、不确定性估计与公平导向表征学习；在HAM10000、ISIC 2018和PH²上评估，报告年龄组敏感性差异但性别无显著差异，并提示需外部验证。
- [A Multi-Model Framework for Explainable Sepsis Mortality Prediction With Dynamic Fairness and Drift Analysis.](https://europepmc.org/article/MED/43056270) · 待核验 · `p-3f9a2ee2dec669d59e15`
  该研究在MIMIC-IV上构建脓毒症死亡预测多模型框架，将公平性重新定义为动态生命周期属性，在15轮再训练与16个交叉子群中监测TPR、FPR、FOR差距，并开展eICU跨机构公平性审计与SHAP稳定性分析。
- [Preoperative Mortality Risk Prediction and Equity Using Preoperative Score to Predict Postoperative Mortality in a Diverse US Surgical Population: Retrospective Cohort Study.](https://europepmc.org/article/MED/43050561) · 建议纳入，待审核 · `p-46c871af6f5cd511e575`
  该回顾性队列研究利用All of Us数据评估POSPOM术前死亡风险评分在17,262例手术患者中的判别与校准，并按种族/民族亚组描述30天和1年死亡差异；发现高危患者判别下降、黑人患者绝对死亡率更高但事件数少，提示需外部验证和重新校准。
- [When multi-institutional dataset aggregation masks shortcut-like behavior in Foundation Models for medical imaging.](https://pubmed.ncbi.nlm.nih.gov/42641372/) · 待核验 · `p-b450c1e3be8d7e77257b`
  该研究以乳腺X线摄影分类为任务，将预训练图像编码器（基础模型）作为特征提取器，在十个采集流程、人群与地区各异的队列上训练分类器，发现聚合异质数据会带来依赖数据集的失效模式，误差率、置信度与校准度在数据集间差异明显。表示层面可轻易恢复数据集身份而临床标签可分性较低，提示捷径式行为；测序向量分解显示任务信号多位于数据集对齐子空间。数据集对抗训练、最差组优化与平衡微调可缓解部分数据集聚差异，但常以总体性能下降为代价；探索性元数据分析还发现年龄相关的标签依赖性概率偏移。
- [Machine learning for maternal risk prediction in resource- constrained antenatal care: evidence-to-implementation gaps and implications for Sustainable Development Goal 3](https://europepmc.org/article/PPR/PPR1365530) · 机器建议排除，待抽查 · `p-ebc11a06a333203c74b7`
  该研究笔记梳理资源受限产前护理中孕产妇风险预测的机器学习证据，指出高准确率可能掩盖漏诊，主张在判别力之外同时评估校准、公平、工作流和前瞻性影响。
- [Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate](https://arxiv.org/abs/2611.22904) · 建议纳入，待审核 · `p-62eefc78443f96579d03`
  该文审计小型临床联邦学习联盟中拜占庭鲁棒聚合的公平性，在3个FLamby数据集上比较8种聚合规则并运行54,214次实验。发现仅按客户端数量判断有效性会漏掉数据份额独裁；加权中位数、GeoMed与CC在单中心占比过半时崩溃；留出对照把性能下降分解为诚实数据损失与真实攻击损害；无权重规则会惩罚更新最异常的医院。
- [Correcting historical bias in machine learning predictions of healthcare utilization in India.](https://europepmc.org/article/MED/43050464) · 待核验 · `p-7abe2e1b40324a466501`
  基于印度LASI 55,698名老年人数据，训练门诊和住院利用预测模型，比较全样本与排除未满足医疗需求子样本模型在不同社会经济与种姓亚组间的预测差异，并用SHAP和全国成本外推评估历史可及性差异的影响。
- [Development and regional validation of a literacy-fair verbal cognitive screen for older adults in India.](https://europepmc.org/article/MED/43042671) · 待核验 · `p-04210e1f154be8b67c44`
  该研究在印度LASI-DAD队列（n=4096）中开发并验证完全口语化、无读写依赖的认知筛查模型Verbal-4，按识字水平分层比较AUC，并进行留一区域验证与临床CDR对照，报告不同识字组判别力相近且具独立预后信息。
- [Context is all you need: A causal framework for governing bias in clinical AI.](https://pubmed.ncbi.nlm.nih.gov/42993732/) · 相关，待核实是否纳入 · `p-4d615fab90a24703edd1`
  文章主张以因果与规范监督区分临床人工智能中临床合理与不合理的群体差异，提出六项标准、四种实现路径，以及兼顾临床敏感性与偏差降低的双向评估设想；未涉及具体疾病或实证实施。
- [AI alone will not transform healthcare: Learning Health Systems as the framework for responsible AI implementation.](https://europepmc.org/article/MED/43004359) · 机器建议排除，待抽查 · `p-ae502679561d916dd517`
  本文为评论文章，主张将医疗AI实施嵌入学习型健康系统（LHS），结合CFIR、ERIC、TEHAI等框架，强调持续评估、治理、子组监测与公平实施。引用美国医院调查指出AI采纳不均和偏倚评估不足，但未对具体临床任务开展算法公平性实证分析。
- [Evidence of limited biases in probed language-based assessments.](https://europepmc.org/article/MED/43002526) · 待核验 · `p-c3083ca58bc9a9905bcc`
  该研究评估开放式心理健康自述经大语言模型嵌入加岭回归预测抑郁/焦虑严重度的公平性：1260名参与者的评估误差与性别、年龄、教育、就业、收入等社会人口学变量及语言特征关联有限，但症状越重评估偏差越大；对训练数据下采样可消除该偏差。
- [Is it possible to vaccinate AI against bias? An exploratory study in epilepsy.](https://europepmc.org/article/MED/43014131) · 待核验 · `p-ec7c0f5cb541d6dacee9`
  该探索性概念验证研究在癫痫临床情景中测试提示指令能否减少六个大语言模型的诊断/治疗准确率差距。富裕与弱势复合画像在性别和社会描述上共同变化；结果按原评分规则重新计算，提示后汇总差距下降，但作者指出不能隔离社会经济偏倚或证明临床有效的去偏干预。
- [Large Language Models' Simulation of Patient Comprehension of Discharge Summaries: Multimodel Evaluation Study.](https://pubmed.ncbi.nlm.nih.gov/42912964/) · 待核验 · `p-ee8b2a7189a3d8b4887f`
  该研究用4个当代LLM按教育、性别和医疗使用生成患者人设，模拟对出院小结的理解回答，并以模态绝对误差和序数距离比较其与99名人类参与者的对齐，考察各亚组公平性及思维链敏感性。
- [Racial Composition and Single-Input Dominance in the First Hospice Special Focus Program Cohort.](https://pubmed.ncbi.nlm.nih.gov/42895138/) · 相关，待核实是否纳入 · `p-e2c8854d96deaa4b99ad`
  该研究审计美国临终关怀特别关注项目（SFP）的复合质量算法：对2024年11月CMS目录中7115家临终关怀机构做横断面分析，用逻辑回归检验入选与机构规模、患者种族构成及独立质量指标（HVLDL）的关系，并对50家入选机构的复合评分做标准化输入分解。结果显示入选与黑人患者比例显著相关，且48/50家入选机构的评分恶化主要由单一输入驱动，提示算法可能不成比例地影响服务黑人患者的机构。
- [Machine Learning Validation Pipelines: From Tabular Benchmarking to Conformal Calibration and Execution-Grounded Agentic Testing](https://europepmc.org/article/PPR/PPR1370333) · 机器建议排除，待抽查 · `p-280deca54061942c17e6`
  提出五层机器学习验证流程，涵盖基准测试与泄漏防护、可解释性审计、共形校准、部署前门控及执行级多智能体验证，并以金融ML元分析和临床分诊等高风险场景说明失败模式。
- [Advancing Equitable and Trustworthy AI in Breast Cancer Detection Through Interpretable Deep Learning](https://europepmc.org/article/PPR/PPR1361567) · 待核验 · `p-6c2d4e6ce2f485ff83ff`
  该文为PRISMA系统综述，聚焦乳腺癌钼靶筛查中深度学习模型的公平性与人口学偏倚，提出解释图“reasoning bias”及多指标热图偏倚评估框架，并指出种族、年龄和乳腺密度交叉亚组证据不足。
- [Trustworthiness Evaluation of Medical Vision-Language Models: A Scoping Review and a Proposed Minimum Evaluation Checklist.](https://europepmc.org/article/MED/42933376) · 机器建议排除，待抽查 · `p-8133fbf008b01c6049b4`
  该范围综述系统梳理医学视觉-语言模型的可信度评估实践，提出八项最低可信度评估清单（MiTEC）并做回溯打分：稳健性11/29、幻觉7/29，而公平性与可解释性各仅4/29（13.8%），亚组分析、形式化校准与图像依赖对照均少见。
- [Explainable and Trustworthy AI for Diabetic Retinopathy: A Systematic Review and Diagnostic Meta-analysis](https://europepmc.org/article/PPR/PPR1350140) · 待核验 · `p-9830d51967755c683818`
  该文为糖尿病视网膜病变（DR）可解释与可信AI的系统综述和诊断Meta分析，汇总10项研究的诊断性能，并讨论可解释性、校准、不确定性、泛化、公平性、隐私和部署证据。
- [Beyond AUROC: External Validation, Calibration, and Explainability of Machine Learning Models for 30-Day Hospital Readmission Using Electronic Health Records—A Rapid Systematic Review](https://europepmc.org/article/PPR/PPR1346087) · 待核验 · `p-fb55a16fedc7a47752c1`
  该快速系统综述评估EHR 30天再入院预测模型的验证、校准、可解释性与亚组公平性报告情况，发现公平性分析仅占4.5%，并提出超越AUROC的最小评估集。
- [Exploring Racial Bias in Rating Facial Attractiveness Among Artificial Intelligence Platforms.](https://europepmc.org/article/MED/42906598) · 待核验 · `p-2511def0b4e92255227b`
  研究用五个商业AI面部分吸引力评分平台，对Black、White、Latino、Asian四组各30张标准化女性图像打分，发现White组平均分最高(8.18)、Black组最低(6.91)，组间及平台间差异显著，提示评分可能偏向Eurocentric面部特征。
- [Evaluating four consumer artificial intelligence chatbots on smartphone dermatology images: diagnostic accuracy, the contribution of clinical context, and skin-tone equity](https://europepmc.org/article/PPR/PPR1365867) · 待核验 · `p-79ee704c380a3242315c`
  该研究在3,005例SCIN智能手机皮肤图像上评估四款消费级AI聊天机器人，比较单图、多图、图像加临床背景及纯文本四种条件下的诊断准确率，并按Fitzpatrick肤色分层检验公平性，发现表现最好的模型存在浅色与深色皮肤间的准确率差异。
- [Continual learning in oncology AI: A framework for safe clinical translation.](https://pubmed.ncbi.nlm.nih.gov/43063946/) · 机器建议排除，待抽查 · `p-28adaf06b29241ce8db3`
  该文综述肿瘤学AI中的持续学习方法，讨论灾难性遗忘、校准与重训等转化障碍，并提出包含亚组安全、校准稳定性等六项安全转化标准。公平性仅作为持续学习临床转化的一项风险被提及。
- [Prognostic Factors for Survival in ICI-Treated NSCLC: An Umbrella Review of Evidence Certainty and Clinical Relevance.](https://europepmc.org/article/MED/43033040) · 待分析／证据不足 · `p-85640a44163a7e495a79`
- [Attitudes Towards Risks and Benefits of Using Generative Artificial Intelligence (GenAI) for African American Family Members of a Person with Dementia.](https://europepmc.org/article/MED/43041993) · 待分析／证据不足 · `p-a3bb94685f1bec630254`
- [Predicting PANSS symptoms in schizophrenia spectrum disorders using speech only: an international, multi-centre, computational secondary analysis across multiple languages.](https://pubmed.ncbi.nlm.nih.gov/42991136/) · 待核验 · `p-dfd76ee4553e36909d88`
  该国际多中心计算二次分析汇总10国453例精神分裂症谱系障碍患者的语音，将录音切分为6664段，比较16种算法预测8个PANSS条目，并按年龄、性别、教育程度和症状严重度做偏倚检查。预训练多语言嵌入表现最佳；除男性N4准确率较低外，未见年龄、性别或教育偏倚，但高症状严重度下性能下降。
- [Orbital morphometry on computed tomography for sex estimation: A systematic review and meta-analysis.](https://pubmed.ncbi.nlm.nih.gov/43057131/) · 待分析／证据不足 · `p-f0405d6bf007e5f2b22c`
- [Smoking and dementia risk: an updated systematic review and meta-analysis of 61 prospective cohort studies and implications for tobacco control.](https://pubmed.ncbi.nlm.nih.gov/43034842/) · 待分析／证据不足 · `p-2308c78840b3881bc14d`
- [Machine learning-based risk prediction of hepatocellular carcinoma in patients with chronic hepatitis B: current evidence and future directions.](https://europepmc.org/article/MED/43064890) · 待分析／证据不足 · `p-b7ac23993de63dc9a3e9`
- [Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706) · 待分析／证据不足 · `p-220173ecbe71aeffc6a2`
- [Data-centric, robust, and explainable multimodal deep learning for clinical decision support: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42667902/) · 待分析／证据不足 · `p-2dc7893202614a28f741`
- [Application of geospatial technologies in mental health research: A scoping review of progress and future directions.](https://europepmc.org/article/MED/43042965) · 待分析／证据不足 · `p-496be92504999e54331b`
- [In-context learning for medical artificial intelligence.](https://pubmed.ncbi.nlm.nih.gov/43008739/) · 待分析／证据不足 · `p-62e5a416316a8b47bef5`
- [Bias and equity in large language model-based applications for health care: a scoping review.](https://europepmc.org/article/MED/43052083) · 待分析／证据不足 · `p-aca067eb1061051f9b86`
- [Intelligent immunotherapy: AI-driven optimization of CAR-T therapy in hematologic malignancies.](https://pubmed.ncbi.nlm.nih.gov/42904142/) · 待分析／证据不足 · `p-d3566a29f4f70f84cac4`
- [Potential and pitfalls of artificial intelligence to address disparities in epilepsy.](https://europepmc.org/article/MED/43064818) · 待分析／证据不足 · `p-801228119b6cf272fa53`

## In-processing Mitigation

- [FSD-Net: A Unified Skin-Tone-Aware Framework for Fair Skin Lesion Segmentation and Classification](https://europepmc.org/article/PPR/PPR1370450) · 待核验 · `p-3daf0c4282bca4f685cf`
  FSD-Net在皮肤病变分割与分类两个阶段同时考虑肤色公平性：用连续肤色评分经FiLM调制ViT-B/16分割骨干，并用分割引导的ROI训练Swin-V2-Tiny分类器。在ISIC-2017/2018、PH2及HAM10000上报告Dice、准确率和Equalized Opportunity差距，并辅以消融、Bootstrap置信区间和McNemar检验。
- [MelanoFusion: An Explainable and Uncertainty-Aware Hybrid CNN–Transformer Framework for Dermoscopic Melanoma Detection](https://europepmc.org/article/PPR/PPR1370178) · 相关，待核实是否纳入 · `p-fd455cc2a36673f35d55`
  提出MelanoFusion混合CNN–Transformer框架用于皮肤镜黑色素瘤检测，结合可解释性、不确定性估计与公平导向表征学习；在HAM10000、ISIC 2018和PH²上评估，报告年龄组敏感性差异但性别无显著差异，并提示需外部验证。
- [Multiview Integration for Robust Echocardiographic Embeddings: Accessible AI for Clinical Practice.](https://pubmed.ncbi.nlm.nih.gov/43050803/) · 待核验 · `p-0aed599c7fa1f8e12a36`
  开发基于Transformer的多视角超声心动图编码器，将多段视频整合为研究级向量嵌入，并在21项二分类任务上评估；同时用对抗学习降低性别和种族捷径依赖，报告较强对抗权重下可预测性下降但临床性能受损。
- [When multi-institutional dataset aggregation masks shortcut-like behavior in Foundation Models for medical imaging.](https://pubmed.ncbi.nlm.nih.gov/42641372/) · 待核验 · `p-b450c1e3be8d7e77257b`
  该研究以乳腺X线摄影分类为任务，将预训练图像编码器（基础模型）作为特征提取器，在十个采集流程、人群与地区各异的队列上训练分类器，发现聚合异质数据会带来依赖数据集的失效模式，误差率、置信度与校准度在数据集间差异明显。表示层面可轻易恢复数据集身份而临床标签可分性较低，提示捷径式行为；测序向量分解显示任务信号多位于数据集对齐子空间。数据集对抗训练、最差组优化与平衡微调可缓解部分数据集聚差异，但常以总体性能下降为代价；探索性元数据分析还发现年龄相关的标签依赖性概率偏移。
- [Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate](https://arxiv.org/abs/2611.22904) · 建议纳入，待审核 · `p-62eefc78443f96579d03`
  该文审计小型临床联邦学习联盟中拜占庭鲁棒聚合的公平性，在3个FLamby数据集上比较8种聚合规则并运行54,214次实验。发现仅按客户端数量判断有效性会漏掉数据份额独裁；加权中位数、GeoMed与CC在单中心占比过半时崩溃；留出对照把性能下降分解为诚实数据损失与真实攻击损害；无权重规则会惩罚更新最异常的医院。
- [Ethical guidelines for deploying artificial intelligence applications in the pathology field: Lessons learned from a prospective framework in a large tertiary care academic medical center.](https://pubmed.ncbi.nlm.nih.gov/42761742/) · 机器建议排除，待抽查 · `p-a9324f28d8acd70d333c`
  文章讨论病理学AI中的年龄、性别、种族和族裔代表性偏差，提出覆盖治理、预处理、处理、部署和监测的伦理指南框架，强调公平使用与持续监测。
- [C3E-RRG:Confounder-Aware Causal Evidence Coupling and Evolution for Chest X-Ray Report Generation.](https://europepmc.org/article/MED/42970651) · 机器建议排除，待抽查 · `p-d62b2748ad6ed04dbe11`
  提出C3E-RRG，在胸片报告生成中融合语言先验与疾病共现以构建混杂变量，并通过跨模态证据一致耦合和双向因果演化抑制模板与共现引起的虚假相关；在IU-XRay和MIMIC-CXR上验证。
- [In-context learning for medical artificial intelligence.](https://pubmed.ncbi.nlm.nih.gov/43008739/) · 待分析／证据不足 · `p-62e5a416316a8b47bef5`
- [Artificial Intelligence in Thoracic Pathology and Biomarker Assessment: An IASLC Pathology Committee Review.](https://europepmc.org/article/MED/43064238) · 待分析／证据不足 · `p-aa1d2c08ab2918b9678a`

## Mitigation with Unverified Stage

- [Applications of Fairness Training in Artificial Intelligence to Ophthalmic Disease Diagnosis using External Eye Photographs](https://europepmc.org/article/PPR/PPR1363752) · 待核验 · `p-21b44eb38a70c944169c`
  摘要报告利用40,687张外部眼照片开发深度学习与视觉语言模型，对威胁视力DR、晚期AMD和青光眼做二分类，并以ES-AUC评估性别、种族和族裔公平性，比较五种公平训练策略。报告称公平训练部分缩小差异并提升VTDR/AMD的AUC，但模型尚不适合临床部署。
- [A Multi-Model Framework for Explainable Sepsis Mortality Prediction With Dynamic Fairness and Drift Analysis.](https://europepmc.org/article/MED/43056270) · 待核验 · `p-3f9a2ee2dec669d59e15`
  该研究在MIMIC-IV上构建脓毒症死亡预测多模型框架，将公平性重新定义为动态生命周期属性，在15轮再训练与16个交叉子群中监测TPR、FPR、FOR差距，并开展eICU跨机构公平性审计与SHAP稳定性分析。
- [Is it possible to vaccinate AI against bias? An exploratory study in epilepsy.](https://europepmc.org/article/MED/43014131) · 待核验 · `p-ec7c0f5cb541d6dacee9`
  该探索性概念验证研究在癫痫临床情景中测试提示指令能否减少六个大语言模型的诊断/治疗准确率差距。富裕与弱势复合画像在性别和社会描述上共同变化；结果按原评分规则重新计算，提示后汇总差距下降，但作者指出不能隔离社会经济偏倚或证明临床有效的去偏干预。

## Post-processing Mitigation

- [Let Samples Sing in Chorus: Mitigating Spurious Correlations via Cross-view Consensus](https://arxiv.org/abs/2611.22668) · 建议纳入，待审核 · `p-67ee09e54a621a213502`
  提出CHORD多视图去偏框架，通过多个表征视图提出类内分区，并在目标表征空间验证反转样本，无需组标注即可重训分类头；在CheXpert胸片二分类上报告WGA 71.43%，高于ERM的31.21%。
- [Ethical guidelines for deploying artificial intelligence applications in the pathology field: Lessons learned from a prospective framework in a large tertiary care academic medical center.](https://pubmed.ncbi.nlm.nih.gov/42761742/) · 机器建议排除，待抽查 · `p-a9324f28d8acd70d333c`
  文章讨论病理学AI中的年龄、性别、种族和族裔代表性偏差，提出覆盖治理、预处理、处理、部署和监测的伦理指南框架，强调公平使用与持续监测。
- [Machine Learning Validation Pipelines: From Tabular Benchmarking to Conformal Calibration and Execution-Grounded Agentic Testing](https://europepmc.org/article/PPR/PPR1370333) · 机器建议排除，待抽查 · `p-280deca54061942c17e6`
  提出五层机器学习验证流程，涵盖基准测试与泄漏防护、可解释性审计、共形校准、部署前门控及执行级多智能体验证，并以金融ML元分析和临床分诊等高风险场景说明失败模式。

## Pre-processing Mitigation

- [Reliable Skin-Tone Fairness in Dermatology AI: From Lesion-Level Leakage to Tone-Adaptive Learning](https://europepmc.org/article/PPR/PPR1345750) · 待核验 · `p-53d198d32447f559a258`
  提出面向皮肤镜与临床图像的色调自适应预处理流程，并建立按病灶分组、类别分层的评估协议，量化病灶级泄漏和肤色代理指标问题；在三个基准上报告深色皮肤敏感度提升，并发布泄漏审计工具。
- [Governed Auditing of Hidden Failure Slice Discovery in Emergency Department Admission Models Agnostic to Sensitive Attributes](https://europepmc.org/article/PPR/PPR1363950) · 待核验 · `p-802f852b1e8f331fe15d`
  提出BASiC与ASAP，在急诊入院预测中利用临床规则和折外误差信号发现隐藏失败切片，并尝试样本加权修复。研究在Kaggle、RIPAS和NHAMCS数据上评估多种模型，发现切片发现较可靠，但修复未带来一致改善，且不建立人口统计学公平或临床有效性。
- [Improving Target-Adverse Event Association Prediction via Inverse Node Frequency Transformation to Mitigate Knowledge Graph Topological Bias](https://europepmc.org/article/PPR/PPR1373652) · 待核验 · `p-3f6acf4e270b22ab1a5d`
  提出逆节点频率（INF）归一化方法，用于缓解生物医学知识图中因节点度数分布不均导致的拓扑偏倚（度偏倚），并以元路径特征为基础预测靶点-不良事件关联。结果显示INF提升了低度数靶点的召回率，并在外部未用于建模的关联集上优于两种基准，属知识图谱偏倚缓解类方法研究。
- [Self-report label bias in machine learning screening for undiagnosed diabetes: development, validation and offline on-device deployment of an interpretable HbA1c-anchored tool.](https://pubmed.ncbi.nlm.nih.gov/43033525/) · 待核验 · `p-8e1089bbb872533b5f51`
  该研究基于NHANES与BRFSS数据，量化自报糖尿病诊断标签如何改变机器学习筛查模型优先识别人群的方式，显示自报标签部分编码了就医可及性；用正-未标记学习校正标签，并开发以HbA1c为锚点的可解释筛查工具，在相同转诊率下与指南规则比较敏感度并做离线部署验证。
- [Ethical guidelines for deploying artificial intelligence applications in the pathology field: Lessons learned from a prospective framework in a large tertiary care academic medical center.](https://pubmed.ncbi.nlm.nih.gov/42761742/) · 机器建议排除，待抽查 · `p-a9324f28d8acd70d333c`
  文章讨论病理学AI中的年龄、性别、种族和族裔代表性偏差，提出覆盖治理、预处理、处理、部署和监测的伦理指南框架，强调公平使用与持续监测。
- [Evidence of limited biases in probed language-based assessments.](https://europepmc.org/article/MED/43002526) · 待核验 · `p-c3083ca58bc9a9905bcc`
  该研究评估开放式心理健康自述经大语言模型嵌入加岭回归预测抑郁/焦虑严重度的公平性：1260名参与者的评估误差与性别、年龄、教育、就业、收入等社会人口学变量及语言特征关联有限，但症状越重评估偏差越大；对训练数据下采样可消除该偏差。
- [Orbital morphometry on computed tomography for sex estimation: A systematic review and meta-analysis.](https://pubmed.ncbi.nlm.nih.gov/43057131/) · 待分析／证据不足 · `p-f0405d6bf007e5f2b22c`
- [Smoking and dementia risk: an updated systematic review and meta-analysis of 61 prospective cohort studies and implications for tobacco control.](https://pubmed.ncbi.nlm.nih.gov/43034842/) · 待分析／证据不足 · `p-2308c78840b3881bc14d`
- [Artificial Intelligence in Coronary Artery Disease: From Detection to Precision Management.](https://europepmc.org/article/MED/43032706) · 待分析／证据不足 · `p-220173ecbe71aeffc6a2`
- [Data-centric, robust, and explainable multimodal deep learning for clinical decision support: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42667902/) · 待分析／证据不足 · `p-2dc7893202614a28f741`
- [In-context learning for medical artificial intelligence.](https://pubmed.ncbi.nlm.nih.gov/43008739/) · 待分析／证据不足 · `p-62e5a416316a8b47bef5`
- [Intelligent immunotherapy: AI-driven optimization of CAR-T therapy in hematologic malignancies.](https://pubmed.ncbi.nlm.nih.gov/42904142/) · 待分析／证据不足 · `p-d3566a29f4f70f84cac4`
- [Artificial Intelligence in Thoracic Pathology and Biomarker Assessment: An IASLC Pathology Committee Review.](https://europepmc.org/article/MED/43064238) · 待分析／证据不足 · `p-aa1d2c08ab2918b9678a`
- [Application of Artificial Intelligence (AI) in cancer symptom management for adult cancer survivors: a scoping review.](https://pubmed.ncbi.nlm.nih.gov/42603423/) · 待分析／证据不足 · `p-622c2ee72af5786411dd`

## 待分类

- [Synthetic tabular healthcare data in health informatics: fixed-size substitution and incremental-value controls for predictive utility Application Paper](https://europepmc.org/article/PPR/PPR1358040) · 机器建议排除，待抽查 · `p-8fc7d8cd62a109859e45`
  该研究构建合成表格医疗数据基准，在固定训练规模与增量价值两种设置下控制样本量和重复预测特征泄漏，评估高斯Copula、CTGAN、TVAE及三种分类器在糖尿病相关数据集上的预测效用，发现合成数据无普遍增益，并明确不涉及公平性结论。
- [DRLCI: Dual-view Representation Learning Framework for Predicting Drug-Gene Interactions via Causal Intervention.](https://europepmc.org/article/MED/43013439) · 机器建议排除，待抽查 · `p-009e12912fe734931786`
  提出DRLCI双视图表示学习框架，用于预测药物-基因相互作用；通过关系感知图卷积、因果干预掩码和因果去偏对比损失抑制混淆因素，并融合医学先验文本，在DrugBank和DGIdb基准上报告最优性能。
- [DINOv3-SAM: Fusing Semantic and Anatomical Foundation Models for Robust Medical Image Classification.](https://europepmc.org/article/MED/42972189) · 机器建议排除，待抽查 · `p-025d4680a20363b0f28f`
  提出DINOv3-SAM双编码器框架，将自监督DINOv3的全局语义特征与冻结的SAM解剖感知特征空间对齐，经CBAM注意力精炼后用于儿科肺炎、心脏增大、RSNA肺炎、COVID-19胸片及皮肤病变分类，报告准确率与AUC提升并强调对数据集偏倚和跨域漂移的鲁棒性。
- [Supporting Ergonomic Risk Assessment: An AI-driven Approach for Action Recognition Using Standard Video Recordings.](https://europepmc.org/article/MED/42925046) · 机器建议排除，待抽查 · `p-0e20310c94fa66bd35f7`
  提出并评估一种基于2D姿态与图卷积网络的视频动作识别方法，用于自动化OCRA工效学风险评估中的技术动作识别与计数；在37个制造场景数据上比较ST-GCN与2S-AGCN，准确率约60%。
- [A preregistered simulation study provided evidence on the appropriate use of data-driven variable selection in descriptive multivariable regression modeling.](https://pubmed.ncbi.nlm.nih.gov/42486194/) · 机器建议排除，待抽查 · `p-2076a6e307f6e08acb19`
  该预注册模拟研究比较流行病学描述性回归中的数据驱动变量选择方法（后退法与Lasso），评估变量选择率、模型选择率及回归系数偏倚，并提供方法选择决策框架；未涉及医学算法公平性、群体差异或公平性缓解。
- [Computational Nutrition 2.0: From Static Models to Closed-Loop Agentic Systems for Personalized Nutrition.](https://pubmed.ncbi.nlm.nih.gov/42805435/) · 机器建议排除，待抽查 · `p-220234c949e46cfa70a4`
  该文为观点性文章，提出计算营养学2.0，主张以AI智能体推动个性化营养从静态模型走向闭环干预，覆盖代谢反应预测、营养因果推断、饮食相关疾病风险监测与营养政策模拟四个方向。
- [Regional and national variation in donor and recipient characteristics, transplant practice, and outcomes after liver transplantation (the IMPROVEMENT collaborative): a multicentre cohort study.](https://europepmc.org/article/MED/42999582) · 机器建议排除，待抽查 · `p-31cf3e898e1f39daf9dc`
  IMPROVEMENT 多中心队列研究汇总 61 个中心、83 个病例序列、5218 例肝移植患者，覆盖五大洲，采用四步分析（世界地图、雷达图、笛卡尔图、混合效应预后模型）刻画供受体风险与风险缓解策略的区域差异，并建立 90 天、1 年、2 年死亡与并发症的预后算法，指出受者因素、冷缺血时间与中心体量是主要决定因素。
- [A Distributionally Robust Framework for Safe and Generalizable Utilization of Surrogate Markers](https://arxiv.org/abs/2611.18970) · 机器建议排除，待抽查 · `p-410a2a1c61be26ff729a`
  提出分布鲁棒框架评估替代终点：将跨治疗臂反事实依赖视为部分识别，通过最大化最坏情况解释方差学习替代标志物变换，并结合迁移学习与去偏机器学习处理协变量偏移。用模拟和CKD试验评估18个月GFR变化对两年GFR变化的替代性。
- [ARBITER: retrieval-augmented generation for automated PROBAST+AI risk-of-bias assessment of HIV, HBV and HCV prediction models: a proof-of-concept validation study](https://europepmc.org/article/PPR/PPR1351930) · 机器建议排除，待抽查 · `p-48b9e5d40beb02d005ae`
  ARBITER 是一个基于检索增强生成（RAG，使用 Gemini 2.5 Pro）的工具，用于自动化完成 PROBAST+AI 偏倚风险评估：识别研究、区分建模与评价路径，并为每个信号问题给出分类判断及原文证据。在 10 项 HIV/HBV/HCV 预测模型研究上进行概念验证，与 Claude Sonnet 4.6 及人类统计专家对比，三者与专家共识均达到较高一致性（κ≈0.70–0.72）。
- [Development and internal validation of a CSF-free machine-learning model to distinguish immune checkpoint inhibitor-induced encephalitis from HSV-1 and anti-LGI1 encephalitis](https://europepmc.org/article/PPR/PPR1354554) · 机器建议排除，待抽查 · `p-4d243e183a986cc09be8`
  该研究基于51例公开回顾性数据，构建并内部验证不含脑脊液特征的随机森林模型，用于区分免疫检查点抑制剂相关脑炎与HSV-1及抗LGI1脑炎，比较含或不含CSF、MRI特征时的判别力、校准与决策曲线表现，全程未涉及算法公平性分析。
- [Development and validation of early warning scores predicting 24 h mortality addressing intercurrent medical interventions in Denmark: a multicentre retrospective cohort study of 2·08 million hospital encounters.](https://pubmed.ncbi.nlm.nih.gov/42988715/) · 机器建议排除，待抽查 · `p-515324d349beb4aea4b7`
  摘要比较NEWS、简化NEWS、DEWS与XGB-EWS对24小时死亡的预测，使用倾向评分处理干预偏倚，并以净获益、AUC和校准评估，报告不同风险亚组的效用异质性。
- [Antibiotic Choice for Community-Acquired Pneumonia in Children With Medical Complexity.](https://europepmc.org/article/MED/42838530) · 机器建议排除，待抽查 · `p-72d2098ba0d9a6374d16`
  该队列研究采用目标试验模拟与逆概率加权，比较儿童医学复杂（CMC）非重症社区获得性肺炎初始广谱与窄谱抗生素的结局。847例次住院中，广谱抗生素在至出院时间、进展为重症及30天再就诊方面与窄谱无显著差异，支持对多数CMC使用氨苄青霉素类。
- [A multimodal CT-based machine-learning model for differentiating pulmonary sarcomatoid carcinoma from conventional non-small cell lung cancer: an internally validated study](https://europepmc.org/article/PPR/PPR1348078) · 机器建议排除，待抽查 · `p-7d6abfecd7636ea459d5`
  该研究基于三个中心的397例患者，比较临床-CT语义特征、影像组学与深度学习特征构建的六种模型，用于病理确诊前区分肺肉瘤样癌（PSC）与常规非小细胞肺癌；全融合模型AUROC 0.890，并分析采集参数异质性带来的残余混杂。
- [Mediterranean Diet, Physical Activity, and Sleep in Endometriosis: An Age-Comparable Case-Control Study with Exploratory Machine Learning Discrimination.](https://pubmed.ncbi.nlm.nih.gov/43030256/) · 机器建议排除，待抽查 · `p-871ab9f4cc09b5f81ad5`
  该研究为病例对照研究（177名女性，77例自报并经手术确诊的子宫内膜症），比较地中海饮食、体力活动、睡眠与症状指标，并用三种机器学习算法做交叉验证判别分析；最佳AUC-ROC为0.933，但限制于前置因素与饮食变量时仅0.67-0.73，作者认为判别主要反映并发症状而非营养因素。
- [Anthropometric and Psychological Variables Associated with Body Mass Index: A Sex-Stratified Evaluation of Students from a Romanian University.](https://pubmed.ncbi.nlm.nih.gov/43028626/) · 机器建议排除，待抽查 · `p-923f4ac4a8b6eae7cf82`
  该横断面研究在445名大学生中分析颈围、BAI、指长比及心理变量与BMI分类的关联，并按性别分层建立回归与探索性ROC。颈围和BAI为主要相关指标，指长比具初步分类效用，心理指标无独立关联；未涉及算法公平性评估。
- [Learning from Maternal Mortality Confidential Enquiries: Sociodemographic Determinants Relevant to Equitable Guideline Development](https://europepmc.org/article/PPR/PPR1359271) · 机器建议排除，待抽查 · `p-97c54bcea3ab95e0c708`
  该综述比较了16个高收入国家孕产妇死亡保密调查报告中社会人口学决定因素的报告差异，并据此制定国别公平清单以支持女性健康指南的制定与评估。全文未涉及任何AI/ML算法或算法公平性评估。
- [Association between patients’ knee posture and patient satisfaction in primary care consultations](https://europepmc.org/article/PPR/PPR1365698) · 机器建议排除，待抽查 · `p-b1c2ba955b21e73bf64e`
  研究探讨门诊咨询结束前30秒患者膝关节姿势与咨询后满意度的关联，203例患者中中立姿势组满意度高于伸展姿势组；属探索性观察研究，未涉及算法或算法公平性。
- [AI-Based Prediction of Total Porosity Volume Fraction from 3D CT Volumes: A Volumetric Regression Approach](https://europepmc.org/article/PPR/PPR1370350) · 机器建议排除，待抽查 · `p-b34d58a13643bfcc986f`
  提出用带全局平均池化的3D CNN从含噪3D CT体积直接回归总孔隙体积分数，绕过体素分割；与Otsu阈值和随机森林基线比较，并分析合成数据中的捷径学习。
- [A deep learning model for detection and staging of osteonecrosis of the femoral head on x-ray images: a retrospective, large-scale, multicentre study in China.](https://europepmc.org/article/MED/42934014) · 机器建议排除，待抽查 · `p-b93a39c7c0676b99e9b3`
  开发并多中心验证基于YOLOv8的X线髋部检测与分期模型OsteoAID，比较其与放射科及骨科医生的诊断表现，并以MRI为参照。
- [Explainable Classification Models for Identifying Elevated Gastrointestinal Symptom Burden in Honduran Communities: A Cross-Sectional Study.](https://pubmed.ncbi.nlm.nih.gov/43028313/) · 相关，待核实是否纳入 · `p-c4d939a39c87bfe230c4`
  在洪都拉斯5省85个社区1838名12–49岁居民中，评估可解释的人口学与生活方式模型能否识别同时存在多种胃肠道症状负担；加入既往消化系统诊断后AUROC由0.663升至0.726，逻辑回归与复杂机器学习表现相当，并报告校准、决策曲线和亚组表现。
- [Memory-guided mutual information optimization in retinal imaging for early stroke detection and subtyping.](https://europepmc.org/article/MED/43014078) · 机器建议排除，待抽查 · `p-e325d3be42451c51b6cb`
  提出 RetCEVD 框架，利用无创视网膜 OCTA 图像进行缺血性脑血管病（ICVD）辅助检测、病因亚型分型及症状状态分类，核心为记忆引导的互信息优化策略，在多中心 24,438 张图像上完成内部与外部验证并报告 AUC。
- [Multiparametric 0.4-T low-field MRI mapping for metabolic dysfunction-associated steatotic liver disease in rats.](https://europepmc.org/article/MED/43034251) · 机器建议排除，待抽查 · `p-e7d4ce6f3482649fcced`
  研究在90只MASLD大鼠中比较0.4-T MRI的T1、FcT1、T2、T2*和PDFF与全切片数字病理，并评估深度学习重建AIRS对T1定量的影响；结果显示各指标与脂肪、炎症、纤维化呈部分阶段依赖相关，AIRS可改变T1绝对值。
- [A Dual-Criterion Variable Inclusion Strategy for Improved Confounder Inclusion in Small-Sample Trauma Cohorts: An Empirical Methodological Study](https://europepmc.org/article/PPR/PPR1348111) · 机器建议排除，待抽查 · `p-f352228a5c9bd18d0291`
  研究在88例脑挫裂伤减压术后患者中提出双标准变量纳入策略，以改善小样本创伤队列的混杂因素纳入，比较ridge回归、随机森林及模型校准，发现该策略减少单阈值筛查的遗漏偏倚并影响危险因素识别。
- [Simulation-Based Development, Stress Testing, and External Physiological Benchmarking of a DKA Early-Warning Framework Intended for Future Nurse-Facing Evaluation.](https://pubmed.ncbi.nlm.nih.gov/43028810/) · 机器建议排除，待抽查 · `p-fc980d34ff004464f5b8`
  该研究用两万条合成15小时DKA病程数据，对比验证冻结的BHB+趋势规则与XGBoost模型的灵敏度与误报率，并通过表型匹配的反事实生命体征、阈值网格和校准分析检验模拟器捷径，另用公开IOBP2数据做生理学外部基准，发现葡萄糖分布存在显著不匹配。
- [Hierarchical detection of neonatal brain pathologies using a two-stage deep learning framework from magnetic resonance imaging.](https://pubmed.ncbi.nlm.nih.gov/43031676/) · 机器建议排除，待抽查 · `p-05c60193f5811117e901`
  该研究提出两阶段分层深度学习流程，基于新生儿T1/T2加权脑MRI，先用脑龄差筛查髓鞘化延迟，再用3-D ResNet-18进行正常、HIE与脑积水三分类，并报告阶段2 AUC为0.919。
- [Responsible Artificial Intelligence: Guiding Principles for Orthopaedic Surgery.](https://europepmc.org/article/MED/43037611) · 机器建议排除，待抽查 · `p-11142b1729015cc61ea3`
  本文为骨科领域负责任人工智能的指导原则类评论，提出透明与可解释、临床可靠性与价值导向、与人类价值对齐、算法公平、公平照护问责、临床专家监督六项原则，主张在肌肉骨骼照护中安全、公平地采用AI。全文仅在原则层面提及公平，未针对具体疾病或任务给出亚组指标、偏差机制或评估框架。
- [Amino acid-based formula and &lt;i&gt;Clostridioides difficile&lt;/i&gt;-associated disease in infants: concerns regarding causal interpretation.](https://europepmc.org/article/MED/43018394) · 机器建议排除，待抽查 · `p-1e7d50a645f4a3f54c29`
  本文评论氨基酸配方喂养与婴儿艰难梭菌相关疾病关联研究，指出因果推断的混杂、事件数不足等方法学问题，并建议前瞻性研究设计；不涉及AI/ML或算法公平性。
- [Healthcare providers' use and acceptance of translation technologies in multilingual healthcare settings: a cross-sectional study.](https://pubmed.ncbi.nlm.nih.gov/42919266/) · 机器建议排除，待抽查 · `p-2f7dce3877d44026419f`
  对443名医疗及心理社会服务提供者开展横断面调查，基于技术接受模型分析翻译技术使用与行为意向，发现感知有用性关联最强，并报告准确性、隐私及治理顾虑。
- [Acute Stroke Classification Using Asymmetric Data Standardization and Orthogonal-Focal Loss Optimized CNN-ViT Cross-Attention Fusion: A Multicenter External Validation Study](https://arxiv.org/abs/2610.34529) · 机器建议排除，待抽查 · `p-57d9615bd4c80bff0bd7`
  提出一种用于急性卒中分型的CNN-ViT交叉注意力CAD系统，结合非对称预处理与正交焦点损失，并进行多中心外部验证；内部F1为95.48%，外部降至58–62%，报告硬件噪声相关域偏移及缺血性卒中敏感性偏低。
- [Association between biological age acceleration and the risk of aortic valve stenosis: An observational epidemiologic and Mendelian randomization study.](https://pubmed.ncbi.nlm.nih.gov/42998401/) · 机器建议排除，待抽查 · `p-92a449ec5369eaed3e6f`
  研究基于RED-CARPET与ARIC队列及孟德尔随机化，评估KDM-BA和PhenoAge计算的生物学年龄加速与主动脉瓣狭窄风险的关联，发现BAA与AVS风险及严重程度相关，并提示KDM-BA加速可能具因果关联。
- [Association of Immunomodulatory Treatment with Long-Term Visual Outcomes in Behçet Uveitis: A Single-Center Retrospective Study.](https://europepmc.org/article/MED/43001002) · 机器建议排除，待抽查 · `p-c2c763dae41b68b833ad`
  单中心回顾性研究描述Behçet病相关葡萄膜炎的临床特征与治疗模式，并探索免疫调节治疗与长期视力结局的关联；未涉及人工智能算法或公平性分析。
- [Latent profiles of artificial intelligence ethical awareness and their association with professional identity among nursing interns: A multicentre cross-sectional study](https://europepmc.org/article/PPR/PPR1369288) · 机器建议排除，待抽查 · `p-4e22d89fc1a2a51893ed`
  该研究对中国12家医院的550名护理实习生开展多中心横断面调查，采用潜在剖面分析基于AI伦理意识六个维度识别出三种意识类型，并比较其专业认同差异及与教育水平、AI熟悉度等因素的关联。
- [Advancing FAIR sharing for epidemiological, clinical and public health study data: the German National Research Data Infrastructure (NFDI4Health).](https://europepmc.org/article/MED/43037923) · 机器建议排除，待抽查 · `p-85c646041c7ede02228d`
  该文介绍德国国家研究数据基础设施NFDI4Health的建设成果：通过健康研究枢纽、本地数据枢纽、FDPG门户、可互操作元数据模式、匿名化与合成数据工具、联邦分析框架等，提升流行病学、临床与公共卫生研究数据的FAIR（可发现、可访问、可互操作、可复用）共享水平。
- [A Relational Framework for Artificial Intelligence-Assisted Shared Decision Making.](https://europepmc.org/article/MED/43028666) · 机器建议排除，待抽查 · `p-0c8552b1982b0a8ff7f6`
  该定性框架综合文章提出AI辅助共享决策的关系框架，围绕AI输出的表面权威、可核验与可质疑性、偏好替代、不确定性与责任分散五项关系关切，转化为可观察的临床要求、临床测试与治理响应，并提出区分技术性能、决策过程、关系质量、公平、安全与治理结果的候选测量框架。
- [Improving the impact of medical student research through structured mentorship: a clinical research enterprise model.](https://europepmc.org/article/MED/42209435) · 机器建议排除，待抽查 · `p-2ffcd2507b0c8b7fa267`
  本文介绍一个医学生临床研究企业式纵向导师制项目，报告2019—2025年的论文产出、引用和职业发展等结果，属于医学教育项目评估。文中仅笼统提及公平与人工智能工具使用，未涉及医疗算法公平性评估、偏倚机制或缓解方法。
- [Application of Explainable Machine Learning for Individualized Risk Stratification and Surgical Optimization in Geriatric Intertrochanteric Fractures.](https://pubmed.ncbi.nlm.nih.gov/42980212/) · 机器建议排除，待抽查 · `p-4403cfa217b51b32b9c0`
  该回顾性队列研究纳入628例股骨转子间骨折行头髓内钉固定的患者，用12个临床与影像变量构建随机森林模型预测内固定失败，并用SHAP分析内侧化进钉点与尖顶距（TAD）的非线性交互，发现内侧化进钉点在TAD超过25mm时具有缓冲效应（测试集AUC 0.877）。
- [Rethinking University Mental Health for the AI Era: From Crisis Response to Core Mission.](https://europepmc.org/article/MED/43013291) · 机器建议排除，待抽查 · `p-99104d3f909768840511`
  文章主张将大学生心理健康纳入大学核心使命，提出整合数字工具、分级照护与精准治疗算法的校园心理健康体系，并强调AI治理、安全与公平。
- [Building and Validating a Data-Governance Workflow for Artificial Intelligence-Based Tuberculosis Detection from Chest Radiographs, and Quantifying the Impact of Data Leakage.](https://europepmc.org/article/MED/42888308) · 机器建议排除，待抽查 · `p-a036330c773f5ab14093`
  提出七步数据治理流程（多源标准化、溯源管理、MD5/pHash/dHash 三重去重、患者级划分、不变性核查、肺分割、指纹版本冻结），在 46,410 张胸片、七个公开来源上量化去重缺失与随机划分造成的数据泄漏对 AUC 的影响，结论是泄漏量级依数据结构而定、必须被测量，治理流程使复用可验证。
- [Theoretical analysis of transfer learning for temporally dependent observations.](https://pubmed.ncbi.nlm.nih.gov/43023018/) · 机器建议排除，待抽查 · `p-a3955dfee5639efddf72`
  本文研究高维向量自回归模型下的迁移学习理论，提出两步迁移学习流程、辅助数据集的信息子集选择方法，以及两种用于参数推断的“去偏”技术，并在温和条件下建立理论性质，最后用模拟数据和EEG数据集检验经验表现。
- [Background Bias Assessment and Mitigation in Plant Disease Detection Using EfficientNet-B0 with Image Processing](https://arxiv.org/abs/2611.00049) · 机器建议排除，待抽查 · `p-af26ec6de648c002a857`
  该文针对植物病害检测中 EfficientNet-B0 的背景捷径偏差，提出原图、仅叶片、仅背景三条件评估协议，并在 PlantVillage 上量化背景偏差系数，发现模型主要依赖叶片特征。属于农业视觉偏差评估，不涉及医学临床任务或受保护人群公平性。
- [Equipping the next generation: addressing the unmet need for artificial intelligence education at research performing organizations.](https://europepmc.org/article/MED/42888462) · 机器建议排除，待抽查 · `p-bd98d28296dc8ae83062`
  本文是一篇评论文章，基于对1200余名医学与生命科学学生及博士后的国际调查，指出生成式AI使用率高但缺乏正规培训与机构政策，并呼吁将AI素养纳入科研与临床教育，重审学术诚信框架，制定透明的负责任使用政策。文中仅在一般性建议层面提及识别幻觉与偏见、促进公平获取。
- [Is postoperative adjuvant therapy necessary for esophageal cancer patients with pathological complete response after neoadjuvant treatment?](https://pubmed.ncbi.nlm.nih.gov/42731259/) · 机器建议排除，待抽查 · `p-c2d58d64ab882a71dc49`
  该回顾性队列研究纳入184例新辅助治疗后达病理完全缓解（pCR）的食管癌患者，采用IPTW比较术后辅助治疗与观察的生存差异，发现cT4a为独立预后危险因素，辅助治疗可降低并延迟复发，并提出按cT4a/cN分层选择辅助治疗的风险适应决策方案。
- [Crossing the Divide: From AI Awareness to AI Assurance in Nursing Administration.](https://europepmc.org/article/MED/43036953) · 机器建议排除，待抽查 · `p-f1ccea6d3b9e79ddd33c`
  该文为护理管理视角的评论文章，主张把AI保障（治理、风险管理、持续监测）纳入护理领导职责，提出治理与问责、公平与偏倚缓解、临床性能与安全监测、透明与伦理、员工能力准备五个领导域，属政策与治理框架综述，未针对具体疾病或临床任务开展算法公平性分析或实证测量。
- [Deep Learning-based Semantic Segmentation of Dental Radiographs: Comparative Evaluation of PSPNet, DeepLabv3, UNet, and UNet++](https://arxiv.org/abs/2610.15061) · 机器建议排除，待抽查 · `p-0a7ab584ceef7f910746`
  该文在统一受控实验设置下比较 PSPNet、DeepLabv3、UNet 与 UNet++ 四种语义分割模型在 1269 张牙科X线片上的表现，考察图像尺寸与批大小的影响，并以 Dice、IoU、准确率、精确率及损失进行评价，UNet++ 取得最高 IoU 与 Dice。
- [Catalysing system reforms in Pakistan’s Healthcare and Health Professions Education: National Stakeholder priorities for strengthening policy and system Governance](https://europepmc.org/article/PPR/PPR1368269) · 机器建议排除，待抽查 · `p-116d132a6a15a073e809`
  该研究通过2026年巴基斯坦健康与教育峰会的混合焦点小组讨论，汇集14名利益相关者对医学与口腔教育质量、治理监管、认证及卫生人力留存的看法，提出从投入型转向产出型认证、建立跨机构治理平台等改革建议。文中仅简要提及谨慎、有目的地整合人工智能，未涉及任何算法公平性评估。
- [Direct Effects Multiplicative Inference (DEMI): causal prediction from pairwise clinical relationships, applied to antidepressant response.](https://europepmc.org/article/MED/42892463) · 机器建议排除，待抽查 · `p-1423f020303a662753a5`
  DEMI从All of Us提取4.3亿医学概念对关系，按时间顺序分解直接与间接效应并乘法聚合预测抗抑郁药应答；15种药物平均AUC 0.934，与逻辑回归0.935无显著差异。未评估公平性。
- [Anatomic Classifications and Functional Outcomes in Preaxial Polydactyly of the Hand.](https://pubmed.ncbi.nlm.nih.gov/42598942/) · 机器建议排除，待抽查 · `p-1cf7f8e7a97808d0cb3c`
  该研究回顾性分析58例（59指）术前轴前多指的术后结局，比较Wassel-Flatt与JK解剖分类系统与JSSH、Rotterdam评分及再手术等结局的关联，并评估临时经关节K针固定的影响。全文为临床外科结局研究，未涉及人工智能或算法公平性。
- [Five-year risk of cardiovascular events in women with history of pregnancy complicated by fetal growth restriction.](https://europepmc.org/article/MED/43050674) · 机器建议排除，待抽查 · `p-1de4b4c47fd32c7cf15f`
  该回顾性队列利用TriNetX数据评估胎儿生长受限与产后5年母亲心血管复合结局的关联，采用倾向评分匹配和Cox回归，未涉及AI/ML算法或算法公平性。
- [Age, tumor size, and therapy timing are associated with survival in primary spinal Ewing sarcoma: a nationwide analysis.](https://europepmc.org/article/MED/42928284) · 机器建议排除，待抽查 · `p-1f518fcb9c579e3639fe`
  该研究利用国家癌症数据库分析原发性脊柱尤文肉瘤中年龄、肿瘤大小与治疗时机对生存的影响，训练五种机器学习生存模型，并用Extra Survival Trees和SHAP分析预后因素。
- [Leveraging AI-ECG Technology for Early Notification and Tracking of AF Development (LATENT): A Randomized Controlled Trial.](https://pubmed.ncbi.nlm.nih.gov/42998297/) · 机器建议排除，待抽查 · `p-263284ee8b9a724f7139`
  LATENT为单中心、开放标签随机对照试验，评估AI-ECG风险分层引导的Holter监测能否提高新发房颤、房扑及前房颤心房表现的检出率。14 665名40–85岁无房颤史成人入组，主要复合终点为0.74% vs 0.48%（OR 1.54，P=0.046），作者自述结果统计学上脆弱、对1例事件重分类敏感。
- [Digital twin control framework uncovers individualized cross-scale links between functional connectivity deviations, communication impairment, and molecular mechanisms in autism.](https://pubmed.ncbi.nlm.nih.gov/42918437/) · 机器建议排除，待抽查 · `p-28fd16540d52d28aa2c6`
  该研究提出基于深度对比学习的数字孪生对照框架，量化自闭症个体的功能连接偏差，并将其与ADOS沟通评分及转录组、神经递质、线粒体等跨尺度机制关联。
- [Prediction of Systemic Lupus Erythematosus from Genotype and Gene-Expression Data: Batch Correction and Leakage-Free Evaluation](https://europepmc.org/article/PPR/PPR1349594) · 相关，待核实是否纳入 · `p-3d223ee6ca3da41000e6`
  该研究利用30个候选单核苷酸多态性与6个基因表达数据集预测系统性红斑狼疮。采用均值型批次校正，并在每个训练折内重新估计预处理与建模以避免数据泄漏，按个体划分折；以ROC-AUC、PR-AUC和MCC及标签置换检验评估。表达模型AUC达0.837至0.915，但仅用研究标签即可达0.857，显示批次与疾病标签强混杂，留出整项研究时性能明显下降。
- [It’s about time: Specifying time zero for target trial emulation in psychological research](https://europepmc.org/article/PPR/PPR1363496) · 机器建议排除，待抽查 · `p-408fcf2c00db10ff8789`
  该文是面向心理学研究的目标试验模拟（TTE）教程，重点讨论"时间零点"这一常被忽视的基石概念。作者系统枚举时间零点各组成部分的排列组合，说明其错位会引入选择偏倚、治疗后混杂、治疗依赖的合格性变化与不死时间偏倚，并提出决策框架与实践建议，以工作场所AI使用与员工倦怠为例进行演示。
- [Adoption and perception of artificial intelligence by corresponding authors in orthopaedic research: A global cross-sectional study.](https://pubmed.ncbi.nlm.nih.gov/41825826/) · 机器建议排除，待抽查 · `p-4aa4395b22cef533ddeb`
  该横断面调查评估骨科研究通讯作者对生成式AI的使用、态度、培训需求与披露实践，并按职业阶段和性别分析未来使用意愿。结果显示使用广泛但披露不足，男性性别与更积极的未来使用感知独立相关。
- [Association between Alzheimer's disease and related dementias and postoperative outcomes after geriatric hip fracture surgery.](https://europepmc.org/article/MED/43013143) · 机器建议排除，待抽查 · `p-4af28d0a37e706d529ca`
  回顾性队列研究，纳入3312例65岁以上髋部骨折手术患者，按电子病历记录的ADRD状态分组，用多因素回归分析ADRD与术后并发症、ICU入住、再入院及1年死亡率的关系，发现ADRD独立关联更差结局。
- [International Consensus on Artificial Intelligence in Undergraduate Dental Student Assessment: A Two-Round Modified Delphi and Live Consensus Study](https://europepmc.org/article/PPR/PPR1359981) · 机器建议排除，待抽查 · `p-4f82f9f44262ebd27f40`
  该研究通过两轮改良德尔菲法及现场共识投票，形成本科牙科学生评估中使用生成式人工智能的国际共识原则与评估形式分类建议，强调治理、披露、问责、数据保护与AI素养，但未评估任何具体算法。
- [It’s about time: Specifying time zero for target trial emulation in psychological research](https://europepmc.org/article/PPR/PPR1363497) · 机器建议排除，待抽查 · `p-58c16252ff091a586ebd`
  摘要介绍目标试验模拟（TTE）及“时间零点”在心理学观察性因果研究中的设计作用，讨论时间零点错位导致的偏倚并提出决策框架，以工作场所AI使用与员工倦怠为例。未涉及医学算法公平性、受保护群体或实证公平评估。
- [Medical leadership between motivation and organisational support: findings from a contemporary survey.](https://pubmed.ncbi.nlm.nih.gov/42814092/) · 机器建议排除，待抽查 · `p-6e502862f36dba96cf40`
  该文报告一项国际横断面问卷调查，分析临床与非临床医疗领导者在领导动机、组织支持（受保护时间、决策支持、共享治理）方面的差距，并将累积支持缺失与感知领导影响力和压力/倦怠关联，提出“动机—支持缺口”框架。
- [Formation of calcium oxalate kidney stones is related to consumption of some ultra-processed foods: a case-control study.](https://pubmed.ncbi.nlm.nih.gov/42470774/) · 机器建议排除，待抽查 · `p-71348eabce0902da8421`
  该研究为德黑兰开展的病例对照研究（366人），用147项食物频率问卷和NOVA分类评估超加工食品摄入与草酸钙肾结石的关联，采用多因素logistic回归。结果显示甜食类摄入与结石风险升高相关，乳制品摄入与风险降低相关，但总超加工食品摄入无显著关联。
- [SGLT2 Inhibitors and Risk of Postmenopausal Bleeding in Women: An Active-Comparator, New-User Cohort Study.](https://europepmc.org/article/MED/42957436) · 机器建议排除，待抽查 · `p-743354216635218b0792`
  该研究为药物流行病学队列分析，利用 All of Us 数据比较 55-90 岁女性新使用 SGLT2 抑制剂与 DPP-4 抑制剂后绝经后出血风险，采用倾向评分匹配与 Cox/Poisson 模型；结果显示风险无显著升高（HR 1.14，95%CI 0.70-1.84）。
- [Circulating miRNA profiling identifies hsa-miR-23a-3p and a three-miRNA signature associated with serous ovarian cancer](https://europepmc.org/article/PPR/PPR1373555) · 机器建议排除，待抽查 · `p-9248ffc4421b28b6931d`
  研究比较卵巢癌患者与对照血浆中8种miRNA，发现hsa-miR-23a-3p及三-miRNA逻辑回归模型具中等区分度，并报告交叉验证后性能下降及样本来源/技术变异等混杂因素。
- [Treatment intensity and survival benefit among older adults with glioblastoma: A population-based analysis.](https://pubmed.ncbi.nlm.nih.gov/42710195/) · 机器建议排除，待抽查 · `p-a11377379ca4050b6b0d`
  该研究基于SEER数据库（2000-2020）回顾性分析21,206例≥65岁胶质母细胞瘤患者，描述手术、放疗与化疗联合治疗强度的年龄趋势，并用中位生存期和24个月限制平均生存时间（ΔRMST0-24）评估各年龄层的绝对生存获益，发现高龄与接受三联治疗概率降低相关，但强化治疗在各年龄层均与更长生存相关。
- [Systemic ethics framework for artificial intelligence in nursing and healthcare.](https://pubmed.ncbi.nlm.nih.gov/42989488/) · 机器建议排除，待抽查 · `p-a13199f8b00c3ef3f702`
  该文通过整合综述提出护理与医疗AI的系统性伦理框架，归纳规范基础、治理问责、信任透明、数据正义与公平、生命周期伦理等八个概念轴，并构建微观—中观—宏观多层次模型，强调问责安排、人类监督与制度支持。
- [Evaluation of chromosome-level structural variation for acute myocardial infarction risk prediction](https://europepmc.org/article/PPR/PPR1362124) · 机器建议排除，待抽查 · `p-aa065ed711d05a970047`
  该研究利用 All of Us 队列中对性别、自报种族和年龄做 1:1 匹配的 3290 例样本，将染色体级别结构变异（全基因组 128 个片段的 LRR 分布统计矩）输入随机森林，进行急性心肌梗死风险预测。10 折交叉验证平均 AUC 仅 0.529，与打乱标签对照（0.491）及随机水平无法区分，结论为宏观结构变异不能解释 AMI 的缺失遗传力。
- [Efficacy and Safety of Stent-Assisted Coiling Versus Coiling Alone for Ruptured Multilobed Aneurysms: A Multicenter Study.](https://pubmed.ncbi.nlm.nih.gov/42974369/) · 机器建议排除，待抽查 · `p-b1770139d184f1002ae3`
  多中心前瞻性队列比较支架辅助栓塞与单纯栓塞治疗破裂多叶颅内动脉瘤的安全性和疗效，采用重叠权重及双稳健回归分析。研究未涉及AI/ML算法评估或算法公平性问题。
- [Analisi dell’appropriatezza prescrittiva ed evoluzione digitale: integrazione tra ricetta dematerializzata, intelligenza artificiale e manuale Rao.](https://europepmc.org/article/MED/42979883) · 机器建议排除，待抽查 · `p-b1f1c2e8dcbc74c8d6c7`
  该摘要介绍意大利马尔凯大区利用 NotebookLM 分析 36,465 份去物质化处方与 RAO 优先标准的符合性，发现 30% 处方不一致且异常集中于少数开方者，属于处方适当性数字审计，并非医疗算法公平性研究。
- [Oxidation over omega-3: Reinterpreting the paradoxical link between fish oil supplements and accelerated cognitive decline.](https://pubmed.ncbi.nlm.nih.gov/42612547/) · 机器建议排除，待抽查 · `p-be1ec4309a4ce2fb4aa3`
  该文为致编辑信，评论一项观察性研究：鱼油补充与认知加速下降相关，并由FDG-PET低代谢介导。作者指出四点方法学局限（暴露错分、残余混杂、机制过度推断、情境依赖），并建议血清EPA+DHA剂量建模、负对照敏感性分析、部分容积校正FDG中介分析等改进。全文未涉及任何AI/ML算法或算法公平性评估。
- [MRCP-derived radiomics features associated with biliary dilation: a multi-step feature reduction, multivariable regression, and diagnostic classification study.](https://pubmed.ncbi.nlm.nih.gov/42138743/) · 机器建议排除，待抽查 · `p-c481c3634d23e0326c99`
  该研究基于MRCP影像提取三维CBD radiomics特征，经ICC可重复性、低方差、相关性、FDR与Cliff's delta多步降维，纳入年龄、性别和胆囊切除状态的多变量回归，并用随机森林等三种分类器做胆管扩张诊断分类，另在6-10 mm临界管径亚组做探索性分析。
- [Cross-cohort analyses of OLFML2B cellular distribution and stromal associations in gastric adenocarcinoma.](https://pubmed.ncbi.nlm.nih.gov/43040151/) · 机器建议排除，待抽查 · `p-c7d769f27ffccb863361`
  该研究整合五个队列的批量、单细胞、空间和蛋白质组数据，分析OLFML2B在胃腺癌中的细胞分布及其与成纤维细胞、ECM、TGF-β程序的相关性，并考察PD-1治疗队列中的反应关联；未涉及算法公平性。
- [Association of objectively measured physical activity with incident spinal stenosis in a Fitbit-linked cohort from the All of Us Research Program.](https://europepmc.org/article/MED/43050913) · 机器建议排除，待抽查 · `p-d577bfdc715f5d3350d6`
  利用 All of Us 研究项目中 Fitbit 可穿戴设备数据与电子健康记录链接的回顾性队列（48,709 人、161,900 人年），以时变 Cox 比例风险模型评估客观测量的日均步数与活跃分钟数与新发椎管狭窄（颈段、腰段）的关联，发现步数较高者椎管狭窄风险较低（HR 0.84）。
- [EXPRESS: Brain Age Gap from Non-Contrast CT Is Independently Associated with Functional Outcome after Acute Ischemic Stroke.](https://europepmc.org/article/MED/43015642) · 机器建议排除，待抽查 · `p-d5df31f2d791fe9c70ba`
  该研究基于1,173例急性缺血性卒中患者的前瞻性多中心队列，用深度学习从对侧非增强CT估计脑年龄，定义BrainAGE（预测年龄减实际年龄），并分析其与90天功能结局的关联。结果显示BrainAGE较高与更差功能结局独立相关，但判别力提升有限。
- [Association of Cumulative Pharmacist Interventions and Interprofessional Adherence With Survival Among Patients Requiring Pharmacotherapeutic Optimization in a Pediatric Intensive Care Unit: A Retrospective Time-Dependent Cohort Study.](https://europepmc.org/article/MED/43000161) · 机器建议排除，待抽查 · `p-e6d3c6428f1e2c8de26d`
  该回顾性队列研究纳入565例儿科重症监护病房（PICU）患者，采用含时变暴露的扩展Cox比例风险模型，评估累计药师干预数及跨专业团队依从性与PICU内生存的关系，并按PIM-2校正基线严重度，报告总体死亡率11.9%、干预接受率72.2%。
- [Tenecteplase vs Alteplase in Basilar Artery Occlusion Treated with Endovascular Thrombectomy: A Propensity Score-Matched Analysis of 90- and 180-Day Outcomes.](https://europepmc.org/article/MED/42217837) · 机器建议排除，待抽查 · `p-e9bbb6c62205518a6b32`
  该研究利用TriNetX回顾性队列（553例基底动脉闭塞行血管内取栓患者），通过倾向性评分匹配比较替奈普酶与阿替普酶桥接溶栓在90天和180天的出血、死亡、功能依赖及康复利用等结局，未发现显著差异，仅康复利用信号在多重检验校正后消失。
- [Morphology-based selvester QRS score for phenotyping acute heart failure in patients with native left bundle branch block.](https://pubmed.ncbi.nlm.nih.gov/42721639/) · 机器建议排除，待抽查 · `p-f2b6a21e012418a77837`
  该摘要评估Selvester QRS评分在伴原生左束支传导阻滞的急性心衰患者中区分HFrEF、HFmrEF、HFpEF和RHF的诊断表现，报告SQS与超声参数相关且对HFrEF区分中等。未涉及AI/算法公平性、敏感人群比较或缓解措施。
- [Association of C-reactive protein to albumin ratio with progression of CKD and all-cause mortality in diabetic CKD.](https://pubmed.ncbi.nlm.nih.gov/42412363/) · 机器建议排除，待抽查 · `p-f497b8eb950e521f7701`
  该研究在231例糖尿病合并慢性肾脏病患者中评估C反应蛋白/白蛋白比值（CAR）与CKD进展及全因死亡的关联，采用Kaplan-Meier、Cox回归、限制性立方样条及SHAP机器学习分析，发现CAR为独立预后因子并可提升风险预测效能。
- [Clinical and sociodemographic predictors of AI use for mental health among college students.](https://pubmed.ncbi.nlm.nih.gov/42217639/) · 机器建议排除，待抽查 · `p-faa1ff8cf33578158f1a`
  基于2024-2025年Healthy Minds Study两所美国高校675名学生的横截面数据，用层次logistic回归分析大学生将生成式AI用于心理健康支持的临床与社会人口学预测因素，发现重度抑郁、重度焦虑、自杀倾向及亚裔身份与更高使用几率相关，并提示边缘群体使用未受监管AI工具的比例偏高。
- [Association Between MIA3 and Coronary Collateral Circulation Formation in Patients with Chronic Total Occlusion](https://europepmc.org/article/PPR/PPR1354723) · 机器建议排除，待抽查 · `p-ff7c424314366178daee`
  该研究纳入489例冠状动脉慢性完全闭塞（CTO）患者，检测血浆MIA3与VEGFA水平，按Rentrop分级分为侧支循环良好组与不良组，采用多因素logistic回归、ROC曲线及NRI/IDI评估MIA3对良好侧支形成的预测价值，并开展临床亚组与交互分析。
- [Ethical Decision-Making in Nursing Management: Comparing Nurse Managers and Generative Artificial Intelligence](https://europepmc.org/article/PPR/PPR1359832) · 机器建议排除，待抽查 · `p-2a813b12a1e170b90af2`
  探索性研究，比较西班牙某公立大学医院护理管理者的伦理决策与三种生成式AI模型在相同管理情景下的回答一致性和重复稳定性。结果显示总体一致性相近，但模型在拒绝执行与知情同意等情景上系统性偏离人类众数；作者强调稳定性、专业一致性与伦理正当性是三个独立问题，不主张临床有效性。
- [Concurrent cognitive, behavioral and systemic physiological features mark preclinical Alzheimer’s disease](https://europepmc.org/article/PPR/PPR1354470) · 机器建议排除，待抽查 · `p-2d4258f545c1b26784f5`
  研究纳入644名自报认知正常的老年人，以血浆p-tau217界定临床前阿尔茨海默病亚组，描述其认知、行为及生理特征，并构建概念验证AI分类器整合多域临床数据，较单独认知筛查提高p-tau217高风险个体识别。
- [Clinical and molecular characteristics associated with megakaryocytic dysplasia in patients with myelodysplastic syndromes.](https://pubmed.ncbi.nlm.nih.gov/43043920/) · 机器建议排除，待抽查 · `p-35e6e11c24cb884c5eeb`
  研究169例骨髓增生异常综合征患者，比较伴或不伴巨核细胞发育异常者的临床、细胞遗传学及突变特征，发现EZH2突变是唯一独立相关因素。该研究为临床-分子关联分析，未涉及AI/ML算法或算法公平性。
- [Early Catheter Ablation for Patients With Atrial Fibrillation and a Stroke History: A Target Trial Emulation Analysis.](https://pubmed.ncbi.nlm.nih.gov/42821842/) · 机器建议排除，待抽查 · `p-481a4db85e5cf700e6a2`
  该研究采用目标试验模拟（克隆-删失-加权法）比较房颤合并缺血性卒中患者早期导管消融与药物治疗的长期结局，纳入6家中心431例患者，报告MACE、再住院、死亡及mRS/AD8功能认知结局的关联，属观察性因果效应估计研究。
- [Value-Based Care in Neurosurgery: Results from Maryland’s Global Budget Revenue Program](https://europepmc.org/article/PPR/PPR1344342) · 机器建议排除，待抽查 · `p-596a0bc151428ccc8ae7`
  研究评估马里兰全球预算收入模型对垂体手术费用、住院时长、再入院及不同保险和年龄患者构成的影响，报告费用下降与低收入患者可及性改善，但未涉及AI/ML算法或算法公平性。
- [How to tackle inequities in bereavement support for ethnically diverse communities: a national qualitative study using experience-based co-design.](https://pubmed.ncbi.nlm.nih.gov/42902353/) · 机器建议排除，待抽查 · `p-7d86f34b5b0505602795`
  该全国定性研究通过访谈、焦点小组和共创工作坊，识别族裔多元群体在丧亲支持获取上的障碍与促进因素，提出文化安全照护、反种族主义实践和社区合作建议，并形成逻辑模型。研究未涉及AI/ML算法或算法公平性评估。
- [Clinical equipoise as inclusion criterion to control for confounding in observational studies.](https://pubmed.ncbi.nlm.nih.gov/42854534/) · 机器建议排除，待抽查 · `p-875da7d10afd9f30ec2b`
  该研究以专家治疗推荐分歧作为临床均势代理，评估不同分歧层级下肱骨近端骨折治疗组基线可比性，发现更严格纳入标准可改善组间平衡但减少样本量。研究不涉及医学AI/ML算法或算法公平性评估。
- [Propensity Score Matching Unmasks Core Predictors of Psychosis Conversion in Clinical High-Risk Individuals.](https://pubmed.ncbi.nlm.nih.gov/42960986/) · 机器建议排除，待抽查 · `p-9a0944cda37da259a878`
  该研究在920例临床高危精神病(CHR-P)个体中随访3年，使用倾向性评分匹配(PSM)平衡年龄、性别、教育程度及6个认知域等混杂因素，再以多因素logistic回归与ROC分析识别精神病转化的独立预测因子。PSM后模型AUC由0.685升至0.808，GAF下降率单项准确率约73%，作者据此强调早期精神病预测中需控制认知与人口学混杂。
- [Extracapsular and joint-dominant hand and wrist MRI patterns in psoriatic and rheumatoid arthritis: an exploratory case-control study.](https://pubmed.ncbi.nlm.nih.gov/42978735/) · 机器建议排除，待抽查 · `p-9ea0a6100ead36f59229`
  该探索性病例对照研究比较41例银屑病关节炎与41例类风湿关节炎患者手/腕3.0T MRI的预设影像学特征，发现关节囊外软组织炎症、附着点相关特征更支持PsA，而关节积液、腕部滑膜炎与骨侵蚀更支持RA，并报告了读者间与读者内一致性系数。
- [The C-reactive protein to lymphocyte ratio and 28-day mortality in critically ill patients with sepsis: a retrospective propensity score-matched cohort study.](https://pubmed.ncbi.nlm.nih.gov/43011466/) · 机器建议排除，待抽查 · `p-a8215224fac5c572c2b3`
  基于MIMIC-IV的回顾性倾向评分匹配队列，评估脓毒症患者C反应蛋白/淋巴细胞比与28天及长期全因死亡率的关联和预测价值；未涉及算法公平性、偏倚机制或缓解评估。
- [Development and validation of a cuff size prediction model for pediatric blood pressure measurement outside the office.](https://pubmed.ncbi.nlm.nih.gov/42207271/) · 机器建议排除，待抽查 · `p-ba6fa6408cc8bbe26dd7`
  基于NHANES数据开发线性回归模型，用年龄、性别、身高、体重等EHR变量预测儿童中臂围以确定动态血压监测袖带尺寸，并在儿科高血压门诊107人外部验证；报告预测一致性（⍴c=0.94）与袖带尺寸符合率（83.2%）。
- [Open-fMIND: A Large-Scale Open-Access fMRI Corpus for Pretraining Brain Foundation Models](https://arxiv.org/abs/2611.21215) · 机器建议排除，待抽查 · `p-c953684f67e297ff37a6`
  Open-fMIND 构建并发布大规模开放 fMRI 分区时间序列语料，覆盖 322 项 OpenNeuro 研究、11,379 名受试者，支持脑基础模型自监督预训练，并在 HCP-YA、ABIDE、ADHD-200 上评估下游预测性能。
- [Artificial Intelligence Applications in General Surgery in the United States of America: A Bibliometric Analysis.](https://pubmed.ncbi.nlm.nih.gov/42104780/) · 机器建议排除，待抽查 · `p-d329a221375326aba663`
  该文是对美国普外科人工智能研究的文献计量分析，纳入2020—2025年59篇文献，统计作者、主题、期刊、国别与资助分布，采用H指数、AIS、布拉德福德定律及泊松/负二项回归等指标，发现研究集中于手术流程识别与临床决策支持，且资金更倾向临床可落地的应用。
- [Same day discharge following bimaxillary osteotomy surgery a single center retrospective study.](https://pubmed.ncbi.nlm.nih.gov/42993311/) · 机器建议排除，待抽查 · `p-d6abeded64d1a68e9115`
  该回顾性队列描述80例双颌截骨术患者同日出院与留院过夜的并发症记录，报告未调整混杂因素的比例差异，未涉及人工智能、算法公平性或受保护群体分析。
- [Good Enough to Sequence: Fluorometry-Guided Salvage of Low-Volume and Compromised Paediatric DNA in Custom Amplicon Next-Generation Sequencing.](https://pubmed.ncbi.nlm.nih.gov/43028320/) · 机器建议排除，待抽查 · `p-f773c3a00472650dfad3`
  该研究基于314例儿童样本，比较Qubit与Nanoquant定量及A260/280质量分组对定制扩增子NGS建库产量、测序深度与覆盖度质控指标的影响，并提出约20 ng/µL的输入阈值以降低建库失败风险。属实验室样本质量控制方法学，不涉及AI算法评估或算法公平性分析。
- [Artificial intelligence in chronic kidney disease care: An integrative review of outcomes and sociotechnical factors.](https://europepmc.org/article/MED/43057074) · 机器建议排除，待抽查 · `p-0ef43e765130077b006e`
  该整合综述梳理CKD照护中AI技术的临床使用结局及社会技术因素，纳入25项研究，报告患者结局、照护流程、资源使用及社会技术报告不均，并指出公平性等报告不足。未开展CKD场景下的算法公平性分析。
- [Density Peak Clustering: A Systematic Survey of Methods, Applications, Challenges, and Future Research Directions](https://europepmc.org/article/PPR/PPR1352750) · 机器建议排除，待抽查 · `p-21c05110656354a438ee`
  这是一篇关于密度峰值聚类（DPC）的系统性综述，梳理2014年以来的方法演进、八大方法族（自适应邻域与密度估计、图与流形建模、自动确定簇数、分配与不确定性、表示学习、隐私/联邦/增量计算、可扩展执行、采样与优化等辅助策略）及其适用假设与计算代价，并列举医疗、网络安全、遥感、交通等领域应用，最后提出面向鲁棒、可解释、公平、隐私保护等方向的未来研究议题。
- [What Factors Influence Hospital Admission for Mandible Fractures in Emergency Departments Across the United States?](https://pubmed.ncbi.nlm.nih.gov/42235594/) · 机器建议排除，待抽查 · `p-2929aa6bb236b998782c`
  基于2022年全国急诊样本的回顾性队列，分析下颌骨骨折患者入院及费用的生物、情境和社会经济预测因素。结果显示男性、多发骨折、合并中面部骨折和枪伤与入院相关，无保险患者入院可能性较低。
- [Promoting Just Culture: Implementing a Medication Error Reporting Process in Nursing Education.](https://pubmed.ncbi.nlm.nih.gov/42089774/) · 机器建议排除，待抽查 · `p-442a05aaacc8e4189c99`
  护理教育中的用药错误报告质量改进项目：培训临床教师使用标准化报告流程（事件上报系统、复盘工具、学生行为分类算法、第二受害者支持），比较培训前后的教师调查结果，教师处理用药错误的信心显著提升，并称促进公平。全文未涉及AI/ML算法或算法公平性分析。
- [Toward Clinically Trustworthy Deep Learning in Cardiology: A Unified Mathematical Synthesis of Representation, Optimization, and Reliability.](https://europepmc.org/article/MED/43028492) · 机器建议排除，待抽查 · `p-4ba526797d8b268917d7`
  该系统综述基于79篇文献，从统一的数学视角梳理心脏病学可信深度学习中的表示学习、优化、不确定性、鲁棒性、公平性、可解释性与泛化，并提出概念性审计框架；作者强调相关指标仅具理论性，并非实际临床指标。
- [Artificial Intelligence in Neglected Tropical Diseases: Current Applications, Challenges, and Opportunities](https://europepmc.org/article/PPR/PPR1371479) · 机器建议排除，待抽查 · `p-b739156d3045cfb0e9ce`
  该文是对AI应用于被忽视热带病（NTDs）的系统综述，纳入289项研究，涵盖诊断、预后、监测、暴发预测、治疗监测与药物发现，指出外部验证、前瞻性评估及数据治理、可解释性、公平性等方面存在不足。
- [Beyond scales: Artificial intelligence, language, and behavior in suicide risk modeling-a narrative review.](https://europepmc.org/article/MED/43035089) · 机器建议排除，待抽查 · `p-ee87c34c3078786f90ec`
  该叙述性综述总结人工智能在自杀想法与行为预测中的多模态应用，涵盖电子健康记录与理赔数据、临床文本自然语言处理、语音与面部行为信号、神经影像及被动传感，并讨论判别与校准、外部验证、类别不平衡和部署伦理，仅泛泛提及算法偏见与公平。
- [Etiology and Anatomical Level of Lower-Limb Amputations in Two Iranian Referral Hospitals: A Retrospective Record-Based Study.](https://pubmed.ncbi.nlm.nih.gov/42940562/) · 机器建议排除，待抽查 · `p-1f719bc172ff6ac3b1d8`
  回顾性分析伊朗两家医院229例下肢截肢记录，描述创伤、血管病和感染等病因及截肢平面，并发现年龄与医院差异；未涉及AI/ML模型或算法公平性评估。
- [The Ethics of Autonomous Clinical AI: Shifting From Model Accuracy to Model Impact.](https://pubmed.ncbi.nlm.nih.gov/42913471/) · 机器建议排除，待抽查 · `p-5e14e8326ab1970479b8`
  该文为观点/评论文章，主张自主临床AI的伦理评估应从模型准确率转向完整诊疗路径结局，并转述Nichol等人的九项试验建议，包括预设亚组表现、随访照护与模型变更等义务。全文未针对任何具体疾病或临床任务提供实质性的算法公平性分析，也无亚组指标或实证测量。
- [Comparative evaluation of training strategies using partially labelled datasets for segmentation of white matter hyperintensities and stroke lesions in FLAIR MRI.](https://pubmed.ncbi.nlm.nih.gov/42659784/) · 机器建议排除，待抽查 · `p-941651f4cc3f2fc37b20`
  该研究在FLAIR MRI上比较六种利用部分标注数据训练联合白质高信号（WMH）与缺血性卒中病灶（ISL）分割模型的策略，汇总2052例MRI体数据，发现伪标签策略效果最佳，可稳定分割WMH并检出多数FLAIR阳性ISL。
- [AI-Supported Semiquantitative CT Characterization of COVID-19 Pneumonia Across SARS-CoV-2 Wild-Type, Alpha, and Delta Variants and Its Association with Clinical Parameters.](https://europepmc.org/article/MED/43028567) · 机器建议排除，待抽查 · `p-a27cbdea53664651a807`
  该回顾性单中心研究使用AI CT肺炎分析原型对255例COVID-19患者的肺部阴影进行半自动定量，比较野生型、Alpha和Delta变异组的CT衰减、体积及COVID-19概率，并分析其与临床和实验室参数的相关性。
- [A Qualitative Study of African Americans' Experiences with Healthcare: Developing Cultural Competency Training for Cancer Care.](https://pubmed.ncbi.nlm.nih.gov/42995326/) · 机器建议排除，待抽查 · `p-a633a59806919d28b53e`
  研究通过30名非洲裔美国人半结构访谈，探讨癌症照护中的就医可及性、文化观念与种族偏见经历，并据此开发文化胜任力模拟教育模块。
- [Fluorescence Encoding-Enabled Multiplexed Droplet Digital Recombinase Polymerase Amplification-CRISPR/Cas12a Assay for Rapid Screening of Lower Respiratory Tract Infection-Associated Bacterial Pathogens.](https://pubmed.ncbi.nlm.nih.gov/42937587/) · 机器建议排除，待抽查 · `p-0f29043f64118c8a4f09`
  该文提出荧光编码多重液滴数字RPA-CRISPR/Cas12a检测平台，结合机器学习解码，实现下呼吸道感染相关细菌病原体多重定量，并用临床样本验证与培养结果的一致性。
- [Association of bilingual language use with brain age: MRI evidence from bilinguals, translators, and interpreters.](https://pubmed.ncbi.nlm.nih.gov/43041269/) · 机器建议排除，待抽查 · `p-102f2c250012d5cd6b69`
  研究用六个预训练脑龄模型比较105名捷克语-英语双语者（非专业双语者、笔译和同传）的年龄校正脑龄差，未发现经FDR校正的组间差异；结果强调脑龄推断对模型选择和年龄偏差校正敏感。
- [Longitudinal pre-diagnostic blood samples predict osteoporosis risk.](https://pubmed.ncbi.nlm.nih.gov/42871651/) · 机器建议排除，待抽查 · `p-15ed546d8e15d79fd402`
  该研究基于丹麦献血者队列的538份纵向血浆代谢组样本（99例prediagnostic骨质疏松患者与99名匹配对照），比较横断面与纵向建模的预测性能：纵向LASSO轨迹模型AUC为0.67–0.76，优于横断面的0.57–0.63，最佳模型独立验证AUC为0.70。全文摘要未涉及算法公平性、亚组差异或偏差机制的分析。
- [Worldwide survey on artificial intelligence in occupational therapy.](https://pubmed.ncbi.nlm.nih.gov/42585570/) · 机器建议排除，待抽查 · `p-16d932da8047442b4c63`
  摘要报告了一项全球职业治疗师调查，了解其对人工智能的知识、使用情况和态度；研究未评估具体算法、群体公平性指标或缓解措施。
- [Excessive Weight Loss with Zepbound Is Associated with Higher Rates of Adverse Events, Electrolyte Imbalances, and Hospitalization than Moderate Weight Loss](https://europepmc.org/article/PPR/PPR1346607) · 机器建议排除，待抽查 · `p-2857d68b3a9af48583e2`
  研究利用去标识化EHR比较Zepbound首年减重≥30%与5%-15%者的不良事件，发现过度减重与更高不良事件、住院及电解质异常相关；LLM仅用于事件提取，未评估算法公平性。
- [Nursing, Artificial Intelligence, and the Algorithmic Time Machine: Safeguarding Techno-Temporal Justice for Person-Centred Care.](https://europepmc.org/article/MED/42952232) · 机器建议排除，待抽查 · `p-29e9e0f870fc81357c24`
  论文提出“算法时间机器”与“技术-时间正义”概念，讨论AI如何通过分类、预测、推荐和压缩重塑护理时间与护士能动性，并主张以时间敏感框架评估AI是否支持公平、人性化、以人为中心的照护。
- [Decision-to-Delivery Interval and Perinatal Outcomes Following Emergency Cesarean Section in Southern Ethiopia](https://europepmc.org/article/PPR/PPR1340265) · 机器建议排除，待抽查 · `p-2a0b7223fe49d5fe9cd3`
  该研究为埃塞俄比亚某医院急诊剖宫产决策至分娩间期（DDI）的横断面调查，纳入284例产妇，用描述统计与二元logistic回归分析DDI延长（&gt;30分钟）的相关因素及其与围产结局（如1分钟Apgar评分）的关联。
- [Navigating barriers: The journey of women surgeons in Türkiye Across decades.](https://pubmed.ncbi.nlm.nih.gov/42648007/) · 机器建议排除，待抽查 · `p-3646728625d955d7bac3`
  文章为土耳其女性外科医生职业历程的视角评论，描述历史先驱、性别刻板印象、骚扰与晋升障碍，以及机构改革建议。未涉及医学人工智能算法、模型公平性评估或缓解方法。
- [Relapse of ANCA-Associated Vasculitis With Kidney Involvement: A Cohort Study.](https://pubmed.ncbi.nlm.nih.gov/43044903/) · 机器建议排除，待抽查 · `p-517e6927ff88a49bc260`
  该研究为法国多中心回顾性队列，分析ANCA相关性血管炎肾受累患者的复发模式、危险因素及复发与肾衰竭/死亡的关联，并评估现有复发风险评分的区分度；未涉及算法公平性、亚组差异或偏倚缓解。
- [How did data sharing evolve in the decade since the FAIR Principles?](https://arxiv.org/abs/2611.20319) · 机器建议排除，待抽查 · `p-636203d18db253767e77`
  对2011–2025年PMC开放获取子集680余万篇生物医学论文进行纵向分析，提取数据可用性声明、仓储链接与JATS4R合规性，并考察学科、地区、资助方、开放获取层级及作者性别相关的数据共享差异。
- [Identifying patients at elevated risk of stroke after transcarotid artery revascularization.](https://pubmed.ncbi.nlm.nih.gov/42323112/) · 机器建议排除，待抽查 · `p-7a7241c81548105604e8`
  利用VQI数据（61,111例TCAR）以CART和随机森林识别院内卒中相关因素，并按症状状态、P2Y12依从性和支架数量分组，报告调整后卒中风险差异。
- [Green AI for Telehealth.](https://europepmc.org/article/MED/42969789) · 机器建议排除，待抽查 · `p-7b736b8d23744e060972`
  文章讨论加拿大远程医疗中的绿色AI，提出IoT-fog-cloud资源感知架构，并主张评估临床性能、资源使用、组织适配与可持续性，同时将公平可及列为负责任AI的考量之一。
- [Retinal imaging for cerebrovascular risk stratification: evidence, limitations, and practical thresholds for the ophthalmologist.](https://pubmed.ncbi.nlm.nih.gov/42390572/) · 机器建议排除，待抽查 · `p-883b35cbccb829e5d82d`
  该叙述性综述评估视网膜影像（眼底、血管几何、OCT/OCTA及AI oculomics）用于脑血管风险分层的证据成熟度与临床转化局限，并提出面向眼科医生的模式化框架。
- [Detecting Language-Related Disparities in Spiritual Care Using Artificial Intelligence.](https://pubmed.ncbi.nlm.nih.gov/42902576/) · 机器建议排除，待抽查 · `p-8c77e8f6e91acd395a98`
  该摘要报告一项基于电子健康记录的研究，使用自然语言处理识别灵性照护文档，并用逻辑回归分析患者语言与正式灵性照护获取及时间的关系，发现非英语使用者获取率更低、支持更晚。
- [A multinational pharmacoepidemiology atlas of prescription medication associations with all-cause mortality across six population cohorts](https://europepmc.org/article/PPR/PPR1367355) · 机器建议排除，待抽查 · `p-9320409dfec5a4ff0cd3`
  该研究在英、美、芬兰、香港和日本六个队列（893万人、14.9亿条处方）中，用时依Cox模型筛查处方药与全因死亡的关联，发现VZV疫苗、阿托伐醌-氯胍等少数药物呈负相关，并提示健康使用者偏倚不能完全解释VZV疫苗信号。
- [Participation in an integrated telemedicine and psychological counseling program and psychological outcomes in patients with HCC: a multicenter retrospective cohort study.](https://europepmc.org/article/MED/42955103) · 机器建议排除，待抽查 · `p-9d5bd94b760b9bad9a79`
  研究评估HCC患者参与整合远程医疗与心理咨询项目的累计程度与12个月心理结局的关联，发现较高参与度与抑郁、焦虑、睡眠和痛苦评分较好相关，但疾病特异性生活质量较低；为多中心回顾性队列，非算法公平性研究。
- [Modifications of diagnosis-related group payment for hospital care: a systematic review](https://europepmc.org/article/PPR/PPR1351285) · 机器建议排除，待抽查 · `p-9ebb0211c5729745c2dd`
  系统综述评估DRG支付方式修改（主要为捆绑支付）对患者结局、质量、利用、成本和公平性的影响；发现捆绑支付与较低住院总费用相关，但公平性证据有限。该文不属于医学AI/ML算法公平性研究。
- [Health Care Delays, Mental Health Care, and Discrimination among US Sexual and Gender Minority Adults: Intersectional Analysis of State-level Policies.](https://europepmc.org/article/MED/42913961) · 机器建议排除，待抽查 · `p-a5f1ff2ceb89d9e47906`
  研究分析美国性与性别少数成年人中，州级政策包容性与就医延迟、心理健康服务使用和医疗歧视的关联，采用交叉性多层分析；未评估任何AI/ML算法或算法公平性。
- [Feasibility and equity in the assessment of parent-child interactions: Lessons from three approaches.](https://europepmc.org/article/MED/42956222) · 机器建议排除，待抽查 · `p-a74fb8515fa29c366d7b`
  该文比较三种亲子互动观察与编码方法（视频会议实时编码、智能手机App结合AI支持编码、可穿戴设备家庭自然情境录像）的可行性、成本、生态效度与公平可及性，并讨论临床与伦理影响，样本量分别为114、27、27。
- [Prognostic prediction models for psoriatic arthritis in psoriasis: A systematic review.](https://pubmed.ncbi.nlm.nih.gov/42312903/) · 机器建议排除，待抽查 · `p-c26def1ad664f90b88d2`
  该系统综述纳入15项研究、490个预后模型，评估银屑病患者发生银屑病关节炎的风险预测模型之预测性能、偏倚风险与报告质量；摘要未涉及算法公平性、亚组差异或缓解措施。
- [The Prevalence and Clinical Characteristics of Atrial Fibrillation and Reflux Esophagitis Among Individuals Undergoing Health Checkups.](https://europepmc.org/article/MED/42875209) · 机器建议排除，待抽查 · `p-ca3d70e3725b143a1044`
  该研究为健康体检人群的横断面流行病学分析，纳入5205名接受胃镜检查的成年人，考察房颤与反流性食管炎的关联；结果显示房颤组食管炎患病率更高，但多因素logistic回归校正性别、年龄等因素后关联不再独立，提示由共同混杂因素解释。
- [Digital Transformation of Rehabilitation Care: A Systems-Based Narrative Review and Conceptual Framework for Connected, Intelligent, and Hybrid Rehabilitation.](https://europepmc.org/article/MED/43028647) · 机器建议排除，待抽查 · `p-cdb91e4a7fe04fb245d1`
  该文为康复领域数字化（远程监测、人工智能、居家与混合照护）的叙事综述，提出由互联、智能、混合三类能力构成的系统框架，并强调互操作性、数据治理、公平与持续评估等社会技术条件。
- [reFLASH: a proof-of-concept meta-analytic framework to validate surrogate endpoints in the absence of randomized clinical trial data.](https://pubmed.ncbi.nlm.nih.gov/42641770/) · 机器建议排除，待抽查 · `p-d336159d7b8908016928`
  提出 reFLASH 元分析框架：将 12 项滤泡性淋巴瘤随机试验拆分为单臂试验并重新配对，用 IPTW 模拟随机化，评估 30 个月完全缓解对无进展生存期的替代终点效度。属于肿瘤学统计方法研究，不涉及医学算法公平性。
- [Short- Versus Long-Course Radiation in Total Neoadjuvant Therapy for Locally Advanced Rectal Cancer: A Propensity-Matched National Cancer Database Analysis.](https://pubmed.ncbi.nlm.nih.gov/42598830/) · 机器建议排除，待抽查 · `p-ef2c73c3a8803f2d0255`
  该研究利用国家癌症数据库比较局部晚期直肠癌全程新辅助治疗中长程与短程放疗的总生存及病理结局；倾向评分匹配后生存无差异，长程组淋巴结降期率较高。未涉及AI/ML算法或公平性分析。
- [Striving for Equity in Cystic Fibrosis Research: Perspectives from Black and Hispanic/ Latino(a) Individuals with CF.](https://pubmed.ncbi.nlm.nih.gov/42896705/) · 机器建议排除，待抽查 · `p-fa3ca2ed93703292ee6b`
  该研究通过半结构化访谈，探讨黑人及西班牙裔/拉丁裔囊性纤维化患者对临床研究的看法、参与障碍与促进因素，并提出以社区支持和信息透明为核心的纳入改进方案。研究聚焦临床研究代表性不足的社会文化因素，未涉及任何算法或AI模型。
