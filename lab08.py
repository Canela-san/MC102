###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: 
# RA: 
###################################################

palavra = input()
for a in range(2):
    resultado = ''
    for i,j in zip(palavra,input()):
        if (i==j):
            resultado += i.upper()
        else:
            resultado += '_'
    print(resultado)
# ...
print("Resposta correta")
# ...
print("Palavra correta:", palavra)