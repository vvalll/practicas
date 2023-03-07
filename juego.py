import random
def juego ():
    ronda = 0
    maquina = 0 
    usuario = 0
    for x in range(1,4):
        ronda+=1
        print("************")
        print("RONDA: ", ronda)
        print("************")
        res = [ ]
        elementos = ["piedra", "papel", "tijera"]
        user = input("Escribe tu eleccion (piedra, papel o tijera): ")
        res.append(random.choice(elementos))
        res.append(user)

        if res[0] == res[1] or res[1] == res [0]:
            print("Maquina: ", res[0], "// Jugador: ", res[1])
            print("EMPATE!")
            print("MAQUINA: ", maquina, " // JUGADOR: ", usuario)

        elif res[0] == "piedra" and res[1] == "tijera" or res[0] == "papel" and res[1] == "piedra" or res[0] == "tijera" and res[1] == "papel":
            print("Maquina: ", res[0], "// Jugador: ", res[1]) 
            maquina+=1
            print("MAQUINA: ", maquina, " // JUGADOR: ", usuario)

        elif res[0] == "piedra" and res[1] == "papel" or res[0] == "papel" and res[1] == "tijera" or res[0] == "tijera" and res[1] == "piedra":
            print("Maquina: ", res[0], "// Jugador: ", res[1])
            usuario+=1
            print("MAQUINA: ", maquina, " // JUGADOR: ", usuario)

    if maquina > usuario:
        print("FIN: Gana la maquina")
    elif usuario > maquina: 
        print("FIN: Gana el jugador, Ganaste!")
    else:
        print("FIN: Empate")



juego()
