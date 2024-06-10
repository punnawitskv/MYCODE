#include <stdio.h>

int sumfun(int number) {
    int sum = 0;
    while (number > 0) {
        int digit = number % 10;
        sum += digit; //sum = sum+digit;
        number /= 10; //numner = number/10;
    }
return sum;
}

int main() {
    int number;
    
    printf("Input : ");
    scanf("%d", &number);

    printf("Output : %d ", number);
    printf("-> %d ", sumfun(number));

    while(sumfun(number)>=10){
        number = sumfun(number);
        printf("-> %d ", sumfun(number));
    }
return 0;
}
