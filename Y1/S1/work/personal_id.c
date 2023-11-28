#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// ฟังก์ชันตรวจสอบรูปแบบหมายเลขบัตรประชาชน
bool isValidPersonalID(const char *input) {
    int len = strlen(input);
    
    // ตรวจสอบว่ามี 13 หลักหรือไม่
    if (len != 13) {
        return false;
    }
    
    // ตรวจสอบว่าเป็นตัวเลขทั้งหมดหรือไม่
    for (int i = 0; i < len; i++) {
        if (input[i] < '0' || input[i] > '9') {
            return false;
        }
    }
    
    // ตรวจสอบว่าเลขทุกตัวเหมือนกันหรือไม่
    char firstDigit = input[0];
    for (int i = 1; i < len; i++) {
        if (input[i] != firstDigit) {
            return true; // ค่าต่างกันแสดงว่าไม่ถูกต้อง
        }
    }
    
    return false; // ค่าเหมือนกันทั้งหมดแสดงว่าไม่ถูกต้อง
}

int main() {
    char input[14]; // สำหรับรับข้อมูล 13 หลัก + 1 หลักสำหรับ null terminator
    
    // รับ Input
    printf("Input : ");
    scanf("%s", input);
    
    // ตรวจสอบและแสดงผลลัพธ์
    if (isValidPersonalID(input)) {
        printf("PersonalID\n");
    } else {
        printf("Not PersonalID\n");
    }
    
    return 0;
}
