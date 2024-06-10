#include<stdio.h>

int sort(int Number[4]) {

    for(int i=0;i<4;i++){
        for(int j = 0 ; j<4-i-1;j++){
            if(Number[j]>Number[j+1]){
                int temp = Number[j];
                Number[j] = Number[j+1];
                Number[j+1] = temp;
            }
        }
    }
    printf("%d", Number[1]+Number[2]);
    
return 0;

}

int main() {
    int numbers[4];

    printf("input : ");
    for (int i = 0; i < 4; i++) {
        scanf("%d", &numbers[i]);
    }
    printf("output : ");
    sort(numbers);
return 0;
}