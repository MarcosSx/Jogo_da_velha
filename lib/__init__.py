def cria_novo_jogo():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def escolhe_jogador(msg, jogador2='x'):
    while True:
        jogador = str(input(msg)).upper().strip()[0]
        if jogador.isalpha() and jogador not in jogador2:
            break
        cabeçalho('Escolha outro caractere valido!')
    return jogador


def atualiza_jogo(game):
    # print()
    for lin in range(0, 3):
        for col in range(0, 3):
            print(f'\033[1;95m {game[lin][col]} ', end='')
            print('|' if col != 2 else '', end='')
        print()
        print('¨' * 11 if lin != 2 else '\033[m')


def preencher_posicao(pos, game, jogador):
    while pos > 9 or pos <= 0:
        cabeçalho(f'Indice {pos} fora de alcance')
        pos = leiaInt('Digite uma posição valida: ')
        print()
    ok = False
    cont = 0
    cabeçalho(f'O jogador {jogador} jogou na posição {pos}')
    while True:
        if ok:
            break
        for l in range(0, 3):
            try:
                c = game[l].index(str(pos))
                game[l][c] = jogador
                ok = True
            except:
                cont += 1
                if cont == 3:
                    pos = leiaInt('\033[31mPosição ja preencida\033[m\n\033[33mEscolha outra posição: \033[m')
                    cabeçalho(f'O jogador {jogador} jogou na posição {pos}')
                    cont = 0
                    break


def jogador_ganhou(game, jogador):
    # Verifica se a horizontal está igual
    for l in range(0, 3):
        cont_h = 0
        for c in range(0, 3):
            if game[l][c] == jogador:
                cont_h += 1
            if cont_h == 3:
                return True

    # Verifica se a diagonal principal esta igual
    c = cont_d1 = 0
    for l in range(0, 3):
        if game[l][c] == jogador:
            cont_d1 += 1
            if cont_d1 == 3:
                return True
        c += 1

    # Verifica se a diagonal secundaria esta igual
    c = 2
    cont_d2 = 0
    for l in range(0, 3):
        if game[l][c] == jogador:
            cont_d2 += 1
            if cont_d2 == 3:
                return True
        c -= 1

    # Verifica se a vertical esta igual
    for c in range(0, 3):
        cont_v = 0
        for l in range(0, 3):
            if game[l][c] == jogador:
                cont_v += 1
            if cont_v == 3:
                return True


def linha(tam=42):
   return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor