#include <stdio.h>
#include <stdlib.h>

void ptr()
{
    printf("========= ptr =========\n");
    char *p;
    // 未初始化，指针指向空（即0）
    printf("%x, %p, %d\n", p, p, sizeof(p));
    p = malloc(sizeof(char));
    // char单字节，8个1，有符号，所以是-1
    *p = 255;
    // p等于&*p
    printf("%x, %p, %d, %p, %d\n", p, &p, *p, &*p, p==&*p);
    printf("========= ptr =========\n");
}

void arr_ptr()
{
    printf("========= arr ptr =========\n");
    int arr[] = {16};
    for (int i = 0; i < 10; i++)
    {
        printf("%x ", arr[i]);
    }
    printf(" size: %lu\n", sizeof(arr));
    // arr == &*arr == &arr[0]; *arr==arr[0]
    printf("%x, %x, %d, %d\n", arr, *arr, arr==&*arr, arr==&arr[0]);
    printf("========= arr ptr =========\n");
}

typedef struct person
{
    int age;
    char *name;
} person_t;

void struct_ptr()
{
    printf("========= struct ptr =========\n");

    person_t p = {18, "hch"};
    person_t *p1 = malloc(sizeof(person_t));
    p1->age = 20;
    p1->name = "abaaba";
    person_t p2 = p;
    p2.name="p2";
    printf("{%d, %s}, {%d, %s}, {%d, %s}\n", p.age, p.name, (*p1).age, p1->name, p2.age,p2.name);
    // &p == &(p.age)
    printf("p: %x, %p\n",&p,&(p.age));

    printf("========= struct ptr =========\n");
}

int main()
{
    ptr();
    arr_ptr();
    struct_ptr();
}