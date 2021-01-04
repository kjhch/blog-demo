package com.github.hch814.sort;

import java.util.Arrays;

/**
 * @author hch
 * @since 2021/1/3
 */
public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = new int[]{3, 2, 5, 4, 1};
        int n = arr.length - 1;
        while (n > 0) {
            int pos = findMaxPos(arr, n);
            int tmp = arr[n];
            arr[n] = arr[pos];
            arr[pos] = tmp;
            n--;
        }
        System.out.println(Arrays.toString(arr));

    }

    /**
     * e.g. 3 2 5 4 1
     */
    public static int findMaxPos(int[] arr, int n) {
        int maxPos = 0;
        for (int i = 0; i <= n; i++) {
            if (arr[i] > arr[maxPos]) {
                maxPos = i;
            }
        }
        return maxPos;
    }
}
