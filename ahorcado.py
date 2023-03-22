import random

palabras = ["abrigo", "clavo", "calvo", "mujer", "mujercitas", "adulto", "adultez", "comer", "cochera", "negro", 
"hermosa", "agujero", "almuerzo", "amor", "besar", "bota", "cabeza", "coneja", "cangrejo", "denso", "decimal", "drena",
"extra", "educar", "facil", "feo", "foca", "gato", "goma", "gratis", "hilo", "huida", "iglu", "iman", "jamon",
"jugar", "jugo", "kilo", "lombriz", "leon", "laton", "mona", "marioneta", "magnitud", "necio", "nutria", "normal", "osa", "ostra", 
"oscar", "pesa", "peso", "persona", "queso", "cuestion", "quizas", "raton", "roma", "rosa", "sal", "sonrei", "sentar", "tomar",
"tiza", "canguro", "uva", "ula", "beso", "vaso", "amigo", "yeso", "bota", "zona", "futbol", "huevo", "carne"]

print("Hola, vamos a jugar a `ahorcados`, por lo que el programa va a elegir una palabra al azar y tu tienes 14 oportunidades para adivinar las letras de la palabra... Empecemos!!")

palabraA = random.choice(palabras)
#print(palabraA)
print("la palabra tiene", palabraA.__len__(),"letras")

for i in range(0,15):
    respuesta = input("Escribe una letra: ")
    if respuesta in palabraA:
        print("Bien, si esta esa letra en el lugar: ", palabraA.index(respuesta)+1)
    else:
        print("Mal, no esta esa letra")

resultado = print("Ahora, vas a decir cual es la palabra, tienes una oportunidad...")
resultado = input('La palabra es: ')
if resultado == palabraA:
    print("Correcto esa es la palabra, Ganaste!!")
else: 
    print('Perdiste...., la palabra era', palabraA, 'Fin del juego.')

        




