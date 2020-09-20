package com.github.hch814.sync;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * 测试synchronized关键字产生的线程间协作问题，用经典的生产者消费者问题作为示例
 *
 * @author hch
 * @since 2020/9/8
 */
public class ProducerAndConsumer {
    public static void main(String[] args) {
        ExecutorService pool = Executors.newCachedThreadPool();
        int producerNum = 5;
        int consumerNum = 3;
        ProductQueue productQueue = new ProductQueue(5);
        for (int i = 0; i < producerNum; i++) {
            pool.execute(new Producer(3, productQueue));
        }
        for (int i = 0; i < consumerNum; i++) {
            pool.execute(new Consumer(5, productQueue));
        }
        pool.shutdown();
    }

    static class Product {
        private static int count = 0;
        private int id = count++;

        @Override
        public String toString() {
            return "product(id=" + id + ")";
        }
    }

    static class ProductQueue {
        private Product[] products;
        private int tail;
        private int head;
        private int size;

        ProductQueue(int size) {
            if (size <= 0) {
                throw new RuntimeException("size must > 0");
            }
            this.size = size;
            this.head = (tail + 1) % size;
            products = new Product[size];
        }

        public synchronized void put(Product product) {
            while (products[(tail + 1) % size] != null) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            int next = (tail + 1) % size;
            products[next] = product;
            tail = next;
            System.out.printf("%s has been put at position %d%n", product, next);
            notifyAll();
        }

        public synchronized Product take() {
            while (products[head] == null) {
                try {
                    wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            Product product = products[head];
            products[head] = null;
            System.out.printf("%s has been taken from position %d%n", product, head);
            head = (head + 1) % size;
            notifyAll();
            return product;
        }
    }

    static class Producer implements Runnable {
        private static int count;
        private int id = count++;
        private int num;
        private ProductQueue queue;

        Producer(int num, ProductQueue queue) {
            this.num = num;
            this.queue = queue;
            System.out.printf("producer%d produces %d products%n", id, num);
        }

        @Override
        public void run() {
            for (int i = 0; i < num; i++) {
                queue.put(new Product());
            }
        }
    }

    static class Consumer implements Runnable {
        private static int count;
        private int id = count++;
        private int num;
        private ProductQueue queue;

        Consumer(int num, ProductQueue queue) {
            this.num = num;
            this.queue = queue;
            System.out.printf("consumer%d consumes %d products%n", id, num);
        }

        @Override
        public void run() {
            for (int i = 0; i < num; i++) {
                queue.take();
            }
        }
    }
}
