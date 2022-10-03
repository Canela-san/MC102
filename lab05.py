##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Gabriel Canela
# RA: 243453
##################################################
V,D,hi,hf,horas_trabalhadas,horas_extras = 0,0,0,0,0,0
V,D = int(input()),int(input())
for day in range(1,D+1):
    week_hour = 0
    for period in range(1,int(input())+1):
        hi,hf = int(input()),int(input())
        week_hour += hf - hi
    if week_hour > 8:
        horas_extras += week_hour-8
    horas_trabalhadas += week_hour
if ((horas_trabalhadas-horas_extras)>44):
    horas_extras += horas_trabalhadas - horas_extras - 44
valor = (horas_trabalhadas * V) + (horas_extras * 0.5 * V)
print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))