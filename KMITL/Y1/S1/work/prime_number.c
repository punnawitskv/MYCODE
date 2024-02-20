#include<stdio.h>
#include<math.h>
int main() {
    int loop, number;
    int prime = 1;
    do{
        prime = 1;
        printf("");
        scanf("%d", &number);
        for(loop = 2; loop < number; loop++) {
            if((number % loop) ==0) {
            prime = 0;
            }
        }
        if (prime == 1)
            printf("Prime number \n");
        else
            printf("Not prime number \n");
    } while(number != -99);
return 0;
}