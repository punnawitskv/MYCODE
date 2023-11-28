#include <stdio.h>
#include <string.h>

int main() {
    char long_string[100];
    char sub_string[100];
    int index;

    // รับ input
    printf("Enter long string: ");
    scanf("%[^\n]", long_string);

    printf("Enter substring: ");
    scanf(" %[^\n]", sub_string);

    // ค้นหา substring ด้วยฟังก์ชัน strstr()
    char* ptr = strstr(long_string, sub_string);

    // ตรวจสอบว่าค้นพบหรือไม่
    if (ptr != NULL) {
        // หา index ของ substring ที่ค้นพบ
        index = ptr - long_string;
        printf("Substring found at index %d\n", index);
    } else {
        printf("Substring not found\n");
    }

    return 0;
}
