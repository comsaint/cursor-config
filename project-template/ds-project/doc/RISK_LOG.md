# RISK_LOG

> 目的：管理專案中的風險、假設、依賴與觸發條件，避免知識遺失並提早做出緩解。  
> 建議：每週固定 review，一旦發生重大變更（資料源、需求、模型策略）立即更新。

## 1) 文件中繼資訊

| 欄位 | 內容 |
| --- | --- |
| 專案名稱 |  |
| 文件 Owner |  |
| 最後更新時間 |  |
| 版本 | v0.1 |
| 會議節奏 | 例：每週風險檢視會 |
| 升級通報機制 | 例：Slack / Email / Standup |

## 2) 評分標準（固定）

### 2.1 Likelihood（機率）
- 1：極低（<10%）
- 2：低（10-30%）
- 3：中（30-60%）
- 4：高（60-80%）
- 5：極高（>80%）

### 2.2 Impact（衝擊）
- 1：可忽略（幾乎無業務影響）
- 2：輕微（局部影響，可快速修正）
- 3：中等（影響一個流程或里程碑）
- 4：重大（影響多流程或上線時程）
- 5：嚴重（關鍵決策失準或服務中斷）

### 2.3 Risk Score
`risk_score = likelihood * impact`  
建議分級：`1-6: Low`、`8-12: Medium`、`15-25: High`

## 3) 風險登錄表（Risk Register）

| risk_id | date_logged | category | risk_statement | trigger_condition | likelihood | impact | risk_score | owner | mitigation_plan | contingency_plan | status (open/monitoring/closed) | target_date | last_reviewed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R-001 |  | Data Quality |  |  |  |  |  |  |  |  |  |  |  |

### 常見 category 建議
- Data Quality
- Data Availability
- Feature Drift / Concept Drift
- Modeling / Evaluation
- Infrastructure / MLOps
- Business / Process
- Compliance / Privacy

## 4) 假設清單（Assumptions Log）

| assumption_id | date_logged | assumption | rationale | validation_method | validation_date | if_false_impact | owner | status (untested/valid/invalid) | related_risk_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 |  |  |  |  |  |  |  |  |  |

## 5) 依賴清單（Dependencies）

| dependency_id | dependency_description | type (team/system/data/vendor) | required_by | owner | failure_impact | fallback |
| --- | --- | --- | --- | --- | --- | --- |
| D-001 |  |  |  |  |  |  |

## 6) 失效條件（Failure Modes）

| failure_mode_id | scenario | early_warning_signal | detection_metric | threshold | immediate_action | owner |
| --- | --- | --- | --- | --- | --- | --- |
| F-001 |  |  |  |  |  |  |

## 7) 變更與審查紀錄

| review_date | participants | key_updates | escalations | decisions | next_review_date |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 8) 檢查清單（每次 review）

- [ ] 新風險是否完成 owner 指派。
- [ ] High 風險是否有 mitigation 與 contingency。
- [ ] 重要假設是否有驗證日期與方法。
- [ ] 既有風險分數是否因新事實而調整。
- [ ] 是否需要更新 `RUNBOOK.md` 與 `EVAL_REPORT.md`。

## 9) 參考最佳實務（摘要）

- 風險描述應具體且可觸發（包含 trigger condition），避免模糊敘述。
- 每個風險都要有 owner 與 target date，否則不易落地。
- 假設必須可驗證，並明確「若假設錯誤」的影響與對策。
- AI/預測專案要額外關注 drift、偏差、公平性與資料穩定性風險。
