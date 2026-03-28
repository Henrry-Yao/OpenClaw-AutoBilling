# 📂 OpenClaw 自动化记账脚本

本方案展示了如何将 **微信指令 -> AI 语义解析 -> Notion 自动入账** 完整串联。

## 🛠️ 使用步骤
1. **获取 Notion 凭证**：在 Notion 开发者后台创建 Integration 并邀请至你的 Database。
2. **准备环境**：
   - 安装 Python 3.8+
   - 运行 `pip install -r requirements.txt`
3. **配置文件**：
   - 将 `config/config.example.yaml` 复制并重命名为 `config.yaml`。
   - 填入你的 `token` 和 `database_id`。
4. **启动程序**：
   - 运行 `python core/main.py`
   - 对着微信发送：“记账：刚才喝了杯拿铁，25块，微信付的”

## 💡 提示
本脚本推荐配合本地 **Ollama** 运行，以保障账单隐私安全。
