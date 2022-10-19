###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: 
# RA: 
###################################################

palavra,temp,resultado = input(),'',''
for a in range(2):
    resultado = ''
    print(len(palavra))
    for i,j,k in zip(palavra,input(),temp):
        if i==j or i==k:
            resultado += i.upper()
        else:
            resultado += '_'
    temp = resultado
    print(resultado)
# ...
print("Resposta correta")
# ...
print("Palavra correta:", palavra)