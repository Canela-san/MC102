#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Caminho Binário Alternado
# Nome: Gabriel Canela
# RA: 243453 
#####################################################
import random as rand
result, L = False,int(input())
tabuleiro = [input().split() for _ in range(L)]
l1, c1, l2, c2 = [int(i) for i in input().split()]
for i in range(900000):
  if l1 == l2 and c1 == c2:  result = True
  aleatorio = rand.randint(0,3) 
  if aleatorio == 0:
    if len(tabuleiro[0]) - 1 != c1:
      if tabuleiro[l1][c1] != tabuleiro[l1][c1 + 1]: c1 += 1
  if aleatorio == 1:
    if l1 + 1 != L: 
      if tabuleiro[l1][c1] != tabuleiro[l1 + 1][c1]: l1 += 1
  if aleatorio == 2:
    if c1 != 0: 
      if tabuleiro[l1][c1] != tabuleiro[l1][c1 - 1]: c1 -= 1
  if aleatorio == 3:
    if l1 != 0: 
      if tabuleiro[l1][c1] != tabuleiro[l1 - 1][c1]: l1 -= 1
  if result: break
[print('caminho encontrado') if result else print('caminho nao encontrado')]