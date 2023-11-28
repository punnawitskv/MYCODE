#include<stdio.h>

int main(){

    int num;

    printf("Enter number : ");
    scanf("%d", &num);

    int i=2;

    printf("Factoring result : ");

    while (num>=i){

        if(num%i==0){
            
            printf("%d", i);
            num = num/i;

            if(num>=i){
                printf(" x ");
            }

        }

        else{
            i++;
        }

    }

return 0;
}