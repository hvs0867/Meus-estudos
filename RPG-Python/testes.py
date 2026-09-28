from random import choices


nomes = ['Slimes', 'Goblins', 'Lobo', 'Esqueleto', "Orc", 'Troll']

escolhido = choices(nomes , weights=[30, 30, 30, 20, 10, 8], k=1)[0]

print(escolhido)

