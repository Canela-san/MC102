##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Gabriel Canela
# RA: 243453
##################################################
torre,x = [int(panqueca) for panqueca in input().split()],1
torre_sort = torre.copy()
torre_sort.sort()
while(x!=0):
    torre[:x] = torre[x-1::-1]
    x = int(input())
[print('Torre estavel') if torre == torre_sort else print ('Torre instavel')]