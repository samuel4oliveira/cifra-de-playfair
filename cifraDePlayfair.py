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


#cifrando o texto
textoCifrado = funcoes.criaListaDePares(texto)

#utilizando a chave do usuário para gerar a matriz
#chave = input("Digite a chave: ")
chave = "SAMUEL"
chave.replace("Y", "")
matriz = funcoes.matriz(chave)


for linha in matriz:
    print(linha)

resultado = funcoes.chamadaRegras(textoCifrado, matriz)
print(resultado)

# pathSaida = input("Digite o endereço do arquivo de saída: ")
# textoCriptografado = open(pathSaida, 'w+')
# textoCriptografado.write(texto + chave)
# textoCriptografado.close()