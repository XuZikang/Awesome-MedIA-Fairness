# 方法学检索策略验证 · 2026-11-09

检索改为9组主检索（偏差缓解、评估指标与基准、偏差机制／医学基础模型）及2组综述补充。主检索明确医疗与算法场景、公平性中心主题，并尽量排除综述发表类型和明显综述标题。未标注或题名不明显的综述仍可能进入主检索，需后续语义筛选。

11个查询均通过真实API语法与返回结果验证。以下命中数是各独立查询的返回总数，存在重叠，不能直接相加当作独立文献数。日期范围为2026-10-10至2026-11-09。

| 来源 | 检索通道 | 分组 | 查询命中数 |
|---|---|---|---|
| arxiv | methodology | 1 | 11 |
| arxiv | methodology | 2 | 8 |
| arxiv | methodology | 3 | 8 |
| europepmc | methodology | 1 | 3 |
| europepmc | methodology | 2 | 10 |
| europepmc | methodology | 3 | 2 |
| europepmc | review_supplement | 1 | 3 |
| pubmed | methodology | 1 | 7 |
| pubmed | methodology | 2 | 11 |
| pubmed | methodology | 3 | 3 |
| pubmed | review_supplement | 1 | 2 |

完整检索与去重后，待审核候选库为29条，其中28条为本轮新发现；原有1条缺摘要候选保留。

自动中文分析尝试8篇，Qoder均返回接口错误；探测确认本地额度已耗尽，服务器dfmodel路由当前不可用。保持Qoder配置，等待恢复，未切换到其他提供方。优先方法学导读由主控阅读摘要后另行整理，未伪称Qoder分析成功。

查询配置：[config/literature.json](../config/literature.json)；优先清单：[methodology-priority-2026-11-09.md](methodology-priority-2026-11-09.md)。
