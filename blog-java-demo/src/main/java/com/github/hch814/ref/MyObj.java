package com.github.hch814.ref;

import java.lang.ref.Reference;

/**
 * 自定义对象用于测试各类引用
 *
 * @author hch
 * @since 2020/9/15
 */
public class MyObj {
    private String name;
    public Reference<byte[]> padding;

    MyObj(String name, Reference<byte[]> padding) {
        this.name = name;
        this.padding = padding;
    }

    @Override
    public String toString() {
        return name;
    }

    @Override
    protected void finalize() throws Throwable {
        System.out.println(this.name + " cleaned...");
    }
}
