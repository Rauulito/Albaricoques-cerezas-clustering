#---- IMPORTAR MÓDULOS --
import random
import pandas as pnd

#---- CARACTERÍSTICAS------

#ALBARICOQUES: ATENCIÓN DOS CASOS DE PRUEBAS EN FUNCIÓN DEL AVANCE DE SU LECTURA
def albaricoques():
    #Caso 1:
    caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

    #Caso 2:
    #caracteristicasAlbaricoques = [[35,39,27],[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

    #GENERACION DE LOS DATOS
    # [DIAMETRO, PESO]
    cantidadObservaciones = 200
    #Generación de los albaricoques
    albaricoques = []
    random.seed()
    for iteration in range(cantidadObservaciones):
        #elección al azar de una característica
        albaricoque = random.choice(caracteristicasAlbaricoques)
        #Generación de un diámetro
        diametro = round(random.uniform(albaricoque[0], albaricoque[1]),2)
        #Generación de un peso
        limiteMinPeso = albaricoque[2] / 1.10
        limiteMaxPeso = albaricoque[2] * 1.10
        peso = round(random.uniform(limiteMinPeso, limiteMaxPeso),2)
        print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))
        albaricoques.append([diametro,peso])