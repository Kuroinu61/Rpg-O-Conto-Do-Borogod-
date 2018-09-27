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

while True:
    print("Você está saindo de casa para inciiar sua aventura" +
        "\n Você tem isso em casa" +
        "\n Espada" +
        "\n Cajado" +
        "\n Balde de água" +
        "\n Ukulele" +
        "\n Toalha")

    op = input("Qual você leva? ")

    if(op.lower() == "espada" or op.lower() == "cajado" or op.lower() == "balde de água" or op.lower() == "ukulele" or op.lower() == "toalha"):
        print("Você pegou a " + str(op))
        item = op.lower
        break
    else:
        print("Esse item não existe animal!")
        this.Player.recebe_dano(2)

while True:
    print("Ao sair de casa você se depara com um enorme anaõ de fogo")
    act = input("\nO que você deseja fazer?"+
                "\nUsar item" +
                "\nFugir")

    if(act.lower() == "usar item"):
        if(item == "espada"):
            print("Você saca sua espada e tenta atacar o enorme anão de fogo"+
                "\n Você se queima, parabéns")
            thisPlayer.recebe_dano(100)
        elif(item == "cajado"):
            print("O cajado queima até as cinzas")
            thisPlayer.recebe_dano(100)
        elif(item == "ukulele"):
            print("o anão se acalma e vai embora")
            break
        elif(item == "balde de água"):
            print("O fogo do anão apaga e ele morre de frio, parabéns seu monstro")
            thisPlayer.recebe_exp(10)
            break
        elif(item == "toalha"):
            print("Você tenta enrolar o anão na toalha, você achou que ela ia queimar mas a toalha era de adamantium" +
                "\nVocê joga o anão longe")
            thisPlayer.recebe_exp(20)
            break
 
