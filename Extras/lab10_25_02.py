###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados Mágicos em uma Matriz
# Nome:
# RA:
###################################################


# Leitura de dados
m = int(input())
matrix = [[0 for _ in range(m)] for _ in range(m)]
for i in range(m):
    temp = input()
    for j in range(m):
        matrix[i][j] = (int(temp[2*j]))


# Processamento de dados
def verifica_3x3(matrix):
    sum,temp,temp2,diag1,diag2 = 0, 0, 0, 0, 0
    for i in range(3):
        sum += matrix[0][i]
        diag1 += matrix[i][i]
        diag2 += matrix[i][2-i]
    if not (sum == diag1 == diag2):
        return 0
    else:
        for i in range(3):
            temp = 0
            for j in range(3):
                temp += matrix[i][j]
                temp2 += matrix[j][i]
            if temp != sum:
                return 0
    return 1

def gerar_submatrix_3x3(matrix):
    m = len(matrix)
    submatrix = []
    for i in range(m - 2):
        for j in range(m - 2):
            submatrix.append([ [matrix[i + x][j + y] for y in range(3)] for x in range(3) ])
    return submatrix


# Saída de dados
submatrix = gerar_submatrix_3x3(matrix)
resposta = 0
for i in range((m-2)**2):
    resposta += verifica_3x3(submatrix[i])
print(f"Número de quadrados mágicos: {resposta}")

