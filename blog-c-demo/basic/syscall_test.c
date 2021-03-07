#include <stdio.h>
#include <sys/types.h>

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

void hello()
{
    char str[] = "Hello\n";
    //注意：64位系统调用中，write函数调用号为1
    asm volatile(
        "mov %2, %%rsi\n"
        "syscall"
        :
        : "a"(1), "b"(0), "c"(str), "d"(6));
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
    move();
    printf("pid: %d %d\n", pid(), getpid());
    hello();
    exit123();
}
