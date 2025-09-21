#PROGRAMA PARA TALLER
#Ordenes de reparacion y tiempos estimados

ordenes=[]
tiempos=[]
opc=0

while opc==8:
    print("\nMENU DE OPCIONES")
    print("1.Ingresar ordenes.")
    print("2.Ingresar horas estimadas por orden.")
    print("3.Mostrar agenda del taller.")
    print("4.Consultar tiempo estimado por orden.")
    print("5.Listado de ordenes pendientes de diagnostico.")
    print("6.Agregar nueva orden.")
    print("7.Actualizar ordenes (Adelanto/Retraso).")
    print("8.Salir")

    opc=input("\nIngrese opcion:")
    while not opc.isdigit():
        opc=input("\nOpcion invalida.Ingrese una opcion del 1 al 8: ")
        continue
    opc=int(opc)
    match opc:
        case 1: #Ingresar ordenes
            ordenes.clear() #Limpia la lista de ordenes cada vez que se utiliza la opcion 1
            cantidad=input("\nCantidad de ordenes que desea cargar: ")

            while not cantidad.isdigit():
                cantidad=input("\nCantidad invalida.Ingrese un numero: ")
                continue
            cantidad=int(cantidad)

            for i in range(cantidad):
                orden_numerica=input("\nIngrese el numero de orden: ")
                while not orden_numerica.isdigit():
                    orden_numerica=input("\nNumero invalida.Ingrese una opcion del 0 al 100: ")
                    continue
                orden_numerica=int(orden_numerica.zfill(3))
                orden="ORD-"+orden_numerica
                print(orden)

        case 8: #Salir del menu
            print("\nHasta luego. Gracias por utilizar nuestro programa")
            break
        case _:
            print("\nOpcion invalida.")