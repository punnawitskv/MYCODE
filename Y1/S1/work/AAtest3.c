#include<stdio.h>

int main()
{
    float input;
    printf("input num: ");
    scanf("%f", &input);

    printf("Check Input: %f\n", input);

    printf("output: 0.");
    for(int i = 0; i < 10; i++)
    {
        input = input*2;
        if(input >= 1)
        {
            printf("1");
            input = input-1;
        }
        else
        {
            printf("0");
        }
    }
    return 0;
}