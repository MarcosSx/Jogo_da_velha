from lib import *

while True:
    jogo = cria_novo_jogo(inicio=True)
    jogador1 = escolhe_jogador('JOGADOR 1: ')
    escolha = leiaInt('Deseja jogar contra:\n1: Pessoa\n2: BOT\n>>')
    bot = False
    if escolha == 2:
        bot = True
    jogador2 = escolhe_jogador('JOGADOR 2: ', jogador1, bot)

    atualiza_jogo(jogo)
    cont = 0
    for i in range(0, 9):
        cont += 1
        if i % 2 == 0:
            pos = leiaInt(f'{jogador1} Digite uma posição: ')
            preencher_posicao(pos, jogo, jogador1)
            atualiza_jogo(jogo)
            if jogador_ganhou(jogo, jogador1):
                cabeçalho(f'O Jogador 1 {jogador1} GANHOUU!!!', cor=3)
                break
        else:
            pos = 0
            if not bot:
                pos = leiaInt(f'{jogador2} Digite uma posição: ')
            preencher_posicao(pos, jogo, jogador2, bot)
            atualiza_jogo(jogo)
            if jogador_ganhou(jogo, jogador2):
                cabeçalho(f'O Jogador 2 {jogador2} GANHOUU!!!', cor=3)
                break
    if cont == 9 and not jogador_ganhou(jogo, jogador1) or not jogador_ganhou(jogo, jogador2):
        cabeçalho('DEU VELHA', cor=9)
    while True:
        resp = str(input('Deseja jogar mais uma? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print(c[2] + 'Opção invalida!!!' + c[0])
    if resp in 'N':
        break
