ano = input()
ano1 = input()
ano2 = input()

print("No ano 1 há", ano1, "flores e no ano 2,", ano2)

ano1 = float(ano1)
ano2 = float(ano2)
ano = int(ano)

anos = [ano1, ano2]

for x in range(2, ano):
    flores = 2*anos[x-1] - anos[x-2]/2
    anos.append(flores)

print("Assim, no ano ", ano, " há ", float("{:.2f}".format(anos[ano-1])), " flores.")