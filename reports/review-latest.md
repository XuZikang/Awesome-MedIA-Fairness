# 每周文献人工审核单 · 2026-11-04

请只修改每篇的“审核决定”和“审核备注”：待审核 / 通过 / 排除 / 暂缓。编号和证据版本请保留。
填写后将此 Markdown 文件交给助手，或在聊天中按编号给出决定；只有明确通过的文章才会进入 README。
模型建议不是你的审核决定；证据不足的通过项仍需补核原文。

## p-11a0ba65de9fc94bbcd8

文章：[Navigating the cultural iceberg: Addressing algorithmic bias, hallucination, and semantic flattening in AI-assisted qualitative thematic analysis.](https://pubmed.ncbi.nlm.nih.gov/42721502/)

审核决定：待审核
审核备注：
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

## p-2ffe88b3f5427706252d

文章：[Explainable Machine Learning for 30-Day Hospital Readmission Risk Prediction in Patients with Diabetes: A Comparative Analysis of Model Performance and Algorithmic Fairness](https://europepmc.org/article/PPR/PPR1351995)

审核决定：暂缓
审核备注：需要你确定一下内容是否与 fairness 相关
证据版本：b3961054455fa87924d688109052482cfeb7bbedf5eb7cc5be2b12c8d9bd89b3

模型建议：suggest_include

中文概述：基于UCI糖尿病130家医院数据，比较逻辑回归、决策树和随机森林预测30天再入院，并按种族、性别、年龄审计召回差距；随机森林召回最高但种族差距最大。

纳入判断：全文为原始研究，完成糖尿病30天再入院机器学习预测，并按种族、性别和年龄报告召回差距，符合任务特定公平性评估的纳入标准。

限制：仅使用单一回顾性数据集，未提出或比较公平性缓解方法，也未进行外部验证；公平性分析主要报告召回差距。

建议分类：Evaluation

证据：
- medical：predict which diabetic inpatients are most likely to be readmitted within 30 days
- algorithm：We tested baseline Logistic Regression, tuned Logistic Regression, tuned Decision Tree, and tuned Random Forest in this project.
- fairness：We audited model performance across race, gender, and age groups because these are sensitive attributes directly related to fairness.
- groups：across race, gender, and age groups
- evaluation：Table 2 shows recall gaps across race, gender, and age groups.

[分析原文](https://www.researchsquare.com/article/rs-11517784/v1.pdf)

人工原文补查：已核查Research Square全文§7.2与Table 2，明确比较race/gender/age的recall gap，范围相关；模型偏差并未被消除，仍等你决定。详见 held-scope-audit-2026-11-04.md。

## p-cb6eb929d7f879132fb0

文章：[Fairness-Aware Design for Contextual Experiments: Guaranteeing Reliability and Equity in Heterogeneous Subgroups](https://arxiv.org/abs/2611.01867)

审核决定：暂缓
审核备注：你确认一下是否与 medical 相关
证据版本：待取得有效分析

模型建议：待分析／原分析已过期

人工原文补查：已核查arXiv全文；有临床试验数据，但奖励为试验研究结果是否发布，而非患者临床结局，属于边界相关方法学，继续暂缓。详见 held-scope-audit-2026-11-04.md。

