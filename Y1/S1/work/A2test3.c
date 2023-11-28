#include<stdio.h>
#include<math.h>

int main()
{
    int maxnum = 5;
    int px[maxnum];
    int py[maxnum];

    //input
    for(int i=0; i<maxnum; i++)
    {
        printf("Point[%d] : ", i);
        scanf("%d %d", &px[i], &py[i]);
        printf("Input[%d] Success\n", i);
    }
    printf("InputSuccess");

    //checkinput
    printf("\nCheckInput : ");
    for(int i=0; i<maxnum; i++)
    {
        printf("(%d,%d) ", px[i], py[i]);
    }
    printf("\nCheckInputSuccess");

    //cal
    float dismost = 0;
    float disnew;
    int opx[2];
    int opy[2];
    printf("\nCalculating");
    for(int i=0; i<maxnum; i++)
    {
        for(int j=0; j<maxnum; j++)
        {
            disnew = sqrt( pow( (px[i]-px[j]), 2 ) + pow( (py[i]-py[j]), 2 ) );
            if(disnew > dismost)
            {
                dismost = disnew;
                opx[0] = px[i];
                opy[0] = py[i];
                opx[1] = px[j];
                opy[1] = py[j];
            }
        }
    }
    printf("\nOutput : Point(%d,%d) and Point(%d,%d) Distance(%.2f)", opx[0], opy[0], opx[1], opy[1], dismost);
    printf("\nSuccess");
    return 0;
}