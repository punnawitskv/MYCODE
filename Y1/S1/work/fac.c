#include<stdio.h>
#include<math.h>

int fac(int number);

int main() {
    int number;
        printf("number:");
        scanf("%d", &number);
    //int output = fac(number);
        //printf("%d", output);
        printf("%d", fac(number));
return 0;
}

int fac(number){ 
    if (number!=1){
        number *= fac(number-1); //number = number * fac(number-1)
        }
return number;
}