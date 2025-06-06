###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados Mágicos em uma Matriz
# Nome:
# RA:
###################################################


# Leitura de dados
m = int(input())
agenda = [[0 for _ in range(m)] for _ in range(m)]
for i in range(m):
    temp = input()
    agenda[i] = [int(x) for x in temp.split()]

# Processamento de dados
def verifica_3x3(agenda):
    sum,temp,temp2,diag1,diag2 = 0, 0, 0, 0, 0
    for i in range(3):
        sum += agenda[0][i]
        diag1 += agenda[i][i]
        diag2 += agenda[i][2-i]
    if not (sum == diag1 == diag2):
        return 0
    else:
        for i in range(3):
            temp = 0
            for j in range(3):
                temp += agenda[i][j]
                temp2 += agenda[j][i]
            if temp != sum:
                return 0
    return 1

def gerar_subagenda_3x3(agenda):
    m = len(agenda)
    subagenda = []
    for i in range(m - 2):
        for j in range(m - 2):
            subagenda.append([ [agenda[i + x][j + y] for y in range(3)] for x in range(3) ])
    return subagenda


# Saída de dados
subagenda = gerar_subagenda_3x3(agenda)
resposta = 0
for i in range((m-2)**2):
    resposta += verifica_3x3(subagenda[i])
print(f"Número de quadrados mágicos: {resposta}")

