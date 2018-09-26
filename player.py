class Player:

    level = 1   #nível atual do player
    hp = 0
    con = 0     #constituição
    str = 0     #força
    agi = 0     #agilidade
    int = 0     #intelecto
    car = 0     #carisma
    atk = 0     #ataque
    defesa = 0  #batata

    atualxp = 0
    proxlevel = 10

    nome = ""
    classe = ""

    Player(nome, classeEscolhida):
        if(classeEscolhida.lower() == "guerreiro"):
            hp = 10
            str = 7
            agi = 3
            int = 1
            car = 3
            con = 1
        elif(classeEscolhida.lower() == "mago"):
            hp = 7
            str = 3
            agi = 4
            int = 7
            car = 1
            con = 1
        elif(classeEscolhida.lower() == "bardo"):
            hp = 4
            str = 2
            agi = 2
            int = 5
            car = 5
            con = 1

        calcular_ataque()
        calcular_defesa()

        self.classe = classeEscolhida
        self.nome = nome

    def calcular_ataque():
        if(classe.lower() == "guerreiro"):
            self.atk = (2*self.str + self.agi + self.int + self.car) / 5
        elif(classe.lower() == "mago"):
            self.atk = (2*self.int + self.str + self.car + self.agi) / 5
        elif(classe.lower() == "bardo"):
            self.atk = (3*self.car + 2*self.int + self.str + self.agi) / 5

        return self.atk

    def calcular_defesa():
        defesa = str * con / 10

    def calcular_hp():
        if(con == 1 || level == 1):
            hp = 0
        else:
            hp = level * con

    def endGame():
        print("Suas escolhas lhe levaram a ruína. Você precisa de mais borogodó")
        time.sleep()
        sys.exit()

    def goto(line):
        global lineNumber
        line = lineNumber

    def recebe_dano(qtd):
        calcular_defesa()
        dano -= qtd - defesa

        print("Você recebe " + dano + " de dano")

        if(dano != 0):
            hp -= dano
            print("Agora você possúi " + str(hp) + "pontos de vida\n")

        if(hp <= 0):
            endGame()

    def exibir_status():
        print(nome + ", Nível: " + level + ", status: \n" +
              "força: " + str(str) + "\n"
              "constituição: " + str(con) + "\n"
              "inteligência: " + str(int) + "\n"
              "agilidade: " + str(agi) + "\n"
              "carisma:: " + str(car) + "\n"
              "ataque: " + str(calcular_ataque()) + "\n"

    def recebe_exp(xp):
        atualxp += xp
        if(atualxp >= proxlevel):
            level += 1
        proxlevel += (10*proxlevel)/100
