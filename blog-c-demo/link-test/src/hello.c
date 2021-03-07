#include <stdio.h>
// #include "../include/hello.h"
// #include "../include/hello_name.h"

/* 
    注意：此处就算不导入头文件也没关系，只要在调用hello的文件（main.c）中include即可

    1) 制作静态链接库：
    gcc hello.c -c -o ../lib/hello.o
    cd ../lib 
    ar -r libhello_static.a hello.o
    这里的ar相当于tar的作用，将多个目标文件打包。

    2) 制作动态链接库：
    gcc hello.c -shared -fPIC -o ../lib/libhello.so 
 */
void hello()
{
    printf("hch: hello\n");
    return;
}