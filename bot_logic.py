import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_emoji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"
    
def juego():
    print("Ok, cada uno empieza con una bala. Dime 'terminar' cuando quieras acabar el juego.")
    balas = 1
    opciones = ["recargar", "disparar", "bloquear"]
    
    while True:
        jugador = input("Elige una opción (disparar, recargar, bloquear): ")
        if jugador == "terminar":
            print("El juego ha terminado.")
            exit()
        
        if balas == 0:
            opciones = ["recargar", "bloquear"] 
        else:
            opciones = ["recargar", "disparar", "bloquear"]
        
        elección = random.choice(opciones)
        
        if jugador == "disparar":
            if elección == "disparar":
                balas-=1
                print("Los dos hemos disparado, las balas se chocan. Seguimos jugando.")
            elif elección == "bloquear":
                print("Me disparaste mientras bloqueaba. Seguimos jugando.")
            elif elección == "recargar":
                print("Me disparaste mientras recargaba. Has ganado.")
                exit()
 
        
        elif jugador == "bloquear":
            if elección == "disparar":
                balas-=1
                print("Te disparé mientras bloqueabas. Seguimos jugando.")
            elif elección == "bloquear":
                print("Los dos hemos bloqueado. Seguimos jugando.")
            elif elección == "recargar":
                balas+=1
                print("He recargado mientras bloqueabas. Seguimos jugando.")
        
        elif jugador == "recargar":
            if elección == "disparar":
                print("Te he disparado mientras recargabas. He ganado.")
                exit()
            elif elección == "bloquear":
                print("He bloqueado mientras recargaba. Seguimos jugando.")
            elif elección == "recargar":
                balas+=1
                print("Los dos hemos recargado. Seguimos jugando.")
