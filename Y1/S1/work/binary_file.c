#include<stdio.h>

int main()
{
    const int plycount = 5;

    struct player
    {
        char name[100];
        int level;
        float score;
    };

    struct player ply[plycount];
    for (int i = 1; i <= plycount; i++)
    {
        printf("your name[%d] : ", i);
        scanf("%s", &ply[i].name);
        printf("your level[%d] : ", i);
        scanf("%d", &ply[i].level);
        printf("your score[%d] : ", i);
        scanf("%f", &ply[i].score);
    }
    
    FILE* fp;
    fp = fopen("ac_textfiletest.txt","w");
    for (int i = 1; i <= plycount; i++)
    {
        fwrite(ply[i].name, sizeof(char), sizeof(ply[i].name), fp);
        fwrite(&ply[i].level, sizeof(int), 1, fp);
        fwrite(&ply[i].score, sizeof(float), 1, fp);
    }
    close(fp);

    printf("success");

    return 0;
}
