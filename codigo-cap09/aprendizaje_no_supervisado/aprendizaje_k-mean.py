
import pandas as pnd
import matplotlib.pyplot as plt


#Caraga de datos
frutas = pnd.read_csv("/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Albaricoques-cerezas-clustering/codigo-cap09/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)


#Aprendizaje con el algoritmo K-Mean
from sklearn.cluster import KMeans
modelo=KMeans(n_clusters=2)
modelo.fit(frutas)

#Predicciones
predicciones_kmeans = modelo.predict(frutas)

#Visualización de la clusterización
plt.scatter(frutas.DIAMETRO, frutas.PESO, c=predicciones_kmeans, s=50, cmap='viridis')
plt.xlabel("DIAMETRO")
plt.ylabel("PESO")

#Visualización de los centroides
centers = modelo.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()