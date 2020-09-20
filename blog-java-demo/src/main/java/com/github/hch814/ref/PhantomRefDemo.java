package com.github.hch814.ref;

import java.lang.ref.PhantomReference;
import java.lang.ref.Reference;
import java.lang.ref.ReferenceQueue;

/**
 * 测试虚引用，你永远无法获取虚引用指向的对象，当虚引用指向的对象被gc时，虚引用对象就会进入到引用队列中。
 * 虚引用是jvm管理堆外内存的一种方式
 *
 * @author hch
 * @since 2020/9/15
 */
public class PhantomRefDemo {
    public static void main(String[] args) throws InterruptedException {
        Object obj = new Object();    // 可以看做是堆外内存
        ReferenceQueue<Object> referenceQueue = new ReferenceQueue<>();
        PhantomReference<Object> phantomReference = new PhantomReference<>(obj, referenceQueue);
        System.out.println(phantomReference.get());
        System.out.println(referenceQueue.poll());

        Thread thread = new Thread(() -> {
            Reference reference;
            for (reference = referenceQueue.poll(); reference == null; ) {
                reference = referenceQueue.poll();
            }
            System.out.println(reference);    // 感知到堆外内存被gc了，unsafe清理堆外内存
        });

        thread.start();
        obj = null;
        System.gc();    //堆外内存被gc
        thread.join();
    }
}
