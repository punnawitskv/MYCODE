#include <stdio.h>

int main()
{
    int count = 5;
    int geb;
    int success = 0;
    int input[count];
    for(int i=0; i<count; i++)
    {
        printf("input[%d] : ", i);
        scanf("%d", &input[i]);
    }
    
    while(!success)
    {
            for(int i=0; i<count; i++)
            {
                if (input[i]>input[i+1])
                {
                    geb = input[i];
                    input[i] = input[i+1];
                    input[i+1] = geb;
                }
            }
    }
    for(int i=0; i<count; i++)
    {
        printf("output[%d] : %d\t", i, input[i]);
    }
}