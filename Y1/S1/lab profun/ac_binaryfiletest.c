#include <stdio.h>
#include <string.h>

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
    for (int i = 0; i < plycount; i++)
    {
        printf("Enter your name[%d]: ", i+1);
        scanf("%s", ply[i].name);
        printf("Enter your level[%d]: ", i+1);
        scanf("%d", &ply[i].level);
        printf("Enter your score[%d]: ", i+1);
        scanf("%f", &ply[i].score);
    }
    
    FILE* fp;
    fp = fopen("ac_binaryfiletest.txt", "wb"); // เปิดไฟล์ในโหมด binary
    if (fp == NULL)
    {
        perror("Error opening file");
        return 1;
    }
    
    for (int i = 0; i < plycount; i++)
    {
        fwrite(ply[i].name, sizeof(char), 1, fp);
        fwrite(&ply[i].level, sizeof(int), 1, fp);
        fwrite(&ply[i].score, sizeof(float), 1, fp);
    }
    
    fclose(fp); // ปิดไฟล์หลังจากใช้งาน

    printf("Success\n");

    // อ่านข้อมูลจากไฟล์ binary
    fp = fopen("ac_binaryfiletest.txt", "rb"); // เปิดไฟล์ในโหมด binary
    if (fp == NULL)
    {
        perror("Error opening file");
        return 1;
    }

    for (int i = 0; i < plycount; i++)
    {
        fread(ply[i].name, sizeof(char), 1, fp);
        fread(&ply[i].level, sizeof(int), 1, fp);
        fread(&ply[i].score, sizeof(float), 1, fp);

        // แสดงข้อมูลที่อ่าน
        printf("Name: %s\t", ply[i].name);
        printf("Level: %d\t", ply[i].level);
        printf("Score: %f\n", ply[i].score);
    }

    fclose(fp); // ปิดไฟล์

    return 0;
}
