def criaListaDePares(texto):
    
    textoAux = ''
    for i in range(len(texto)):
        try:  
            if texto[i] == texto[i+1]:
                textoAux += texto[i]+'X'
            else:
                textoAux += texto[i]
        except:
            textoAux += texto[i]
    if len(textoAux) % 2 != 0:
        textoAux += 'X'
    
    #separando texto em pares
    textoCifrado = []
    for i in range(0, len(textoAux), 2):
    
        aux = textoAux[i] + textoAux[i+1] 
        textoCifrado.append(aux)         
    return textoCifrado


import string
def matriz(chave):

    #recebendo alfabeto
    alfabeto = list(string.ascii_uppercase)
    alfabeto.remove('Y')

    #inserindo chave no alfabeto
    for i in range(len(chave)-1, -1, -1):
        alfabeto.remove(chave[i])
        alfabeto.insert(0, chave[i])

    #transformando alfabeto em matriz
    linha = []
    matriz = []
    for i in range(len(alfabeto)):
        
        linha.append(alfabeto[i])
        if i == 4 or i == 9 or i == 14 or i == 19 or i == 24:
            matriz.append(linha)
            linha = []
            pass

    return matriz

def posicao(letra, matriz):

    for i in range(5):
        for j in range(5):
            if letra == matriz[i][j]:
                return i, j

def aplicacaoRegra1(linha, coluna1, coluna2):

    coluna1 = (coluna1 + 1) % 5
    coluna2 = (coluna2 + 1) % 5 
    resultado = linha[coluna1] + linha[coluna2]
    return resultado

def aplicacaoRegra2(matriz, linha1, linha2, coluna):

    linha1 = (linha1 + 1) % 5
    linha2 = (linha2 + 1) % 5 
    resultado = matriz[linha1][coluna] + matriz[linha2][coluna]
    return resultado

