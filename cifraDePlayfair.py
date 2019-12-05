import matriz

pathEntrada = input("Digite o endereço do arquivo de entrada: ")
texto = open(pathEntrada, 'r').read()

chave = input("Digite a chave: ")

matriz = matriz.matriz(chave)


pathSaida = input("Digite o endereço do arquivo de saída: ")
textoCriptografado = open(pathSaida, 'w+')
textoCriptografado.write(texto + chave)
textoCriptografado.close()