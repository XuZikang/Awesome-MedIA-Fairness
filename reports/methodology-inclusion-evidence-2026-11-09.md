# 六篇方法学文献收录证据 · 2026-11-09

六篇均为用户明确批准纳入的原始研究。核查层级逐条列出；未统一宣称完成全文审阅，未调用或冒充Qoder输出。

## p-25f166919d5808c5e366

[Detection and Validation of Hidden Subgroup Disparities in Clinical AI](https://arxiv.org/abs/2610.32362)

分类：Fairness Evaluation；Stage：Evaluation

中文判断：学习表征上的亚组发现和验证属于公平性评估；缓解实验为次要贡献，摘要不足以确认其干预阶段。发现亚组不是已核实的人口属性群体。

核查与限制：已核对arXiv原始摘要；分割策略、亚组稳定性和缓解训练协议未完成全文核验。

原始证据短引：

> Traditional subgroup analyses can expose such disparities only when rich metadata

人工证据版本：dbf08f2c97bb6cdff0795e0bdc1287d938216eee0044f89a2a79cfd26de75315

## p-45778789f12c424e7649

[Trajectory-Guided Steering: Mitigating Spurious Feature Bias in Clinical Classification](https://arxiv.org/html/2610.22618v1)

分类：Post-processing；Stage：Post-processing

中文判断：原文方法、对照实验和计算资源段明确TGS在推理时选择并修正预测，基础模型参数不更新，因此归入Post-processing。这里修改的是推理过程，不是训练中的公平性正则。

核查与限制：已核对原始摘要及原文推理方法、评估和计算资源段；不是独立复现实验，基线调参及数据划分可能影响比较。

原始证据短引：

> No base-LLM parameters are updated in any experiment.

人工证据版本：32b1bc735b5c101fa3cf3e849d1e7f98dce9a59ca550500aafb5ab189d55f73b

## p-f4567d6da1046873aea0

[Refocusing algorithmic fairness on feature-level bias: A diagnostic approach using dutch EHR data.](https://europepmc.org/article/MED/42932339)

分类：Fairness Evaluation；Stage：Evaluation

中文判断：在具体住院风险预测任务中提出FL-BIAS特征层诊断框架，以公平性度量、Shapley分析和探索性中介分析定位差异，归入Evaluation与Bias mechanisms。迁移背景以Other标注，SES单独标注，不将迁移背景直接等同于种族。

核查与限制：已核对Europe PMC原始记录与摘要；迁移背景不是种族的直接测量，标签表示人口背景分组，不能将观察性中介分析称为已识别因果效应。

原始证据短引：

> we propose and apply a diagnostic framework termed Feature-Level Bias Identification And Sensemaking

人工证据版本：1fb62141d5b950d7e0240bf4c94e53279e189a5c573d726ff52894f9f2e95b40

## p-8aeef9186465b5deed36

[Improving the fairness and robustness of deep learning classification models through bias mitigation and post hoc calibration.](https://link.springer.com/article/10.1007/s11548-026-03805-x)

分类：In-processing；Stage：In-processing, Post-processing

中文判断：出版商原文显示CF-Net对抗训练和PMDN网络内特征残差化均参与训练优化，主要归入In-processing；训练后校准另以Post-processing标签保留。校准作用于CNN输出，不能把它误写成PMDN的必然串联步骤。

核查与限制：已核对出版商摘要、模型方法和结果段；AD组仍存在年龄关联，去混杂与校准指标不能等同于所有年龄组下游误差的平等。

原始证据短引：

> At inference, only confounding components are subtracted.

人工证据版本：c59178b6680da6122d7ee7151c85dfc0f9bb55da5770bf5ea99936950959468a

## p-59068cc978cafdc33230

[Responsible Quantum Machine Learning for Medical Imaging: A Fairness Audit Across Sensitive Subgroups](https://arxiv.org/abs/2610.37819)

分类：Fairness Evaluation；Stage：Evaluation, In-processing

中文判断：主要贡献是对经典与量子分类器进行医学亚组公平性审计，归入Fairness Evaluation；EO正则和梯度反转作为训练中干预对照保留In-processing标签。

核查与限制：已核对arXiv原始摘要；非劣性是在论文所设性能容忍界限下的判断，不代表临床有效性验证。

原始证据短引：

> All quantum models run in classical simulation; we claim no quantum advantage.

人工证据版本：1449e6c2ebb733993eaa6bc7566491963e0679520e31b25f25a70fa1de547032

## p-47f59ce8e66d8459e0e2

[Decision-Architecture Dependence and Patient-Gender-Conditioned Allocation in Large-Language-Model-Assisted Nursing Allocation: A Multi-Model Counterfactual Audit.](https://europepmc.org/article/MED/42940596)

分类：Fairness Evaluation；Stage：Evaluation

中文判断：针对具体护理人员分配任务进行性别反事实审计与决策架构敏感性分析，归入Fairness Evaluation。未提出或验证缓解方法，不赋予Mitigation标签。

核查与限制：已核对Europe PMC原始记录与摘要；候选标签、呈现顺序、评价顺序和模板锚定共同变化，不能声称单独证明位置偏差，也不能推广为全部LLM的结论。

原始证据短引：

> this pattern indicates Candidate-A dependence under the tested decision architecture

人工证据版本：ddd790c1ee716ea0c98f265a98861ea9259123e06b432c80b635e1c22576203f
