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
flag = t = 0   
while t < tam:
    print(operando)
    print(operador)
    print(prioridade_operador)
    print()

    if equa[t] == 'V' or equa[t] == 'F':
        operando.append(equa[t])
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

        if len(operador) != 0 and prioridade_operador[-1] > aux:
            operando1 = operando[-1]
            operando.pop()
            operando2 = operando[-1]
            operando.pop()
            if operador[-1] == 'v':
                if operando1 == 'V' or operando2 == 'V':
                    operando.append('V')
                else:
                    operando.append('F')
                operador.pop()
                prioridade_operador.pop()
            elif operador[-1] == '^':
                if operando1 == "V" and operando2 == 'V':
                    operando.append('V')
                else:
                    operando.append('F')
                operador.pop()
                prioridade_operador.pop()
            elif operador[-1] == 's':
                if operando1 == 'F' and operando2 == 'V':
                    operando.append('F')
                else:
                    operando.append('V')
                operador.pop()
                prioridade_operador.pop()
            elif operador[-1] == 'd':
                if operando1 == operando2:
                    operando.append('V')
                else:
                    operando.append('F')
                operador.pop()
                prioridade_operador.pop()  
        prioridade_operador.append(aux)
        operador.append(equa[t])
    t+=1

while len(operador) > 0:
    print(operando)
    print(operador)
    print(prioridade_operador)
    print()
    operando1 = operando[-1]
    operando.pop()
    operando2 = operando[-1]
    operando.pop()
    if operador[-1] == 'v':
        if operando1 == 'V' or operando2 == 'V':
            operando.append('V')
        else:
            operando.append('F')
        operador.pop()
        prioridade_operador.pop()
    elif operador[-1] == '^':
        if operando1 == "V" and operando2 == 'V':
            operando.append('V')
        else:
            operando.append('F')
        operador.pop()
        prioridade_operador.pop()
    elif operador[-1] == 's':
        if operando1 == 'F' and operando2 == 'V':
            operando.append('F')
        else:
            operando.append('V')
        operador.pop()
        prioridade_operador.pop()
    elif operador[-1] == 'd':
        if operando1 == operando2:
            operando.append('V')
        else:
            operando.append('F')
        operador.pop()
        prioridade_operador.pop()

print(operando)
print(operador)
print(prioridade_operador)
print()