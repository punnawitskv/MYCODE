#include<stdio.h>

int main()
{
    int i = 0;
    int input[10];

    //input
    while (input[i-1] != 0 && i<=9)
    {
        printf("input[%d] : ", i);
        scanf("%d", &input[i]);
        i++;
    }
    
    //check
    int x = 0;
    printf("\nCheckInput : ");
    while (x<i)
    {
        printf("[%d]:%d\t", x, input[x]);
        x++;
    }

    //odd
    int j=0;
    printf("\nOdd : ");
    while (j<i)
    {
        if(input[j]%2 != 0)
        {
            printf("%d ", input[j]);
        }
        j++;
    }
    
    //even
    int k=0;
    printf("\nEven : ");
    while (k<i)
    {
        if(input[k]%2 == 0)
        {
            printf("%d ", input[k]);
        }
        k++;
    }

    return 0;
}