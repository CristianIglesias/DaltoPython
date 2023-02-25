#import pygame
#Generala? 
import random
#formato con claves: valores? dado1
#funcion generar random rapido
def numeroRandom():
    return random.randint(1,6)

def mostrarDados(dados):
    print(f'Tus dados dieron los siguientes resultados: {dados}')


#Paradigma orientado a objetos

class Dado():
    def __init__(self):
        self.id =0
        self.valor=0
        self.queda=True

    def __init__(self,id):
        self.id=id
        self.valor=numeroRandom()
        self.queda=True


#se instancian los dados- hay que cargarlos con nros aleatorios
dados_Dict = {
    "dado1":"0",
    "dado2":"0",
    "dado3":"0",
    "dado4":"0",
    "dado5":"0",
    "dado6":"0" }

dadito1=Dado(1)
dadito2=Dado(2)
dadito3=Dado(3)
dadito4=Dado(4)
dadito6=Dado(5)
dadito5=Dado(6)

#se cargan los dados con valores random entre 1 y 6.
for i in dados_Dict:
    dados_Dict[i] = numeroRandom()

mostrarDados(dados_Dict)

dados_a_rerollear = 5
#while dados_a_rerollear!=0:
    # dados_a_rerollear= int(input("Cuantos dados querés cambiar campeon: "))

#for i in dados:
#    if(i<1):
#        dados[i] = numeroRandom()
#mostrarDados()
    

    
    
    
    
    
    
    
    
        
    #input("que dados querés cambiar rey? ")
















#cant_Dados=6
#while(cant_Dados!=0):
#    cant_Dados= input("decime cuantos dados tirás rey: ")
#
#    if(cant_Dados>'6'):
#        print("dale amigo, maximo 6")


