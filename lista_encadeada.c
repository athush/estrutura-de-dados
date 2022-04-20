#include <stdio.h>
#include <stdlib.h>

typedef struct noLista{
    int dado;
    struct noLista *prox;
} no;

//

void initLista(no **pNovo){
    (*pNovo)->prox = NULL;
}

//
void insereInicioLista(no **pNovo){
    no *temp;
    int valor;

    printf("\nInforme um Valor a ser Inserido : ");
    scanf("%d", &valor);

    temp = (no *)malloc(sizeof(no));
    temp->dado = valor;
    temp->prox = (*pNovo)->prox;
    (*pNovo)->prox = temp;
}
//
void imprimeLista(no **pNovo){
    no *temp;
    if((*pNovo)->prox == NULL){
        printf("Lista Vazia!\n");
    }
    else{
        temp = (no *)malloc(sizeof(no));
        temp = (*pNovo)->prox;

        while(temp != NULL){
            printf("Valor : %d\n", temp->dado);
            temp = temp->prox;
        }
    }
}
//
void removeElementoLista(no **pNovo){
    no *temp;
    if((*pNovo)->prox == NULL){
        printf("\nLista Vazia!");
    }
    else{
        temp = (*pNovo)->prox;
        (*pNovo)->prox = temp->prox;
        free(temp);
    }
}

int main(){

no *pLista;

int n, i, valor;
pLista = (no *)malloc(sizeof(struct noLista));
initLista(&pLista);


printf("\nInforme o número de elementos da lista : ");

scanf("%d", &n);

for(i = 0; i < n ; i++){ insereInicioLista(&pLista); }

printf("\nLista inserida \n");

imprimeLista(&pLista);

removeElementoLista(&pLista);

printf("\nLista após o remove: \n");

imprimeLista(&pLista);

return 0;

}