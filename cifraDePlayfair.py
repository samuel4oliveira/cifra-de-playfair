import matriz
import criarListaDePares
import posicao
import regra1
import regra2

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
textoCifrado = criarListaDePares.criaListaDePares(texto)
print(textoCifrado)

#utilizando a chave do usuário para gerar a matriz
#chave = input("Digite a chave: ")
chave = "SAMUEL"
chave.replace("Y", "")
matriz = matriz.matriz(chave)
for linha in matriz:
    print(linha)

resultado = ''
print(textoCifrado)
for i in range(len(textoCifrado)):
        linha1, coluna1 = posicao.posicao(textoCifrado[i][0], matriz)
        linha2, coluna2 = posicao.posicao(textoCifrado[i][1], matriz)
        
        if linha1 == linha2:
            resultado += regra1.aplicacaoRegra1(matriz[linha1], coluna1, coluna2)
        elif coluna1 == coluna2:
            resultado += regra2.aplicacaoRegra2(matriz, linha1, linha2, coluna1)
        else:
            coluna1, coluna2 = coluna2, coluna1
            resultado += matriz[linha1][coluna1]
            resultado += matriz[linha2][coluna2]

print(resultado)

# pathSaida = input("Digite o endereço do arquivo de saída: ")
# textoCriptografado = open(pathSaida, 'w+')
# textoCriptografado.write(texto + chave)
# textoCriptografado.close()