###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Gabriel Canela
# RA: 243453
###################################################
P = {}
while True: 
    x = input()
    if(x!='FIM'):
        if int(x[x.index(':')+2::])>0:
            if x[:x.index(':')-1:] in list(P):  P[x[:x.index(':')-1:]] = {'E':P[x[:x.index(':')-1:]].get('E') + int(x[x.index(':')+2::]),'V':P[x[:x.index(':')-1:]].get('V'),'C':P[x[:x.index(':')-1:]].get('C')+1} 
            else:   P[x[:x.index(':')-1:]] = {'E':int(x[x.index(':')+2::]),'V':0,'C':1}
        else:
            if x[:x.index(':')-1:] not in list(P) or 0 > (P[x[:x.index(':')-1:]].get('E') + int(x[x.index(':')+2::])):  print('Quantidade indisponivel para a venda de '+str(int(x[x.index(':')+2::])*-1)+' unidade(s) do produto '+x[:x.index(':')-1:]+".")
            else:   P[x[:x.index(':')-1:]] = {'E':P[x[:x.index(':')-1:]].get('E') + int(x[x.index(':')+2::]),'V':P[x[:x.index(':')-1:]].get('V')+1,'C':P[x[:x.index(':')-1:]].get('C')}
    else:   break
for i in sorted(P): print("Produto: "+str(i)+"\nQuantidade em Estoque: "+str(P[str(i)].get('E'))+"\nPedidos de Compra: "+str(P[str(i)].get('C'))+"\nPedidos de Venda: "+str(P[str(i)].get('V')))