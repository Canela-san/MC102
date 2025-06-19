###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - A Grande Caçada aos Tesouros Perdidos
# Nome: Victor kenzo bae
# RA: 257474
###################################################


def main():
    M, N = map(int, input().split())
    matriz = []
    for _ in range(M):
        linha = input().strip().split()
        matriz.append(linha)
    P = int(input())
    print(max_tesouros(matriz, M, N, P))



def max_tesouros(mapa, M, N, P):
    if P % 2 == 1: P -= 1
    max_tesouros = 0

    prefix_sum = [[0] * (N + 1) for _ in range(M + 1)]
    for i in range(M):
        for j in range(N):
            is_tesouro = 1 if mapa[i][j] == 'X' else 0
            prefix_sum[i+1][j+1] = (
                prefix_sum[i+1][j] +
                prefix_sum[i][j+1] -
                prefix_sum[i][j] +
                is_tesouro
            )

    def contar_tesouros(r1, c1, r2, c2):
        return (
            prefix_sum[r2+1][c2+1]
            - prefix_sum[r2+1][c1]
            - prefix_sum[r1][c2+1]
            + prefix_sum[r1][c1]
        )

    for linha_inicio in range(M):
        for linha_fim in range(linha_inicio, M):
            for coluna_inicio in range(N):
                for coluna_fim in range(coluna_inicio, N):
                    altura = linha_fim - linha_inicio + 1
                    largura = coluna_fim - coluna_inicio + 1
                    perimetro = 2 * (altura + largura)
                    if perimetro <= P:
                        tesouros = contar_tesouros(linha_inicio, coluna_inicio, linha_fim, coluna_fim)
                        if tesouros > max_tesouros:
                            max_tesouros = tesouros

    return max_tesouros


main()

