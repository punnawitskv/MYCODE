#include <stdio.h>

int main() {
    int number;
    int sum = 0;
    
    printf("Input Number: ");
    scanf("%d", &number);
    
    while (number > 0) {
        int digit = number % 10;
        sum += digit;
        number /= 10;
    }
    
    printf("Sum = %d\n", sum);
    
    return 0;
}
