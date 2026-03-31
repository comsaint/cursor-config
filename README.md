# cursor-config
Cursor 設定倉庫，用來在不同機器之間同步我的 AI 開發習慣、資料科學專案模板、常用 commands、以及 MCP 設定。

此 repo 的設計原則：

- **Global rules 保持精簡**：只放所有專案都適用的常駐規範。
- **Commands 保持手動觸發**：像 `build`、`review`、`test-*`、`cycle_code`、`parquet-*` 這類流程，不在每次小改動時自動啟動。
- **Project template 開箱即用**：新資料科學專案可直接複製模板，包含 rules、commands、pre-commit、pyproject、文件模板。
- **跨機器同步**：透過 Git 管理，讓新機器快速完成相同設定。

---

## Repo Structure

```text
cursor-config/
├── README.md
├── bootstrap.sh
│
├── global/
│   ├── AGENTS_GLOBAL.md
│   ├── mcp.json
│   ├── rules/
│   │   ├── 00-base.mdc
│   │   └── 10-python-quality.mdc
│   └── commands/
│       ├── build.md
│       ├── review.md
│       ├── test-write.md
│       ├── test-fix.md
│       ├── cycle_code.md
│       ├── parquet-dict.md
│       └── parquet-map.md
│
└── project-template/
    └── ds-project/
        ├── .cursor/
        │   ├── rules/
        │   │   ├── ds-core.mdc
        │   │   ├── ds-data.mdc
        │   │   └── ds-ml.mdc
        │   └── commands/
        │       ├── build.md
        │       ├── review.md
        │       ├── test-write.md
        │       ├── test-fix.md
        │       ├── cycle_code.md
        │       ├── parquet-dict.md
        │       └── parquet-map.md
        ├── .pre-commit-config.yaml
        ├── pyproject.toml
        ├── PLAN.md
        ├── STATUS.md
        ├── DECISION_LOG.md
        └── doc/
            ├── DATA_DICTIONARY.md
            ├── EVAL_REPORT.md
            ├── EXPERIMENT_LOG.md
            ├── INVESTIGATION_LOG.md
            ├── RISK_LOG.md
            └── RUNBOOK.md
```

---

## What goes where?

### `global/rules/`
放**所有專案都適用**的全域規範，例如：

- 預設語言與回覆風格
- 保留 type hints / docstrings
- 小改動優先，不亂重構
- 品質工具存在，但不要每輪都自動跑

這些規則應該短小、穩定、長期有效。

### `global/commands/`
放**需要時才手動執行**的流程型 prompts，例如：

- `/build`
- `/review`
- `/test-write`
- `/test-fix`
- `/cycle_code`
- `/parquet-dict`
- `/parquet-map`

這些不是常駐規則，而是可重複呼叫的工作流。

### `project-template/ds-project/`
放**新的資料科學專案模板**。建立新專案時直接複製這個目錄即可，裡面已包含：

- DS 專案專用 rules
- 常用 commands
- pre-commit hooks
- `pyproject.toml`
- `PLAN.md` / `STATUS.md` / `DECISION_LOG.md`
- 文件模板

---

## New machine setup

先 clone 此 repo：

```bash
git clone https://github.com/comsaint/cursor-config ~/cursor-config
cd ~/cursor-config
```

執行 bootstrap：

```bash
bash bootstrap.sh
```

`bootstrap.sh` 建議負責以下事情：

- 安裝 Python 品質工具：`pre-commit`、`ruff`、`mypy`、`pytest`、`pytest-cov`、`mutmut`
- 同步 `global/rules/` 到本機 Cursor 全域 rules 位置
- 準備 Git template 或其他本機初始化設定
- 提醒使用者填入 MCP 所需的 token / path

---

## Create a new data science project

從模板建立新專案：

```bash
cp -r ~/cursor-config/project-template/ds-project ~/work/my-ds-project
cd ~/work/my-ds-project
git init
```

安裝 hooks：

```bash
pre-commit install
pre-commit install --hook-type pre-push
```

之後依需求修改：

- `pyproject.toml`
- `.pre-commit-config.yaml`
- `.cursor/rules/*.mdc`
- `PLAN.md`
- `STATUS.md`
- `DECISION_LOG.md`

---

## Quality workflow

本模板的預設策略：

### Co