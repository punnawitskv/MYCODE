#include<stdio.h>
#include<math.h>

int main() {

    float num1;
    float num2;
    float num3;

    printf("num_1:");
    scanf("%f", &num1);

    printf("num_2 :");
    scanf("%f", &num2);

    printf("num_3 :");
    scanf("%f", &num3);

    if(num1>num2 & num1>num3) {
        printf("mostnumis %f\n", num1);

    } else if(num1<num2 & num2>num3) {
        printf("mostnumis %f\n", num2);

    } else{
        printf("mostnumis %f\n", num3);

    }

    return 0;

}