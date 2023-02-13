
#a- diferencia porcentual entre 
# este curso y el curso mínimo, 
# promedio y maximo
#

#b teniendo en cuenta que el crudo del promedio es 5hs
#y el crudo de este video fue 3.5hs
#que porcentaje de material vacío se reduce


este_curso = 1.5
este_curso_crudo = 3.5

minimo = 2.5
maximo = 7
promedio = 4
promedio_crudo = 5

diferencia_porcentualA = 100 - (este_curso/minimo)*100

print(f'la dif con el mas chico es{diferencia_porcentualA}' )

diferencia_porcentualB = 100 - (este_curso//maximo)*100
print(f'la dif con el mas mas grande es {diferencia_porcentualB}')


diferencia_porcentualC = 100 - (este_curso/promedio)*100
print(f'la dif con el mas promedio es {diferencia_porcentualC}')



promedio_crudo = 5 
este_curso_crudo = 3.5






diferencia_porcentualCrudos =(este_curso_crudo/promedio_crudo)*100

print(f'la dif con los crudos es {diferencia_porcentualCrudos}')
