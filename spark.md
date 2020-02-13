提交任务：
    spark-submit --master local[2] --py-files E:\spark-2.4.3-bin-hadoop2.7\examples\src\main\python\streaming\network_wordcount.py localhost 9999

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