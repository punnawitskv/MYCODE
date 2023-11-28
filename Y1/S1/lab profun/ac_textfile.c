#include<stdio.h>

int main()
{
    const int plycount = 5;

    struct player
    {
        char name[100];
        int level;
    };

    struct player ply[plycount];
    for (int i = 1; i <= plycount; i++)
    {
        printf("your name[%d] : ", i);
        scanf("%s", &ply[i].name);
        printf("your level[%d] : ", i);
        scanf("%d", &ply[i].level);
    }
    
    FILE* fp;
    fp = fopen("ac_textfiletest.txt","w");
    for (int i = 1; i <= plycount; i++)
    {
        fprintf(fp,"player[%d] : %s\t",i,ply[i].name);
        fprintf(fp,"%d\n",ply[i].level);
    }
    close(fp);

    printf("success");

    return 0;
}
