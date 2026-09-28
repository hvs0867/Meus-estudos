from random import choices

class Monstro:
    nomes = ['Slime', 'Goblin', 'Lobo', 'Esqueleto', "Orc", 'Troll']

    escolhido = choices(nomes , weights=[30, 30, 30, 20, 10, 8], k=1)[0]

    def __init__(self):
        self.nivel = 1
        self.dano = 10
        self.hp = 100
        self.defesa = 5
        self.defesa_magica = 4
        self.velocidade = 4
        self.critico = 2
        self.xp = 10
        self.moedas = 20
        self.nome = self.escolhido
        self.dano_magico = 10

        self.status()


    def status(self):
        match self.escolhido:
            case 'Goblin':
                self.hp = 70
                self.dano = 11
                self.defesa = 4
                self.defesa_magica = 3
                self.velocidade =6 
                self.critico = 5
                self.moedas = 15

            case 'Lobo':
                self.nivel = 2
                self.hp = 85
                self.defesa_magica = 3
                self.defesa = 3
                self.velocidade = 9
                self.critico = 8
                self.xp = 20
                self.moedas = 20

            case 'Slime':
                self.moedas = 8
                self.xp = 10
                self.critico = 2
                self.velocidade = 2
                self.defesa_magica = 2
                self.defesa = 2
                self.dano = 8 
                self.hp = 50


    def mostra(self, mons):
        print('Estado do Monstro')
        for i,v in vars(mons).items():
            print(f'{i} = {v} |', end='')
        print()



class MonstroMgc:
    nomes = ['Slime Magico', 'Mago Goblin', 'Feiticeiro']

    escolha = choices(nomes, weights=[40,40, 10], k=1)[0]

    def __init__(self):
        self.nivel = 1
        self.dano = 10
        self.dano_magico = 5
        self.hp = 100
        self.defesa = 5
        self.defesa_magica = 4
        self.velocidade = 4
        self.critico = 2
        self.xp = 10
        self.moedas = 20
        self.nome = self.escolha

        self.status()


    def status(self):
        match self.escolha:
            case 'Slime Magico':
                self.nivel = 3
                self.hp = 90
                self.dano = 8
                self.defesa = 4
                self.dano_magico = 10
                self.defesa_magica = 8
                self.velocidade = 5
                self.critico = 5
                self.xp =3500
                self.moedas = 25


            case 'Mago Goblin':
                self.moedas = 28
                self.xp = 50
                self.critico = 8
                self.velocidade = 7
                self.defesa_magica = 10
                self.dano_magico = 22
                self.defesa_magica = 10
                self.defesa = 7
                self.hp = 80
                self.nivel = 4

            case 'Feiticeiro':
                self.nivel = 6
                self.hp = 130
                self.dano = 10
                self.defesa = 6
                self.dano_magico = 20
                self.defesa_magica = 15
                self.velocidade = 6
                self.critico = 10
                self.xp = 90
                self.moedas = 50        
            

    def mostra(self, mons):
        print('Estado do Monstro Magico')
        for i,v in vars(mons).items():
            print(f'{i} = {v} |', end='')
        print()


if __name__ == "__main__":
    m1 = MonstroMgc()

    m1.mostra(m1)