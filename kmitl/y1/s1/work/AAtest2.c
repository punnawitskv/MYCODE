#include<stdio.h>

int main()
{
    int num1, num2, num3;
    printf("input num: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    //Check input
    printf("Check Input: %d %d %d\n", num1, num2, num3);

    int korornor = 1;
    while (korornor % num1 != 0 || korornor % num2 != 0 || korornor % num3 != 0)
    {
        korornor++;
    }

    printf("output: %d", korornor);

    return 0;   
}