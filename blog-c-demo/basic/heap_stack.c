#include <stdio.h>
#include <stdlib.h>

/*
    变量a,b存在内存栈中，地址由上至下分配，打印出的地址值一般来说是虚拟地址
    gcc默认开启栈保护所以是由下至上，编译时可以加上参数-fno-stack-protector
    malloc动态申请的内存存在堆中，地址由下至上
*/
int main()
{
    char a = 1;
    char b = 2;
    char *c = (char*)malloc(sizeof(char));
    char *d = (char*)malloc(sizeof(char));
    printf("pos of a: %p, pos of b: %p, pos of c: %p, post of d: %p\n", &a, &b, &c, &d);
    printf("pos of *c: %p, pos of *d: %p\n", c, &*d);
}