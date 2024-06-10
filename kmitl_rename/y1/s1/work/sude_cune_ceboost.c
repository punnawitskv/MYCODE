#include<stdio.h>
#include<math.h>
int main() {
    int input;
    printf("");
        scanf("%d", &input);
    int i = 0;
    do{
        i = i+1;
        printf("%d * %d = %d\n",input,i,input*i);
    } while(i != 12);
    return 0;
}