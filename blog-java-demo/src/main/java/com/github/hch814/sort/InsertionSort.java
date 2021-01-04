package com.github.hch814.sort;

import java.util.Arrays;

/**
 * @author hch
 * @since 2021/1/3
 */
public class InsertionSort {
    public static void main(String[] args) {
        int[] arr = new int[]{3, 2, 5, 4, 1};
        for (int i = 1; i < arr.length; i++) {
            insert(arr, i);
        }
        System.out.println(Arrays.toString(arr));
    }

    public static void insert(int[] arr, int n) {
        int key = arr[n];
        int i = n;
        for (; i > 0 && arr[i - 1] > key; i--) {
            arr[i] = arr[i - 1];
        }
        arr[i] = key;

    }
}
