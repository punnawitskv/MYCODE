#include <stdio.h>

int main()
{
    FILE *fptr;
    int noffset;
    struct player
    {
        char name[20];
        char lv[10];
        int scr;
    } s;
    fptr = fopen("ac_binaryfile.txt", "w");

    for (int i = 0; i < 5; i++)
    {
        printf("NAME[%c] : ", i + 'A');
        scanf("%s", s.name);
        printf("LEVEL[%c] : ", i + 'A');
        scanf("%s", s.lv);
        printf("SCORE[%c] : ", i + 'A');
        scanf("%d", &s.scr);
        fwrite(&s, sizeof(struct player), 1, fptr); // Write one element
    }

    fclose(fptr);

    fptr = fopen("ac_binaryfile.txt", "r");
    for (int i = 0; i <= 4; i++)
    {
        noffset = i * sizeof(struct player);
        if (fseek(fptr, noffset, SEEK_SET) == 0)
        {
            if (fread(&s, sizeof(struct player), 1, fptr) != 0)
            {
                printf("Name[%c]: %s\t", i + 'A', s.name);
                printf("Level: %s\tScore: %d\n", s.lv, s.scr);
                printf("--------------------------------------------------\n");
            }
        }
    }
    fclose(fptr);
    return 0;
}