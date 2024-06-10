#include<stdio.h>
#include<string.h>

int main()
{
    char input[30];
    int adcheck = 0, mailcheck = 0, dotcheck = 0;
    printf("input : ");
    scanf("%s", &input);
    printf("ad:%d mail:%d dot:%d\n", adcheck, mailcheck, dotcheck);
    printf("output : %s is ", input);
    for(int i = 0; i <= strlen(input); i++) //ad
    {
        if(input[i] == '@')
        {
            adcheck = 1;
            for(i; i <= strlen(input); i++) //aftad
            {
                if( ((input[i] >= 'a')&&(input[i] <= 'z')) || ((input[i] >= 'A')&&(input[i] <= 'Z')))
                {
                    mailcheck = 1;
                    for(i; i <= strlen(input); i++) //dot
                    {
                        if(input[i] == '.')
                        {
                            dotcheck = 1;
                        }
                    }
                }
            }
        }
    }
    if(!adcheck || !mailcheck || !dotcheck)
    {
        printf("not ");
    }
    printf("email address\n");
    return 0;
}
