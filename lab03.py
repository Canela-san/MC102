###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Gabriel Canela
# RA: 243453
###################################################

# leitura de dados
day, hour, minutes, student, method = int(input()),int(input()),int(input()),input(),input()
def Valor(d, h, minutes, stu, met):
    result = 0
    if h >= 19: temp = 1
    elif h==18 and minutes >= 30:   temp = 1
    else:   temp = 0
    if d in [1, 7]:
        if temp and day==7: result = 40
        else:   result = 30 
    if d in [2, 3, 4]:
        if temp:
            if d in [2, 3]: result = 20
            else:   result = 30
        else:   result = 15
    if d in [5, 6]:
        if temp:
            if d == 5:  result = 30
            else:   result = 40
        else:   result = 20
    if stu == 'N':
        if met == 'C':
            if d in [2, 3, 4, 5]:   result *= 0.5
            if d == 1:  result *= 0.7
            if d == 7:  result *= 0.8
            if d == 6:
                if temp:    result *= 0.7
    else:   result *= 0.5
    return result
ingresso = Valor(day, hour, minutes, student, method)
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))