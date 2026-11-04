# 主目录筛选判断证据

机器建议及中文证据，仅供审核；必须由维护者明确通过后才加入主 README。请填写 review-latest.md 或按文章编号回复助手。

## Explainable Machine Learning for 30-Day Hospital Readmission Risk Prediction in Patients with Diabetes: A Comparative Analysis of Model Performance and Algorithmic Fairness

年度：2026；主题：Fairness Evaluation and Benchmarking、Bias Mechanisms and Measurement、EHR, Physiological Signals and Healthcare

```markdown
- (*Paper'26*) **Explainable Machine Learning for 30-Day Hospital Readmission Risk Prediction in Patients with Diabetes: A Comparative Analysis of Model Performance and Algorithmic Fairness**
  [[📝 Paper](https://europepmc.org/article/PPR/PPR1351995)]
  **Metadata:** `Domain: EHR and clinical prediction` · `Focus: Evaluation` · `Stage: Evaluation` · `Attributes: Race and ethnicity + Sex and gender + Age` · `Assets: Paper only` · `Evidence: Primary full text`
  > **Why it qualifies:** 全文为原始研究，完成糖尿病30天再入院机器学习预测，并按种族、性别和年龄报告召回差距，符合任务特定公平性评估的纳入标准。
```

### 方法证据

- medical：predict which diabetic inpatients are most likely to be readmitted within 30 days
- algorithm：We tested baseline Logistic Regression, tuned Logistic Regression, tuned Decision Tree, and tuned Random Forest in this project.
- fairness：We audited model performance across race, gender, and age groups because these are sensitive attributes directly related to fairness.
- groups：across race, gender, and age groups
- evaluation：Table 2 shows recall gaps across race, gender, and age groups.

[全文证据](https://www.researchsquare.com/article/rs-11517784/v1.pdf)
