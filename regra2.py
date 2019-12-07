def aplicacaoRegra2(matriz, linha1, linha2, coluna):

    linha1 = (linha1 + 1) % 5
    linha2 = (linha2 + 1) % 5 
    resultado = matriz[linha1][coluna] + matriz[linha2][coluna]
    return resultado