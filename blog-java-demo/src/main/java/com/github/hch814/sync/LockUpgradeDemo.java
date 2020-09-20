package com.github.hch814.sync;

import org.openjdk.jol.info.ClassLayout;

import java.util.concurrent.TimeUnit;

/**
 * @author hch
 * @since 2020/9/8
 */
public class LockUpgradeDemo {
    public static void main(String[] args) throws InterruptedException {
        testNonLock();
        testLightWeightLock();
        // testBiasedLock();
    }

    public static void testBiasedLock() throws InterruptedException {
        TimeUnit.MILLISECONDS.sleep(4100);

        System.out.printf("%n----------------可以偏向----------------%n");
        Object biasedLockObj = new Object();
        System.out.println(ClassLayout.parseInstance(biasedLockObj).toPrintable());
        System.gc();

        System.out.printf("%n----------------偏向锁(gc age + 1)----------------%n");
        synchronized (biasedLockObj) {
            System.out.println(ClassLayout.parseInstance(biasedLockObj).toPrintable());
        }

        System.out.printf("%n----------------偏向锁升级----------------%n");
        Object stillBiasedLockObj = new Object();
        Thread t = new Thread(() -> {
            synchronized (stillBiasedLockObj) {
                System.out.println("thread....");
                System.out.println(ClassLayout.parseInstance(stillBiasedLockObj).toPrintable());

            }
        });

        synchronized (stillBiasedLockObj) {
            System.out.println(ClassLayout.parseInstance(stillBiasedLockObj).toPrintable());
            t.start();
            //只能看到偏向锁升级到重量级锁
            System.out.println(ClassLayout.parseInstance(stillBiasedLockObj).toPrintable());
        }

        System.out.printf("%n----------------解锁----------------%n");
        TimeUnit.MILLISECONDS.sleep(1000);
        System.out.println(ClassLayout.parseInstance(stillBiasedLockObj).toPrintable());
    }

    public static void testLightWeightLock() throws InterruptedException {
        System.out.printf("%n----------------无锁----------------%n");
        Object lightWeightLock = new Object();
        System.out.println(ClassLayout.parseInstance(lightWeightLock).toPrintable());
        System.gc();

        System.out.printf("%n----------------轻量级锁----------------%n");
        synchronized (lightWeightLock) {
            System.out.println(ClassLayout.parseInstance(lightWeightLock).toPrintable());
        }

        System.out.printf("%n----------------解锁(gc age+1)----------------%n");
        TimeUnit.MILLISECONDS.sleep(200);
        System.out.println(ClassLayout.parseInstance(lightWeightLock).toPrintable());

        System.out.printf("%n----------------轻量级锁升级----------------%n");
        Object LWLock = new Object();
        Thread t = new Thread(() -> {
            synchronized (LWLock) {
                System.out.println("thread:");
                System.out.println(ClassLayout.parseInstance(LWLock).toPrintable());

            }
        });

        synchronized (LWLock) {
            System.out.println(ClassLayout.parseInstance(LWLock).toPrintable());
            t.start();
            System.out.println(ClassLayout.parseInstance(LWLock).toPrintable());
        }

        // t.join();
        TimeUnit.SECONDS.sleep(1);
        System.out.printf("%n----------------解锁----------------%n");
        System.out.println(ClassLayout.parseInstance(LWLock).toPrintable());
    }

    public static void testNonLock() throws InterruptedException {
        System.out.printf("%n----------------无锁----------------%n");
        Object nonLockObj = new Object();
        System.out.println(ClassLayout.parseInstance(nonLockObj).toPrintable());

        System.out.printf("%n----------------依旧无锁----------------%n");
        TimeUnit.SECONDS.sleep(3);
        Object stillNonLockObj = new Object();
        System.out.println(ClassLayout.parseInstance(stillNonLockObj).toPrintable());
    }
}
