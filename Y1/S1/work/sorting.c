#include<stdio.h>
#include<string.h>

int main() {
    
    int num1,num2,num3,num4,num5;
    printf("");
    scanf("%d %d %d %d %d", &num1,&num2,&num3,&num4,&num5);

    int a=num1,b=num2,c=num3,d=num4,e=num5,f;

    while (a>b || b>c || c>d || d>e){
        if(a>b){
            f=a;
            a=b;
            b=f;
            printf("[%d-%d] %d %d %d\n", a,b,c,d,e);
        }
        if(b>c){
            f=b;
            b=c;
            c=f;
            printf("%d [%d-%d] %d %d\n", a,b,c,d,e);
        }
        if(c>d){
            f=c;
            c=d;
            d=f;
            printf("%d %d [%d-%d] %d\n", a,b,c,d,e);
        }
        if(d>e){
            f=d;
            d=e;
            e=f;
            printf("%d %d %d [%d-%d]\n", a,b,c,d,e);
        }
    }

    printf("%d %d %d %d %d", a,b,c,d,e);
    
return 0;

}