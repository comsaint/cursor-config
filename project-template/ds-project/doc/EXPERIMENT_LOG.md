# EXPERIMENT_LOG

> 目的：系統化記錄每次實驗的假設、設定、結果與決策，確保可重現性並避免重複踩坑。  
> 原則：每次實驗一筆，不只記「結果」，也要記「為何這樣做」。

## 1) 文件中繼資訊

| 欄位 | 內容 |
| --- | --- |
| 專案名稱 |  |
| 文件 Owner |  |
| 最後更新時間 |  |
| 版本 | v0.1 |
| 任務類型 | 時序預測（可改） |
| 主要評估指標 | 例：WAPE、MAE、RMSE |

## 2) 實驗總覽表（Index）

| exp_id | date | objective/hypothesis | data_version | feature_set_version | model_family | primary_metric | result | decision (promote/reject/hold) | run_artifacts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EXP-0001 |  |  |  |  |  |  |  |  |  |

## 3) 單次實驗模板（每次複製一段）

---
### EXP-XXXX：`<短標題>`

#### A. 背景與假設
- 問題描述：
- 實驗假設（可被驗證）：
- 預期改善方向與幅度：
- 失敗判定條件：

#### B. 可重現設定（Reproducibility）
| 欄位 | 值 |
| --- | --- |
| run_datetime |  |
| operator |  |
| code_version (git commit) |  |
| random_seed |  |
| python_version |  |
| dependency_lock |  |
| hardware_env |  |
| runtime_budget | 例：<= 2 hr / <= 16 GB RAM |

#### C. 資料與切分
| 項目 | 內容 |
| --- | --- |
| data_source |  |
| training_window |  |
| validation_window |  |
| test_window |  |
| split_strategy | 例：time-based rolling |
| leakage_check |  |
| sample_count |  |
| missing_ratio_summary |  |

#### D. 特徵設定
| 項目 | 內容 |
| --- | --- |
| feature_set_version |  |
| included_features |  |
| excluded_features_and_reason |  |
| feature_engineering_steps |  |
| scaling/encoding_strategy |  |
| feature_selection_strategy |  |

#### E. 模型與超參數
| 項目 | 內容 |
| --- | --- |
| model_family |  |
| objective/loss |  |
| hyperparameters |  |
| early_stopping |  |
| training_time |  |
| peak_memory_usage |  |

#### F. 結果（整體 + 切片）
| 指標 | train | val | test | baseline | delta_vs_baseline |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

切片分析（建議）：  
- 路線別：  
- 平/假日：  
- 尖峰/離峰：  
- 低量體 route：

#### G. 誤差分析與異常樣本
- Top error cases（含案例連結）：
- 可能成因：
- 是否涉及資料品質問題：

#### H. 風險與成本
- 計算成本（時間/記憶體）：
- 推論延遲風險：
- 上線風險：
- 監控需求（drift、資料延遲）：

#### I. 結論與決策
- 結論（1-3 句）：
- 決策：`promote` / `reject` / `hold`
- 採用或淘汰理由：
- 下一步：

#### J. 產出物（Artifacts）
- 模型檔案：
- 訓練 log：
- 指標報表：
- Notebook / Script：
- 相關 PR / Issue：

---

## 4) 撰寫規範

- 每次 run 完成當天更新，避免事後回填造成資訊遺失。
- 指標必須附 baseline 與 delta，不記「單點數字」。
- 失敗實驗也必須記錄，尤其是「失敗原因」與「不再嘗試條件」。
- 若資源成本過高（時間或 RAM），需記錄優化方案或停損條件。

## 5) 參考最佳實務（摘要）

- 先寫假設再跑實驗，可避免結果導向的事後合理化。
- 實驗紀錄至少要能重建：資料版本、程式版本、隨機種子、超參數、環境。
- 必須保留決策脈絡（為何採用/淘汰），不只保留分數。
- 建議設置總覽表，讓團隊快速比較不同實驗與版本演進。
