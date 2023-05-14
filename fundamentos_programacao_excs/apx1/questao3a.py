ano = input()
ano1 = input()
ano2 = input()

print("No ano 1 há", ano1, "flores e no ano 2,", ano2)

ano1 = float(ano1)
ano2 = float(ano2)
ano = int(ano)

#anos = [ano1, ano2]


def calcularflores(x, y, z):
    thisyear = 2*y - x/2
    if z > 3:
        z = z -1
        return calcularflores(y, thisyear, z)
    else:
        return float("{:.2f}".format(thisyear))


flores = calcularflores(ano1,ano2,ano)

print("Assim, no ano ", ano, " há ", flores, " flores.")