from random import choice
print("Bienvenido!")
lista_opciones=["piedra","papel","tijera"]
game_on=True
def empate():
    print("Ambos sacaron igual, intentalo de nuevo")
def win(computer_input):
    print("La computadora eligio",computer_input,"ganaste")
def lose(computer_input):
    print("La computadora eligio",computer_input,"perdiste")
while game_on:
    computer_input = choice(lista_opciones)
    print("Elige 0 para piedra,1 para papel,2 para tijera y 3 para terminar partida: ")
    user_input = int(input())
    if user_input==0: #USUARIO ELIGE PIEDRA
        if computer_input=="piedra":
            empate()
        elif computer_input=="papel":
            lose("papel")
        else:
            win("tijera")
    elif user_input==1: #USUARIO ELIGE PAPEL
        if computer_input=="papel":
            empate()
        elif computer_input=="piedra":
            win("piedra")
        else:
            lose("tijeras")
    elif user_input==2: #USUARIO ELIGE TIJERA
        if computer_input=="tijera":
            empate()
        elif computer_input=="piedra":
            lose("piedra")
        else:
            win("papel")
    elif user_input==3:
        print("Gracias por jugar!")
        game_on=False
    else:
        print("Invalid input")



