import random
import time

from dados import dicionario

forca = []

for _ in range(8):
    forca.append(list('' for _ in range(11)))

forca[0][1] = '_'
forca[0][2] = '_'
forca[0][3] = '_'
forca[0][4] = '_'
forca[0][5] = '_'
forca[0][6] = '_'
forca[0][7] = '_'
forca[0][8] = '_'
forca[0][9] = '_'

forca[1][1] = '|'
forca[1][2] = '/'
forca[1][9] = '|'

forca[2][1] = '|'

forca[3][1] = '|'

forca[4][1] = '|'

forca[5][1] = '|'

forca[6][1] = '|'

forca[7][0] = '_'
forca[7][2] = '_'

letreiro = [['-----------------'],
            ['| JOGO DA FORCA |'], ['-----------------']]

counter = 0


def print_matrix(arr):
    print('\n')
    for y in arr:
        for x in y:
            if x == '':
                print(' ', end=" ")
            else:
                print('{}'.format(x), end=" ")
        print('\n')


def print_list(arr, sep=' '):
    for x in arr:
        if x == '':
            print(' ', end=" ")
        else:
            print('{}'.format(x), end=" ")


while counter < 6:
    if counter == 0:
        theme = random.choice(list(dicionario.keys()))

        palavra = random.choice(list(dicionario[theme].keys()))

        dica = dicionario[theme][palavra]

        letras_erradas = []

        forca_copy = list(forca)

        palavra_split = []

        for _ in palavra:
            if _ == ' ':
                palavra_split.append('')
            else:
                palavra_split.append(_)

        palavra_hidden = []

        for _ in palavra:
            if _ == ' ':
                palavra_hidden.append('')
            else:
                palavra_hidden.append('_')

        counter = counter + 1
        print_matrix(letreiro)

    time.sleep(1)
    print_matrix(forca_copy)

    if counter == 5:
        print(' -----GAME OVER-----')
        replay = input('Deseja jogar novamente? (sim/não) ')
        if replay == 'sim':
            forca_copy[2][9] = ''
            forca_copy[3][9] = ''
            forca_copy[4][9] = ''
            forca_copy[4][8] = ''
            forca_copy[4][10] = ''
            forca_copy[5][9] = ''
            forca_copy[6][8] = ''
            forca_copy[6][10] = ''
            counter = 0
            continue
        else:
            break
            

    print(f'TEMA: {theme}')
    print_list(palavra_hidden)
    print('  | Letras não encontradas:', end=" ")
    print_list(letras_erradas, ',')
    if counter > 1:
        print(f'  | Dica: {dica}')
    print('\n')
    letra = input('Digite uma letra: ').lower()

    if letra in palavra_split:
        for _ in range(len(palavra_split)):
            if palavra_split[_] == letra:
                palavra_hidden[_] = palavra_split[_]
        print('\n')
        print_list(palavra_hidden)
        if '_' not in palavra_hidden:
            print('\n')
            print('!!! PARABÉNS, VOCÊ GANHOU !!!')
            counter = 5
    else:
        print(f'Letra "{letra}" não encontrada\n')
        letras_erradas.append(letra)
        if counter == 1:
            forca_copy[2][9] = 'O'
        if counter == 2:
            forca_copy[3][9] = '^'
            forca_copy[4][9] = '|'
        if counter == 3:
            forca_copy[4][8] = '/'
            forca_copy[4][10] = '\\'
        if counter == 4:
            forca_copy[5][9] = '^'
            forca_copy[6][8] = '/'
            forca_copy[6][10] = '\\'
            print('!!! VOCÊ PERDEU !!!')
        counter = counter + 1
