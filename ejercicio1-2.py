frase =input("decime una frase y te digo cuanto tardarías en hablarla: ")
palabras_separadas= frase.split(" ")
cantidad_palabras= len(palabras_separadas)

tiempo_Hablando= int(cantidad_palabras)/2

print(f'La Persona pasaría {tiempo_Hablando} para decir las {cantidad_palabras} palabras.')