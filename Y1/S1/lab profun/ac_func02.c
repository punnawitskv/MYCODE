#include <stdio.h>
#include <math.h>

float area(x1,y1,x2,y2,x3,y3)
{
    float output;
    output = (abs((x1*(y2-y3)) + (x2*(y3-y1)) + (x3*(y1-y2))))/2;
    return output;
}

main ()
{
    int x1,y1,x2,y2,x3,y3;
    printf("input : ");
    scanf("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);
    printf("output : %.2f" ,area(x1,y1,x2,y2,x3,y3));
}