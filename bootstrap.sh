# 1. 安裝工具
pip install pre-commit ruff mypy pytest pytest-cov mutmut

# 2. 同步全域 rules
ln -sf ~/cursor-config/global/rules ~/.cursor/rules

# 3. 新專案時再複製 template
cp -r ~/cursor-config/project-template/ds-project ~/work/my-new-project