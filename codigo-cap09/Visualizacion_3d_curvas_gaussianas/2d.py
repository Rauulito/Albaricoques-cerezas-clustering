import pandas as pnd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
def dim_2():
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

    fig = plt.figure(figsize=(8,8))
    ax = fig.gca()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    cfset = ax.contourf(xx, yy, f, cmap='coolwarm')
    ax.imshow(np.rot90(f), cmap='coolwarm', extent=[xmin, xmax, ymin, ymax])
    cset = ax.contour(xx, yy, f, colors='k')
    ax.clabel(cset, inline=1, fontsize=10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()
