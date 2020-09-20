package com.github.hch814.cipher;

import javax.crypto.Cipher;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.charset.StandardCharsets;
import java.security.*;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Base64;

/**
 * 测试RSA2048非对称加密解密。密信场景：公钥加密，私钥解密
 * <p>
 * 密钥会进行持久化存储
 *
 * @author hch
 * @since 2020/9/6
 */
public class RSADemo {
    static final String KEY_FILE_DIR = "/tmp/";
    static final String PUBLIC_KEY_FILE_NAME = "public.key";
    static final String PRIVATE_KEY_FILE_NAME = "private.key";

    public static void main(String[] args) throws Exception {
        generateRSAKeyPair(KEY_FILE_DIR);
        byte[] ciphertext = encrypt(new File(KEY_FILE_DIR, PUBLIC_KEY_FILE_NAME), "hello, world!");
        System.out.println("ciphertext: " + Base64.getEncoder().encodeToString(ciphertext));
        System.out.println("plaintext: " + decrypt(new File(KEY_FILE_DIR, PRIVATE_KEY_FILE_NAME), ciphertext));

    }

    static void generateRSAKeyPair(String keyDir) throws Exception {
        KeyPairGenerator kpGen = KeyPairGenerator.getInstance("RSA");
        kpGen.initialize(2048);
        KeyPair kp = kpGen.generateKeyPair();
        try (FileOutputStream publicKeyOut = new FileOutputStream(new File(keyDir, PUBLIC_KEY_FILE_NAME));
             FileOutputStream privateKeyOut = new FileOutputStream(new File(keyDir, PRIVATE_KEY_FILE_NAME))) {
            publicKeyOut.write(kp.getPublic().getEncoded());
            privateKeyOut.write(kp.getPrivate().getEncoded());
        }
    }

    static byte[] encrypt(File publicKeyFile, String message) throws Exception {
        try (FileInputStream publicKeyIn = new FileInputStream(publicKeyFile)) {
            // 从文件中生成publicKey对象
            byte[] publicKeyBytes = new byte[publicKeyIn.available()];
            publicKeyIn.read(publicKeyBytes);
            KeyFactory kf = KeyFactory.getInstance("RSA");
            PublicKey publicKey = kf.generatePublic(new X509EncodedKeySpec(publicKeyBytes));

            // 消息加密
            Cipher cipher = Cipher.getInstance("RSA");
            cipher.init(Cipher.ENCRYPT_MODE, publicKey);
            return cipher.doFinal(message.getBytes(StandardCharsets.UTF_8));
        }
    }

    static String decrypt(File privateKeyFile, byte[] ciphertext) throws Exception {
        try (FileInputStream privateKeyIn = new FileInputStream(privateKeyFile)) {
            // 从文件中生成privateKey对象
            byte[] privateKeyBytes = new byte[privateKeyIn.available()];
            privateKeyIn.read(privateKeyBytes);
            KeyFactory kf = KeyFactory.getInstance("RSA");
            PrivateKey privateKey = kf.generatePrivate(new PKCS8EncodedKeySpec(privateKeyBytes));

            // 消息解密
            Cipher cipher = Cipher.getInstance("RSA");
            cipher.init(Cipher.DECRYPT_MODE, privateKey);
            byte[] plaintext = cipher.doFinal(ciphertext);
            return new String(plaintext, StandardCharsets.UTF_8);
        }
    }
}
