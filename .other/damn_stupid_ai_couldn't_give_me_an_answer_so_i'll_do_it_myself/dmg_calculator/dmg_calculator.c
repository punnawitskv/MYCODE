#include <stdio.h>

void damage_calculator(float atk, float def, float pen);

int main(){
    float atk[] = {0, 1, 10, 100, 1000};
    float def[] = {0, 1, 10, 100, 1000};
    float pen[] = {0, 1, 10, 100, 1000};

    for(int i = 0; i < sizeof(atk)/sizeof(atk[0]); i++){
        for(int j = 0; j < sizeof(def)/sizeof(def[0]); j++){
            for(int k = 0; k < sizeof(pen)/sizeof(pen[0]); k++){
                damage_calculator(atk[i], def[j], pen[k]);
            }
            printf("\n");
        }
        printf("**************************************************************************\n\n");
    }

    return 0;
}

void damage_calculator(float atk, float def, float pen){
    float damage = atk * (1 - (def / (def + pen + 100)));
    printf("atk: %.2f\tdef: %.2f\tpen: %.2f\tdamage: %.2f\n", atk, def, pen, damage);
}