import csv
import os

def inicializar_archivo(inventario):
    if not os.path.exists("inventario.csv"):
        with open("inventario.csv","w",newline="",encoding="utf-8") as archivo:
            escritor=csv.DictWriter(archivo,fieldnames=["herramientas","cantidad"])
            escritor.writeheader

def cargar_datos():
    try:
        lista=[]
        with open("inventario","r",encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo,fieldnames=["herramientas","cantidad"])
            next(lector)
            for fila in lector:
                try:
                    fila["cantidad"]=int(fila["cantidad"])
                    lista.append(fila)
                except ValueError:
                    print("\nDatos invalidos.")
        return lista
    except FileExistsError:
        print("\bCsv incorrecto")

def cargar_herramienta():
    pass
def mostrar_herramientas(lista):
    if not lista:
        print("\nNo hay herramientas cargadas")
    else:
        for herra in list:
            print(f"-{herra["herramuenta"].title()} | {herra["cantidad"]} unidades.")
            
def modificar_herramienta():
    pass
def eliminar_herramienta():
    pass
def list_sin_stock():
    pass
def vender_comprar():
    pass
def buscar_por_precio():
    pass
#Programa principal
def programa():
    inicializar_archivo()
    inventario=cargar_datos()
    while True:
        try:
            print('\n--- MENU PRINCIPAL ---')
            print('1- Cargar herramientas.')
            print('2- Mostrar herramientas.')
            print('3- Modificar herramienta.')
            print('4- Eliminar herramienta.')
            print('5- Lista sin stock.')
            print('6- Vender / Comprar')
            print('7- Buscar por precio(extra).')
            print('8- Salir.')

            opcion = int(input('Ingrese una opción: '))

            match opcion:
                case 1:
                    cargar_herramienta(inventario)
                case 2:
                    mostrar_herramientas()
                case 3:
                    modificar_herramienta(inventario)
                case 4:
                    eliminar_herramienta(inventario)
                case 5:
                    list_sin_stock()
                case 6:
                    vender_comprar(inventario)
                case 7:
                    buscar_por_precio()
                case 8:
                    print("\nGracias por utilizar nuestro programa.Hasta luego")
                    break
                case _:
                    print("\nOpcion incorrecta.Ingrese un numero del 1 al 8.")
        except ValueError:
            print("\nOpcion invalida.")

programa()            
