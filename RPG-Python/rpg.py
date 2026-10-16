from random import choices
from Monstro import Boss, Monstro, MonstroMgc
from Boneco import Personagem
from mecanicas import batalha
from rich import print


def gerar_monstro(jogador):
    if jogador.level >= 3 and choices([True, False], weights=[20, 80], k=1)[0]:
        return Boss()
    return choices([Monstro(), MonstroMgc()], weights=[80, 20], k=1)[0]


def loja(jogador):
    while True:
        print('\n[gold]LOJA[/]')
        print(f'Você tem {jogador.moeda} moedas.')
        print('1 - Poção (5)')
        print('2 - Elixir (12)')
        print('3 - Melhorar arma (20)')
        print('4 - Sair da loja')

        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('[red]Opção inválida.[/]')
            continue

        if escolha == 1:
            if jogador.moeda >= 5:
                jogador.moeda -= 5
                jogador.inventario['poção'] = jogador.inventario.get('poção', 0) + 1
                print('[green]Você comprou uma poção.[/]')
            else:
                print('[red]Moedas insuficientes.[/]')

        elif escolha == 2:
            if jogador.moeda >= 12:
                jogador.moeda -= 12
                jogador.inventario['elixir'] = jogador.inventario.get('elixir', 0) + 1
                print('[green]Você comprou um elixir.[/]')
            else:
                print('[red]Moedas insuficientes.[/]')

        elif escolha == 3:
            if jogador.moeda >= 20:
                jogador.moeda -= 20
                jogador.dano += 3
                jogador.dano_magico += 2
                jogador.defesa += 1
                print('[green]Sua arma foi melhorada.[/]')
            else:
                print('[red]Moedas insuficientes.[/]')

        elif escolha == 4:
            return

        else:
            print('[red]Opção inexistente.[/]')


def menu_jogo(jogador):
    while True:
        print('\n[cyan]MENU[/]')
        print('1 - Batalhar')
        print('2 - Loja')
        print('3 - Ver status')
        print('4 - Sair')

        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print('[red]Opção inválida.[/]')
            continue

        if escolha == 1:
            monstro = gerar_monstro(jogador)
            print(f'Um [red]{monstro.nome}[/] apareceu!')

            while jogador.hp > 0 and monstro.hp > 0:
                resultado = batalha(jogador, monstro)
                if resultado is True:
                    print(f'{jogador.nome} conseguiu fugir da batalha!')
                    break

            if jogador.hp <= 0:
                print(f'[red]{jogador.nome} foi derrotado! Fim de jogo.[/]')
                return False

            if monstro.hp <= 0:
                jogador.moeda += monstro.moedas
                jogador.upar_level(monstro)
                print(f'[green]Você derrotou o {monstro.nome}![/]')
                print(f'Você ganhou {monstro.moedas} moedas.')
                if isinstance(monstro, Boss):
                    print('[gold]Você venceu o boss final![/]')
                    return True

            jogador.mostra(jogador)

        elif escolha == 2:
            loja(jogador)

        elif escolha == 3:
            jogador.mostra(jogador)

        elif escolha == 4:
            print('[yellow]Obrigado por jogar![/]')
            return False

        else:
            print('[red]Opção inexistente.[/]')


def main():
    print('OLA, GUERREIRO! SEJA BEM VINDO AO [red]PYRPG![/] VAMOS COMECA A CRIAR O SEU PERSONAGEM!')
    while True:
        nome = input(' INSIRA O NOME DO DEU PERSNAGEM: ')
        if len(nome) > 16:
            print('Porfavor insira um nome com menos caracteres (maximo é 16)')
        else:
            break

    jogador = Personagem(nome)
    print('AQUI ESTÃO OS SEUS STATUS INCIAIS: ')
    jogador.mostra(jogador)
    print('-' * 40)

    fim = menu_jogo(jogador)
    if fim is True:
        print('[gold]Parabéns! Você concluiu o jogo.[/]')


if __name__ == '__main__':
    main()