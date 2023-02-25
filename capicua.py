def escapicua(numero):
    numero_Str= str(77)
    return numero_Str == numero_Str[::-1]

numero=77

if(escapicua(numero)):
    print(f"{numero} es capicua")
else:
    print(f"{numero} no es capicua")

def conversion(grados):
    return (grados-32)*5 /9

resultado = conversion(50)

caca =len("hola mundo")

print (caca)


def valoresunicos(lista):
    return set(lista)

resultado = valoresunicos([1,2,3,2,3,4,5])

print (resultado)