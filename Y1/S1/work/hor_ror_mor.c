#include<stdio.h>
#include<math.h>
int main(){

    int num1,num2;
    
    printf("Enter first number : ");
    scanf("%d", &num1);
    printf("Enter second number : ");
    scanf("%d", &num2);

    int i;

    if(num1<=num2){
        i=num1;
        while((num1%i!=0)||(num2%i!=0)){
            i=i-1;
        }
    }

    else{
        i=num2;
        while((num1%i!=0)||(num2%i!=0)){
            i=i-1;
        }
    }

    printf("Greatest common divisor : %d", i);

return 0;    
}