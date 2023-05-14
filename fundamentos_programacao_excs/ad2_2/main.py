import struct

Registro = struct.Struct("20s 50s 50s 100s")

nomearq = input("digite o nome do arquivo que deseja carregar \n")

urltxt = nomearq + ".txt"

urlbin = urltxt.split('.')[1] + ".bin"

with open(urltxt, 'rt', encoding="utf-8") as arqtxt:
    with open(urlbin, 'w+b') as arqbin:
        for line in arqtxt:
            line = line.split('#')
            line[3] = line[3].strip('\n')
            bloco = Registro.pack(line[0].encode('utf-8'), line[1].encode('utf-8'), line[2].encode('utf-8'), line[3].encode('utf-8'))
            arqbin.write(bloco)

        bloco = arqbin.read(20)
        campos = Registro.unpack(bloco)
        print(campos[0].decode('utf-8'))




