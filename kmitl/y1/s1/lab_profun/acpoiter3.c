#include <stdio.h>
#include <string.h>

int main() {
    printf("\n");

    char Str1[50];
    scanf("%s", Str1);

    char Str2[50];
    scanf("%s", Str2);

    char* Str1Pt = Str1;
    char* Str2Pt = Str2;

    int Equal = 1; // Changed to int and initialized as true (1)

    while (*Str1Pt != '\0' || *Str2Pt != '\0') {
        char currentCharStr1;
        char currentCharStr2;

        if (*Str1Pt != '\0') {
            while (*(Str1Pt + 1) == *Str1Pt && *Str1Pt != '\0') {
                Str1Pt++;
            }
            currentCharStr1 = *Str1Pt;
        }

        if (*Str2Pt != '\0') {
            while (*(Str2Pt + 1) == *Str2Pt && *Str2Pt != '\0') {
                Str2Pt++;
            }
            currentCharStr2 = *Str2Pt;
        }

        if (currentCharStr1 != currentCharStr2) {
            Equal = 0; // Changed to 0 to represent false
            break;
        }

        Str1Pt++;
        Str2Pt++;   
    }

    if (Equal == 1) { // Check for true (1)
        printf("Equal");
    } else {
        printf("NotEqual");
    }
return 0;
}
