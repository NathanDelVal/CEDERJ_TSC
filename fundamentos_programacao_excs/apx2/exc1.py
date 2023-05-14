target_file = input("Digite o nome do arquivo .txt que deseja ordenar: \n")

arquivo = open(target_file + '.txt', 'r')

matriz = []

matriz_soma = []

#lê o arquivo .txt e armazena seus valores na variável matriz[] como inteiros
print('CONTEÚDO DA MATRIZ LIDA ANTES DA ORDENAÇÃO: \n')
for linha in arquivo:
    print(linha)
    dados = linha.strip('\n').split(' ')
    temp_matriz = []
    for x in dados:
        if x:
            temp_matriz.append(int(x))
    matriz.append(temp_matriz)

#itera sob cada linha da matriz e armazena o valor de sua respectiva soma em matriz_soma
for linha in matriz:
    soma = 0
    for dados in range(len(linha)):
        soma = soma + linha[dados]
        if dados == len(linha) - 1:
            matriz_soma.append(soma)

maior_soma = matriz_soma[0]

#loop básico para descobrir qual é a maior soma
for soma in matriz_soma:
    if soma > maior_soma:
        maior_soma = soma

""""" maior_soma_matriz = matriz[matriz_soma.index(maior_soma)]

y = len(maior_soma_matriz) - 1

for x in maior_soma_matriz:
    if x > maior_soma_matriz[y]:
        temp = x
        x = maior_soma_matriz[y]
        maior_soma_matriz[y] = x
    y = y - 1
"""""

#busco a referência da linha com maior soma através do método nativo index()
matriz[matriz_soma.index(maior_soma)] = sorted(matriz[matriz_soma.index(maior_soma)])


arquivo.close()

arquivo = open('exc1.txt', 'w')

for x in matriz:
    for y in x:
        arquivo.write(str(y) + " ")
    arquivo.write('\n')

arquivo.close()

arquivo = open('exc1.txt', 'r')

print('CONTEÚDO DA MATRIZ LIDA DEPOIS DA ORDENAÇÃO: \n')

for x in arquivo:
    print(x)

arquivo.close()