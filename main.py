#pruebas
#Importamos directorios
import sys
sys.path.insert(0,"/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/aprendizaje_no_supervisado" )
sys.path.insert(0, "/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/generacion_de_datos")
sys.path.insert(0, "/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/Visualizacion_3d_curvas_gaussianas")
#Importamos funciones
from aprendizaje_k_mean import
from aprendizeje_no_supervisado import
from clustering2 import
from cerezas import
from albaricoques import
from clustering import


def iniciar():
    print("Iniciando...")

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al Albaricoques-Cerezas-Clustering  ")
        print("========================")
        print("[1] Escoga la carpeta y con ello la funcion de ella que quiere escoger")
        print("[2] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")

        if opcion == '1':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] Informacion Transformacion")
                print("[2] Normalizacion")
                print("[3] Stopwords")
                opcion2 = input("> ")
                if opcion2 == '1':
                    Info_original()
                elif opcion2 == '2':
                    normalizacion2()
                elif opcion2 == '3':
                    Stop_words()
                elif opcion2 == '4':
                    stemming()
                elif opcion2 == '5':
                    lematizacion()
                elif opcion2 == '6':
                    canalizacion()
                elif opcion2 == '7':
                    print("Volviendo...")
                    break
        if opcion == '2':
            print("Saliendo...")
            break
    


if __name__ == "__main__":
    iniciar()