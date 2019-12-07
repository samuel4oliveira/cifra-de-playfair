def aplicacaoRegra1(linha, coluna1, coluna2):

    coluna1 = (coluna1 + 1) % 5
    coluna2 = (coluna2 + 1) % 5 
    resultado = linha[coluna1] + linha[coluna2]
    return resultado