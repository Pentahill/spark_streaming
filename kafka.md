消息队列：
    生产者
    消费者
    数据： 数据流/消息
    
核心概念：
    producer:
    consumer:
    broker:
    topic:
    
windows:
1) 启动
    kafka-server-start E:\\kafka_2.11-2.4.0\\config\\server.properties
2） 创建topic
     kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic hello_topic
3) 查看topic
    kafka-topics --list --bootstrap-server localhost:9092
3) 订阅topic
    kafka-console-consumer --bootstrap-server localhost:9092 --topic hello_topic --from-beginning
4) 发送消息
    kafka-console-producer --broker-list localhost:9092 --topic hello_topic