#include <stdio.h>


int main() {
    char str[100];
    printf("Input : ");
    scanf("%s", str);

    printf("Output : ");
    for (int i = 0; str[i] != '\0'; i++) {
        if (isupper(str[i])) {
            printf("%c", str[i]);
        }
    }

    return 0;
}