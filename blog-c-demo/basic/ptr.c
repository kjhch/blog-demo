#include <stdio.h>
#include <stdlib.h>

void arr_ptr()
{
    char *p;
    printf("%x, %p\n", p, p);
    p = malloc(sizeof(char));
    printf("%x, %p, size: %d\n", p, p, sizeof(p));

    int arr[]={};
    for (int i = 0; i < 10; i++)
    {
        printf("%x ", arr[i]);
    }
    printf(" size: %d\n", sizeof(arr));

    printf("%x, %x, %p, %p\n", arr, &*arr, arr, &arr[0]);
}

int main()
{
    arr_ptr();
}