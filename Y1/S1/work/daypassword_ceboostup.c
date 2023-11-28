#include<stdio.h>
#include<math.h>
int main(){
printf("");
int year,month,day,hour,min,sec,spsec;
char dotyear,dotmonth,dotday,dothour,dotmin,dotsec;
scanf("%d %c %d %c %d %c %d %c %d %c %d %c %d", &year,&dotyear,&month,&dotmonth,&day,&dotday,&hour,&dothour,&min,&dotmin,&sec,&dotsec,&spsec);
int A=year*month*sec;
int B=(hour+spsec)*sec;
char C;
if((day*spsec)>1500){
C='A';
}
else{
C='B';
}
printf("%d%d%c", A,B,C);
return 0;
}