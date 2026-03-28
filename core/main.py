import openclaw_sdk as oc
import time

# 初始化 OpenClaw 本地代理
agent = oc.Agent(config_path="config.yaml")

@agent.on_message(source="wechat")
def handle_billing(msg):
    # 1. 语义提取：调用本地大模型解析指令
    # 示例输入："记账：刚才喝了杯拿铁，25块，微信付的"
    raw_text = msg.content
    print(f"收到指令: {raw_text}")

    # 调用内置解析模块
    billing_data = agent.ai_parser.extract_fields(
        text=raw_text,
        fields=["item", "amount", "category", "payment_method"]
    )

    # 2. 结构化数据映射
    # 自动补充日期并进行分类
    record = {
        "日期": time.strftime("%Y-%m-%d"),
        "项目": billing_data["item"],
        "金额": float(billing_data["amount"]),
        "类别": billing_data["category"] or "日常消费",
        "支付方式": billing_data["payment_method"] or "未指定",
        "状态": "✅ 已入账"
    }

    # 3. 自动入账执行
    try:
        # 联动 Notion API
        agent.notion.add_row(database_id=agent.config.database_id, data=record)
        
        # 4. 反馈给用户
        agent.wechat.send_reply(f"🚀 记账成功！已存入 Notion：{record['项目']} - {record['金额']}元")
    except Exception as e:
        agent.wechat.send_reply(f"❌ 入账失败，请检查网络或配置：{str(e)}")

if __name__ == "__main__":
    agent.run()