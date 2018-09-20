import random
import sys
import time

hp = 10

def dano(qtd):
    hp -= qtd
    if(hp <= 0):
        endGame()
    else:
        print("Você agora possúi " + hp + "pontos de vida")

def endGame():
    print("Suas escolhas lhe levaram a ruína. Você precisa de mais borogodó")
    time.sleep()
    sys.exit()

while True:
    playerName = input("Qual o seu nome, nobre aventureiro? ")

    print("Então seu nome é " + playerName + "???")

    option = input("0 - Trocar de nome\n 1 - Manter o nome")

    if(option == "1"):
        break


while True:
    op = input("E qual sera sua classe? \n" +
                        "0 - Guerreiro \n" +
                        "1 - Mago \n" +
                        "2 - Bardo \n")
    if(op == "0"):
        playerName = playerName + ", o Guerreiro"
        break
    elif(op == "1"):
        playerName = playerName + ", o Mago"
        break
    elif(op == "2"):
        playerName = playerName + ", o Tocador de ukulele"
        break
    else:
        print("Esse tipo de classe não existe...")
        dano(10)

