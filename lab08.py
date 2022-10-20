###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Gabriel Canela
# RA: 243453
###################################################

palavra,resultado,tentativas = input(),'',6
for a in range(tentativas):
    resultado = ''
    for i,j in zip(palavra,input()):
        if i == j:  resultado += j.upper()
        elif j in palavra:  resultado += j
        else:   resultado += '_'
    print (resultado)
    if resultado.lower()==palavra:
        print("Resposta correta")
        break
    else:   [print("Palavra correta:", palavra) if a==tentativas-1 else None]