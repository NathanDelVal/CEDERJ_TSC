import math

qtd = int(input('DIGITE O TAMANHO DA SEQUÊNCIA \n'))
elemento1 = int(input('DIGITE O PRIMEIRO ELEMENTO \n'))
elemento2 = int(input("DIGITE O SEGUNDO ELEMENTO \n"))

sequencia = [elemento1, elemento2]

pares = []

perfect_square = []

for x in range(qtd - 2):
    index = x + 2
    sequencia.append(sequencia[index - 1] + sequencia[index - 2])

for y in sequencia:
    if y%2 == 0:
        pares.append(y)
    if y > 1:
        sqrt = math.sqrt(y)
        perfect_sqrt = sqrt / math.floor(sqrt)
        if perfect_sqrt == 1:
            perfect_square.append(y)



print('Os %d elementos da sequência são:' % (qtd), end=" ")
print('[%s]' % ', '.join(map(str, sequencia)))

if pares:
    print('Os elementos pares da sequência são: ', end=" ")
    print('[%s]' % ', '.join(map(str, pares)))
else:
    print('Não há elementos pares na sequência até a posição %d.' % (qtd))

if perfect_square:
    print('Dentre esses, os que são quadrado perfeito são: ', end=" ")
    print('[%s]' % ', '.join(map(str, perfect_square)))
else:
    print('Não há elemento par quadrado perfeito')