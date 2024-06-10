#include<stdio.h>
#include<math.h>
int kuukee(int num);
int main(){
    int number;
    printf("number:");
    scanf("%d", &number);
    kuukee(number);
    return 0;
}
int kuukee(num){
    if(num % 2 == 0){
        printf("kuu");
        }
    else{
        printf("kee");
        }
}