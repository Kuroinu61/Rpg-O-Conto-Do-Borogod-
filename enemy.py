class Enemy:
    hp = 0
    atk = 0
    exp = 0
    loot = None
    nome = ""

    def __init__(self, nome, hp, atk, exp, loot):
        self.name = nome
        self.hp = hp
        self.atk = atk
        self.exp = exp
        self.loot = loot
