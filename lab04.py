###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Gabriel Canela
# RA: 243453
###################################################
x,z,y,i = 1,0,0,[]
while (x!=0):
    x = int(input())
    if (x!=0):
        y+=x
        if (y<0):
            i.append('Quantidade indisponível para a venda de ' + str(-x) + ' unidades.')
            y-=x
        elif (x<0): 
            z+=1
for j in i:
    print(j)
print("Quantidade de vendas realizadas: " + str(z))
print("Quantidade em estoque: " + str(y))