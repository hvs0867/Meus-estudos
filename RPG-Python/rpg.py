from random import choices
from time import sleep
from Monstro import *
from Boneco import *
from mecanicas import *

from rich import print




def gerar_monstro():
    #monstros = choices(([Monstro(), MonstroMgc()]), weights=[60, 40], k=1)[0]
    monstros = MonstroMgc()
    return monstros



def main():
    print('OLA, GUERREIRO! SEJA BEM VINDO AO [red]PYRPG![/] VAMOS COMECA A CRIAR O SEU PERSONAGEM!')
    nome = input(" INSIRA O NOME DO DEU PERSNAGEM: ")

    Jogador = Personagem(nome)
    #sleep(0.8)

    print('AQUI ESTÃO OS SEUS STATUS INCIAIS: ')
    Jogador.mostra(Jogador)
    print("-"*40)

    monstro = gerar_monstro()

    while Jogador.hp > 0 and monstro.hp > 0:
        batalha(Jogador, monstro)

    Jogador.mostra(Jogador)

if __name__ == '__main__':
    main()