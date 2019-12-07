def posicao(letra, matriz):

    for i in range(5):
        for j in range(5):
            if letra == matriz[i][j]:
                return i, j