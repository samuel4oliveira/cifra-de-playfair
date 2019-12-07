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