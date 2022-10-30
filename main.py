#pruebas
#Importamos directorios
import sys
sys.path.insert(0,"/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/aprendizaje_no_supervisado" )
sys.path.insert(0, "/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/generacion_de_datos")
sys.path.insert(0, "/Users/rauln/Documents/Desarrolo orientado a objetos/Albaricoques-cerezas-clustering/codigo-cap09/Visualizacion_3d_curvas_gaussianas")
#Importamos funciones
from aprendizaje_k_mean import 
from aprendizeje_no_supervisado import 
from clustering2 import stemming
from cerezas import lematizacion
from albaricoques import canalizacion
from clustering import Info_original


def iniciar():
    print("Iniciando...")

def iniciar():
    while True:

        print("========================")
        print("  Bienvenido al Albaricoques-Cerezas-Clustering  ")
        print("========================")
        print("[1] Ejecute el programa")
        print("[2] Ejecute alguna funcion en concreto")
        print("[3] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")

        if opcion == '1':
            print("DETERMINACION OPINIONES TWITTER")
            pruebas()
        if opcion == '2':
            while True:
                print("¿Qué opción quieres escoger?")
                print("[1] Informacion Transformacion")
                print("[2] Normalizacion")
                print("[3] Stopwords")
                print("[4] Stemming")
                print("[5] Lematizacion")
                print("[6] Canalizacion")
                print("[7] Volver al menu principal")
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
        if opcion == '3':
            print("Saliendo...")
            break
    


if __name__ == "__main__":
    iniciar()