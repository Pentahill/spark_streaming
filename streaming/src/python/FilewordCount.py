from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    sc = SparkContext("local", "filewordcount")
    ssc = StreamingContext(sc, 10)

    lines = ssc.textFileStream("E:\\spark-2.4.3-bin-hadoop2.7\\ss\\")
    counts = lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
    counts.pprint()

    ssc.start()
    ssc.awaitTermination()
