#include <stdio.h>

int findMin(int numbers[], int size) {
    int min = numbers[0];
    int i = 1;
    while (i < size) {
        if (numbers[i] < min) {
            min = numbers[i];
        }
        i++;
    }
    return min;
}

int findMax(int numbers[], int size) {
    int max = numbers[0];
    int i = 1;
    while (i < size) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
        i++;
    }
    return max;
}

int main() {
    int numbers[5];

    // Receive input of 5 numbers
    printf("Please enter 5 numbers: ");
    int i = 0;
    while (i < 5) {
        scanf("%d", &numbers[i]);
        i++;
    }

    // Find the minimum and maximum values
    int minimum = findMin(numbers, 5);
    int maximum = findMax(numbers, 5);

    // Display the results
    printf("Minimum value: %d\n", minimum);
    printf("Maximum value: %d\n", maximum);

    return 0;
}
