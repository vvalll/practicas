import random
#Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
#El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#La función recibe un listado que contiene pares, representando cada jugada.
#El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#"✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 
elementos = ["tijeras", "papel", "piedra", "lagarto", "spock"]

juego1 = []

juego1.append(random.choices(elementos, k = 2))
juego1.append(random.choices(elementos, k = 2))
juego1.append(random.choices(elementos, k = 2))

print(juego1)
#print(juego1[0][1])

if juego1[0][0] == "tijeras" and juego1[0][1] == "tijeras":
    print("empate")

elif juego1[0][0] == "tijeras" and juego1[0][1] == "papel":
    print("Gana el jugador 1")

elif juego1[0][0] == "tijeras" and juego1[0][1] == "piedra":
    print("Gana el jugador 2")

elif juego1[0][0] == "tijeras" and juego1[0][1] == "lagarto":
    print("Gana el jugador 1")

elif juego1[0][0] == "tijeras" and juego1[0][1] == "spock":
    print("Gana el jugador 2")

elif juego1[0][0] == "papel" and juego1[0][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[0][0] == "papel" and juego1[0][1] == "papel":
    print("empate")

elif juego1[0][0] == "papel" and juego1[0][1] == "piedra":
    print("Gana el jugador 1")

elif juego1[0][0] == "papel" and juego1[0][1] == "lagarto":
    print("Gana el jugador 2")

elif juego1[0][0] == "papel" and juego1[0][1] == "spock":
    print("Gana el jugador 1")

elif juego1[0][0] == "piedra" and juego1[0][1] == "tijeras":
    print("Gana el jugador 1")

elif juego1[0][0] == "piedra" and juego1[0][1] == "piedra":
    print("empate")

elif juego1[0][0] == "piedra" and juego1[0][1] == "lagarto":
    print("Gana el jugador 1")

elif juego1[0][0] == "piedra" and juego1[0][1] == "spock":
    print("Gana el jugador 2")

elif juego1[0][0] == "piedra" and juego1[0][1] == "papel":
    print("Gana el jugador 2")

elif juego1[0][0] == "lagarto" and juego1[0][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[0][0] == "lagarto" and juego1[0][1] == "papel":
    print("Gana el jugador 1")

elif juego1[0][0] == "lagarto" and juego1[0][1] == "piedra":
    print("Gana el jugador 2")

elif juego1[0][0] == "lagarto" and juego1[0][1] == "lagarto":
    print("empate")

elif juego1[0][0] == "lagarto" and juego1[0][1] == "spock":
    print("Gana el jugador 1")

elif juego1[0][0] == "lagarto" and juego1[0][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[0][0] == "spock" and juego1[0][1] == "tijeras":
    print("Gana el jugador 1")

elif juego1[0][0] == "spock" and juego1[0][1] == "spock":
    print("empate")

elif juego1[0][0] == "spock" and juego1[0][1] == "papel":
    print("Gana el jugador 2")

elif juego1[0][0] == "spock" and juego1[0][1] == "piedra":
    print("Gana el jugador 1")

elif juego1[0][0] == "spock" and juego1[0][1] == "lagarto":
    print("Gana el jugador 2")
#--
if juego1[1][0] == "tijeras" and juego1[1][1] == "tijeras":
    print("empate")

elif juego1[1][0] == "tijeras" and juego1[1][1] == "papel":
    print("Gana el jugador 1")

elif juego1[1][0] == "tijeras" and juego1[1][1] == "piedra":
    print("Gana el jugador 2")

elif juego1[1][0] == "tijeras" and juego1[1][1] == "lagarto":
    print("Gana el jugador 1")

elif juego1[1][0] == "tijeras" and juego1[1][1] == "spock":
    print("Gana el jugador 2")

elif juego1[1][0] == "papel" and juego1[1][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[1][0] == "papel" and juego1[1][1] == "papel":
    print("empate")

elif juego1[1][0] == "papel" and juego1[1][1] == "piedra":
    print("Gana el jugador 1")

elif juego1[1][0] == "papel" and juego1[1][1] == "lagarto":
    print("Gana el jugador 2")

elif juego1[1][0] == "papel" and juego1[1][1] == "spock":
    print("Gana el jugador 1")

elif juego1[1][0] == "piedra" and juego1[1][1] == "tijeras":
    print("Gana el jugador 1")

elif juego1[1][0] == "piedra" and juego1[1][1] == "piedra":
    print("empate")

elif juego1[1][0] == "piedra" and juego1[1][1] == "lagarto":
    print("Gana el jugador 1")

elif juego1[1][0] == "piedra" and juego1[1][1] == "spock":
    print("Gana el jugador 2")

elif juego1[1][0] == "piedra" and juego1[1][1] == "papel":
    print("Gana el jugador 2")

elif juego1[1][0] == "lagarto" and juego1[1][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[1][0] == "lagarto" and juego1[1][1] == "papel":
    print("Gana el jugador 1")

elif juego1[1][0] == "lagarto" and juego1[1][1] == "piedra":
    print("Gana el jugador 2")

elif juego1[1][0] == "lagarto" and juego1[1][1] == "lagarto":
    print("empate")

elif juego1[1][0] == "lagarto" and juego1[1][1] == "spock":
    print("Gana el jugador 1")

elif juego1[1][0] == "lagarto" and juego1[1][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[1][0] == "spock" and juego1[1][1] == "tijeras":
    print("Gana el jugador 1")

elif juego1[1][0] == "spock" and juego1[1][1] == "spock":
    print("empate")

elif juego1[1][0] == "spock" and juego1[1][1] == "papel":
    print("Gana el jugador 2")

elif juego1[1][0] == "spock" and juego1[1][1] == "piedra":
    print("Gana el jugador 1")

elif juego1[1][0] == "spock" and juego1[1][1] == "lagarto":
    print("Gana el jugador 2")
#---
if juego1[2][0] == "tijeras" and juego1[2][1] == "tijeras":
    print("empate")

elif juego1[2][0] == "tijeras" and juego1[2][1] == "papel":
    print("Gana el jugador 1")

elif juego1[2][0] == "tijeras" and juego1[2][1] == "piedra":
    print("Gana el jugador 2")

elif juego1[2][0] == "tijeras" and juego1[2][1] == "lagarto":
    print("Gana el jugador 1")

elif juego1[2][0] == "tijeras" and juego1[2][1] == "spock":
    print("Gana el jugador 2")

elif juego1[2][0] == "papel" and juego1[2][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[2][0] == "papel" and juego1[2][1] == "papel":
    print("empate")

elif juego1[2][0] == "papel" and juego1[2][1] == "piedra":
    print("Gana el jugador 1")

elif juego1[2][0] == "papel" and juego1[2][1] == "lagarto":
    print("Gana el jugador 2")

elif juego1[2][0] == "papel" and juego1[2][1] == "spock":
    print("Gana el jugador 1")

elif juego1[2][0] == "piedra" and juego1[2][1] == "tijeras":
    print("Gana el jugador 1")

elif juego1[2][0] == "piedra" and juego1[2][1] == "piedra":
    print("empate")

elif juego1[2][0] == "piedra" and juego1[2][1] == "lagarto":
    print("Gana el jugador 1")

elif juego1[2][0] == "piedra" and juego1[2][1] == "spock":
    print("Gana el jugador 2")

elif juego1[2][0] == "piedra" and juego1[2][1] == "papel":
    print("Gana el jugador 2")

elif juego1[2][0] == "lagarto" and juego1[2][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[2][0] == "lagarto" and juego1[2][1] == "papel":
    print("Gana el jugador 1")

elif juego1[2][0] == "lagarto" and juego1[2][1] == "piedra":
    print("Gana el jugador 2")

elif juego1[2][0] == "lagarto" and juego1[2][1] == "lagarto":
    print("empate")

elif juego1[2][0] == "lagarto" and juego1[2][1] == "spock":
    print("Gana el jugador 1")

elif juego1[2][0] == "lagarto" and juego1[2][1] == "tijeras":
    print("Gana el jugador 2")

elif juego1[2][0] == "spock" and juego1[2][1] == "tijeras":
    print("Gana el jugador 1")

elif juego1[2][0] == "spock" and juego1[2][1] == "spock":
    print("empate")

elif juego1[2][0] == "spock" and juego1[2][1] == "papel":
    print("Gana el jugador 2")

elif juego1[2][0] == "spock" and juego1[2][1] == "piedra":
    print("Gana el jugador 1")

elif juego1[2][0] == "spock" and juego1[2][1] == "lagarto":
    print("Gana el jugador 2")