#include <stdio.h>
#include <string.h>

int slen(char *s)
{
    return sizeof(s);
}

int main()
{
    // 0等价于'\0'
    char s[] = {'a', 'b', 'c', 0};
    char *cs = "中文";
    printf("%s, %c\n", cs, *s);
    for (int i = 0; i < strlen(cs); i++)
    {
        printf("%x ", *(cs + i));
    }
}
