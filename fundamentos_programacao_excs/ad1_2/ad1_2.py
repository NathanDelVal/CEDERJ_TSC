lista = []

def doTheThing(list):
    if bool(list) is False:
        print("Execução encerrada")
    else:
        count = 0
        repetidos = []
        listareserva = list
        for x in listareserva:
            counter = listareserva.count(x)
            if counter > 1:
                repetidos.append(x)
                while x in listareserva:
                    listareserva.remove(x)
        print(repetidos)

def capturarInputs():
    numero = input("Digite um número ou aperte enter \n")
    if bool(numero) is False:
        doTheThing(lista)
    else:
        numero = int(numero)
        lista.append(numero)
        capturarInputs()

capturarInputs()
