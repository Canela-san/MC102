###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Gabriel Canela
# RA: 243453
###################################################

# leitura de dados
day = int(input())
hour = int(input())
min = int(input())
student = input()
methonhunuybunihod = input()

# valor do ingresso inteiro
#Bora por função porque acho que o aprendizado é maior (>*-*)>
def Valor(d, h, min, stu, met):
    result = 0
    if h >= 19:
        temp = 1
    elif h==18 and min >= 30:
        temp = 1
    else:
        temp = 0
    if d in [1, 7]:
        if temp and day==7:
            result = 40
        else:
            result = 30 
    if d in [2, 3, 4]:
        if temp:
            if d in [2, 3]:
                result = 20
            else:
                result = 30
        else:
            result = 15
    if d in [5, 6]:
        if temp:
            if d == 5:
                result = 30
            else:
                result = 40
        else:
            result = 20
    if stu == 'N':
        if met == 'C':
            if d in [2, 3, 4, 5]:
                result *= 0.5
            if d == 1:
                result *= 0.7
            if d == 7:
                result *= 0.8
            if d == 6:
                if temp:
                    result *= 0.7
    else:
        result *= 0.5
    return result

# valor a pagar
ingresso = Valor(day, hour, min, student, methonhunuybunihod)

# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))