from random import choice
print("Bienvenido!")
lista_opciones=["piedra","papel","tijera"]
computer_input=choice(lista_opciones)
game_on=True
while game_on:
    print("Elige 0 para piedra,1 para papel,2 para tijera y 3 para terminar partida: ")
    user_input = int(input())
    if user_input==0:
        print("\n" * 50)
        print("Elegiste piedra")
        if computer_input=="piedra":
            print("Ambos sacaron piedra, intentalo de nuevo")
        elif computer_input=="papel":
            print("La computadora eligio papel, perdiste.")
        else:
            print("La computadora eligio tijera, ganaste")
    elif user_input==1:
        print("Elegiste papel")
        print("\n" * 50)
        if computer_input=="papel":
            print("Ambos sacaron papel, intentalo de nuevo")
        elif computer_input=="piedra":
            print("La computadora eligio piedra, ganaste")
        else:
            print("La computadora eligio tijera, perdiste")
    elif user_input==2:
        print("Elegiste tijera")
        print("\n" * 50)
        if computer_input=="tijera":
            print("Ambos sacaron tijera, intentalo de nuevo")
        elif computer_input=="piedra":
            print("La computadora eligio piedra, perdiste")
        else:
            print("La computadora eligio papel,ganaste")
    elif user_input==3:
        print("Gracias por jugar!")
        game_on=False
    else:
        print("Invalid input")

