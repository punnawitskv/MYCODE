#include<stdio.h>
#include<math.h>

int main()
{
    int input;
    printf("input : ");
    scanf("%d", &input);
    printf("output : \n");
    int i = 0;
    do{
        i = i+1;
        printf("%d x %d = %d\n",input,i,input*i);
    } while(i != 12);
    return 0;
}