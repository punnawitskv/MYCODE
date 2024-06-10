#include<stdio.h>

int main()
{ 
    FILE *fptr;
    struct student
    { char name[20];
        char ID[9];
        int age;
    }s;

    fptr = fopen("StRecord.txt", "r");

    if (fptr == (FILE *)NULL) 
        printf("Cannot open file\n");
    else
        while (fread(&s,sizeof(struct student),1,fptr)!=0)
        { 
            printf("Name: %s\n", s.name);
            printf("ID: %s and Age: %d\n", s.ID,s.age);
            printf("---------------------------------\n");
        }
        
    fclose(fptr);
    return 0;
}