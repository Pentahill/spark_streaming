离线计算和实时计算的区别：
1）数据来源：
    离线：hdfs 历史数据
    实时：消息队列（kafka),实时新增/修改记录
2）处理过程：
    离线：MapReduce(map + reduce)
    实时：Spark(DStream/SS)
3) 处理速度：
    离线：慢
    实时：快
    
流式框架：
1) Apache Storm
2) Apache Spark Streaming
3) Apache Kafka
4) Apache Flink


实时流处理流程：
（1）web,app访问请求
（2）webserver写日志（nginx)
（3）Flume收集日志
（4）放入Kafka,缓存日志(离线处理则放到hdfs)
（5）Spark/Storm处理
（6）结果写入数据库
（7）可视化展示


企业场景：
1）电信行业： 流量提醒
2）电商行业： 商品推荐












