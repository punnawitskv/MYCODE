#include<stdio.h>
#include<math.h>
int main() {
    int i=0;
    do{
    printf("%d is ",i);      
        if(i%2==0){
            printf("even\n");
        }
        else{
            printf("odd\n");
        }
    i++;
    } while(i<=10);
return 0;
}