from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils

# flume-ng agent --name a1 --conf E:\apache-flume-1.9.0-bin\conf --conf-file E:\apache-flume-1.9.0-bin\conf\flume-pull-streaming.properties -property  "flume.root.logger=INFO,console"
# spark-submit --master local[2] --jars E:\spark-streaming-flume-assembly_2.11-2.4.3.jar D:\ws\spark_streaming\streaming\src\python\FlumePull.py

if __name__ == "__main__":

    sc = SparkContext("local[2]", "filewordcount")
    ssc = StreamingContext(sc, 5)

    address = [("localhost", 41414)]
    flumeStream = FlumeUtils.createPollingStream(ssc, address)
    result = flumeStream.flatMap(lambda x: x[1].split(" "))
    result.pprint()

    ssc.start()
    ssc.awaitTermination()
