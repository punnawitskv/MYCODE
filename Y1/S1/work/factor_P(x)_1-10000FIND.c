#include<stdio.h>
int factor_all(int num){
    printf("P(%d) = ", num);

        int i=2;
        int j=0;
        
        if(num>=1){
            printf("1");
            j++;
        }
        else{
            printf("X");
        }

        while (num>i){
            if(num%i==0){         
                printf(" + %d", i);
                j=j+i;
            }
            i++;
        }

        if(j==num){
            printf(" = %d", j); 
            }
}

int main(){

    for(int num=1;num<10000;num++){

        int i=2;
        int j=0;

        if(num>=1){
            j++;
        }

        while (num>i){
            if(num%i==0){         
                j=j+i;
            }
            i++;
        }

        if(j==num){
        factor_all(num);
        printf("\n");
        }
    }

return 0;
}