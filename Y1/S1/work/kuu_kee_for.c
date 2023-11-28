#include<stdio.h>
#include<math.h>
int main() {
    int i = 0;
    for (i;i <= 10;) {
    printf("%d is ",i);      
        if(i%2==0){
            printf("even\n");
        }
        else{
            printf("odd\n");
        }
    i++;
    }
return 0;
}