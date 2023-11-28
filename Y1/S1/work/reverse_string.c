#include<stdio.h>
#include<string.h>

int main() {
    char str[100];
    printf("");
    scanf("%s", str);

    int i=strlen(str);
    while (i>=0) {
        printf("%c", str[i]);
        i--;
    }
    
return 0;
}