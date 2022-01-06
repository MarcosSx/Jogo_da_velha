from lib import *

jogo = cria_novo_jogo()

print('BEM VINDO À VELHA')
jogador1 = str(input('Escolha um caractere para te representar\nJOGADOR 1: ')).upper().strip()[0]
jogador2 = str(input('Escolha um caractere para te representar\nJOGADOR 2: ')).upper().strip()[0]
print('Escolha um dos indices numerados')
atualiza_jogo(jogo)
while True:
    for i in range(0, 9):
        if i % 2 == 0:
            pos = int(input('Digite uma posição: '))
            preencher_posicao(pos, jogo, jogador1)
            atualiza_jogo(jogo)
            if jogador_ganhou(jogo, jogador1):
                print(f'O Jogador 1 {jogador1} GANHOUU!!!')
                break
        else:
            pos = int(input('Digite uma posição: '))
            preencher_posicao(pos, jogo, jogador2)
            atualiza_jogo(jogo)
            if jogador_ganhou(jogo, jogador2):
                print(f'O Jogador 2 {jogador2} GANHOUU!!!')
                break
    break
