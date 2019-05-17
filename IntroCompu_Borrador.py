from random import choice
fichas_disponibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fichas_usuario = []
fichas_compu = []
print("Bienvenido"+"\n"+"Presiona 1 para empezar y 2 para que la computadora comience")
game_starter=int(input())
def EscogerFicha(input,l):
    l.append(input)
    fichas_disponibles.remove(input)
def User_play():
    print("Elige una ficha de las disponibles")
    user_inp = int(input())
    EscogerFicha(user_inp,fichas_usuario)
    print("Tus fichas:", fichas_usuario)
def ComputerPlay():
    computer_inp = choice(fichas_disponibles)
    EscogerFicha(computer_inp, fichas_compu)
    print("Fichas de la compu:", fichas_compu)
while sum(fichas_usuario) != 15 and sum(fichas_compu) != 15:
    if game_starter==1:
        print("Disponibles:", fichas_disponibles)
        User_play()
        ComputerPlay()
    elif game_starter==2:
        ComputerPlay()
        print("Disponibles:", fichas_disponibles)
        User_play()
if sum(fichas_usuario)==15:
    print("Ganaste!!")
elif sum(fichas_compu)==15:
    print("Perdiste...")
