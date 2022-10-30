import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
def dim_3():
    #necesario
    frutas = pnd.read_csv("/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/datas/frutas.csv", names=['DIAMETRO','PESO'], header=None)



    # Extraer x e y
    x = frutas.DIAMETRO
    y = frutas.PESO
    # Define los límites
    deltaX = (max(x) - min(x))/10
    deltaY = (max(y) - min(y))/10
    xmin = min(x) - deltaX
    xmax = max(x) + deltaX
    ymin = min(y) - deltaY
    ymax = max(y) + deltaY
    print(xmin, xmax, ymin, ymax)
    # Crear meshgrid
    xx, yy = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]

    posiciones = np.vstack([xx.ravel(), yy.ravel()])
    values = np.vstack([x, y])
    kernel = st.gaussian_kde(values)
    f = np.reshape(kernel(posiciones).T, xx.shape)

    from mpl_toolkits.mplot3d import axes3d, Axes3D
    fig = plt.figure(figsize=(13, 7))
    ax = plt.axes(projection='3d')
    surf = ax.plot_surface(xx, yy, f, rstride=1, cstride=1, cmap='coolwarm', edgecolor='none')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    fig.colorbar(surf, shrink=0.5, aspect=5) # añadir barra de color indicando el PDF
    ax.view_init(60, 35)
    plt.show()
