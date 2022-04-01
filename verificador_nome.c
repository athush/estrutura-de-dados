#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define alfabeto 27

int verifica_char(char caractere, char alphabet[]){
    int i = 0;
    for(;i < alfabeto; i++) if(caractere == alphabet[i]) return 1;
    return 0;
}

int main(){
    int i = 0, j, tam, veri = 1;
    char nome[101];

    char minuscula[alfabeto] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
    char maiuscula[alfabeto] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
    printf("\nInsira um nome para que seja feita sua verificacao\n");
    fgets(nome, 100, stdin);

    tam = strlen(nome) - 1;
    printf("\nTamanho: %d\n", tam);

    while(i<tam){
        if(i == 0){
            veri = verifica_char(nome[i], maiuscula);
            if(veri == 0){
                printf("Nome inserido incorretamente, verifique o uso correto de letras maiusculas, espacos e caracteres."); 
                break;
            }
        }else if(nome[i-1] == ' '){
            veri = verifica_char(nome[i], maiuscula);
            if(veri == 0){
                printf("Nome inserido incorretamente, verifique o uso correto de letras maiusculas, espacos e caracteres.2"); 
                break;
            }
        }else{
            veri = verifica_char(nome[i], minuscula); 
            if(veri == 0){
                printf("\nCharactere(s) Invalido(s), Insira apenas letras."); 
                break;
            }
        }
        i++;
    }
    if(veri == 1){
        printf("Nome inserido corretamente!");
    }
    return 0;
}