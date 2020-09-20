package com.github.hch814.ref;

import java.util.concurrent.TimeUnit;

/**
 * 强引用测试，只要强引用存在，其指向的对象无论何时都不会被jvm回收，换句话说只要引用不指向null该对象就会一直存活。
 *
 * @author hch
 * @since 2020/9/15
 */
public class StrongRefDemo {
    public static void main(String[] args) throws InterruptedException {
        MyObj myObj = new MyObj("obj", null);
        System.gc();
        myObj = null;
        System.gc();
        TimeUnit.MILLISECONDS.sleep(100);
    }
}
