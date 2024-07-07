/*
  เขียนโปรแกรมรับ input เป็นตัวเลข 2 ตัว ตัวแรก (m) คือตัวเลขสำหรับคำนวณความยาวด้านของรูปสี่เหลี่ยมจตุรัส โดยขนาดของรูปสี่เหลี่ยมจะมีด้านยาว =2m+1 ส่วนตัวที่สอง (n) คือตัวเลขที่อยู่ตรงกลาง โดยถ้า m=3,n=0 จะได้สี่เหลี่ยมที่มีความกว้าง = 7 และมีตัวเลขที่อยู่ตรงกลางคือ 0 ดังนี้

input :
m=3
n=0
output : 
3  3  3  3  3  3  3
3  2  2  2  2  2  3
3  2  1  1  1  2  3
3  2  1  0  1  2  3
3  2  1  1  1  2  3
3  2  2  2  2  2  3
3  3  3  3  3  3  3
  
input :
m = 2
n = 1
output :
3  3  3  3  3
3  2  2  2  3
3  2  1  2  3
3  2  2  2  3
3  3  3  3  3


*/

#include<stdio.h>
#include<math.h>

int main()
{
    int num;
    printf("number : ");
    scanf("%d", &num);

    int centernum;
    printf("centernumber : ");
    scanf("%d", &centernum);

    int width = 2*num + 1;

    int bordernum = num + centernum;

    printf("num:%d  centernum:%d  width:%d  bordernum:%d\n", num, centernum, width, bordernum);

    for(int i=0; i<width; i++)
    {
        for(int j=0; j<width; j++)
        {
            if(i >= j && i+j < width) 
            {
              printf("%d  ", (bordernum - j)%10);
              //printf("A  ");
            }
            else if(j >= i && i+j < width) 
            {
              printf("%d  ", (bordernum - i)%10);
              // printf("B  ");
            }
            else if(j >= i && j >= width/2)
            {
              printf("%d  ", (bordernum - width + 1 + j)%10);
              //printf("C  ");
            }      
            else
            {
              printf("%d  ", (bordernum - width + 1 + i)%10);
              //printf("D  ");
            }
        }
        printf("\n");
    }

    return 0;
}
