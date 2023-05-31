animales=["gato","perro","loro","cocodrilo"]

numeros=[10,62,12,72]

#for clasico. 
for i in range(5,20):
    print(i)
else:print('chupala gato esto se ejecuta a la ultima vuelta siempre')


#recorriendo animales.
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')
#recorriendo numeritos y multiplicanding
for numero in numeros:
    resultado= numero*10
    print(resultado)

#Recorriendo listas con mismos tamaños a la vez.
for numero, animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')


#transforma los valores individuales en
#tuplas, (indice, valor)
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    
    print(num)
    print(num[0])
    print(num[1])
    if(num[0]>2):
        print(f'este valor está despues del segundo de la fila')
    
diccionario = {
    "nombre": "Cristian",
    "apellido": "Iglesias",
    "subs": 10000
}

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} y el valor es {value}')

    