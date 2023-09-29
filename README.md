# pulsar-test

## docker pull
docker pull apachepulsar/pulsar-standalone

## 启动
docker run -d -p 6650:6650 -p 8080:8080 --name pulsar-standalone apachepulsar/pulsar-standalone
docker stop pulsar-standalone
docker rm pulsar-standalone

## 查看集群列表
docker exec -it pulsar-standalone /bin/bash
/pulsar/bin/pulsar-admin clusters list
