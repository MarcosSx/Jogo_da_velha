from random import randint
from time import sleep

c = (
    '\033[m',       # 0Limpa
    '\033[1;97m',   # 1Branco
    '\033[0;31m',   # 2Vermelho
    '\033[0;32m',   # 3Verde
    '\033[0;33m',   # 4Amarelo
    '\033[0;34m',   # 5Azul
    '\033[0;35m',   # 6Magenta
    '\033[0;36m',   # 7Ciano
    '\033[1;96m',   # 8Ciano claro
    '\033[1;95m',   # 9Pink
    '\033[;7m'      # 10Inverte
    )


def cria_novo_jogo(inicio=False):
    '''
    -> Esta função cria uma lista onde o jogo é armazenado.
    :param inicio: Se for verdadeiro imprime os cabeçalhos de um jogo novo
    :return: Retorna lista do jogo independente de como esteja o jogo
    '''
    if inicio:
        cabeçalho('BEM VINDO À VELHA', cor=5)
        cabeçalho('Escolha um caractere para te representar:', cor=8)
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def escolhe_jogador(msg, jogador2='x', bot=False):
    '''
    -> Esta função escolhe os caracteres que cada jogador devera usar
    :param msg: Este parametro imprime na tela a mensagem que o jogador deseja
    :param jogador2: Este parametro (opcional), define qual caractere esta disponivel
    :param bot: Se verdadeiro, escolhe sozinho seu caractere, se falso, o segundo jogador devera escolher seu caractere
    :return: Restorna o valor do caractere do jogador
    '''
    if bot:
        jogador = 'X'
        if jogador in jogador2:
            jogador = 'O'
        print(str(c[3] + msg + jogador + c[0]))
    else:
        while True:
            jogador = str(input(c[3] + msg + c[0])).upper().strip()[0]
            if jogador.isalpha() and jogador not in jogador2:
                break
            cabeçalho('Escolha outro caractere valido!', 2)
    cor = randint(1, 6)
    return c[cor] + jogador + c[0]


def atualiza_jogo(game):
    '''
    -> Esta função imprime o jogo no estado em que está
    :param game: Lista do jogo
    :return: Não retorna nada apenas imprime o jogo
    '''
    cabeçalho('Escolha um dos indices numerados', cor=8)
    for lin in range(0, 3):
        for col in range(0, 3):
            print(f' {c[9] + game[lin][col] + c[0]} ', end='')
            print(f'{c[8]}|' if col != 2 else '', end='')
        print()
        print(f'{c[8]}-' * 11 if lin != 2 else f'{c[0]}')


def preencher_posicao(posição, game, jogador, bot=False):
    '''
    -> Esta função preenche apenas espaços vazios
    :param posição: Posição escolhida pelo jogador
    :param game: Lista do jogo
    :param jogador: Caractere do jogador
    :param bot: Caractere do jogador("Computador")
    :return: -
    '''
    while posição > 9 or posição <= 0:
        if bot:
            posição = randint(1, 9)
            sleep(1)
            break
        cabeçalho(f'Indice {posição} fora de alcance')
        posição = leiaInt('Digite uma posição valida: ', 4)
        print()
    ok = False
    cont = 0
    cabeçalho(f'{c[4]}O jogador {c[0]}{jogador}{c[4]} jogou na posição {str(posição) + c[0]}')
    while True:
        if ok:
            break
        for l in range(0, 3):
            try:
                col = game[l].index(str(posição))
                game[l][col] = jogador
                ok = True
            except:
                cont += 1
                if cont == 3:
                    if bot:
                        posição = randint(1, 9)
                    else:
                        posição = leiaInt('Posição ja preencida\nEscolha outra posição: ', 2)
                        cabeçalho(f'{c[4]}O jogador {c[0]}{jogador}{c[4]} jogou na posição {posição}{c[0]}')
                    cont = 0
                    break


def jogador_ganhou(game, jogador):
    '''
    -> Esta função verifica todas as diagonais, verticais e horizontais e diz se o jogador ganhoy
    :param game: Lista do jogo
    :param jogador: Jogador
    :return: Retorna True se o jogador ganhou
    '''
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


def cabeçalho(txt, cor=0):
    '''
    -> Esta função faz os cabeçalhos do jogo
    :param txt: Texto a ser impresso no cabeçaçho
    :param cor: Cor escolhida
    :return: Imprime o cabeçalho
    '''
    linha = '-' * 42
    print(c[7] + linha + c[0])
    print(c[cor] + txt.center(42) + c[0])
    print(c[7] + linha + c[0])


def leiaInt(msg, cor=8):
    '''
    -> Função para ler apenas numeros inteiros
    :param msg: Texto para input
    :param cor: Cor escolhida
    :return: Retorna o valor inteiro
    '''
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

