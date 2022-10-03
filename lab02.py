###################################################
# MC102 - Algoritmos e Programação de Computadores 
# Laboratório 2 - Rumo a Marte 
# Nome: Gabriel Canela
# RA: 243453 ################################################### 
D1 = int(input())
V1 = int(input())
T = int(input())
D2 = int(input())
V2 = int(input())
T1 = ((D1 / V1) / 24) - T
T2 = (D2 / V2) / 24
if (T1 < T2):
    print("True")
else:
    print("False")
