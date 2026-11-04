# 目录更新草稿

仅含全文证据支持的机器纳入建议。人工审核后，再同步年度目录与 By Topic；本程序不改写 README。

## Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、Pre-processing Mitigation、Post-processing Mitigation、Clinical NLP and Foundation Models、EHR, Physiological Signals and Healthcare

```markdown
- (*arXiv'26*) **Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems**
  [[📝 Paper](https://arxiv.org/abs/2610.38215)]
  **Metadata:** `Domain: Clinical NLP and foundation models` · `Focus: Evaluation + Bias mechanisms + Mitigation` · `Stage: Pre-processing` · `Attributes: Race and ethnicity + Sex and gender` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文报告了临床多智能体LLM的公平性实证审计与缓解：包含急诊分诊任务、模型与拓扑评估、种族和性别反事实组以及20格实证测量，满足五项纳入标准。
```

### 方法证据

- algorithm：five model families and four aggregation topologies
- evaluation：We ran the ensemble in all 20 cells
- fairness：the disparity is relocated, never removed
- groups：Race and sex enter the experiments as single explicit tokens
- medical：You are an emergency medicine physician evaluating a patient in the ED

[全文证据](https://arxiv.org/html/2610.38215v1)

## A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering

年度：2026；主题：Bias Mechanisms and Measurement、In-processing Mitigation、EHR, Physiological Signals and Healthcare

```markdown
- (*arXiv'26*) **A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering**
  [[📝 Paper](https://arxiv.org/abs/2611.00298)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Bias mechanisms + Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Race and ethnicity` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文包含临床 UTI 预测任务、TabPFN 算法、反事实公平问题、种族敏感属性和实证测量，五个纳入证据均具备，故建议纳入。
```

### 方法证据

- algorithm：We instantiate the framework on a single-estimator classifier, TabPFN v2
- evaluation：We evaluate on two real-world tabular benchmarks with distinct domains
- fairness：We propose a framework, Mechanistic Interpretability for Counterfactual Fairness (MICF)
- groups：a binary race variable as the sensitive feature
- medical：UTICalc, a clinical urinary tract infection risk model shown to have significant racial bias

[全文证据](https://arxiv.org/html/2611.00298v1)

## Fairness Metrics based on the AUC in Clinical Predictive AI

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement

```markdown
- (*arXiv'26*) **Fairness Metrics based on the AUC in Clinical Predictive AI**
  [[📝 Paper](https://arxiv.org/abs/2611.05222)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation + Theory and measurement` · `Stage: Evaluation` · `Attributes: Sex and gender` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 该文针对临床预测AI的AUC公平性指标开展正式分析与模拟测量，明确以性别定义亚组并比较组内/跨组差异，满足临床任务、算法评估、公平性问题和实证评价五项标准。
```

### 方法证据

- algorithm：Clinical prediction models using artificial intelligence (AI)
- evaluation：We then illustrate their behaviour using simulations based on the EuroSCORE II
- fairness：We examine eight AUC-based fairness metrics proposed in the literature
- groups：defined by patient sex at birth (binary sensitive attribute)
- medical：clinical prediction models for binary outcomes

[全文证据](https://arxiv.org/html/2611.05222v1)
