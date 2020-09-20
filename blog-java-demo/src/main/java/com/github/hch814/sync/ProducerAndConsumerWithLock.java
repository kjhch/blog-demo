package com.github.hch814.sync;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;

/**
 * 测试ReentrantLock的使用，用经典的生产者消费者问题作为示例
 *
 * @author hch
 * @see ProducerAndConsumer
 * @since 2020/9/9
 */
public class ProducerAndConsumerWithLock {
    public static void main(String[] args) {
        ExecutorService pool = Executors.newCachedThreadPool();
        ProductQueue queue = new ProductQueue(5);
        for (int i = 0; i < 5; i++) {
            pool.execute(new Producer(3, queue));
        }
        for (int i = 0; i < 3; i++) {
            pool.execute(new Consumer(5, queue));
        }
        pool.shutdown();
    }

    private static class Product {
        private static int count = 0;
        private int id = count++;
        private Product next;

        @Override
        public String toString() {
            return "product(id=" + id + ")";
        }

        public void setNext(Product next) {
            this.next = next;
        }

        public Product getNext() {
            return next;
        }
    }

    private static class ProductQueue {
        private int maxSize;
        private int currentSize;
        private Product head;
        private Product tail;
        private ReentrantLock lock = new ReentrantLock();
        // 生产者等待条件队列
        private Condition producerCondition = lock.newCondition();
        // 消费者等待条件队列
        private Condition consumerCondition = lock.newCondition();

        ProductQueue(int maxSize) {
            if (maxSize <= 0) {
                throw new IllegalArgumentException("size must > 0");
            }
            this.maxSize = maxSize;
        }

        public void put(Product product) {
            lock.lock();
            try {
                // 队列满时生产者进入生产者等待队列，并且自动释放锁。这个与Object#wait()相同
                while (currentSize == maxSize) {
                    producerCondition.await();
                }
                // 队列为空
                if (head == null && tail == null) {
                    head = product;
                } else {
                    tail.setNext(product);
                }
                tail = product;
                currentSize++;
                // 生产后通知所有消费等待者，而Object#notifyAll()只能通知所有的线程
                consumerCondition.signalAll();
                System.out.printf("%s has been put%n", product);
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                // unlock通常放在finally中，确保锁一定会释放
                lock.unlock();
            }
        }

        public Product take() {
            lock.lock();
            try {
                // 队列为空时，消费者进入消费者等待队列，并且释放锁
                while (head == null && tail == null) {
                    consumerCondition.await();
                }
                Product currentHead = head;
                Product nextHead = head.getNext();
                currentHead.setNext(null);
                head = nextHead;
                // 队列只有一个元素时
                if (nextHead == null) {
                    tail = null;
                }
                currentSize--;
                // 消费后通知所有生产等待者
                producerCondition.signalAll();
                System.out.printf("%s has been taken%n", currentHead);
                return currentHead;
            } catch (InterruptedException e) {
                e.printStackTrace();
                throw new RuntimeException("interrupted");
            } finally {
                lock.unlock();
            }
        }
    }

    private static class Producer implements Runnable {
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

    private static class Consumer implements Runnable {
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
