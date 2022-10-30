import pandas as pnd
import matplotlib.pyplot as plt


#Caraga de datos
frutas = pnd.read_csv("/Users/Lorenzo/Documents/programacion/2.Desarrollo_OO/Albaricoques-cerezas-clustering/codigo-cap09/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)

#Visualización gráfica de los datos
frutas.plot.scatter(x="DIAMETRO",y="PESO")
plt.show()
