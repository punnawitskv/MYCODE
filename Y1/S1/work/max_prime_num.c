#include <stdio.h>

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);

    int maxPrime = 0;

    for (int i = 2; i <= number; i++) {
        while (number % i == 0) {
            maxPrime = i;
            number /= i;
        }
    }

    printf("Maximum prime factor: %d\n", maxPrime);

    return 0;
}
