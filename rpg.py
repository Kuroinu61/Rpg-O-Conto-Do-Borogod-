import random
import player
import enemy
import sys
import time

#Funções

def D(lados):
    valor = random.randint(0, lados)
    print("Você rolou um dado de " + str(lados) + " lados e tirou " + str(valor) + "\n")
    return valor

def atk(playeratk):
    orchp - 1

def danoOrc(orchp):
    if(orchp <= 0):
        print("Parabéns, você derrotou o Orc! ")
    else:
        print("O orc agora possúi %i pontos de vida" %orchp)


#Laços

while True:
    playerName = input("Qual o seu nome, nobre aventureiro? ")

    print("Então seu nome é " + playerName + "???")

    option = input("0 - Trocar de nome \n1 - Manter o nome")

    if(option == "1"):
        break


while True:
    op = input("E qual sera sua classe? \n" +
                        "Guerreiro \n" +
                        "Mago \n" +
                        "Bardo \n")
    if(op.lower() == "guerreiro"):
        thisPlayer = player.Player(playerName, op.lower())
        playerName = playerName + ", o Guerreiro"
        print(playerName)
        break

    elif(op.lower() == "mago"):
        thisPlayer = player.Player(playerName, op.lower())
        playerName = playerName + ", o Mago"
        print(playerName)
        break

    elif(op.lower() == "bardo"):
        thisPlayer = player.Player(playerName, op.lower())
        playerName = playerName + ", o Tocador de ukulele"
        print(playerName)
        break

    else:
        print("Esse tipo de classe não existe...")
        dano(10)

#História e Batalha

print("Você é o " + playerName + ", não é? Eu tenho uma missão para você... \n" +
          "Perto daqui existe uma floresta infestada de orcs, quero que você vá lá e mate 5 Orcs \n" +
          "eu posso te dar uma recompensa muito boa por isso. Vá e volte quando terminar")
time.sleep(1)
round = 0
while round < 5:
    batalha = input("Você avista um orc, o que você irá fazer? \n Fugir \n Batalhar \n")
    orc = enemy.Enemy("Orc", 10, 5, 10, None)
    if(batalha.lower() == "fugir"):

        rolar_dado = D(20)

        if(rolar_dado > 15):
            print("Você conseguiu fugir desse orc, mas existem vários por aí. Prepare-se para a próxima batalha\n")
            time.sleep(2)
        elif(rolar_dado > 8):
            print("Você conseguiu fugir, mas o Orc lhe acertou pelas costas enquanto você corria\n")
            thisPlayer.recebe_dano(3)
            time.sleep(2)
        else:
            print("Você cometeu um grande erro ao tentar fugir, o Orc lhe feriu gravemente quando você tentou correr\n")
            thisPlayer.recebe_dano(5)
            time.sleep(2)

    elif(batalha.lower() == "batalhar"):
        round += 1
        while True:

            print("Orc HP = %i \n" %orchp +
                "Orc Attack = %i \n" %orcatk +
                "Orc Level = %i \n" %orclvl)

            playerRound = input("O que você irá fazer?" +
                                "\n Atacar "+
                                "\n Defender "+
                                "\n Poção \n")

            if(playerRound.lower() == "atacar"):
                     print("Você ataca o Orc!")

                     print("Agora ele está com %i " %orchp)
