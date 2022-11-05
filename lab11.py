#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome:
# RA:
#####################################################


'''
Dica: A criação das seguintes funções pode facilitar o desenvolvimento
do laboratório:
1) Uma função para rotacionar a peça em 90 graus para direita.
2) Uma função para verificar se é possível encaixar a peça a partir de
uma determinada linha e coluna do tabuleiro.
'''

# Leitura do tabuleiro
tabuleiro, peca = [],[]
for _ in range(int(input())):   tabuleiro.append(input().split())
for _ in range(int(input())):   peca.append(input().split())

print (tabuleiro)
print (peca)
