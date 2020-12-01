#include <stdio.h>
#include <stdlib.h>

void arr_ptr()
{
    char *p;
    printf("%x, %p\n", p, p);
    p = malloc(sizeof(char));
    *p = 255;
    printf("%#x, %x, %p, size: %d\n", *p, p, p, sizeof(p));

    int arr[] = {};
    for (int i = 0; i < 10; i++)
    {
        printf("%x ", arr[i]);
    }
    printf(" size: %lu\n", sizeof(arr));

    printf("%x, %x, %p, %p\n", arr, &*arr, arr, &arr[0]);
}

typedef struct person
{
    int age;
    char *name;
} person_t;

void struct_ptr()
{
    person_t p = {18, "hch"};
    person_t *p1 = malloc(sizeof(person_t));
    p1->age = 20;
    p1->name = "abaaba";
    printf("{%d, %s} {%d, %s}\n", p.age, p.name, (*p1).age, p1->name);
}

int main()
{
    arr_ptr();
    struct_ptr();
}