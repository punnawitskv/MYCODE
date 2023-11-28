# include<stdio.h>

int main()
{
    int dec;
    int dec2bin;
    int dec2hexdec;
    int bin[32];
    char hexdec[32];
    int i;

    printf("Decimal : ");
    scanf("%d", &dec);

    dec2bin = dec;
    dec2hexdec = dec;

    i = 0;
    do
    {
        bin[i] = dec2bin % 2;
        dec2bin = dec2bin / 2;
        i++;
    } while (dec2bin != 0);
    printf("Binary : ");
    for (i--; i >= 0; --i)
    {
        printf("%d", bin[i]);
    }

    printf("\n");

    i = 0;
    do {
        int remainder = dec2hexdec % 16;
        if (remainder < 10) {
            hexdec[i] = remainder + '0';
        } else {
            hexdec[i] = remainder + 'A' - 10;
        }
        dec2hexdec = dec2hexdec / 16;
        i++;
    } while (dec2hexdec != 0);
    printf("Hexadecimal : ");
    for (i--; i >= 0; --i) {
        printf("%c", hexdec[i]);
    }
    
    return 0;
}