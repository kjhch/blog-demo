package com.github.hch814.cipher;

import org.apache.commons.codec.binary.Hex;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

/**
 * 测试一些编码方式
 *
 * @author hch
 * @since 2020/9/6
 */
public class EncodingDemo {
    public static void main(String[] args) throws UnsupportedEncodingException {
        testEncoding();
    }

    static void testEncoding() throws UnsupportedEncodingException {
        System.out.println("——————" + "字符编码" + "——————");
        // GBK和UTF-8字符编码测试
        System.out.println("UTF-8: " + new String(new byte[]{(byte) 0b11100100, (byte) 0b10111000, (byte) 0b10101101}, StandardCharsets.UTF_8));
        System.out.println("GBK: " + new String(new byte[]{(byte) 0b11010110, (byte) 0b11010000}, "GBK"));
        System.out.println("UTF-8 with GBK bytes: " + new String(new byte[]{(byte) 0b11010110, (byte) 0b11010000}, StandardCharsets.UTF_8));
        // URL字符编码测试
        System.out.println("URL: " + URLEncoder.encode("#不爱学习的灰灰", "UTF-8"));

        System.out.println("——————" + "二进制编码" + "——————");
        // 十六进制二进制编码测试
        System.out.println("Hex: " + new String(Hex.encodeHex(new byte[]{(byte) 0b11100100, (byte) 0b10111000, (byte) 0b10101101})));
        // BASE64二进制编码测试
        System.out.println("Base64: " + Base64.getEncoder().encodeToString(new byte[]{(byte) 0b11100100, (byte) 0b10111000, (byte) 0b10101101}));

    }
}
