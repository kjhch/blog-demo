package com.github.hch814.sync;

/**
 * synchronized关键字会产生对象锁，并且该对象锁可重入
 *
 * @author hch
 * @since 2020/9/8
 */
public class SynchronizedDemo {
    public static void main(String[] args) {
        SynchronizedDemo test = new SynchronizedDemo();
        test.m1();
        m3();
    }

    // 构造方法不支持synchronized关键字
    // synchronized SynchronizedTest(){}

    /**
     * m1方法等价于m2
     */
    public synchronized void m1() {
        System.out.println("m1...");
        m2();
    }

    /**
     * 若锁的对象引用发生改变（指向其他对象或者null）则锁会失效，所以锁对象时，引用通常会用final修饰
     */
    public void m2() {
        synchronized (this) {
            System.out.println("m2...");
        }
    }

    /**
     * m3方法等价于m4
     */
    public static synchronized void m3() {
        System.out.println("m3...");
        m4();
    }

    public static void m4() {
        synchronized (SynchronizedDemo.class) {
            System.out.println("m4...");
        }
    }
}
