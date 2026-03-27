# DATA_DICTIONARY
> 目的：建立單一可信欄位定義（Single Source of Truth），降低欄位誤解、口徑不一致與資料品質風險。  
> 適用範圍：`demand_forecast` 專案所有輸入、特徵、中繼與輸出資料表。
## 1) 文件中繼資訊
| 欄位 | 內容 |
| --- | --- |
| 專案名稱 |  |
| 文件 Owner |  |
| 技術 Owner |  |
| 最後更新時間 |  |
| 版本 | v0.1 |
| 更新頻率 | 例：每次 schema 變更 / 每週例行檢視 |
| 相關文件 | `README.md`、`SPEC.md`、`RISK_LOG.md`、`RUNBOOK.md` |
## 2) 命名與標準（建議固定）
### 2.1 命名規範
- `snake_case` 命名（table、column、feature 一致）。
- 時間欄位以 `_ts`（timestamp）或 `_date`（date）結尾。
- 布林欄位以 `is_` / `has_` 開頭。
- ID 欄位命名統一（例：`route_id`、`stop_id`、`service_id`）。
### 2.2 型別與可空值規範
- 明確標註型別（`int`、`float`、`string`、`date`、`datetime`、`boolean`）。
- 明確標註可空值（`nullable: yes/no`）。
- 對關鍵欄位（主鍵、時間、目標變數）預設不可空，若可空需說明原因。
### 2.3 值域與商業規則
- 欄位需定義允許值、上下界或 enum（例：`dow` 只能 1~7）。
- 必要時補充跨欄位規則（例：`service_end_date >= service_start_date`）。
## 3) Dataset 登錄表
| dataset_name | 層級 (raw/staging/feature/mart) | 粒度 | 主鍵 | 時間欄位 | 更新頻率 | 上游來源 | owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
## 4) 欄位字典（核心模板）
> 每個資料表各自建立一段；欄位多時可拆為多個小表，避免單表過長難維護。
### 4.1 表：`<table_name>`
| column_name | business_definition | data_type | nullable | allowed_values_or_range | default_value | example | key_type (PK/FK/none) | pii | source_column | transform_logic | dq_rules | freshness_sla | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#### 補充（可選）
- 表用途：
- 粒度：
- 與其他表關聯：
- 已知限制：
## 5) 資料品質規則（DQ Rulebook）
| rule_id | table | rule_description | severity (P0/P1/P2) | check_sql_or_logic | threshold | owner | alert_channel | action_if_failed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DQ-001 |  |  |  |  |  |  |  |  |
### 常見規則建議
- 完整性：關鍵欄位 `NULL` 比例不得超過閾值。
- 唯一性：主鍵不可重複。
- 合法性：值域、格式需符合定義。
- 一致性：跨表對帳（筆數、聚合）差異在允許範圍內。
- 新鮮度：資料延遲不得超過 SLA。
## 6) 版本與變更紀錄（Schema Change Log）
| change_date | changed_by | table/column | change_type (add/modify/drop) | backward_compatible (Y/N) | migration_plan | impacted_jobs/models | approved_by |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
## 7) 維運檢查清單（每次更新請確認）
- [ ] 新增/修改欄位是否已更新本文件。
- [ ] 相關 pipeline 與特徵工程程式是否同步更新。
- [ ] DQ 規則是否新增或調整。
- [ ] 下游模型/報表是否完成相容性驗證。
- [ ] `RISK_LOG.md` 是否需新增風險。
## 8) 參考最佳實務（摘要）
- 資料字典要同時覆蓋「技術定義 + 商業定義 + 品質規則」，不可只列欄位名稱。
- 一定要有 owner、版本、變更紀錄，避免定義漂移。
- 欄位需定義允許值/值域與可空策略，降低模型輸入污染風險。
- 建議把 DQ 規則直接內嵌於字典，讓文件可以直接轉成資料驗證任務。