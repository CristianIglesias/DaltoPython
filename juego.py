
#import pygame
#Generala? 
import random

#cant_Dados=6
dados= list([0,0,0,0,0,0])
#while(cant_Dados!=0):
#    cant_Dados= input("decime cuantos dados tirás rey: ")
#
#    if(cant_Dados>'6'):
#        print("dale amigo, maximo 6")

for i in dados:
    dados[i] =  random.randint(1,6)
    

print(dados)







