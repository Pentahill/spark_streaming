package com.ljy.spark.kafka;

import org.junit.Test;

public class NumberProducerTest {

    @Test
    public void run() {
        new NumberProducer(KafkaProperties.TOPIC).start();

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        new NumberCosumer(KafkaProperties.TOPIC).start();

        try {
            Thread.sleep(50000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}