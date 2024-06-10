#include <stdio.h>

void swap(int*a,int*b)
{
    int geb;
    geb = *a;
    *a = *b;
    *b = geb;
}

int a,b;

int main()
{
    printf("input : ");
    scanf("%d %d", &a, &b);

    swap(&a,&b);
    printf("output : %d %d", a,b);
}