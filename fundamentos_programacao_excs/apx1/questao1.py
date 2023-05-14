circulo = input("Digite as coordenadas (x,y) e o raio de seu círculo \n").split()

if bool(circulo) is False:
    print("Execução encerrada")

else:
    cx = int(circulo[0])
    cy = int(circulo[1])
    raio = int(circulo[2])
    coordenadas = input("Digite as coordenadas de pontos (x,y) \n").split()

    if bool(coordenadas) is False:
        print("Execução encerrada")
    else:
        hits = 0
        matches = []
        processed = 0
        hit_tax = 0
        while bool(coordenadas) is True:
            processed = processed + 1
            px = int(coordenadas[0])
            py = int(coordenadas[1])
            if px in range(cx - raio, cx + raio + 1) and py in range(cy - raio, cy + raio + 1):
                matches.append([px, py])
                hits = hits + 1
            coordenadas = input().split()
        hit_tax = (hits/processed)*100
        for x in matches:
            print("(%d, %d) está dentro do círculo (%d, %d, %d)" % (x[0], x[1], cx, cy, raio))
        print("Quantidade de Pontos Processados: %d" % processed)
        print("Quantidade de Pontos Dentro de Círculo: %d" % hits)
        print("Percentual de Pontos Dentro: %4.1f" % hit_tax, end="%")