#include <stdio.h>

int main() {
    int n, i, j, k=1;

    printf("Enter a number : ");
    scanf("%d", &n);

    //upper
    for (i = 1; i < n; i++) {
        
        for (j=0;j<k;j++){
            printf(" * ");
        }  
        for (j=1;j<2*(n-k);j++) {
            printf(" - ");
        }  
        for (j=0;j<k;j++){
            printf(" * ");
        }

    k++;
    printf("\n");
    }

    //midle
    for(i=1;i<n*2;i++){
        printf(" * ");
    }
    printf("\n");

    //lower
    for(i=n;i>1;i--){

        for (j=1;j<k;j++){
            printf(" * ");
        }
        for (j=0;j<=2*(n-k);j++) {
            printf(" - ");
        }
        for (j=1;j<k;j++){
            printf(" * ");
        }

    k--;
    printf("\n");
    }

    return 0;
}
