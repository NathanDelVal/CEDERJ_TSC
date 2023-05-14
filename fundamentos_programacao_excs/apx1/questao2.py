def checkLine(x):
    if x.isdigit() is False:
        return checkLine(input("Você não digitou um número. Digite um número maior que 0 \n"))
    elif int(x) <= 0:
        return checkLine(input("Você digitou um número menor ou igual a 0. Digite um número maior que 0 \n"))
    return x

linhas = int(checkLine(input("Digite um número maior que zero para começar \n")))

palavras = []

ocorrencias = {}

print("Digite seu texto")

for x in range(0, linhas):
    line = input().split()
    while x == 0 and bool(line) is False:
        line = input("Você não digitou nenhuma palavra para ser lida. Digite uma palavra \n").split()
    for x in line:
        palavras.append(x)

for x in palavras:
    ocorrencias[x] = palavras.count(x)

maisRepetidas = []

ocorrenciasList = []

max = 0

for x in ocorrencias.items():
    ocorrenciasList.append(x)

for x in range(len(ocorrenciasList)):
    if x == 0:
        max = ocorrenciasList[0][1]
    else:
        if ocorrenciasList[x][1] >= max:
            max = ocorrenciasList[x][1]

for x in range(len(ocorrenciasList)):
    if max == ocorrenciasList[x][1]:
        maisRepetidas.append(ocorrenciasList[x])


for x in maisRepetidas:
    print(x[0].upper())

print("Ocorreu(ram) %d vez(es)" % max)

