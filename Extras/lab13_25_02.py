###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Agência de Marketing
# Nome: Victor kenzo bae
# RA: 257474
###################################################

def estrategia_ingenua(influenciadores, custo_maximo):
    custo_total = 0.0
    seguidores_alcancados = set()
    influenciadores_disponiveis = influenciadores[:]
    
    while True:
        influenciadores_disponiveis.sort(key=lambda x: (x['custo'], -len(x['seguidores'])))
        
        contratado_nesta_rodada = False
        for i, influenciador in enumerate(influenciadores_disponiveis):
            if custo_total + influenciador['custo'] <= custo_maximo:
                custo_total += influenciador['custo']
                seguidores_alcancados.update(influenciador['seguidores'])
                influenciadores_disponiveis.pop(i)
                contratado_nesta_rodada = True
                break
        
        if not contratado_nesta_rodada:
            break
            
    return custo_total, len(seguidores_alcancados)


def estrategia_atual(influenciadores, custo_maximo):
    custo_total = 0.0
    seguidores_alcancados = set()
    influenciadores_disponiveis = influenciadores[:]

    while True:
        influenciadores_disponiveis.sort(key=lambda x: (x['custo'] / len(x['seguidores']), -len(x['seguidores'])))
        
        contratado_nesta_rodada = False
        for i, influenciador in enumerate(influenciadores_disponiveis):
            if custo_total + influenciador['custo'] <= custo_maximo:
                custo_total += influenciador['custo']
                seguidores_alcancados.update(influenciador['seguidores'])
                influenciadores_disponiveis.pop(i)
                contratado_nesta_rodada = True
                break
        
        if not contratado_nesta_rodada:
            break
            
    return custo_total, len(seguidores_alcancados)


def estrategia_nova(influenciadores, custo_maximo):
    custo_total = 0.0
    seguidores_alcancados = set()
    influenciadores_disponiveis = influenciadores[:]

    while True:
        candidatos = []
        for i, influenciador in enumerate(influenciadores_disponiveis):
            seguidores_novos = set(influenciador['seguidores']) - seguidores_alcancados
            
            if len(seguidores_novos) > 0:
                custo_beneficio_residual = influenciador['custo'] / len(seguidores_novos)
                candidatos.append((custo_beneficio_residual, influenciador, i))

        if not candidatos:
            break

        candidatos.sort(key=lambda x: (x[0], -len(x[1]['seguidores'])))

        contratado_nesta_rodada = False
        for _, influenciador, index_original in candidatos:
            if custo_total + influenciador['custo'] <= custo_maximo:
                custo_total += influenciador['custo']
                seguidores_alcancados.update(influenciador['seguidores'])

                for i, item in enumerate(influenciadores_disponiveis):
                    if item == influenciador:
                        influenciadores_disponiveis.pop(i)
                        break

                contratado_nesta_rodada = True
                break
        
        if not contratado_nesta_rodada:
            break

    return custo_total, len(seguidores_alcancados)

custo_maximo = float(input().strip())
num_influenciadores = int(input().strip())
influenciadores = []
for _ in range(num_influenciadores):
        linha = input().strip().split(',')
        custo = float(linha[0])
        seguidores = list(map(int, linha[1:]))
        influenciadores.append({"custo": custo, "seguidores": seguidores})

custo_ingenua, alcance_ingenua = estrategia_ingenua(influenciadores[:], custo_maximo)

custo_atual, alcance_atual = estrategia_atual(influenciadores[:], custo_maximo)

custo_nova, alcance_nova = estrategia_nova(influenciadores[:], custo_maximo)
   
print(f"Estratégia Ingênua: {custo_ingenua:.1f}, {alcance_ingenua}")
print(f"Estratégia Atual: {custo_atual:.1f}, {alcance_atual}")  
print(f"Estratégia Nova: {custo_nova:.1f}, {alcance_nova}")