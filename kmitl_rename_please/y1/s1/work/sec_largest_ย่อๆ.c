#include <stdio.h>

int findsecnum(int numbers[], int size) {
    int maxnum = numbers[0];
    int maxsec = numbers[1];

    for (int i = 1; i < size; i++) {
        if (numbers[i] > maxnum) {
            maxsec = maxnum;
            maxnum = numbers[i];
        } else if (numbers[i] > maxsec && numbers[i] != maxnum) {
            maxsec = numbers[i];
        }
    }

    return maxsec;
}

int main() {
    int numbers[8];

    printf("Please enter 8 numbers: ");
    for (int i = 0; i < 8; i++)
        scanf("%d", &numbers[i]);

    printf("Second Largest Element = %d\n", findsecnum(numbers, 8));

    return 0;
}
