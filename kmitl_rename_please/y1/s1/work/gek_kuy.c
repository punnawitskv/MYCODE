#include<stdio.h>
#include<math.h>
int main() {
    int number;
    printf("");
    scanf("%d", &number);
    int i=number;
    int output=number;
    while(i>=5){
        i=i-4;
        output++;
    }
    printf("%d", output);
return 0;
}