int main(){

    for(int num=1;num<=10000;num++){
        int x=1;

        for(int i=2;i<num;i++){
            if(num%i==0){
                x=x+i;
            }
        }

        if(x==num){
            printf("%d\n",x);
        }
    }

return 0;
}