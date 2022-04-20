#include <stdio.h>
#include <string.h>

/*
    Funções para aplicar:
        -Retornar a Cabeça
        -Retornar a Cauda
        -Concatenar Arrays
        -Printar elementos          *
        -Adicionar elementos        *
        -Retornar Comprimento       *
        -Verificar elemento
        -Inverter array
*/

/*
 fila de prioridade
 pilha ordenada - torre de hanoi
 
*/

#define TAM 20

void adicona_elemento(int lista[], int* tamanho){
    if(*tamanho == TAM){
        printf("Lista Cheia!\n");
    }else{
        scanf("%d", &lista[*tamanho]); 
        *tamanho+=1;
    }
}

void remover_elemento(int lista[], int tamanho, int* shift_i){
    int elemento, i;
    printf("Qual elemento deseja Remover? ");
    scanf("%d", &elemento);
    for(i = 0; i < tamanho; i++){
        if(elemento == lista[i]){
            lista[i] = -1;
            *shift_i+=1;
        }else if(i == tamanho-1){
            printf("Elemento nao encontrado na lista.\n");
        }
    }
}

void printar_lista(int lista[], int tamanho){
    int i;
    for(i=0; i < tamanho; i++){
        if(lista[i] == -1);
        else {
            if(i == tamanho - 1) printf("%d\n", lista[i]);
            else printf("%d, ", lista[i]);
        }
    }
}

void tamanho_lista(int tamanho){
    printf("O comprimento da Lista é de %d Elementos\n", tamanho);
}

void procura_elemento(int lista[], int tamanho){
    int elemento, i;
    printf("Qual elemento deseja Procurar? ");
    scanf("%d", &elemento);

    for(i = 0; i < tamanho; i++){
        if(elemento == lista[i]){
            printf("O elemento %d, esta na lista na posicao %d", lista[i], i);
        }else if (i == tamanho -1){
            printf("Elementos não encontrado");
        }
        
    }
}

void cabeca_lista(int lista[]){
    printf("A cabeça da lista e o Elemento: %d", lista[0]);
}

void cauda_lista(int lista[], int tamanho){
    printf("Os elementos da Cauda sao: ");
    int i;
    for(i=1; i < tamanho; i++){
        if(lista[i] == -1) i++;
        if(i == tamanho - 1) printf("%d\n", lista[i]);
        else printf("%d, ", lista[i]);
    }
}

void inverter_lista(int lista[], int tamanho){
    int i, aux, t = tamanho /2;
    for(i= 0; i < t; i++){
        aux = lista[i];
        lista[i] = lista[tamanho-1-i];
        lista[tamanho-1-i] = aux;
    }
}

void reiniciar_lista(int *tamanho){
    *tamanho = 0;
}

void shift(int lista[], int* tamanho, int* shift_i){
    int i, j;
    for(i = 0; i < *tamanho; i++){
        if(lista[i] == -1){
            for(j = i;j < *tamanho; j++){
                lista[j] = lista[j+1];
            }
            *shift_i-=1;
            *tamanho-=1;
        }
    }
}

int main(){
    int lista[TAM], tamanho = 0,shift_i = 0, comand = -1;
    int *tamanho_p, *shift_p;
    tamanho_p = &tamanho;
    shift_p = &shift_i;

    while(1){
        printf("\nO que Deseja fazer?\n");
        printf("\t[1] - Adicionar Elemento\n");
        printf("\t[2] - Remover Elemento\n");
        printf("\t[3] - Printar Lista\n");
        printf("\t[4] - Exibir Tamanho da Lista\n");
        printf("\t[5] - Procurar Elemento\n");
        printf("\t[6] - Saber Cabeça da Lista\n");
        printf("\t[7] - Saber Cauda da Lista\n");
        printf("\t[8] - Inverter Lista\n");
        printf("\t[9] - Reiniciar Lista\n");
        printf("\t[0] - Fechar Programa\n");
        scanf("%d", &comand);

        if(comand == 1){adicona_elemento(lista, tamanho_p);}
        else if(comand == 2){remover_elemento(lista, tamanho, shift_p);}
        else if(comand == 3){printar_lista(lista, tamanho);}
        else if(comand == 4){tamanho_lista(tamanho);}
        else if(comand == 5){procura_elemento(lista, tamanho);}
        else if(comand == 6){cabeca_lista(lista);}
        else if(comand == 7){cauda_lista(lista, tamanho);}
        else if(comand == 8){inverter_lista(lista, tamanho);}
        else if(comand == 9){reiniciar_lista(tamanho_p);}
        else if(comand == 0){printf("Programa Encerrado!\n"); break;}
        else{printf("Digite um comando valido.\n");}

        if(shift_i == 5){printf("%d", shift_i); shift(lista, tamanho_p, shift_p); printf("%d", shift_i);}
    }

    return 0;
}