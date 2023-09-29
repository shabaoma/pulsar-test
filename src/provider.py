from pulsar import Client

# 创建 Pulsar 客户端
client = Client("pulsar://localhost:6650")

# 创建生产者
producer = client.create_producer(topic="eew")

# 发送消息
while True:
    try:
        message = "配信数据".encode("utf-8")
        producer.send(message)
    except Exception as e:
        print(e)
