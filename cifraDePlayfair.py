import funcoes

#recebendo e tratando o texto
#pathEntrada = input("Digite o endereço do arquivo de entrada: ")
texto = open("entrada.txt", 'r').read()
texto = texto.upper()
texto = texto.replace(" ", "")
texto = texto.replace("\n", "")
texto = texto.replace(":", "")
texto = texto.replace(".", "")
texto = texto.replace(")", "")
texto = texto.replace("Y", "")

#chave = input("Digite a chave: ")
chave = "SAMUEL"
chave.replace("Y", "")

escolha = int(input("Criptografar: 1 ou Descriptografar: 2 "))

if escolha == 1:
    
    #utilizando a chave do usuário para gerar a matriz
    matriz = funcoes.matriz(chave)

    #transformando o texto em lista de pares
    textoCifrado = funcoes.criaListaDePares(texto)

    resultado = funcoes.chamadaRegras(textoCifrado, matriz)
    print(resultado)

    # pathSaida = input("Digite o endereço do arquivo de saída: ")
    # textoCriptografado = open(pathSaida, 'w+')
    # textoCriptografado.write(texto + chave)
    # textoCriptografado.close()
else:

    pass