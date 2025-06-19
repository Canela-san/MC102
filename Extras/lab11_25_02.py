###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Organizando a Agenda da Semana
# Nome:
# RA:
###################################################

dias = {
    "Segunda":0,
    "Terça":1,
    "Quarta":2,
    "Quinta":3,
    "Sexta":4,
    }

def main():
    agenda = [input().split() for _ in range(5)]
    n = int(input())
    for i in range(n):
        comando = input().split()
        if comando[0] == "Remover":
            D = dias[comando[1]]
            I = int(comando[2])
            F = int(comando[3])
            for j in range(F - I):
                agenda[D][I-8+j] = "Livre"
        if comando[0] == "Adicionar":
            T = comando[1]
            H = int(comando[2])
            hora_livre = Encontra_Horário_Livre(H,agenda)
            if hora_livre != 0:
                for i in range(H):
                    agenda[hora_livre[0]][hora_livre[1]+i] = T
            else:
                print(f"Não foi possível alocar a atividade {T}")
    print_agenda(agenda)

def Encontra_Horário_Livre(H, agenda):
    contador = 0
    for i in range(5):
        contador = 0
        for j,val in enumerate(agenda[i]):
            if val == "Livre":
                contador+=1
                if contador == H:
                    return(i,j-H+1)                        
            else:
                contador=0
    return 0

def print_agenda(agenda):
  print(' '.join([j.ljust(10) for j in ['Horário', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']]))
  horario = list(range(8, 19))
  for i in range(10):
    saida = [(str(horario[i]) + '-' + str(horario[i+1])).ljust(10)]
    saida = saida + [agenda[j][i].ljust(10) for j in range(5)]
    print(' '.join(saida))
    
main()


