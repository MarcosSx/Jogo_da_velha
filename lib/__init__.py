def cria_novo_jogo():
    return [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def atualiza_jogo(game):
    print()
    for lin in range(0, 3):
        for col in range(0, 3):
            print(f' {game[lin][col]} ', end='')
            print('|' if col != 2 else '', end='')
        print()
        print('¨' * 11 if lin != 2 else '')


def preencher_posicao(pos, game, jogador):
    while pos > 9 or pos <= 0:
        print(f'Indice {pos} fora de alcance')
        pos = int(input('Digite uma posição valida: '))
        print()
    else:
        ok = False
        cont = 0
        print(f'O jogador {jogador} jogou na posição {pos}')
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
                        pos = int(input('\033[31mPosição ja preencida\033[m\n\033[33mEscolha outra posição: \033[m'))
                        print(f'O jogador {jogador} jogou na posição {pos}')
                        cont = 0
                        break


def jogador_ganhou(game, jogador):
    for l in range(0, 3):
        cont = 0
        for c in range(0, 3):
            if game[l][c] == jogador:
                cont += 1
            if cont == 3:
                return True

        # print(cont)
    # return True

