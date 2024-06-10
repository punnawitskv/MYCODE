#include <stdio.h>

int main(void) {
    int n;
    n = 10;

    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (row + col < n) {
                printf("   ");
            } else {
                printf(" X ");
            }
        }
        printf(" # \n");
    }

    return 0 ;
}
