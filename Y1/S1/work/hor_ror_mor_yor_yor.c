#include<stdio.h>
#include<math.h>

int main(){

    int num1,num2,i;
    printf("");
        scanf("%d", &num1);
    printf("");
        scanf("%d", &num2);

    if(num1<num2){
        i=num1;
    }
    else{
        i=num2;
    }

    while((num1%i!=0)||(num2%i!=0)){
        i=i-1;
    }

    printf("%d", i);
    
return 0;    
}