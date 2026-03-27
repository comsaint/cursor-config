# EVAL_REPORT

> 目的：在每個里程碑提供可決策的模型評估報告，涵蓋驗證設計、切片表現、業務影響、風險與下一步。  
> 場景：模型升級、重新訓練、版本比較、對 PM/業務匯報。

## 1) 報告中繼資訊

| 欄位 | 內容 |
| --- | --- |
| 報告名稱 |  |
| 專案 |  |
| 報告日期 |  |
| 模型版本 |  |
| 評估負責人 |  |
| 審閱者 |  |
| 對比 baseline 版本 |  |
| 決策狀態 | draft / approved / rejected |

## 2) Executive Summary（先給決策）

- 核心結論（1-3 句）：
- 是否建議上線：`yes/no/conditional`
- 關鍵收益（例：WAPE 改善、覆蓋率提升）：
- 主要風險（例：特定 route 退化）：
- 建議決策與條件（例如需先補監控）：

## 3) 評估範圍與目標

| 項目 | 內容 |
| --- | --- |
| 預測目標變數 |  |
| 預測範圍（horizon） |  |
| 評估期間 |  |
| 評估粒度 | 例：route x day |
| 使用資料版本 |  |
| 不在本次範圍內 |  |

## 4) 驗證設計（Validation Design）

### 4.1 資料切分
| 項目 | 內容 |
| --- | --- |
| split strategy |  |
| train window |  |
| validation window |  |
| test window |  |
| leakage controls |  |

### 4.2 對照組設定
| model_name | type (baseline/candidate) | notes |
| --- | --- | --- |
|  |  |  |

## 5) 主要結果（整體）

| metric | baseline | candidate | delta | pass_criteria | pass/fail |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 6) 切片結果（必填）

> 至少包含：路線別、平/假日、尖離峰、需求量級分組。

| slice_dimension | slice_value | baseline_metric | candidate_metric | delta | sample_size | note |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## 7) 回測與穩定性分析

| 項目 | 內容 |
| --- | --- |
| backtesting_method |  |
| rolling windows count |  |
| performance variability |  |
| worst_period |  |
| exceptional_days_behavior |  |

### 建議附圖（可連結檔案）
- 實際值 vs 預測值趨勢圖
- 誤差分布圖（含長尾）
- 各切片指標對比圖
- 版本比較表

## 8) 業務影響評估

| 指標 | baseline | candidate | impact_estimate | 假設條件 |
| --- | --- | --- | --- | --- |
| 例：人力排班偏差成本 |  |  |  |  |

- 成本面（訓練成本 / 推論成本）：
- 效益面（準點率、調度品質、作業效率）：
- 風險面（錯誤決策成本）：

## 9) 風險、限制與監控計畫

| risk_id | risk_description | severity | mitigation | monitoring_metric | owner |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

- 已知限制：
- 失效條件（何時模型可能失效）：
- 上線後觀測期與門檻：

## 10) 決策與後續行動

| action_item | owner | due_date | status |
| --- | --- | --- | --- |
|  |  |  |  |

- 最終建議：`promote` / `hold` / `rollback`
- 若 `hold`：需補齊條件
- 若 `rollback`：回退版本與觸發條件

## 11) 附錄

- 指標計算定義：
- 資料品質檢查摘要：
- 實驗與模型 artifacts 連結：
- 相關文件：`EXPERIMENT_LOG.md`、`RISK_LOG.md`、`RUNBOOK.md`

## 12) 參考最佳實務（摘要）

- 評估報告必須同時含「整體 + 切片 + 穩定性」，避免平均指標掩蓋風險。
- 除技術指標外，應固定呈現成本/延遲/業務影響，支援跨角色決策。
- 報告應以決策導向撰寫（是否上線、條件是什麼），而非僅羅列分數。
