frase =input("decime una frase y te digo cuanto tardarías en hablarla: ")
palabras_separadas= frase.split(" ")
cantidad_palabras= len(palabras_separadas)

tiempo_Hablando= float(cantidad_palabras)/2

print(f'La Persona pasaría {tiempo_Hablando} para decir las {cantidad_palabras} palabras.')
print(f'Dalto pasaría {tiempo_Hablando*0.7} para decir todo eso.')


if(tiempo_Hablando>60):
    print('pará flaco, tampoco me escribas un testamento.')