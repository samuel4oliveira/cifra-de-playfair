import funcoes

#recebendo e tratando o texto
entrada = input("Digite o endereço do arquivo de entrada: ")
texto = open(entrada, 'r').read()
texto = texto.upper()
texto = texto.replace(" ", "")
texto = texto.replace("\n", "")
texto = texto.replace("Y", "")

#recebendo e tratando a chave
chave = input("Digite a chave: ")
chave = chave.upper()
chave = chave.replace("Y", "")

#utilizando a chave do usuário para gerar a matriz
matriz = funcoes.matriz(chave)

#transformando o texto em uma lista de pares
listaDePares = funcoes.criaListaDePares(texto)

encriptar = int(input("Descriptografar - 0 || Criptografar - 1: "))
if encriptar == 1:

    #Verifica e aplica a regra de cada par
    resultado = funcoes.chamadaRegras(listaDePares, matriz, encriptar)
else:

    #Verifica e aplica a regra de cada par
    resultado = funcoes.chamadaRegras(listaDePares, matriz, encriptar)

#Criando e escrevendo o resultado da encriptação/decriptação
pathSaida = input("Digite o endereço para o arquivo de saída: ")
arquivoResultado = open(pathSaida, 'w+')
arquivoResultado.write(resultado)
arquivoResultado.close()