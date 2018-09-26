#Eu tentei, mas acabei tendo que sair ;-;


import random
import player
import sys
import time

orchp = 10
playeratk = 1

#Funções

def atk(playeratk):
    orchp - 1

def atkOrc(orcatk):
    playerhp - 1

def dano(hp):
    if(hp <= 0):
        endGame()
    else:
        print("Você agora possúi %i pontos de vida" %hp)

def danoOrc(orchp):
    if(orchp <= 0):
        print("Parabéns, você derrotou o Orc! ")
    else:
        print("O orc agora possúi %i pontos de vida" %orchp)


#Lassos

while True:
    playerName = input("Qual o seu nome, nobre aventureiro? ")

    print("Então seu nome é " + playerName + "???")

    option = input("0 - Trocar de nome \n 1 - Manter o nome")

    if(option == "1"):
        break


while True:
    op = input("E qual sera sua classe? \n" +
                        "0 - Guerreiro \n" +
                        "1 - Mago \n" +
                        "2 - Bardo \n")
    if(op == "0"):
        playerName = playerName + ", o Guerreiro"
        print(playerName)
        break
    elif(op == "1"):
        playerName = playerName + ", o Mago"
        print(playerName)
        break
    elif(op == "2"):
        playerName = playerName + ", o Tocador de ukulele"
        print(playerName)
        break
    else:
        print("Esse tipo de classe não existe...")
        dano(10)


thisPlayer = player.Player()
#História e Batalha

print("Você é o " + playerName + " não é? Eu tenho uma missão para você. \n" +
          "Perto daqui existe uma floresta infestada de orcs, quero que você vá lá e mate 5 Orcs \n" +
          "eu posso te dar uma recompensa muito boa por isso. Vá e volte quando terminar")


time(.300)
batalha = input("Você avista um orc, o que você irá fazer? \n 0 - Fugir \n 1 - Batalhar \n")
if(batalha == 0):
    print("O que pensa que está fazendo? Volte para a missão!")
    goto(64)
if(batalha == 1):
    print("Orc HP = %i \n" %orchp +
        "Orc Attack = %i \n" %orcatk +
        "Orc Level = %i \n" %orclvl)

playerRound = input("O que você irá fazer? \n 0 - Atacar \n 1 - Defender \n 2 - Poção \n")
if(playerRound == 0):
         print("Você ataca o Orc!")
         atk
         print("Agora ele está com %i " %orchp)
