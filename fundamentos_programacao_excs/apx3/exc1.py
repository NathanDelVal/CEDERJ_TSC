import struct

apostas = open('apostas.txt', 'r')


entrada = input('Digite os números de sua aposta \n').split(' ')

hits = 0
hits6 = 0
hits5 = 0
hits4 = 0
hits3 = 0

print('CONTEÚDO DO ARQUIVO "APOSTAS.TXT" \n')
for x in apostas:
    print(x)
    linha = x.strip('\n').split(' ')
    for y in linha:
        if y in entrada:
            hits = hits + 1
    if hits == 6:
        hits6 = hits6 + 1
    elif hits == 5:
        hits5 = hits5 + 1
    elif hits == 4:
        hits4 = hits4 + 1
    elif hits == 3:
        hits3 == hits3 + 1
    hits = 0

print('Quantidade de apostas premiadas:')
print('    Com 6 acertos tivemos: %d aposta(s)' % (hits6))
print('    Com 5 acertos tivemos: %d aposta(s)' % (hits5))
print('    Com 4 acertos tivemos: %d aposta(s)' % (hits4))
print('    Com 3 acertos tivemos: %d aposta(s)' % (hits3))

apostas.close()






