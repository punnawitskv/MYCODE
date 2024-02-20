#include<stdio.h>

int main()
{
    FILE *fptr; int noffset;
    struct student 
    {
        char name[20];
        char ID[9];
        int age;
    } s;
    fptr = fopen("StRecord.txt", "w");

    strcpy (s.name,"Student A"); strcpy (s.ID,"48010000");
    s.age = 17;
    fwrite(&s, sizeof(struct student), 1, fptr);

    strcpy (s.name,"Student B"); strcpy (s.ID,"48012000");
    s.age = 18;
    fwrite(&s, sizeof(struct student), 1, fptr);

    strcpy (s.name,"Student C"); strcpy (s.ID,"48015000");
    s.age = 2000;
    fwrite(&s, sizeof(struct student), 1, fptr);
    
    fclose(fptr);

    fptr = fopen("StRecord.txt", "r");
    noffset = 0 * sizeof(struct student);
    if (fseek( fptr, noffset, 0) == 0 )
    { 
        if (fread(&s,sizeof(struct student),1,fptr) != 0)
        { 
            printf("Name: %s\n", s.name);
            printf("ID: %s and Age: %d\n", s.ID,s.age);
            printf("---------------------------------\n");
        }
    }
    fclose(fptr);

    fptr = fopen("StRecord.txt", "r");
    noffset = 1 * sizeof(struct student);
    if (fseek( fptr, noffset, 0) == 0 )
    { 
        if (fread(&s,sizeof(struct student),1,fptr) != 0)
        { 
            printf("Name: %s\n", s.name);
            printf("ID: %s and Age: %d\n", s.ID,s.age);
            printf("---------------------------------\n");
        }
    }
    fclose(fptr);

    fptr = fopen("StRecord.txt", "r");
    noffset = 2 * sizeof(struct student);
    if (fseek( fptr, noffset, 0) == 0 )
    { 
        if (fread(&s,sizeof(struct student),1,fptr) != 0)
        { 
            printf("Name: %s\n", s.name);
            printf("ID: %s and Age: %d\n", s.ID,s.age);
            printf("---------------------------------\n");
        }
    }
    fclose(fptr);
}