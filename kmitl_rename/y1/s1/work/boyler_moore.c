#include <stdio.h>
#include <string.h>

#define MAX_CHAR 256

// void precomputeBadCharShift(char *keyword, int keyword_length, int badCharShift[MAX_CHAR]) {
//     int i;
//     for (i = 0; i < MAX_CHAR; i++) {
//         badCharShift[i] = keyword_length;
//     }
//     for (i = 0; i < keyword_length - 1; i++) {
//         badCharShift[(int)keyword[i]] = keyword_length - i - 1;
//     }
// }

// int max(int a, int b) {
//     return (a > b) ? a : b;
// }

// void searchBoyerMoore(char *text, char *keyword) {
//     int text_length = strlen(text);
//     int keyword_length = strlen(keyword);
    
//     int badCharShift[MAX_CHAR];
//     precomputeBadCharShift(keyword, keyword_length, badCharShift);
    
//     int s = 0; // Shift of the pattern with respect to text
//     int found = 0; // Flag to indicate if keyword is found
    
//     while (s <= text_length - keyword_length) {
//         int j = keyword_length - 1;
        
//         while (j >= 0 && keyword[j] == text[s + j]) {
//             j--;
//         }
        
//         if (j < 0) {
//             printf("%d\n", s);
//             found = 1;
//             s += (s + keyword_length < text_length) ? keyword_length - badCharShift[(int)text[s + keyword_length]] : 1;
//         } else {
//             s += max(1, badCharShift[(int)text[s + j]] - j);
//         }
//     }
    
//     if (!found) {
//         printf("Keyword not found\n");
//     }
// }

int main() {
    char text[1000], keyword[100];
    
    printf("text: ");
    fgets(text, sizeof(text), stdin);
    //text[strcspn(text, "\n")] = '\0'; // Remove newline character
    
    printf("keyword: ");
    fgets(keyword, sizeof(keyword), stdin);
    //keyword[strcspn(keyword, "\n")] = '\0'; // Remove newline character
    
    printf("output:\n");
    //searchBoyerMoore(text, keyword);
    printf(text);
    printf(keyword);
    
    return 0;
}
