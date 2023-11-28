#include<stdio.h>
#include<math.h>

int main()
{
    int ip1,ip2,ip3,ip0;
    printf("input : ");
    scanf("%d %d %d", &ip1, &ip2, &ip3);
    printf("output : ");

    if(ip1 > ip2 && ip1 > ip3)
    {
        if((ip1)*(ip1) == (ip2)*(ip2) + (ip3)*(ip3))
        {
            printf("yes");
        }
    }
    if(ip2 > ip1 && ip2 > ip3)
    {
        if((ip2)*(ip2) == (ip1)*(ip1) + (ip3)*(ip3))
        {
            printf("yes");
        }
    }
    if(ip3 > ip1 && ip3 > ip2)
    {
        if((ip3)*(ip3) == (ip1)*(ip1) + (ip2)*(ip2))
        {
            printf("yes");
        }
    }

    return 0;
}