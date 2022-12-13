###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Caça-Palavras
# Nome: Gabriel Canela
# RA: 243453
###################################################
x, tabuleiro, palavras = 0, [], []
while True:
    x = input()
    if x == '0':
        break
    tabuleiro.append(x)
x = 0 
while True:
    x = input()
    if x == '0':
        break
    palavras.append(x)

# def verifica (tabuleiro, palavra)

def achar(tabuleiro, x, y, palavra):
    for i in tabuleiro[y]
        return [tabuleiro[y].find(palavra[1]), y]
    for t in tabuleiro:

for p in palavras:
    for y in range(len(tabuleiro)):
        x = t[y].find(p[0])
        if x != -1:
            achar(tabuleiro, x, y, palavra)
