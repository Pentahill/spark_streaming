from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from mysql.connector import connect


def create_new_connection():
    return connect(host="localhost", user="root", password="root")


if __name__ == "__main__":

    sc = SparkContext("local[2]", "filewordcount")
    ssc = StreamingContext(sc, 5)

    def send_partition(iter):
        connection = create_new_connection()

        cusor = connection.cursor()
        for record in iter:
            sql = f'insert into wordcount(word, wordcount) value("{record[0]}", record[1])'
            cusor.execute(sql)
        connection.close()

    lines = ssc.socketTextStream("localhost", 9999)
    lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .foreachRDD(lambda rdd: rdd.foreachPartition(send_partition))

    ssc.start()
    ssc.awaitTermination()
