from lib import *

while True:
    jogo = cria_novo_jogo()
    cabeçalho('BEM VINDO À VELHA', cor=5)
    cabeçalho('Escolha um caractere para te representar:', cor=8)
    jogador1 = escolhe_jogador('JOGADOR 1: ')
    jogador2 = escolhe_jogador('JOGADOR 2: ', jogador1)
    cabeçalho('Escolha um dos indices numerados', cor=8)
    atualiza_jogo(jogo)
    cont = 0
    for i in range(0, 9):
        cont += 1
        if i % 2 == 0:
            pos = leiaInt('Digite uma posição: ')
            preencher_posicao(pos, jogo, jogador1)
            atualiza_jogo(jogo)
            if jogador_ganhou(jogo, jogador1):
                cabeçalho(f'O Jogador 1 {jogador1} GANHOUU!!!', cor=3)
                break
        else:
            pos = leiaInt('Digite uma posição: ')
            preencher_posicao(pos, jogo, jogador2)
            atualiza_jogo(jogo)
            if jogador_ganhou(jogo, jogador2):
                cabeçalho(f'O Jogador 2 {jogador2} GANHOUU!!!', cor=3)
                break
    if cont == 9 and not jogador_ganhou(jogo, jogador1) or jogador_ganhou(jogo, jogador2):
        cabeçalho('DEU VELHA', cor=9)
    while True:
        resp = str(input('Deseja jogar mais uma? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print(c[2] + 'Opção invalida!!!' + c[0])
    if resp in 'N':
        break
