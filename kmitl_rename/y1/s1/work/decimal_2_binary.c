#include <stdio.h>

void decimalToBinary(int decimal) {
    int binary[32];  // Assuming 32-bit binary representation
    
    int i = 0;
    while (i >= 0) {
        binary[i] = decimal % 2;
        decimal = decimal / 2;
        i++;
        
        if (decimal == 0)
            break;
    }
    
    printf("Binary representation: ");
    while (i > 0) {
        i--;
        printf("%d", binary[i]);
    }
    printf("\n");
}

int main() {
    int decimal;
    printf("Enter a decimal number: ");
    scanf("%d", &decimal);
    
    decimalToBinary(decimal);
    
    return 0;
}
