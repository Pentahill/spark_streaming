from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == '__main__':

    sc = SparkContext("local[2]", "filewordcount")
    ssc = StreamingContext(sc, 10)

    ssc.checkpoint(".")

    def update_function(current_value, pre_value):
        return (pre_value or 0) + sum(current_value)

    lines = ssc.socketTextStream("localhost", 9999)
    state = lines.flatMap(lambda line: line.split(" "))\
        .map(lambda word: (word, 1))\
        .updateStateByKey(update_function)
    state.pprint()

    ssc.start()
    ssc.awaitTermination()
