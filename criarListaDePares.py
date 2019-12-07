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