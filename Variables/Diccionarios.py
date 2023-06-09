diccionario ={
    "nombre": "Cristian",
    "apellido" : "Iglesias",
    "edad": "24"
}

claves = diccionario.keys()

for key in diccionario.items():
    print(key)

valor_de_elemento_por_clave = diccionario.get("nombre")

#diccionario.clear()
diccionario.pop("edad")
diccionario_iterable = diccionario.items()


print (diccionario_iterable)


