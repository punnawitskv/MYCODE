#include<stdio.h>
#include<math.h>

int main(){

    printf("Enter number : ");
    int level;
    scanf("%d", &level);

    int i=0;
    while (i<level){
        printf("*");
        i++;
    }

    int xlevel=0;
    while((xlevel+2)<level){
        xlevel++;
        printf("\n");
        printf("*");

        int j=0;
        while (j<(level-2)){
            printf(" ");
            j++;
        }

    printf("*");
    }

    printf("\n");

    int k=0;
    while (k<level){
        printf("*");
        k++;
    }
        
return 0;
}