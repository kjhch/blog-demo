package com.github.hch814.sync;

import java.util.concurrent.TimeUnit;

/**
 * 测试volatile关键字
 * 有个很有意思的情况可以看下即使不加volatile，只要在循环中加入一点耗时的操作即可实现普通变量的可见性。
 * 网上查了一些问答给出的是这个原因：CPU空闲后会遵循jvm优化基准，尽可能快的保证数据的可见性，从而将变量b从主内存同步到工作内存中，最终导致程序的结束
 *
 * @author hch
 * @since 2020/9/15
 */
public class VolatileDemo {
    static volatile boolean b = true;

    public static void main(String[] args) throws InterruptedException {
        new Thread(() -> {
            try {
                TimeUnit.MILLISECONDS.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            change();
        }, "t").start();

        while (b) {
            // TimeUnit.NANOSECONDS.sleep(1);
            // Thread.yield();
            // System.out.print("\r");
        }
        System.out.println("finish");
    }

    public static void change() {
        b = false;
    }
}
