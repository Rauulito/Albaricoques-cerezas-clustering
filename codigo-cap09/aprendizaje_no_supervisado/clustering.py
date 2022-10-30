
#Guardar el modelo (eliminar marca de comentario # si es necesario)
#from joblib import dump
#dump(modelo,'modelos/kmean.joblib')

#--- Realización de las clasificaciones --
#CEREZA: 26,98 mm de diametro ,8,75 gramos
#ALBARICOQUE: 55,7  mm de diámetro , 102,16 gramos


import pandas as pnd
import matplotlib.pyplot as plt

#Carga de datos
frutas = pnd.read_csv("/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Albaricoques-cerezas-clustering/codigo-cap09/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)


#Aprendizaje con el algoritmo K-Mean
from sklearn.cluster import KMeans
modelo=KMeans(n_clusters=2)
modelo.fit(frutas)




cereza = [[26.98,8.75]]
numCluster = modelo.predict(cereza)
print("Número de clúster de las cerezas: "+ str(numCluster))


albaricoque = [[55.7,102.16]]
numCluster = modelo.predict(albaricoque)
print("Número de clúster de los albaricoques: " + str(numCluster))

#Instrucciones a adaptar en función de los números de clústeres
#determinados con anterioridad:

cereza = [[26.98,8.75]]
numCluster = modelo.predict(cereza)
if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza! ")


albaricoque = [[55.7,102.16]]
numCluster = modelo.predict(albaricoque)
if int(numCluster)==0:
    print("¡Es un albaricoque!")
else:
    print("¡Es una cereza!")


#---- Modelo de mezclas Gaussianas (GMM) -----------
from sklearn import mixture

#Determinación de los clústeres (encontrar 2)
gmm = mixture.GaussianMixture(n_components=2)

#Aprendizaje
gmm.fit(frutas)

#Clasificación
clusteres = gmm.predict(frutas)

#Visualización de los clústeres
plt.scatter(frutas.DIAMETRO, frutas.PESO, c=clusteres, s=40, cmap='viridis')
plt.xlabel("DIAMETRO")
plt.ylabel("PESO")
plt.show()
