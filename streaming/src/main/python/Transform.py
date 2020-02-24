from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == "__main__":

    sc = SparkContext("local[2]", "filewordcount")
    ssc = StreamingContext(sc, 2)

    rdd_out = sc.parallelize(['lisi', 'wangwu'])
    rdd_out = rdd_out.map(lambda r: (r, True))
    print(rdd_out.collect())

    lines = ssc.socketTextStream("localhost", 9999)
    result = lines.map(lambda x: (x.split(',')[1], x)) \
        .transform(lambda rdd: rdd.leftOuterJoin(rdd_out).filter(lambda r: not r[1][1]).map(lambda r: r[1][0]))
    result.pprint()

    ssc.start()
    ssc.awaitTermination()
