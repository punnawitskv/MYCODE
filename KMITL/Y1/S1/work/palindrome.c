#include<stdio.h>
#include<string.h>

int main() {
    char input[100];

    printf("input : ");
    scanf("%s", &input);
    printf("output : %s is ", input);

    int count=strlen(input);

    for(int i=0;i<count/2;i++)
    {
        if(input[i]!=input[count-1-i])
        {
            printf("not ");
            break;
        }
    }

    printf("palindrome");

    return 0;
}