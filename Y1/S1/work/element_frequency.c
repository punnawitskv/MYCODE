#include <stdio.h>

#define SIZE 10

int main() {
    int numbers[SIZE];
    int counts[SIZE] = {0}; // ตั้งค่าจำนวนเริ่มต้นให้เป็น 0 สำหรับแต่ละตัวเลข

    printf("Enter 10 numbers : ");
    for (int i = 0; i < SIZE; i++) {
        scanf("%d", &numbers[i]);
    }

    // นับจำนวนเต็มในอาร์เรย์ numbers
    for (int i = 0; i < SIZE; i++) {
        counts[numbers[i]]++;
    }

    printf("Number frequencies:\n");
    for (int i = 0; i < SIZE; i++) {
        if (counts[i] > 0) {
            printf("Element %d: Frequency = %d\n", i, counts[i]);
        }
    }

    return 0;
}
