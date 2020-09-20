package com.github.hch814.cipher;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.security.GeneralSecurityException;
import java.security.SecureRandom;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

/**
 * 测试AES256/CBC/PKCS5PADDING的对称加密解密
 *
 * @author hch
 * @since 2020/9/6
 */
public class AESDemo {
    static final String MESSAGE = "Hello, world!";
    static final String KEY = "1234567890abcdef1234567890abcdef";

    public static void main(String[] args) throws Exception {
        // 原文:
        System.out.println("Message: " + MESSAGE);
        // 256位密钥 = 32 bytes Key:
        byte[] key = KEY.getBytes(StandardCharsets.UTF_8);
        // 加密:
        byte[] data = MESSAGE.getBytes(StandardCharsets.UTF_8);
        Map<String, byte[]> encryptedResult = encrypt(key, data);
        byte[] ciphertext = encryptedResult.get("ciphertext");
        byte[] iv = encryptedResult.get("iv");
        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(ciphertext));
        // 解密:
        byte[] decrypted = decrypt(key, iv, ciphertext);
        System.out.println("Decrypted: " + new String(decrypted, StandardCharsets.UTF_8));
    }

    static Map<String, byte[]> encrypt(byte[] key, byte[] plaintext) throws GeneralSecurityException {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
        // CBC模式需要生成一个16 bytes的initialization vector:
        SecureRandom sr = SecureRandom.getInstanceStrong();
        byte[] iv = sr.generateSeed(16);
        IvParameterSpec ivps = new IvParameterSpec(iv);
        cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivps);
        byte[] ciphertext = cipher.doFinal(plaintext);
        // IV不需要保密，把IV和密文一起返回:
        Map<String, byte[]> result = new HashMap<>();
        result.put("iv", iv);
        result.put("ciphertext", ciphertext);
        return result;
    }

    static byte[] decrypt(byte[] key, byte[] iv, byte[] ciphertext) throws GeneralSecurityException {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec keySpec = new SecretKeySpec(key, "AES");
        IvParameterSpec ivps = new IvParameterSpec(iv);
        cipher.init(Cipher.DECRYPT_MODE, keySpec, ivps);
        return cipher.doFinal(ciphertext);
    }

}
