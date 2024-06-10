#include <stdio.h>

void printChars(char c, int num) {
    for (int i = 0; i < num; i++) {
        printf("%c", c);
    }
}

int main() {
    int n;

    printf("Enter a number: ");
    scanf("%d", &n);

    // Upper
    for (int i = n - 1; i > 0; i--) {
        printChars('*', (n - i));
        printChars('-', (i - 1) * 2 + 1);
        printChars('*', (n - i));
        printf("\n");
    }

    // Middle
    printChars('*', n * 2 - 1);
    printf("\n");

    // Lower
    for (int i = 1; i < n; i++) {
        printChars('*', (n - i));
        printChars('-', (i - 1) * 2 + 1);
        printChars('*', (n - i));
        printf("\n");
    }

    return 0;
}
