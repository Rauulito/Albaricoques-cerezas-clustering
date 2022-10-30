#---- IMPORTAR MÓDULOS --
import random
import pandas as pnd

#---- CARACTERÍSTICAS------
def cerezas():
    #CEREZAS
    caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]

    #GENERACION DE LOS DATOS
    # [DIAMETRO, PESO]
    cantidadObservaciones = 200

    #Generación de las cerezas
    cerezas = []
    random.seed()
    for iteration in range(cantidadObservaciones):
        #elección al azar de una característica
        cereza = random.choice(caracteristicasCerezas)
        #Generación de un diámetro
        diametro = round(random.uniform(cereza[0], cereza[1]),2)
        #Generación de un peso
        peso = round(random.uniform(cereza[2], cereza[3]),2)
        print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))
        cerezas.append([diametro,peso])
