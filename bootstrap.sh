# 1. 安裝工具
pip install pre-commit ruff mypy pytest pytest-cov mutmut

# 2. 同步全域 rules
ln -sf ~/cursor-config/global/rules ~/.cursor/rules

# 3. 新專案時再複製 template，然後在專案根目錄設定套件名與 pytest 的 pythonpath：
#    cp -r ~/cursor-config/project-template/ds-project ~/work/my-new-project
#    cd ~/work/my-new-project
#    python configure_package.py my_package              # 預設 pythonpath=src
#    python configure_package.py my_package --pythonpath .