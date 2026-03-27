# INVESTIGATION_LOG

> 目的：記錄「調查過程與證據」，而不是最終決策。  
> 分工：正式決策寫到 `DECISION_LOG.md`；待辦寫到 `PLAN.md`；每輪摘要寫到 `STATUS.md`。

## 1) 使用規則（精簡）

- 一個「調查主題」一個 `INV-XXX`，可重複執行多次（`RUN-01`, `RUN-02`...）。
- 每次只要先填 6 段：`Question`、`Hypothesis`、`Data`、`Method`、`Findings`、`Next Actions`。
- 每個結論都要有證據路徑（表、圖、SQL、notebook）。
- 若結果影響決策，標註 `Decision needed: Yes` 並同步 `DECISION_LOG.md`。

---

## 2) Investigation Index（主題總覽）


| inv_id  | topic                               | owner      | status (open/monitoring/closed) | first_opened | last_run_date | run_count | priority | decision_needed |
| ------- | ----------------------------------- | ---------- | ------------------------------- | ------------ | ------------- | --------- | -------- | --------------- |
| INV-001 | Phase 1.4 閾值診斷（load_factor 分布與候選路線） | longp / DS | monitoring                      | 2026-03-19   | 2026-03-19    | 1         | H        | Yes             |


---

## 3) Run History（每次執行一列）


| run_id  | inv_id  | date       | trigger            | data_window                         | method_short                                            | key_finding_short        | confidence (L/M/H) | outcome (continue/close/escalate) | artifact_path                                  |
| ------- | ------- | ---------- | ------------------ | ----------------------------------- | ------------------------------------------------------- | ------------------------ | ------------------ | --------------------------------- | ---------------------------------------------- |
| RUN-001 | INV-001 | 2026-03-19 | 完成 PLAN 1.4 後的結果確認 | 2024-01-01 ~ 2025-12-31（bucket 聚合後） | Route-level quantiles + histogram bins + candidate rule | 12 路線方向全數非候選；建議閾值維持 0.95 | H                  | continue                          | `demand_forecast/artifacts/reports/threshold/` |


---

## 4) Investigation Entry Template（每個主題一段）

### INV-XXX — `<topic>`

- Owner:
- Status: open / monitoring / closed
- Priority: H / M / L
- Related files/tables:
- Related plan item:
- Related decision:

#### Question

- 本次要回答的核心問題：

#### Hypothesis

- H1:
- H2:

#### Scope & Data

- 分析期間：
- 粒度：
- 主要資料來源：
- 排除範圍 / 限制：

#### Latest Run (RUN-XXX)

- Date:
- Trigger:
- Method (SQL/Python/Chart):
- Findings:
  - F1:
  - F2:
- Evidence:
  - `path/to/table_or_chart`
  - `path/to/notebook_or_sql`

#### Interpretation (optional)

- 代表意義：
- 不確定性：

#### Next Actions

- Action 1
- Action 2

#### Handoff

- Decision needed: Yes / No
- Plan update needed: Yes / No
- Status update needed: Yes / No

---

## 5) 快速檢查清單

- 是否有 `inv_id` 與 `run_id`。
- 是否有可重現的資料期間與方法。
- 是否有至少一個可追溯證據路徑。
- 是否明確寫出下一步與 owner。

---
