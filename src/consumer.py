from pulsar import Client

# 创建 Pulsar 客户端
client = Client("pulsar://localhost:6650")

# 订阅主题
consumer = client.subscribe("eew", "my-subscription")

try:
    while True:
        # 接收消息
        msg = consumer.receive()

        try:
            message = msg.data().decode("utf-8")
            # 处理消息
            print(f"Received message: {message}")

            # 手动确认消息
            consumer.acknowledge(msg)
        except Exception as e:
            # 处理消息时出现错误
            print("Error processing message: {}".format(e))
            consumer.negative_acknowledge(msg)
except KeyboardInterrupt:
    # 用户按下 Ctrl+C 停止订阅
    pass

# 关闭 Pulsar 客户端连接
client.close()
