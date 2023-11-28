#include<stdio.h>
#include<math.h>

int main(){
    int startyear,endyear;
    scanf("%d %d", &startyear,&endyear);

    int i=startyear,j=endyear,leapyear=0;

    while ((i%4!=0)||(i<=0)) {
        i++;
    }

    while (j%4!=0) {
        j--;
    }

    leapyear=((j-i)/4)+1;

    printf("%d", leapyear);

return 0;
}
