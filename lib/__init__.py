from random import randint

c = (
    '\033[m',       # Limpa
    '\033[0;30m',   # Preto
    '\033[0;31m',   # Vermelho
    '\033[0;32m',   # Verde
    '\033[0;33m',   # Amarelo
    '\033[0;34m',   # Azul
    '\033[0;35m',   # Magenta
    '\033[0;36m',   # Ciano
    '\033[1;96m',   # Ciano claro
    '\033[1;95m',   # Pink
    '\033[;7m'      # Inverte
    )


def cria_novo_jogo():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def escolhe_jogador(msg, jogador2='x'):
    while True:
        jogador = str(input(c[3] + msg + c[0])).upper().strip()[0]
        if jogador.isalpha() and jogador not in jogador2:
            break
        cabeçalho('Escolha outro caractere valido!')
    cor = randint(1, 6)
    return c[cor] + jogador + c[0]


def atualiza_jogo(game):
    # print()
    for lin in range(0, 3):
        for col in range(0, 3):
            print(f' {c[9] + game[lin][col] + c[0]} ', end='')
            print(f'{c[8]}|' if col != 2 else '', end='')
        print()
        print(f'{c[8]}¨' * 11 if lin != 2 else f'{c[0]}')


def preencher_posicao(pos, game, jogador):
    while pos > 9 or pos <= 0:
        cabeçalho(f'Indice {pos} fora de alcance')
        pos = leiaInt('Digite uma posição valida: ')
        print()
    ok = False
    cont = 0
    cabeçalho(f'{c[4]}O jogador {c[0]}{jogador}{c[4]} jogou na posição {str(pos) + c[0]}')
    while True:
        if ok:
            break
        for l in range(0, 3):
            try:
                col = game[l].index(str(pos))
                game[l][col] = jogador
                ok = True
            except:
                cont += 1
                if cont == 3:
                    pos = leiaInt('Posição ja preencida\nEscolha outra posição: ', 2)
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


def cabeçalho(txt, cor=0):
    print(c[7] + linha() + c[0])
    print(c[cor] + txt.center(42) + c[0])
    print(c[7] + linha() + c[0])


def leiaInt(msg, cor=8):
    ok = False
    valor = 0
    while True:
        n = str(input(c[cor] + msg + c[0]))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(c[2] + 'ERRO! Digite um número inteiro válido.' + c[0])
        if ok:
            break
    return valor
