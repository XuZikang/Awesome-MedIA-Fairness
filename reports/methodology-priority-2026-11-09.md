# 方法学候选优先导读 · 2026-11-09

本轮以方法学为主检索，回溯2026-10-10至2026-11-09。以下6篇基于已读取的原始摘要进行人工辅助整理，优先供你判断；不是全文审核完成或纳入批准。Qoder本轮返回额度限制，自动中文分析尚未完成。更新：用户于2026-11-09明确批准以下6篇；已核对原始证据并加入README。具体核查层级与判断见[收录证据](methodology-inclusion-evidence-2026-11-09.md)。

## p-25f166919d5808c5e366

[Detection and Validation of Hidden Subgroup Disparities in Clinical AI](https://arxiv.org/abs/2610.32362)

建议方向：Fairness Evaluation

方法要点：用学习到的表征发现隐藏亚组，在心脏扩大胸片分类任务中对比亚组性能差距与语义可解释性，并探索用发现的亚组标注改善偏差。

核查重点：这是亚组发现与验证方法，不是泛泛讨论公平性；需全文核对分割策略、亚组稳定性及缓解协议。

审核决定：纳入（用户明确批准，已收录）

## p-45778789f12c424e7649

[Trajectory-Guided Steering: Mitigating Spurious Feature Bias in Clinical Classification](https://arxiv.org/abs/2610.22618)

建议方向：Post-processing（推理时干预，协议待核对）

方法要点：利用模型在不同层的预测轨迹，按样本决定是否以及如何进行推理时修正；临床分类实验检查性别词替换引起的预测不一致。

核查重点：方法强调有选择的干预，而不是对所有样本统一修正；训练／冻结协议及跨模型结果仍需全文确认。

审核决定：纳入（用户明确批准，已收录）

## p-f4567d6da1046873aea0

[Refocusing algorithmic fairness on feature-level bias: A diagnostic approach using dutch EHR data.](https://europepmc.org/article/MED/42932339)

建议方向：Fairness Evaluation / Bias mechanisms

方法要点：提出FL-BIAS诊断框架，使用荷兰EHR与社会人口学信息，结合预测模型、特征归因和中介分析检查群体差异背后的特征层机制。

核查重点：需要区分特征归因和机制假说与已识别的因果效应；不能把潜在混杂下的中介结果视为已验证因果解释。

审核决定：纳入（用户明确批准，已收录）

## p-8aeef9186465b5deed36

[Improving the fairness and robustness of deep learning classification models through bias mitigation and post hoc calibration.](https://europepmc.org/article/MED/42891802)

建议方向：In-processing（兼有Post-processing）

方法要点：在阿尔茨海默病MRI分类中比较对抗训练与特征残差化，并进一步比较多种训练后概率校准方法。

核查重点：适合关注具体缓解机制；年龄编码减弱、概率校准改善与下游群体公平性是不同结论，应分别核查。

审核决定：纳入（用户明确批准，已收录）

## p-59068cc978cafdc33230

[Responsible Quantum Machine Learning for Medical Imaging: A Fairness Audit Across Sensitive Subgroups](https://arxiv.org/abs/2610.37819)

建议方向：Fairness Evaluation（含训练中缓解对照）

方法要点：比较经典与量子分类器在皮肤和胸片任务中的亚组公平性，并测试EO正则、梯度反转及组合干预，纳入相对基线的非劣性判断。

核查重点：全部量子模型运行在经典模拟中；更小的群体差距可能来自总体性能下降，不应据此宣称量子优势或临床有效。

审核决定：纳入（用户明确批准，已收录）

## p-47f59ce8e66d8459e0e2

[Decision-Architecture Dependence and Patient-Gender-Conditioned Allocation in Large-Language-Model-Assisted Nursing Allocation: A Multi-Model Counterfactual Audit.](https://europepmc.org/article/MED/42940596)

建议方向：Fairness Evaluation

方法要点：对多个LLM的护理任务分配做反事实审计，控制护士专业条件，改变A/B候选安排和患者性别，检查选择稳定性。

核查重点：候选标签、呈现顺序和模板锚定同时变化，不能将观测到的Candidate-A偏好单独归因为位置效应。

审核决定：纳入（用户明确批准，已收录）
