#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int verifica_num(char num, char numbers[]){
    int i = 0;
    for(; i < 11; i++) if(num == numbers[i]) return 1;
    return 0;
}

int mais(){
    char num[101];
    char numbers[11] = {'0','1','2','3','4','5','6','7','8','9','-'};
    printf("Digite o numero que deseja verificar: ");
    fgets(num, 100, stdin);
    int i = 0, tam, neg, flo = 0, veri = 1;
    tam = strlen(num)-1;
    printf("%d", tam);
    if(num[i] == "-") neg = 1;
    else neg = 0;
    
    while(i < tam){
        if(num[i] == ",") flo = 1;
        else{
            veri = verifica_num(num[i], numbers);
            if(veri == 0) printf("\nCharacter(s) Invalido(s), tente novamente"); break;
        }
        i++;
    }
    if(veri == 1){
        if(neg == 0 && flo == 0){
            printf("\nE um numero NATURAL");
        }else if(flo == 0){
            printf("\nE um numero INTEIRO");
        }else{
            printf("E um numero REAL");
        }
    }

    return 0;
}
//Inteiro
//Real
//Natural