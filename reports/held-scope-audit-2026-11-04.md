# 两篇暂缓文章的原文补查 · 2026-11-04

两篇均保持维护者的“暂缓”决定。全文相关性核验不等于已获准纳入。

## 糖尿病患者30天再入院预测

[Research Square 原文](https://www.researchsquare.com/article/rs-11517784/v1.pdf)明确使用 UCI 糖尿病住院数据，比较多个模型，并在 §7.2 和 Table 2 按 race、gender、age 报告 recall gap。这是实际的临床预测公平性审计，并非仅在标题中提及 fairness。原文还显示模型选择存在总体召回率与群体差距之间的取舍，不能写成已成功消除偏差；它仍是预印本。

短证据：`We audited model performance across race, gender, and age groups`；表题为 `Fairness Audit Across Models by Recall Gap`。

建议：范围相关，可考虑纳入 Fairness Evaluation；等待你的最终决定。新规则下 Qoder 全文分析也建议纳入，本次不据此替代人工批准。

## Fairness-Aware Design for Contextual Experiments

[arXiv 原文](https://arxiv.org/pdf/2611.01867)是公平约束下的自适应实验设计方法，包含理论与合成实验，也使用 COVID-19 Clinical Trials 数据。真实数据实验根据试验级 Gender、Age、Phase 定义上下文，并按干预类别分配；奖励是研究结果是否发布，而非患者诊断、预后或治疗反应。

短证据：`Contexts are defined by study Gender, Age, and Phase`；`The reward is whether study results are posted (1) or not (0)`。

建议：方法学和临床试验研究相关，但与患者级医疗算法公平性的边界需由你决定，继续暂缓。Qoder 对本篇的自动全文分析未通过短引句精确匹配校验，未保存为有效机器结论；以上为主控重新检查原始 PDF 后的判断。
