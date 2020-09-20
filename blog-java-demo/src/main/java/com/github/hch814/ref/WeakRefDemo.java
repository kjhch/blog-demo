package com.github.hch814.ref;

import java.lang.ref.WeakReference;

/**
 * 测试弱引用，弱引用指向的对象只要在gc之后就会被释放回收
 *
 * @author hch
 * @since 2020/9/15
 */
public class WeakRefDemo {
    public static void main(String[] args) {
        WeakReference<byte[]> weak = new WeakReference<>(new byte[1]);
        System.out.println(weak.get());
        System.gc();
        System.out.println(weak.get());
    }
}
