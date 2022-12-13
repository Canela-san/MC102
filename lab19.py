###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 19 - Redimensionamento de Imagens
# Nome: Gabriel Canela
# RA: 243453
###################################################

def imprimir_imagem(imagem):
    print("P2\n" + str(len(imagem[0])) +" "+ str(len(imagem)) + "\n255")
    for i in range(len(imagem)):    print(" ".join(str(int(x)) for x in imagem[i]))
def expansao(imagem_original):
    pixel = [[1 for _ in range((len(imagem_original[0])*2)-1)] for _ in range((len(imagem_original)*2)-1)]
    for i in range(1, len(imagem_original)+1):
        for j in range(1, len(imagem_original[0])+1):
            pixel[(i*2)-2][(j*2)-2] = imagem_original[i-1][j-1]
            if j != 1 and (i*10)%2 == 0:    pixel[(i*2)-2][(j*2)-3] = int((pixel[(i*2)-2][(j*2-4)] + pixel[(i*2)-2][(j*2-2)]) / 2)
            if i != 1 and (j*10)%2 == 0:    pixel[(i*2)-3][(j*2-2)] = int((pixel[(i*2)-4][(j*2-2)] + pixel[(i*2)-2][(j*2-2)]) / 2)
            if j != 1 and i != 1 and (i*10)%2 == 0 and (j*10)%2 == 0:    pixel[(i*2)-3][(j*2)-3] = int((pixel[(i*2)-2][(j*2)-2]+pixel[(i*2)-2][(j*2)-4]+pixel[(i*2)-4][(j*2)-4]+pixel[(i*2)-4][(j*2)-2])/4)
    return pixel
def retracao(imagem_original):
    pixel = [[1 for _ in range(int((len(imagem_original[0])/2)+1 if (len(imagem_original[0])/2) % int(len(imagem_original[0])/2) else len(imagem_original[0])/2))] for _ in range(int((len(imagem_original)/2)+1 if (len(imagem_original)/2) % int(len(imagem_original)/2) else len(imagem_original)/2))]
    for i in range(len(pixel)):
        for j in range(len(pixel[0])):
            pixel[i][j] = int(imagem_original[2*i][2*j] + (imagem_original[(2*i)+1][2*j] if (2*i)+1 != len(imagem_original) else 0) + (imagem_original[2*i][(2*j)+1] if (2*j)+1 != len(imagem_original[0]) else 0) + (imagem_original[(2*i)+1][(2*j)+1] if (2*j)+1 != len(imagem_original[0]) and (2*i)+1 != len(imagem_original) else 0)) / (1 + (1 if (2*j)+1 != len(imagem_original[0]) else 0) + (1 if (2*i)+1 != len(imagem_original) else 0) + (1 if (2*j)+1 != len(imagem_original[0]) and (2*i)+1 != len(imagem_original) else 0))
    return pixel
_  = input()
m, n = [int(x) for x in input().split()]
_, imagem_original = input(), []
for i in range(n):  imagem_original.append([int(x) for x in input().split()])
imprimir_imagem(expansao(imagem_original) if input() == 'expansao' else retracao(imagem_original))