from pyspark import SparkContext
from pyspark import Row
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession


def get_spark_session_instance(spark_conf):

    if("sparkSessionSingletonInstance" not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession.builder\
                                                                 .config(conf=spark_conf)\
                                                                 .getOrCreate()
    return globals()['sparkSessionSingletonInstance']


def process(time, rdd):

    try:
        spark = get_spark_session_instance(rdd.context.getConf())

        row_rdd = rdd.map(lambda w: Row(word=w))
        words_data_frame = spark.createDataFrame(row_rdd)

        words_data_frame.createOrReplaceTempView("words")

        word_counts_data_frame = spark.sql("select word, count(*) as total from words group by word")
        word_counts_data_frame.show()
    except:
        pass


if __name__ == "__main__":

    sc = SparkContext("local[2]", "filewordcount")
    ssc = StreamingContext(sc, 2)

    lines = ssc.socketTextStream("localhost", 9999)
    lines.flatMap(lambda x: x.split(" ")).foreachRDD(process)

    ssc.start()
    ssc.awaitTermination()
