###################################################
# MC102 - Algoritmos e Programação de Computadores 
# Laboratório 2 - Rumo a Marte 
# Nome: Gabriel Canela
# RA: 243453 ################################################### 
D1, V1, T, D2, V2 = int(input()),int(input()),int(input()),int(input()),int(input())
[print("True") if (((D1 / V1) / 24) - T) < ((D2 / V2) / 24) else print("False")]