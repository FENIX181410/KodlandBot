import random

def gen_pass(pass_length:int):
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
    
def juego(jugador):
    balas = 1
    opciones = ["recargar", "disparar", "bloquear"]
    
    elección = random.choice(opciones)
        
    if jugador == "disparar":
        if elección == "disparar":
            balas-=1
            if balas == 0:
                opciones = ["recargar", "bloquear"] 
            return"Los dos hemos disparado, las balas se chocan. Seguimos jugando."
        elif elección == "bloquear":
            return "Me disparaste mientras bloqueaba. Seguimos jugando."
        elif elección == "recargar":
            return"Me disparaste mientras recargaba. Has ganado."
                
    elif jugador == "bloquear":
        if elección == "disparar":
            balas-=1
            if balas == 0:
                opciones = ["recargar", "bloquear"] 
            return"Te disparé mientras bloqueabas. Seguimos jugando."
        elif elección == "bloquear":
            return"Los dos hemos bloqueado. Seguimos jugando."
        elif elección == "recargar":
            balas+=1
            if balas == 0:
                opciones = ["recargar", "bloquear"]
            return"He recargado mientras bloqueabas. Seguimos jugando."
        
    elif jugador == "recargar":
        if elección == "disparar":
            return"Te he disparado mientras recargabas. He ganado."
        elif elección == "bloquear":
            return"He bloqueado mientras recargabas. Seguimos jugando."
        elif elección == "recargar":
            balas+=1
            if balas == 0:
                opciones = ["recargar", "bloquear"] 
            return"Los dos hemos recargado. Seguimos jugando."
            
    return "Opción no válida. Escoge entre 'recargar', 'disparar' o 'bloquear'."    

def reciclaje(material):
    reciclable=["aluminio","baterías","cartón","celulares","ropa","papel","bolsas","plástico","periódico","metal","vidrio","madera"]   
    if material in reciclable:
        return "Tu material sí es reciclable! No olvides depositarlo en las canecas con el símbolo de hace un rato ;)"
    else:
        return "Tu material no es reciclable, busca canecas que no tengan el símbolo de reciclable para depositarlo ahí ;)"
        
