###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Gabriel Canela
# RA: 243453
###################################################
x = {'0': -1, 'Branco': 0, 'Nulo': 0}
while (x['0'] != 0):
    temp = input()
    try: x[temp] += 1
    except: x[temp] = 1
x.pop('0')
for i in sorted(x.items(),key=lambda item: item[1], reverse=True):  
    if not (i[0] == 'Nulo' or i[0] == 'Branco'): print(i[0], i[1])
if x['Branco']: print('Brancos',x['Branco'])
if x['Nulo']: print('Nulos', x['Nulo'])
