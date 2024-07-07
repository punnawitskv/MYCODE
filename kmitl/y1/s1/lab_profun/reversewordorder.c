#include <stdio.h>
#include <string.h>
#include <stdlib.h> // เพิ่มไลบรารีสำหรับ atoi()

void bubbleSort(char arr[][100], int n) {
    int i, j;
    char temp[100];
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (atoi(arr[j]) > atoi(arr[j+1])) { // ใช้ atoi() เพื่อแปลงข้อความเป็นตัวเลข
                strcpy(temp, arr[j]);
                strcpy(arr[j], arr[j+1]);
                strcpy(arr[j+1], temp);
            }
        }
    }
}

int main() {
    char input[1000];
    char input2[1000];
    char words[200][100];
    int wordCount = 0;

    printf("input : ");
    gets(input);
    printf("input2 : ");
    gets(input2);

    char* token = strtok(input, " ");
    while (token != NULL) {
        strcpy(words[wordCount], token);
        wordCount++;
        token = strtok(NULL, " ");
    }

    token = strtok(input2, " ");
    while (token != NULL) {
        strcpy(words[wordCount], token);
        wordCount++;
        token = strtok(NULL, " ");
    }

    bubbleSort(words, wordCount);

    printf("output : ");
    for (int i = 0; i < wordCount; i++) {
        printf("%s ", words[i]);
    }
    return 0;
}
