#Importaciones necesarias
import cerezas
import albaricoques
import random
import pandas as pnd

def clustering():
    #Constitución de las observaciones
    frutas = cerezas.cerezas+albaricoques.albaricoques #Estamos cogiendo las listas de cerezas y albaricoques y las unimos en una sola lista
    print(frutas)

    #Mezcla de las observaciones
    random.shuffle(frutas)

    #Guardado de las observaciones en un archivo
    dataFrame = pnd.DataFrame(frutas)
    dataFrame.to_csv("datas/frutas.csv", index=False,header=False)
