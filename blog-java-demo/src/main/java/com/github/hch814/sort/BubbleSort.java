package com.github.hch814.sort;

import java.util.Arrays;

/**
 * @author hch
 * @since 2021/1/3
 */
public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = new int[]{3, 2, 5, 4, 1};
        for (int i = 0; i < arr.length - 1; i++) {
            bubble(arr);
        }
        System.out.println(Arrays.toString(arr));
    }

    /**
     * e.g. 3 2 5 4 1
     */
    public static void bubble(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
}
