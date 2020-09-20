package com.github.hch814.ref;

import java.lang.ref.SoftReference;

/**
 * 继承了软引用的对象，用于测试软引用
 *
 * @author hch
 * @since 2020/9/15
 */
public class SoftObj extends SoftReference<byte[]> {
    private String name;

    SoftObj(String name, byte[] bytes) {
        super(bytes);
        this.name = name;
    }

    @Override
    protected void finalize() throws Throwable {
        System.out.println(this.name + " cleaned...");
    }
}
