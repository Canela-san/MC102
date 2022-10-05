###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome:
# RA:
###################################################
defense,attack,v,d,e,result = [],[],0,0,0,0
for n in range(int(input())):
    defense.append(int(input()))
for n in range(int(input())):
    attack.append(int(input()))
for n in range(len(defense)-len(attack)):
    v,d,e = 0,0,0
    for m in range(len(attack)):
        if defense[n+m] < attack[m]:
            v+=1
        elif defense[n+m] > attack[m]:
            d+=1
        elif defense[n+m] == attack[m]:
            e+=1
    if ((v>d)or(v==d and e>0)):
        result = n+1
        break    
[print('Derrota') if result == 0 else print('Vitória posicionando as tropas a partir da posição', result)]