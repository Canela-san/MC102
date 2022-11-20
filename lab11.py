#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Gabriel Canela
# RA: 243453
#####################################################
def rotacionar(x):
    temp = [[None for _ in range(len(x))] for _ in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            temp[j][len(temp[0])-1-i] = x[i][j]
    return temp
tabuleiro, peca, temp, quant, result = [],[],0,0,''
for _ in range(int(input())):   tabuleiro.append(input().split())
for _ in range(int(input())):   peca.append(input().split())
for a in range (4):
    quant = 0
    for o in range(len(tabuleiro)-len(peca)+1):
        for i in range(len(tabuleiro[0])-len(peca[0])+1):
            temp = 0
            for j in range(len(peca)):
                for k in range(len(peca[0])):
                    if (peca[j][k] == 'X' and tabuleiro[j+o][k+i] == 'X'):  temp += 1
            if (temp == 0): quant += 1
    result += str('' if result == "" else ',')+str(quant)
    peca = rotacionar(peca)
print (result)