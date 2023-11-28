#include <stdio.h>

int main()
{
    const int stdcount = 3;

    struct student
    {
        int id;
        char name[100];
        int age;
    };


    struct student std[stdcount];
    for (int i=0;i<stdcount;i++)
    {
        printf("your id : ");
        scanf("%d", &std[i].id);
        printf("your name : ");
        scanf("%s", &std[i].name);
        printf("your age : ");
        scanf("%d", &std[i].age);
    }

    for (int i=0;i<stdcount;i++)
    {
        printf("id : %d\t", std[i].id);
        printf("name : %s\t", std[i].name);
        printf("age : %d\n", std[i].age);
    }

    return 0;
}
