#include<stdio.h>
#include<math.h>
int main() {
    int level;
        scanf("%u", &level);
    for (int i = 0; i < level; i++) {
        for (int j = 0; j <= i; j++)
            {
            printf("#");
            }
        printf("\n");
        }
return 0;
}