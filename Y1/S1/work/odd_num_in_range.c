#include<stdio.h>

int main() {

    int num1,num2;

    printf("");
        scanf("%d", &num1);
    printf("");
        scanf("%d", &num2);

    if (num1%2==0) {
        num1=num1-1;
    }    


    while (num1<(num2-2)) {
        num1=num1+2;
        printf("%d\n", num1);
    }

 return 0;

}