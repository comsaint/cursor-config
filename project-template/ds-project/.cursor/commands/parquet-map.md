請使用 DuckDB MCP 完成 parquet relationship mapping。

我會在這個 command 後面提供 1 個或多個 parquet 路徑。
每行一個路徑；也可能是 glob，例如：
- C:/path/to/file.parquet
- C:/path/to/folder/*.parquet

任務目標：
分析這些 parquet 之間的可能關係、粒度、鍵值、join 風險，並輸出 RELATIONSHIP_MAP.md 草稿。

工作流程：

1. 必須真的使用 DuckDB MCP。

2. 對每個 parquet：
   - 先看 schema
   - 抽樣看資料
   - 判斷資料粒度（例如 route-day、trip-level、customer-level、event-level）
   - 找出主鍵候選與外鍵候選

3. 跨檔比較時，請重點分析：
   - 同名欄位
   - 名稱不同但值域相似的欄位
   - ID 類欄位的 distinct / uniqueness 特徵
   - 日期欄位與時間欄位是否能對齊
   - 是否有明顯 1:1、1:N、N:1、N:N 關係
   - 是否可能是 fact table 與 dimension table
   - 是否存在 grain mismatch
   - 是否存在無法安全 join 的風險

4. 如有需要，可用下列方式思考與驗證：
   - DESCRIBE SELECT * FROM read_parquet('<path>');
   - 樣本 LIMIT 查詢
   - 對候選 key 做 distinct count / row count 比較
   - 對候選 join key 做小樣本 join 檢查

5. 最後輸出 RELATIONSHIP_MAP.md，格式如下：

# RELATIONSHIP_MAP.md

## Overview
- Input parquet(s):
- Mapping confidence:
- Major caveats:

## Dataset summary
| dataset_name | guessed_grain | row_count_estimate | primary_key_candidates | datetime_columns | notes |
|---|---|---:|---|---|---|

## Relationship candidates
| left_dataset | right_dataset | candidate_join_keys | guessed_cardinality | confidence | evidence | risks |
|---|---|---|---|---|---|---|

## Join recommendations
- Recommended joins:
- Joins needing human confirmation:
- Dangerous joins to avoid:
- Grain mismatch warnings:

## Open questions
- Q1
- Q2
- Q3

重要原則：
- 不要因為欄位同名就直接假設可 join。
- 對關係不確定時，明確標記 confidence = Low。
- 如果只有 1 個 parquet，也請輸出其 grain、主鍵候選、未來可能關聯欄位。
- 先給 relationship summary，再給完整 RELATIONSHIP_MAP.md。
