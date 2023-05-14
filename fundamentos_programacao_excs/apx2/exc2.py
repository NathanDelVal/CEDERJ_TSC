#Nesta parte do código, abro o .txt e dou um split() para organizar as informações em uma lista, para então poder formatá-las
#e jogá-las para o arquivo .bin

with open('exc2.txt', 'rt', encoding="utf-8") as natal:
    with open('exc2.bin','wb') as natalbin:
        for x in natal:
            dados = x.strip('\n').split('#')
            natalbin.write(dados[0][:20].ljust(20, chr(0)).encode('utf-8'))
            natalbin.write(dados[1][:20].ljust(20, chr(0)).encode('utf-8'))
            natalbin.write(dados[2][:100].ljust(100, chr(0)).encode('utf-8'))

nome_lista = input('Digite o nome que deseja pesquisar na lista de natal: \n')

natalbin = open('exc2.bin', 'rb')

#usei o seek() para descobrir o comprimento do arquivo
natalbin.seek(0, 2)

tam = natalbin.tell()

natalbin.seek(0)

#a função buscardados() busca os respectivos campos do registro passado como parâmetro na chamada da função
def buscardados(nome):
    parentesco = natalbin.read(20).decode('utf-8').rstrip(chr(0))
    presente = natalbin.read(100).decode('utf-8').rstrip(chr(0)).replace(',','.').split(';')
    presente_stripped = []
    valor_total = 0
    for x in presente:
        dados = x.split('&')
        presente_stripped.append(dados)
    for y in presente_stripped:
        valor_total = valor_total + float(y[1])
    print('Para comprar os presentes para %s, que é meu/minha %s, gastarei R$%4.2f \n' % (nome, parentesco, valor_total))
    print('Os itens da lista para %s são:' % (nome))
    for item in presente_stripped:
        print(item[1])

tem_na_lista = False

#um loop em função do número de registros (ou seja, Tamanho(tam) do arquivo dividido pelo tamnho dos registros(140)
#se o nome digitado no input for igual a nome_bin, a funcão buscardados() busca o registro referenciado pelo input
for x in range(int(tam/140)):
    nome_bin = natalbin.read(20).decode('utf-8').rstrip(chr(0))
    if nome_bin == nome_lista:
        buscardados(nome_bin)
        tem_na_lista = True
        break
    else:
        natalbin.seek(120,1)

#se o nome não tiver na lista, ele imprime um erro
if tem_na_lista is False:
    print('%s não está na lista' % (nome_lista))

natalbin.close()


