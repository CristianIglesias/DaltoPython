#los datos con set, no son modificables.
#creando conjunto con set

conjunto =set(["dato1","dato2"])

#metiendo un conjunto dentro de otro (?)
conjunto1=frozenset(["dato1","dato2"])
conjunto2= {conjunto1,"dato3"}

print(conjunto2)

#Teoría de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 ={1,5,3}

#verificando que sea subconjunto
resultado= conjunto2.issubset(conjunto1)
print(resultado)

resultado = conjunto2<=conjunto1

print(resultado)

#Verificando que sea superconjunto
resultado= conjunto2.issuperset(conjunto1)
print(resultado)

resultado = conjunto1>=conjunto2

print(resultado)

#verificar si no hay un numero en común - devolvería true

resultado=conjunto2.isdisjoint(conjunto1)


