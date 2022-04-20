#prioridade 'd' = 1
#prioridade 's' = 2
#prioridade 'v' = 3
#prioridade '^' = 4
#prioridade '()' = 10
#prioridade '[]' = 20

# equa -> t
# operando -> i
# operador -> j

equa = str(input('Digite a operação que deseja fazer: '))
operando = []
operador = []
prioridade_operador = []
equa = equa.replace(" ","")
tam = len(equa)
i = j = flag = t = aux = 0   
while t < tam:
    print(operando)
    print(operador)
    print(prioridade_operador)
    print(f't = {t}, i = {i}, j = {j}')
    print()

    if equa[t] == 'V' or equa[t] == 'F':
        operando.append(equa[t])
        i+=1
    elif equa[t] == '(':
        flag += 10
    elif equa[t] == '[':
        flag += 20
    elif equa[t] == ']':
        flag -= 20
    elif equa[t] == ')':
        flag -= 10
    else:
        if equa[t] == 'd':
            aux = 1+flag
        elif equa[t] == 's':
            aux = 2+flag
        elif equa[t] == 'v':
            aux = 3+flag
        elif equa[t] == '^':
            aux = 4+flag

        if j != 0 and prioridade_operador[-1] > aux:
            j-=1
            i-=1

            if operador[j] == 'v':
                if operando[i] == 'V' or operando[i-1] == 'V':
                    operando[i-1] ='V'
                else:
                    operando[i-1] ='F'
                operador.pop()
                operando.pop()
                prioridade_operador.pop()
            elif operador[j] == '^':
                if operando[i] == "V" and operando[i-1] == 'V':
                    operando[i-1] ='V'
                else:
                    operando[i-1] ='F'
                operador.pop()
                operando.pop()
                prioridade_operador.pop()
            elif operador[j] == 's':
                if operando[i] == 'F' and operando[i-1] == 'V':
                    operando[i-1] ='F'
                else:
                    operando[i-1] ='V'
                operador.pop()
                operando.pop()
                prioridade_operador.pop()
            elif operador[j] == 'd':
                if operando[i] == operando[i-1]:
                    operando[i-1] ='V'
                else:
                    operando[i-1] ='F' 
                operador.pop()
                operando.pop()
                prioridade_operador.pop()  
        prioridade_operador.append(aux)
        operador.append(equa[t])
        j+=1
    t+=1

while j > 0:
    print(operando)
    print(operador)
    print(prioridade_operador)
    print(f't = {t}, i = {i}, j = {j}')
    print()
    j-=1
    i-=1
    if operador[j] == 'v':
        if operando[i] == 'V' or operando[i-1] == 'V':
            operando[i-1] ='V'
        else:
            operando[i-1] ='F'
        operador.pop()
        operando.pop()
        prioridade_operador.pop()
    elif operador[j] == '^':
        if operando[i] == "V" and operando[i-1] == 'V':
            operando[i-1] ='V'
        else:
            operando[i-1] ='F'
        operador.pop()
        operando.pop()
        prioridade_operador.pop()
    elif operador[j] == 's':
        if operando[i] == 'F' and operando[i-1] == 'V':
            operando[i-1] ='F'
        else:
            operando[i-1] ='V'
        operador.pop()
        operando.pop()
        prioridade_operador.pop()
    elif operador[j] == 'd':
        if operando[i] == operando[i-1]:
            operando[i-1] ='V'
        else:
            operando[i-1] ='F' 
        operador.pop()
        operando.pop()
        prioridade_operador.pop()
print(equa)

print(operando)
print(operador)
print(prioridade_operador)
print(f't = {t}, i = {i}, j = {j}')
print()