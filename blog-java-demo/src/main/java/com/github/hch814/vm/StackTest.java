package com.github.hch814.vm;

import java.util.LinkedList;
import java.util.List;

/**
 * 测试线程栈，栈默认占用1m堆外内存，可通过例如"-Xss200k"修改为200k
 */
public class StackTest {
    static List list = new LinkedList();

    public static void main(String[] args) {
        m(0);
    }

    static void m(int i) {
        try {
            list.add(new Object());
            list.add(new Object());
            // byte byt = 0;
            // int a = 4;
            long b = 0;
            // long b1 = 0;
            // Object o = new Object();

            m(++i);
        } catch (Throwable e) {
            System.out.println(i);
        }

    }
}
