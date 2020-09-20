package com.github.hch814.sys;

import java.util.concurrent.TimeUnit;

/**
 * 测试回车和换行，并利用回车符打印进度条
 *
 * @author hch
 * @since 2020/9/15
 */
public class PrintProgressDemo {
    public static void main(String[] args) throws InterruptedException {
        int totalLen = 50;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < totalLen; i++) {
            sb.append("#");
            System.out.print("\r" + sb.toString());
            for (int j = 0; j < totalLen - sb.length(); j++) {
                System.out.print(" ");
            }
            System.out.printf("|%f%%", (sb.length() * 1.0 / totalLen) * 100);
            TimeUnit.MILLISECONDS.sleep(200);
        }
    }
}
