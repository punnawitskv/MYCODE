#include <stdio.h>

int main() {
    int numbers[5];
    int i, ascending = 1;

    // รับค่าจำนวนเต็ม 5 ค่าและเก็บในอาเรย์
    printf("Enter 5 integers: ");
    for (i = 0; i < 5; i++) {
        scanf("%d", &numbers[i]);
    }

    // ตรวจสอบว่าลำดับของตัวเลขเป็น Ascending order หรือไม่
    for (i = 1; i < 5; i++) {
        if (numbers[i] < numbers[i - 1]) {
            ascending = 0;
            break;
        }
    }

    // แสดงผลลัพธ์
    if (ascending) {
        printf("Ascending order\n");
    } else {
        printf("Not ascending order\n");
    }

    return 0;
}
