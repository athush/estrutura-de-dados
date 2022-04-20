#prioridade 'd' = 1
#prioridade 's' = 2
#prioridade 'v' = 3
#prioridade '^' = 4
#prioridade '()' = 10
#prioridade '[]' = 20

print('\033[;1m'+ '\033[1;34m'+'\n         Verificador de Expressões Booleanas'+'\033[0;0m')
print('\033[;1m'+'Coloque expressões bem formadas podendo fazer o uso de parenteses e colchetes.')
print('\033[1;92m'+'Instruções para o input:\n  [ V ]-> Verdadeiro\n  [ F ]-> Falso\n  [ ^ ]-> And\n  [ v ]-> Or\n  [ s ]-> Implica\n  [ d ]-> Bi-implica\n'+'\033[0;0m')

equa = str(input('\033[;1m'+'Digite a expressão que deseja verificar: '+'\033[0;0m'))
operando = []
operador = []
prioridade_operador = []
equa = equa.replace(" ","")
tam = len(equa)
flag = t = 0   
while t < tam:
    if equa[t] == 'V' or equa[t] == 'F':
        print(f'\033[1;35mPilha dos Operandos:            {operando}\033[0;0m')
        print(f'\033[1;93mPilha dos Operadores:           {operador}\033[0;0m')
        print(f'\033[1;30mPilha Prioridade de Operadores: {prioridade_operador}\n\033[0;0m')

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
        print(f'\033[1;35mPilha dos Operandos:            {operando}\033[0;0m')
        print(f'\033[1;93mPilha dos Operadores:           {operador}\033[0;0m')
        print(f'\033[1;30mPilha Prioridade de Operadores: {prioridade_operador}\n\033[0;0m')
        if equa[t] == 'd':
            aux = 1+flag
        elif equa[t] == 's':
            aux = 2+flag
        elif equa[t] == 'v':
            aux = 3+flag
        elif equa[t] == '^':
            aux = 4+flag

        while len(operador) != 0 and prioridade_operador[-1] > aux:
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
    print(f'\033[1;35mPilha dos Operandos:            {operando}\033[0;0m')
    print(f'\033[1;93mPilha dos Operadores:           {operador}\033[0;0m')
    print(f'\033[1;30mPilha Prioridade de Operadores: {prioridade_operador}\n\033[0;0m')
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
print(f'\033[1;35mPilha dos Operandos:            {operando}\033[0;0m')
print(f'\033[1;93mPilha dos Operadores:           {operador}\033[0;0m')
print(f'\033[1;30mPilha Prioridade de Operadores: {prioridade_operador}\n\033[0;0m')
print('\033[;1m'+'Essa expressão é: ', end='')
if operando[-1] == 'V': print('\033[1;32m'+'Verdadeira!\n'+'\033[0;0m')
elif operando[-1] == 'F': print('\033[1;31m'+'Falsa!\n'+'\033[0;0m')