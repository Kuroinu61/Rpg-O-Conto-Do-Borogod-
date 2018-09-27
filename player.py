import time

class Player:

    level = 1   #nível atual do player
    maxhp = 0
    hp = 0
    con = 0     #constituição
    str = 0     #força
    agi = 0     #agilidade
    int = 0     #intelecto
    car = 0     #carisma

    atualxp = 0
    proxlevel = 10

    nome = ""
    classe = ""

    def __init__(self, nome, classeEscolhida):
        if(classeEscolhida == "guerreiro"):
            self.hp = 5
            self.str = 7
            self.agi = 3
            self.int = 1
            self.car = 3
            self.con = 1
        elif(classeEscolhida == "mago"):
            self.hp = 5
            self.str = 3
            self.agi = 4
            self.int = 7
            self.car = 1
            self.con = 1
        elif(classeEscolhida == "bardo"):
            self.hp = 5
            self.str = 2
            self.agi = 2
            self.int = 5
            self.car = 5
            self.con = 1

        self.maxhp = 5
        self.level = 1

        self.classe = classeEscolhida
        self.nome = nome

    def ataque(self):
        atk = 0
        if(self.classe.lower() == "guerreiro"):
            atk = (2*self.str + self.agi + self.int + self.car) / 5
        elif(self.classe.lower() == "mago"):
            atk = (2*self.int + self.str + self.car + self.agi) / 5
        elif(self.classe.lower() == "bardo"):
            atk = (3*self.car + 2*self.int + self.str + self.agi) / 5

        return atk

    def defesa(self):
        return self.str * self.con / self.hp


    def calcular_hp(self):
        if(self.con == 1 and self.level == 1):
            self.maxhp = 5
        else:
            self.maxhp = (self.level * self.con * 0.2) + 5
        return self.maxhp

    def endGame(self):
        print("\n\n\n\nSuas escolhas lhe levaram a ruína. Você precisa de mais borogodó\n\n\n\n")
        time.sleep(5)
        sys.exit()

    def goto(line):
        global lineNumber
        line = lineNumber

    def recebe_dano(self, qtd):
        dano = int(qtd - self.defesa())

        print("Você recebe " + str(dano) + " de dano\n")

        if(dano != 0):
            self.hp -= dano
            print("Agora você possúi " + str(self.hp) + " pontos de vida\n")

        if(self.hp <= 0):
            self.endGame()

    def exibir_status(self):
        print(nome + ", você está no nível: " + level + ", seus status são: " +
              "\nforça: " + str(self.str) +
              "\nconstituição: " + str(self.con) +
              "\ninteligência: " + str(self.int) +
              "\nagilidade: " + str(self.agi) +
              "\ncarisma:: " + str(self.car) +
              "\nataque: " + str(ataque()) +
              "\nVocê possúi " + str(self.atualxp) + " e precisa de " +
              str(proxlevel - atualxp) + " para ir para o próximo nívelz\n\n")

    def recebe_exp(self, xp):
        self.atualxp += xp
        if(self.atualxp >= self.proxlevel):
            self.level += 1
        self.proxlevel += self.proxLevel + (10*self.proxlevel)/100
