#include<stdio.h>
#include<math.h>
int main() {
    int input;
    printf("number:");
        scanf("%d", &input);
    printf("multiplication table for %d\n", input);
    int i = 0;
    do{
        i = i+1;
        printf("%d x %d = %d\n",input,i,input*i);
    } while(i != 12);
    return 0;
}