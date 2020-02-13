package com.ljy.spark.kafka;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class NumberProducer extends Thread {

    private String topic;

    private Producer<String, String> producer;

    public NumberProducer(String topic) {
        this.topic = topic;

        Properties properties = new Properties();
        properties.put("bootstrap.servers", KafkaProperties.BROKER_LIST);
        properties.put("acks", "all");
        properties.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        properties.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        producer = new KafkaProducer<String, String>(properties);
    }

    @Override
    public void run() {
        int messageNo = 1;

        while(true) {
            String message = "number_" + messageNo;
            producer.send(new ProducerRecord<String, String>(topic, message));
            System.out.println("Sent: " + message);

            messageNo++;

            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
