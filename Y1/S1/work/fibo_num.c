#include<stdio.h>
#include<math.h>

int fibo(int num);
int main() {
    printf("input : ");
        int num;
            scanf("%d", &num);
                printf("output : %d", fibo(num));
return 0;
}
int fibo(num) {
    int output=0;
        if(num==2){
            output=1;
        }
            if(num>2){
                output=fibo(num-1)+fibo(num-2);
            }
return output;
}