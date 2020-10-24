#include <stdio.h>
/* 
    sizeof(void): 1
    sizeof(char): 1, sizeof(unsigned char): 1
    sizeof(short): 2, sizeof(unsigned short): 2
    sizeof(int): 4, sizeof(unsigned int): 4
    sizeof(long): 8, sizeof(unsigned long): 8
    sizeof(float): 4, sizeof(double): 8
    sizeof(long int): 8, sizeof(long long): 8, sizeof(long double): 16
    sizeof(void*): 8, sizeof(char*): 8, sizeof(short*): 8, sizeof(int*): 8, sizeof(long*): 8
 */
int main(int argc, char const *argv[])
{
    printf("sizeof(void): %lu\n", sizeof(void));
    printf("sizeof(char): %lu, sizeof(unsigned char): %lu\n", sizeof(char), sizeof(unsigned char));
    printf("sizeof(short): %lu, sizeof(unsigned short): %lu\n", sizeof(short), sizeof(unsigned short));
    printf("sizeof(int): %lu, sizeof(unsigned int): %lu\n", sizeof(int), sizeof(unsigned int));
    printf("sizeof(long): %lu, sizeof(unsigned long): %lu\n", sizeof(long), sizeof(unsigned long));
    printf("sizeof(float): %lu, sizeof(double): %lu\n", sizeof(float), sizeof(double));
    printf("sizeof(long int): %lu, sizeof(long long): %lu, sizeof(long double): %lu\n", sizeof(long int), sizeof(long long), sizeof(long double));
    printf("sizeof(void*): %lu, sizeof(char*): %lu, sizeof(short*): %lu, sizeof(int*): %lu, sizeof(long*): %lu\n", sizeof(void *), sizeof(char *), sizeof(short *), sizeof(int *), sizeof(long *));
    return 0;
}
