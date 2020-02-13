Flume:
1) 收集，聚合，移动日志数据。
2）竞品： Logstash

windows:
1) flume-ng agent \ 
    --name a1 \
    --conf E:\apache-flume-1.9.0-bin\conf \
    --conf-file E:\apache-flume-1.9.0-bin\conf\exec-memory-avro.properties \
    -property  "flume.root.logger=INFO,console"
    
        flume-ng agent --name a1 --conf E:\apache-flume-1.9.0-bin\conf --conf-file E:\apache-flume-1.9.0-bin\conf\avro-memory-kafka.properties -property  "flume.root.logger=INFO,console"