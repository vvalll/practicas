import random 
'''Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */'''

numeros = [0,1,2,3,4,5,6,7,8,9]

simbolos = ["|", "°", "¬", "!", "#", "$", "%", "&", "/", "(", ")", "=", "?", "'", "\\", "¿", "¡", "<", ">", "@", ",", ";", ".", ":", "-" , "_", "´", "¨", "+", "*", "~", "{", "}", "[", "]", "^","`"]

abc = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

abcM = "".join(abc)
mayusculas = abcM.upper()
abecedario_mayuscula = list(mayusculas)

#print(abecedario_mayuscula)


print("----------------------------------------------------------------------------------")

def password():
    passwordi = []
    for x in range(0, 4):
        opciones = [abecedario_mayuscula, numeros, abc,simbolos]
        random.shuffle(opciones)
        #print(opciones)

        passwordi.append(random.choice(opciones[0]))
        passwordi.append(random.choice(opciones[1]))
        passwordi.append(random.choice(opciones[2]))
        passwordi.append(random.choice(opciones[3]))
        password = "".join(map(str, passwordi))
    print(password)

password()
