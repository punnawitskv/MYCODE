#include <stdio.h>

int main() {
    int n1, n2;

    // รับ input ชุดที่ 1
    printf("Enter the size of the first set: ");
    scanf("%d", &n1);

    int set1[n1];
    printf("Enter the elements of the first set in ascending order:\n");
    for (int i = 0; i < n1; i++) {
        scanf("%d", &set1[i]);
    }

    // รับ input ชุดที่ 2
    printf("Enter the size of the second set: ");
    scanf("%d", &n2);

    int set2[n2];
    printf("Enter the elements of the second set in ascending order:\n");
    for (int i = 0; i < n2; i++) {
        scanf("%d", &set2[i]);
    }

    // เริ่มการเปรียบเทียบและแสดงผลลัพธ์
    int i = 0, j = 0;

    printf("Merged and sorted set: ");
    while (i < n1 && j < n2) {
        if (set1[i] < set2[j]) {
            printf("%d ", set1[i]);
            i++;
        } else {
            printf("%d ", set2[j]);
            j++;
        }
    }

    // เมื่อตัวใดตัวหนึ่งในชุดเหลืออยู่
    while (i < n1) {
        printf("%d ", set1[i]);
        i++;
    }

    while (j < n2) {
        printf("%d ", set2[j]);
        j++;
    }

    return 0;
}
