提交任务：
    (1) spark-submit --master local[2] --py-files D:\ws\spark_streaming\streaming\src\python\Flume.py
    (2) 集成flume
    // 注意scala版本
    spark-submit --master local[2] --jars E:\spark-streaming-flume-assembly_2.11-2.4.3.jar D:\ws\spark_streaming\streaming\src\python\Flume.py
    (3) 集成kafka
        1) 启动zk
        2) 启动kafka
        3) 创建topic

Context:
    Spark SQL: SQLContext/HiveContext
    Spark Core: SparkContext
    Spark Streaming: StreamingContext

核心概念：
    (1) StreamingContext spark streaming的入口
    (2) DStream 一些列的RDD
    (3) Input DStream和Receiver
    (4) Transformations
    (5) Output Operations

粗粒度：
    spark按秒将数据拆分成批量数据，交给spark引擎处理。

Spark Stream数据处理流程：    
    Driver （先启动Receiver）-> Receiver (接收和切分数据)-> other Recevier(如果有备份）
    Receiver (反馈数据接收以及副本信息）-> StreamingContext （根据切分的数据启动job)-> SparkContext (在executor上启动task运行job)-> Executor 