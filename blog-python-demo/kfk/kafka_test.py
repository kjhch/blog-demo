# -*- coding: utf-8 -*-
"""
kafka在python中的用法

@author: hch
@date  : 2020/12/8
"""

from kafka import KafkaConsumer, KafkaProducer


class KafkaTest:

    @classmethod
    def test_consumer(cls):
        consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], group_id='group1')
        print('consumer started...')
        for msg in consumer:
            print(msg)

    @classmethod
    def test_poll(cls):
        consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], group_id='group1',
                                 enable_auto_commit=False)
        while True:
            result = consumer.poll(3000)
            print(result)


    @classmethod
    def test_producer(cls):
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        future = producer.send('test1', value='im a producer...'.encode('utf-8'))
        print(future.get(10))


if __name__ == '__main__':
    # KafkaTest.test_producer()
    # KafkaTest.test_consumer()
    KafkaTest.test_poll()
