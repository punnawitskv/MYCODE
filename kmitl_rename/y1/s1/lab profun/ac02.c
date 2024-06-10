#include <stdio.h>

int isPrime(int num);

int main() {
    int num;
    printf("Input : ");
    scanf("%d", &num);

    printf("Output : ");

    if (isPrime(num) == 0) {
        printf("Not Prime Number");
    } else {
        printf("Prime Number");
    }

    return 0;
}

int isPrime(int num) {
    if (num <= 1) {
        return 0;  
    }

    for (int loop = 2; loop * loop <= num; loop++) {
        if (num % loop == 0) {
            return 0; 
        }
    }

    return 1; 
}
