import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.spark.SparkConf;
import org.apache.spark.streaming.api.java.JavaInputDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;
import org.apache.spark.streaming.kafka010.ConsumerStrategies;
import org.apache.spark.streaming.kafka010.KafkaUtils;
import org.apache.spark.streaming.Duration;
import org.apache.spark.streaming.kafka010.LocationStrategies;
import scala.Tuple2;

import java.util.*;

public class KafkaSparkStreaming {

    Map<String, Object> kafkaParams = new HashMap<>();
    Set<String> topics;

    public KafkaSparkStreaming(String servers, Set<String> topics) {
        this.kafkaParams.put("bootstrap.servers", servers);
        this.kafkaParams.put("key.deserializer", StringDeserializer.class);
        this.kafkaParams.put("value.deserializer", StringDeserializer.class);
        this.kafkaParams.put("group.id", "use_a_separate_group_id_for_each_stream");
        this.kafkaParams.put("auto.offset.reset", "latest");
        this.kafkaParams.put("enable.auto.commit", false);

        this.topics = topics;
    }

    public void run() throws InterruptedException {
        SparkConf conf = new SparkConf().setAppName("kafka spark streaming").setMaster("local[2]");
        JavaStreamingContext ssc = new JavaStreamingContext(conf, new Duration(2000));
        JavaInputDStream<ConsumerRecord<String, String>> stream =
                KafkaUtils.createDirectStream(ssc, LocationStrategies.PreferConsistent()
                                                , ConsumerStrategies.<String, String>Subscribe(this.topics, this.kafkaParams));

        stream.mapToPair(r -> new Tuple2<>(r.key(), r.value())).print();

        ssc.start();
        ssc.awaitTermination();
    }

    public static void main(String[] args) throws InterruptedException {
        Set<String> topics = new HashSet<>();
        topics.add("kafka_streaming_topic");
        KafkaSparkStreaming kss = new KafkaSparkStreaming("localhost:9092", topics);
        kss.run();
    }

}
