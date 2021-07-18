#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>

void posix_func()
{
    printf("posix func getpid: %d\n", getpid());
}

void posix_syscall()
{
    char *str = "posix syscall write: ";
    printf("%d\n", syscall(1, 0, str, strlen(str)));
}

/*
(1)int $0x80
eax ebx ecx edx esi edi ebp eax
(2)syscall
rax rdi rsi rdx r10 r8 r9 rax

三个冒号的含义
:输出参数
:输入参数
:会被修改的寄存器
参数限定符
i 立即数
m 内存地址
r 寄存器

注意
%n从第一个冒号的参数开始算起，0是第一个，1是第二个以此类推
输出操作数约束应该带有一个约束修饰符”=”，指定它是输出操作数
*/
ssize_t using_asm()
{
    ssize_t rt;
    char *str = "using_asm size: ";
    long l = strlen(str);
    asm("movq %1, %%rax;"
        "movq %2, %%rdi;"
        "movq %3, %%rsi;"
        "movq %4, %%rdx;"
        // "movl %%rax, %0;"
        "syscall;"
        : "=r"(rt)
        : "i"(1), "i"(0), "m"(str), "m"(l));
    return rt;
}

void exit123()
{
    unsigned long syscall_nr = 60;
    long exit_status = 123;

    asm("movq %0, %%rax\n"
        "movq %1, %%rdi\n"
        "syscall"
        : /* output parameters, we aren't outputting anything, no none */
          /* (none) */
        : /* input parameters mapped to %0 and %1, repsectively */
        "m"(syscall_nr), "m"(exit_status)
        : /* registers that we are "clobbering", unneeded since we are calling exit */
        "rax", "rdi");
}

pid_t pid()
{
    unsigned long syscall_nr = 39;
    pid_t rt;

    asm volatile(
        "movq %1, %%rax\n"
        // "movq %1, %%rdi\n"
        "syscall"
        : "=r"(rt)
        : "p"(syscall_nr));
    return rt;
}

void move()
{
    int input = 8;
    int result = 0;
    asm("movl %1,%0"
        : "=r"(result)
        : "r"(input));
    printf("move result: %d\n", result);
}

int main(int argc, char *argv[])
{
    posix_func();
    posix_syscall();
    printf("%d\n", using_asm());

    move();
    printf("pid: %d %d\n", pid(), getpid());

    exit123();
}
