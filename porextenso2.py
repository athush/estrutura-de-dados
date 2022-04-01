num = list(str(input("\nDigite o número para saber ele por extenso: ")))
extenso = []
tam = len(num)
i = 0
conjuntos = tam // 3
resto = tam % 3
print(f'numero: {num}\n tamanho: {tam}\n conjuntos: {conjuntos}\n Resto: {resto}')
while(i < tam):
    if num[i] == '1':
        if resto == 0:
            if tam >=3 and num[i+1] == '0' and num[i+2] == '0':
                extenso.append('Cem')
            else:
                extenso.append('Cento')
                extenso.append('e')
                resto = 2
        elif resto == 2:
            if num[i+1] == '0':
                extenso.append('Dez')
            elif num[i+1] == '1':
                extenso.append('Onze')
            elif num[i+1] == '2':
                extenso.append('Doze')
            elif num[i+1] == '3':
                extenso.append('Treze')
            elif num[i+1] == '4':
                extenso.append('Quatorze')
            elif num[i+1] == '5':
                extenso.append('Quinze')
            elif num[i+1] == '6':
                extenso.append('Dezesseis')
            elif num[i+1] == '7':
                extenso.append('Dezessete')
            elif num[i+1] == '8':
                extenso.append('Dezoito')
            elif num[i+1] == '9':
                extenso.append('Dezenove')
            resto-=2
            i+=1
        elif resto == 1:
            extenso.append('Um')
            resto-=1
    elif num[i] == '2':
        if resto == 0:
            extenso.append('Duzentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Vinte')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Dois')
            resto-=1
    elif num[i] == '3':
        if resto == 0:
            extenso.append('Trezentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Trinta')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Três')
            resto-=1
    elif num[i] == '4':
        if resto == 0:
            extenso.append('Quatrocentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Quarenta')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Quatro')
            resto-=1
    elif num[i] == '5':
        if resto == 0:
            extenso.append('Quinhentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Cinquenta')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Cinco')
            resto-=1   
    elif num[i] == '6':
        if resto == 0:
            extenso.append('Seiscentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Sessenta')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Seis')
            resto-=1
    elif num[i] == '7':
        if resto == 0:
            extenso.append('Setecentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Setenta')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Sete')
            resto-=1
    elif num[i] == '8':
        if resto == 0:
            extenso.append('Oitocentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Oitenta')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Oito')
            resto-=1
    elif num[i] == '9':
        if resto == 0:
            extenso.append('Novecentos')
            extenso.append('e')
            resto = 2
        elif resto == 2:
            extenso.append('Noventa')
            extenso.append('e')
            resto-=1
        elif resto == 1:
            extenso.append('Nove')
            resto-=1
    elif num[i] == '0':
        if resto == 1 and num[i-1] != '1':
            extenso.pop()
            resto-=1
        elif resto == 0:
            resto = 2
        elif resto == 2 or resto == 1:
            resto-=1

    print(f'Resto: {resto}\nI: {i}')

    if resto == 0:
        if conjuntos == 5:
            extenso.append('Trilhões')
        elif conjuntos == 4:
            extenso.append('Bilhões')
        elif conjuntos == 3:
            extenso.append('Milhões')
        elif conjuntos == 2:
            extenso.append('Mil')
        conjuntos-=1
    i+=1
print()
for l in extenso:
    print(f'{l}', end=" ")