package com.github.hch814.cipher;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.math.BigInteger;
import java.security.MessageDigest;

/**
 * 使用SHA512算法测试消息摘要
 *
 * @author hch
 * @since 2020/9/6
 */
public class SHADemo {
    public static void main(String[] args) throws Exception {
        System.out.println(getDigest(new File(System.getProperty("user.home"), ".bash_history")));
    }

    static String getDigest(File file) throws Exception {
        // 创建一个MessageDigest实例:
        MessageDigest md = MessageDigest.getInstance("SHA-512");

        try (FileInputStream in = new FileInputStream(file);
             BufferedInputStream bufferedInputStream = new BufferedInputStream(in)) {
            int r;

            // 反复调用update输入数据:
            while ((r = bufferedInputStream.read()) != -1) {
                md.update((byte) r);
            }

            // 计算结果
            byte[] result = md.digest();
            return new BigInteger(1, result).toString(16);
        }
    }
}
