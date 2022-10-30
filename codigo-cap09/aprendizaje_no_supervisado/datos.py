import pandas as pnd
import matplotlib.pyplot as plt


#Caraga de datos
frutas = pnd.read_csv("/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)

#Visualización gráfica de los datos
frutas.plot.scatter(x="DIAMETRO",y="PESO")
plt.show()
