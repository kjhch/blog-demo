package com.github.hch814.ref;

import java.lang.ref.SoftReference;
import java.util.concurrent.TimeUnit;

/**
 * 测试软引用，软引用指向的对象在jvm堆内存不足时会被释放。比较适用于有用但不是必须的对象，可以用作缓存。
 * 需要增加虚拟机参数-Xmx10M
 *
 * @author hch
 * @since 2020/9/15
 */
public class SoftRefDemo {
    public static void main(String[] args) throws InterruptedException {
        MyObj myObj1 = new MyObj("soft1", new SoftReference<>(new byte[5 * 1024 * 1024]));
        MyObj myObj2 = new MyObj("soft2", new SoftReference<>(new byte[5 * 1024 * 1024]));
        System.out.println(myObj1.padding.get());
        System.out.println(myObj2.padding.get());

        SoftReference<byte[]> bytes1 = new SoftReference<>(new byte[5 * 1024 * 1024]);
        SoftReference<byte[]> bytes2 = new SoftReference<>(new byte[5 * 1024 * 1024]);
        System.out.println(myObj2.padding.get());
        System.out.println(bytes1.get());
        System.out.println(bytes2.get());

        SoftObj softObj1 = new SoftObj("soft3", new byte[5 * 1024 * 1024]);
        SoftObj softObj2 = new SoftObj("soft4", new byte[5 * 1024 * 1024]);
        System.out.println(bytes2.get());
        System.out.println(softObj1.get());
        System.out.println(softObj2.get());

        TimeUnit.MILLISECONDS.sleep(100);
    }

}
