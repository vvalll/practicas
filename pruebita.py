def mensaje(text):
    respuestas = {"computadora":"Con mi computadora puedo programar", 
                  "celular": "En mi celular puedo aprender usando la app de Platzi",
                    "cable": "¡Hay un cable en mi bota!" }
    if text in respuestas:
        print(respuestas[text])
    else:
        print(text, ": Articulo no encontrado")
   

com = "computadora"
ola = mensaje(com)