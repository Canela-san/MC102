#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Gabriel Canela
# RA: 243453
#####################################################
score,matriz,team,quant = {'azul':0,'vermelho':0},[input().split() for _ in range(int(input()))],input(),int(input())
for x in range(quant):
    position = [0,0]
    for y in input():
        if y=='N': position = [position[0]-1,position[1]]
        if y=='S': position = [position[0]+1,position[1]]
        if y=='L': position = [position[0],position[1]+1]
        if y=='O': position = [position[0],position[1]-1]
        if matriz[position[0]][position[1]] == '*':
            matriz[position[0]][position[1]] = '.'
            if team == 'azul': score = {'azul':score.get('azul')+1,'vermelho':score.get('vermelho')} if x%2 == 0 else {'azul':score.get('azul'),'vermelho':score.get('vermelho')+1}
            else: score = {'azul':score.get('azul'),'vermelho':score.get('vermelho')+1} if x%2 == 0 else {'azul':score.get('azul')+1,'vermelho':score.get('vermelho')}
print ('Tesouros encontrados pelo time azul: '+str(score.get('azul'))+'\nTesouros encontrados pelo time vermelho: '+str(score.get('vermelho')))
[print('Vitoria do time azul') if score.get('azul')>score.get('vermelho') else [print('Vitoria do time vermelho') if score.get('azul')<score.get('vermelho') else print ('Empate')]]