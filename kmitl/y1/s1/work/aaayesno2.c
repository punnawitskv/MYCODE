#include<stdio.h>

int sort(int Number[3]) {

    for(int j = 0 ; j<2;j++){
        if(Number[j] > Number[j+1]){
            int temp = Number[j];
            Number[j] = Number[j+1];
            Number[j+1] = temp;
        }
    }
    if (Number[2]*Number[2] == Number[1]*Number[1] + Number[0]*Number[0])
    {
        printf("yes");
    }
    else
    {
        printf("no");
    }
    
return 0;

}

int main() {
    int numbers[3];

    printf("input : ");
    for (int i = 0; i < 3; i++) {
        scanf("%d", &numbers[i]);
    }
    printf("output : ");
    sort(numbers);
return 0;
}