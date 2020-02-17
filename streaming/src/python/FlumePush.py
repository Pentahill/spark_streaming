from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.flume import FlumeUtils


if __name__ == "__main__":

    sc = SparkContext("local[2]", "filewordcount")
    ssc = StreamingContext(sc, 5)

    flumeStream = FlumeUtils.createStream(ssc, "localhost", 41414)
    result = flumeStream.flatMap(lambda x: x[1].split[1])
    result.pprint()

    ssc.start()
    ssc.awaitTermination()
