#include <stdio.h>
#include <stdlib.h>

int main()
{
    // 不同的字面量表示10这个数字
    int decimal = 10, hex = 0xa, octal = 012, binary = 0b1010;
    printf("%x, %d, %#x, %#o\n", decimal, hex, octal, binary);

    // char本质上就是一个字节的变量而已
    char c = '\0', c1=65, c2=0b01100001, c3=0x62;
    printf("%d, %c, %c, %c\n", c, c1, c2, c3);

    int *p = malloc(sizeof(int));
    int a;
    printf("input two numbers(seperated by a space): ");
    // scanf要求提供的是变量地址
    scanf("%d %d", p, &a);
    // printf提供的是变量名，即地址别名
    printf("%d %d\n", *p, a);
}