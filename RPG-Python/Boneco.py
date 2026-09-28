from rich import print
from time import sleep

class Personagem:
    def __init__(self, nome:str):
        self.nome = nome
        self.dano = 15
        self.defesa = 5
        self.dano_magico = 10
        self.defesa_magica = 5
        self.velocidade = 5
        self.chan_crit = 5
        self.level = 1
        self.xp = 0
        self.xp_lvl_up = 100
        self.hp = 100
        self.max_hp = self.hp
        #self.mp = status que define a "Stamina" do jogador para ele usar as habilidades dele
        self.mp = 100
        self.max_mp = self.mp
        self.classe = self.escolha_classe(self)
        self.habilidade = None
        self.moeda = 10
        self.armadura = None
        self.arma = None


        self.status()



    def escolha_classe(self, valor):
        classes = ['Guerreiro', 'Mago', 'Ladino']

        print('Escolha a sua classe:')
        for i, v in enumerate(classes):
            print(f'[blue] {i +1} = {v} [/]')

        while True:
            try:
                valor = int(input('Digite o numero da sua classe: '))

                if valor < 1 or valor > 3:
                    print('Digite apenas um valor de 1 à 3 !')

                else:
                    print(f'[blue] Parabens! Voçê escolheu a classe {classes[valor - 1]}[/]')
                    break
            except ValueError:
                print("[red] ERRO! Voce digitou um valor invalido tente novamente! [/]")

        #retorna a classe no indice que o jogador escolheu -1. EXEMPLO= jogador botou 2 ele vai selecionar o indice 1
        return classes[valor - 1]



    def status(self):
        if self.classe == 'Guerreiro':
            self.hp += 50
            self.max_hp = self.hp
            self.defesa += 7
            self.dano += 3
            self.dano_magico -= 1
            self.velocidade -= 1

        elif self.classe == "Mago":
            self.hp -= 20
            self.max_hp = self.hp
            self.dano -= 5
            self.defesa -= 2
            self.dano_magico += 15
            self.defesa_magica += 7
            self.velocidade += 1

        else:
            self.hp -= 10
            self.max_hp = self.hp
            self.dano += 5
            self.defesa -= 2
            self.dano_magico = 0
            self.defesa_magica = 0
            self.velocidade += 7
            self.chan_crit = 10





    def mostra(self, jog):
        print('Estado do jogador')
        for i,v in vars(jog).items():
            print(f'[lightblue]{i} [/] = {v} | ')
        print()

 




if __name__ == "__main__":

    Boneco = Personagem('hebert')
    Boneco.mostra(Boneco)