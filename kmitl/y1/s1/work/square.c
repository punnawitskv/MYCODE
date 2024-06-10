#include<stdio.h>
#include<math.h>

int main() {

    int a,b;
    printf("");
    scanf("%d %d", &a,&b);

    for(int i=0;i<a;i++){
        for(int j=0;j<b;j++){
            printf("*");
        }
        printf("\n");
    }

return 0;
}