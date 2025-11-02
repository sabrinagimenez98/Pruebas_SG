import csv
import os

def inicializar_archivo():
    if not os.path.exists("inventario.csv"):
        with open("inventari.csv", "w", newline="utf-8") as archivo:
            escritor=csv.DictWriter(archivo,fieldnames=["instrumentos","unidades"])
            escritor.writeheader()

def cargar_datos():
    try:
        lista=[]
        with open("inventario.csv", "r", encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo,fieldnames=["instrumentos","unidades"])
            for fila in lector:
                try:
                    fila["unidades"]=int(fila["unidades"])
                    lista.append(fila)
                except ValueError:
                    print(f"Datos invalidos.")
        return lista
    except FileExistsError:
        print('Csv incorrecto.')

def actualizar_datos(lista):
    with open('inventario.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['instrumento','unidades'])
        escritor.writeheader()
        #writerow(dict)
        #writerows(list[dict])
        escritor.writerows(lista)

def mostrar_menu():
    print('--- MENU PRINCIPAL ---')
    print('1- Mostrar inventario.')
    print('2- Agregar instrumentos.')
    print('3- Editar unidades.')
    print('4- Eliminar instrumento.')
    print('5- Mostrar sin stock.')
    print('6- Vender / Comprar')
    print('7- Consultar stock.')
    print('8- Salir.')
    
def mostrar_inventario(lista):
    if not lista:
        print('No hay instrumentos disponibles.')
    else:
        for elem in lista:
            print(f'- {elem['instrumento'].capitalize()} - {elem['unidades']} unidades.')

def agregar_instrumentos(lista):
    try:
        cant_inst = int(input('Cuantos instrumentos quiere agregar? '))
        for i in range(cant_inst):
            nombre = input(f'Nombre del instrumento {i+1}: ').lower().strip()
            while True:
                cant = input('Cantidad de unidades: ')
                if cant.isdigit():
                    cant = int(cant)
                    break
            lista.append({'instrumento':nombre, 'unidades':cant})
        actualizar_datos(lista)
        return lista
    except ValueError:
        print('Debés ingresar un número entero.')

def editar_instrumento(inventario):
    instrumento = input('Ingrese el nombre del instrumento que quiere editar: ').lower().strip()
    for elem in inventario:
        if(instrumento == elem['instrumento']):
            while True:
                try:
                    unid = int(input('Ingrese las unidades del instrumento: '))
                    elem['unidades'] = unid
                    actualizar_datos(inventario)
                    return inventario
                except ValueError:
                    print('Ingrese un número entero.')

def eliminar_instrumento(inventario):
    lista_nva = []
    instrumento = input('Ingrese el nombre del instrumento que quiere eliminar: ').lower().strip()
    for elem in inventario:
        if(instrumento == elem['instrumento']):
            continue
        lista_nva.append(elem)
    actualizar_datos(lista_nva)
    return lista_nva

def mostrar_sin_stock(inventario):
    for elem in inventario:
        if(elem['unidades'] == 0):
            print(f'- {elem['instrumento']}')

def vender_comprar(inventario):
    inst = input('Que instrumento quiere vender o comprar? ').lower().strip()
    for elem in inventario:
        if(inst == elem['instrumento']):
            opcion_vc = input('Querés vender o comprar? (v/c): ').lower().strip()
            match opcion_vc:
                case 'v':
                    if(elem['unidades'] == 0):
                        print('No hay unidades disponibles')
                    else:
                        try:
                            cant = int(input('Cuantas unidades va a vender? '))
                            if(elem['unidades'] < cant):
                                print('No hay unidades disponibles.')
                            else:
                                elem['unidades'] -= cant
                                print('Unidades vendidas.')
                                actualizar_datos(inventario)
                                return inventario
                        except ValueError:
                            print('Las unidades son números enteros.')
                case 'c':
                    try:
                        cant = int(input('Cuantas unidades va a comprar? '))
                        elem['unidades'] += cant
                        print('Unidades agregadas.')
                        actualizar_datos(inventario)
                        return inventario
                    except ValueError:
                        print('Las unidades son números enteros.')
                case _:
                    print('Opcion incorrecta.')
                    return inventario

def consultar_stock(inventario):
    if not inventario:
        print('No hay instrumentos disponibles.')
    else:
        instrumento = input('Ingrese el nombre del instrumento que quiere consultar: ').lower().strip()
        for elem in inventario:
            if instrumento == elem['instrumento']:
                print(f'{elem['unidades']} unidades disponibles.')
            else:
                print('No existe ese instrumento.')

def programa_principal():
    inicializar_archivo()
    inventario = cargar_datos()
    while True:
        try:
            mostrar_menu()
            opcion = int(input('Ingrese una opción: '))
            
            match opcion:
                case 1:
                    mostrar_inventario(inventario)
                case 2:
                    inventario = agregar_instrumentos(inventario)
                case 3:
                    inventario = editar_instrumento(inventario)
                case 4:
                    inventario = eliminar_instrumento(inventario)
                case 5:
                    mostrar_sin_stock(inventario)
                case 6:
                    inventario = vender_comprar(inventario)
                case 7:
                    consultar_stock(inventario)
                case 8:
                    print('Hasta luego.')
                    break
        except ValueError:
            print('Ingreso incorrecto.')
            
if __name__ == '__main__':
    programa_principal()

