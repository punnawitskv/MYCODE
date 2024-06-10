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

    FILE *fp;
    fp = fopen("ac_binaryfiletest.txt", "rb"); // เปิดไฟล์ในโหมด binary
    if (fp == NULL)
    {
        perror("Error opening file");
        return 1;
    }

    for (int i = 0; i < plycount; i++)
    {
        // อ่านข้อมูลจากไฟล์ binary
        fread(ply[i].name, sizeof(char), sizeof(ply[i].name), fp);
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
