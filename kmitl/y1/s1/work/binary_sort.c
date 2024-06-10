#include<stdio.h>

int bubble_sort(int Number[10]) {

    for(int i=0;i<10;i++){
        for(int j = 0 ; j<10-i-1;j++){
            if(Number[j]>Number[j+1]){
                int temp = Number[j];
                Number[j]=Number[j+1];
                Number[j+1] =temp;
            }
        }
    }
   for(int i=0;i<9;i++){
        printf("%d, ",Number[i]);
    }
    printf("%d", Number[9]);
    
return 0;

}

int main() {
    int numbers[10];

    printf("");
    for (int i = 0; i < 10; i++) {
        scanf("%d,", &numbers[i]);
    }

    bubble_sort(numbers);
return 0;
}