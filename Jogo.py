from lib import *

while True:
    jogo = cria_novo_jogo()
    cabeçalho('BEM VINDO À VELHA')
    cabeçalho('Escolha um caractere para te representar:')
    jogador1 = escolhe_jogador('JOGADOR 1: ')
    jogador2 = escolhe_jogador('JOGADOR 2: ', jogador1)
    cabeçalho('Escolha um dos indices numerados')
    atualiza_jogo(jogo)
    while True:
        for i in range(0, 9):
            if i % 2 == 0:
                pos = int(input('Digite uma posição: '))
                preencher_posicao(pos, jogo, jogador1)
                atualiza_jogo(jogo)
                if jogador_ganhou(jogo, jogador1):
                    cabeçalho(f'\033[32mO Jogador 1 {jogador1} GANHOUU!!!\033[m')
                    break
            else:
                pos = int(input('Digite uma posição: '))
                preencher_posicao(pos, jogo, jogador2)
                atualiza_jogo(jogo)
                if jogador_ganhou(jogo, jogador2):
                    cabeçalho(f'\033[32mO Jogador 2 {jogador2} GANHOUU!!!\033[m')
                    break
        break
    while True:
        resp = str(input('Deseja jogar mais uma? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
