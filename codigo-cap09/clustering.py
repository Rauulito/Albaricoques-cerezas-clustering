#Importaciones necesarias
import cerezas
import albaricoques
import random
import pandas as pnd


#Constitución de las observaciones
frutas = cerezas+albaricoques
print(frutas)

#Mezcla de las observaciones
random.shuffle(frutas)

#Guardado de las observaciones en un archivo
dataFrame = pnd.DataFrame(frutas)
dataFrame.to_csv("datas/frutas.csv", index=False,header=False)
print()