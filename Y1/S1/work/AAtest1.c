#include<stdio.h>
#include<string.h>

int main()
{
    char input1[14];
    char input2[14];

    int check = 1;

    int output;

    printf("INPUT1: ");
    scanf("%s", &input1);

    printf("INPUT2: ");
    scanf("%s", &input2);

    //Check Input
    printf("check input: %s,%s\n", input1, input2);

    //Check ว่าตัวอักษรเท่ากันไหม
    if(strlen(input1) == strlen(input2))
    {
        //Check ว่าตัวอักษรเหมือนกันไหม
        for(int i=0; i<=strlen(input1); i++)
        {
            for(int c=0; c<=strlen(input1); c++)
            {
                if((input1[c] == input1[i]) && (i != c))
                {
                    check++;
                }
            }

            printf("test check before = %d\n", check);

            //Checking
            for(int j=0; j<=strlen(input2); j++)
            {
                if(input1[i] == input2[j])
                {
                    check --;
                }
            }

            printf("test check after = %d\n", check);

            if(check == 0)
            {
                output = 1;
            }
            else
            {
                output = 0;
                break;
            }

            check = 1;
        }
    }
    else
    {
        output = 0;
    }


    printf("OUTPUT: ");
    if(output == 1)
    {
        printf("TRUE");
    }
    else
    {
        printf("FALSE");
    }

    return 0;
}