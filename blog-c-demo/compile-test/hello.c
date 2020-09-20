#include <stdio.h>

/*
    预处理输出hello.i）：gcc hello.c -E > hello.i
    编译（输出hello.s）：gcc hello.i -S 
    汇编（输出hello.o）：gcc hello.s -c
    链接（输出hello）：gcc hello.o -o hello
*/
int main(int argc, char const *argv[])
{
    printf("hello, world!");
    return 0;
}
