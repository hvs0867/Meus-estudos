from time import sleep
from random import randint, choices, choice
from rich import print


def monstro_dmg(monstro, jogador):
    # dano_monstro =  monstro.dano - jogador.defesa
    # dano_magico_monstro =  monstro.dano_magico - jogador.defesa_magica

    defesa = jogador.defesa // 2
    variancia_montro = randint(defesa, jogador.defesa)
    dano_monstro = monstro.dano - variancia_montro

    dano_magico_monstro = monstro.dano_magico - variancia_montro
    
    
    #O MONSTRO SEMPRE VAI ESCOLHER O TIPO DE ATAQUE QUE VAI DAR MAIS DANO
    if dano_monstro > dano_magico_monstro:
        print(f'[red]{monstro.nome}[/] infligiu [red]{dano_monstro} de dano fisico[/]  no Jogador!')

        jogador.hp -= dano_monstro
    
    else:
        print(f'[red]{monstro.nome}[/] infligiu [red]{dano_magico_monstro} de dano magico[/]  no Jogador!')

        jogador.hp -= dano_magico_monstro




def batalha(jogador, monstro):
    print(f'{monstro.nome} | {monstro.hp};| {jogador.nome} | {jogador.hp}')


    while True:
        try:
            pergunta = int(input('''Oque Voçê Vai Fazer?
 [1]Atacar | [2]Esquivar
 [3]Inventario| [4]Fujir
 >>>>> '''))
            if 1 < pergunta > 4:
                print('[red]OPÇÃO INEXISTENTE![/]') 
            else:
                break

        except ValueError:
            print("[red]OPÇÃO INVALIDA! TENTE NOVAMENTE[/]")


    match pergunta:
        #ACHO QUE ESSA PARTE AQUI TA AUTO EXPLICATIVA (•_•)

        #case 1 é a parte de ataque! 
        case 1:
          
            defesa = monstro.defesa // 2
            variancia_dmg_jogador = randint(defesa, monstro.defesa)

            dano_jogador = jogador.dano - variancia_dmg_jogador

            dano_magico_jogador = jogador.dano_magico - variancia_dmg_jogador

            #sleep(0.5)

            #Validação da resposta do player; variavel = opcao
            while True:
                try:
                    opcao = int(input(f'''\033[34mVoçê quer usar ataque fisico ou magico?\033[m
[1] Ataque Fisico (DMG= {jogador.dano})  | [2] Ataque magico (DMG= {jogador.dano_magico})
>>>>>  '''))
                    
                    if opcao > 2 or opcao < 1:
                        print('PORFAVO INSIRA APENAS VALORES 1 OU 2')
                    else:
                        break
                except ValueError:
                    print("OPÇÃO INVALIDA!")


            if jogador.velocidade > monstro.velocidade:
                if opcao == 1: 
                    print(f'O jogador {jogador.nome} atacou o montro [red]{monstro.nome}[/] com um ataque fisico e infligiu [red]{dano_jogador}[/] de dano!')

                    monstro.hp -= dano_jogador
                    sleep(0.5)

                else:
                    print(f'O jogador {jogador.nome} atacou o montro [red]{monstro.nome}[/] com um ataque magico e infligiu [red]{dano_magico_jogador}[/] de dano!')

                    monstro.hp -= dano_magico_jogador

                    #sleep(0.5)

                if monstro.hp >0:
                    monstro_dmg(monstro,jogador)

            else:
                monstro_dmg(monstro, jogador)

                if jogador.hp < 1:
                    return jogador.hp, monstro.hp
                
                else:
                    if opcao == 1: 
                        print(f'O jogador {jogador.nome} atacou o montro [red]{monstro.nome}[/] com um ataque fisico e infligiu [red]{dano_jogador}[/] de dano!')

                        monstro.hp -= dano_jogador

                        #sleep(0.5)

                    else:
                        print(f'O jogador {jogador.nome} atacou o montro [red]{monstro.nome}[/] com um ataque magico e infligiu [red]{dano_magico_jogador}[/] de dano!')

                        monstro.hp -= dano_magico_jogador

                        #sleep(0.5)

            print("-"  *40)
            #validação do hp do mosntro ta dentro da função de upar level. se o hp dele for menor que 1 ja da ele como morto e upa os status do jogador
            jogador.upar_level(monstro)

            return jogador.hp, monstro.hp



        case 2:
            esquiva = choices([1,2], weights=(20,80), k=1)[0]

            if esquiva == 1:
                print('Voçê esquivou com sucesso!!')
            else:
                palavras = ['Voçê escorregou e caiu no chão!', 'Voçê tropeçou em uma pedra, caiu no chão!', 'O vento derrubou voçê!', 'Voçê escorregou em uma casca de banana!']

                palavra_escolhida = choice(palavras)

                print(palavra_escolhida)
                monstro_dmg(monstro, jogador)

                
            print("-"*40)

            #sleep(0.5)
            
            return jogador.hp
               



  

