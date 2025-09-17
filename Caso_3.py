#1.Ingresar números de tarjeta: (Registrar las tarjetas SUBE)
#Permite al usuario ingresar los números de identificación de las tarjetas SUBE.
#  Debe validarse que el número ingresado tenga un formato válido (e.g., 16 dígitos).
#2.Ingresar saldos correspondientes: (Asignar saldos iniciales a las tarjetas)
#Permite al usuario ingresar el saldo inicial para cada tarjeta SUBE. 
#3.Mostrar todas las tarjetas y saldos: (Listar todas las tarjetas registradas y sus saldos)
#4.Consultar saldo por número: (Verificar el saldo de una tarjeta específica)
#Permite al usuario ingresar un número de tarjeta SUBE y ver su saldo actual. 
#Si la tarjeta no está registrada, se debe mostrar un mensaje de error. 
#5.Listar saldos en negativo o cero: (Identificar tarjetas con saldo insuficiente)
#Muestra una lista de todos los números de tarjeta SUBE que tienen un saldo negativo o cero.
#6.Agregar tarjeta: (Sumar una nueva tarjeta al sistema)
#Permite al usuario agregar un nuevo número de tarjeta SUBE al sistema, incluyendo su saldo inicial.
#7.Ver saldos ≤ 0: (Mostrar las tarjetas con saldos negativos o cero)
#Muestra una lista de las tarjetas cuyo saldo es menor o igual a cero.
#8.Cargar/debitar saldo: (Aumentar o disminuir el saldo de una tarjeta)
#Permite al usuario cargar (agregar) o debitar (restar) saldo de una tarjeta SUBE. 
# Debe solicitarse el monto a cargar o debitar, y realizar las validaciones necesarias 
# (e.g., no permitir débitos que resulten en saldos menores a un valor mínimo).
#9.Ver todas: (Mostrar todas las tarjetas y saldos)
#Muestra una lista completa de todas las tarjetas registradas y sus saldos, similar a la opción 3.
#10.Salir: (Terminar el programa)

#Programa tarjeta SUBE
#Para la practica usaremos tarjetas de 4 digitos
print("Bienvenido al sistema de gestión de tarjetas SUBE")
tarjetas = []
saldos = []
opc=0
while opc !=9:
    print("\n Menu de opciones") 
    print("1. Ingresar tarjetas y sus respectivos saldos")
    print("2. Mostrar listado de tarjetas y sus saldos")
    print("3. Consultar saldo de una tarjeta")
    print("4. Lista de tarjetas con saldos insuficientes")
    print("5. Agregar una nueva tarjeta")
    print("6. Tarjetas con saldos <= 0")
    print("7. Cargar/Debitar de una tarjeta")
    print("8. Listado completo de tarjetas registradas con sus saldos")
    print("9. Salir del menu de opciones")

    opc=int(input("\n Ingresa una opcion: "))

    if opc==1:
        tarjetas.clear()
        saldos.clear()
        cantidad = int(input("\n Ingresa la cantidad de tarjetas que quieres cargar: "))
        for i in range(cantidad):
            tarjeta = input(f"\n Ingresá el numero de la tarjeta {i+1}: ")
            while tarjeta == "" or tarjeta in tarjetas or len(tarjeta)<4 :
                tarjeta = input("\n Numero de tarjeta invalido o duplicado . Ingresá otro: ")
            saldo = int(input(f"\n Ingrese saldo tarjeta {i+1}: "))
            tarjetas.append(tarjeta)
            saldos.append(saldo)

    elif opc==2:
        if len(tarjetas) == 0 or len(saldos) == 0:
            print("\n No hay datos cargados.")
        else:
            print("\n Listado Tarjetas y Saldos")
            print("")
        for i in range(cantidad):
            print(f"Tarjeta {i+1}: {tarjetas[i]} - Saldo: {saldos[i]}")

    elif opc==3:
        tarjeta=input("\n Ingrese numero de tarjeta a evaluar: ")
        while tarjeta == "" or len(tarjeta)<4 :
                tarjeta = input("\n Numero de tarjeta invalido o duplicado . Ingresá otro: ")
        if tarjeta in tarjetas:
            i = tarjetas.index(tarjeta)
            print("")
            print(f"Tarjeta evaluada: {tarjeta} - Saldo: {saldos[i]}")
        else:
            print("")
            print("\n Tarjeta no encontrada")

    elif opc==4:
        minimo= min(saldos)
        if minimo <= 0:
            print("\n Listado de Tarjetas con saldos insuficientes")
            for i in range(len(tarjetas)):
                if saldos[i]<=0:
                    print(f"Tarjeta {tarjetas[i]} - Saldo: {saldos[i]}")
        else:
            print("\n No hay tarjetas con saldos insuficientes")
    
    elif opc==5:
        tarjeta = input("\n Ingres3 el numero de la nueva tarjeta : ")
        while tarjeta == "" or tarjeta in tarjetas or len(tarjeta)<4 :
                tarjeta = input("\n Numero de tarjeta invalido o duplicado . Ingresá otro: ")
        saldo = int(input("\n Ingrese saldo tarjeta: "))
        tarjetas.append(tarjeta)
        saldos.append(saldo)

    elif opc==6:
        minimo= min(saldos)
        if minimo <= 0:
            print("\n Listado de Tarjetas con saldos <= 0")
            for i in range(len(tarjetas)):
                if saldos[i]<=0:
                    print(f"Tarjeta {tarjetas[i]} - Saldo: {saldos[i]}")
        else:
            print("\n No hay tarjetas con saldos <= 0")

    elif opc==7:
        tarjeta=input("\n Con que tarjeta vas a operar?: ")
        while tarjeta == "" and tarjeta in tarjetas and len(tarjeta)<4 :
                tarjeta = input("\n Numero de tarjeta invalido. Ingresá otro: ")
        accion=str(input("\n Operacion CARGAR (C) / DEBITAR (D): ")).upper
        if accion=="C":
            indice=tarjetas.index(tarjeta)
            carga=int(input("\n Cuanto quieres sumar a tu tarjeta?"))
            saldo_nuevo=saldos[indice]+carga
            saldo[indice]=saldo_nuevo
            print(f"\n Tarjeta {tarjeta} - Saldo Total: {saldo_nuevo}")
        elif accion=="D":
            indice=tarjetas.index(tarjeta)
            debito=int(input("\n Cuanto quieres resta a tu tarjeta?"))
            saldo_nuevo=saldos[indice]-debito
            saldo[indice]=saldo_nuevo
            print(f"\n Tarjeta {tarjeta} - Saldo Total: {saldo_nuevo}")
        else:
            print("\n La operacion igresada no es correcta")

       








print("\n Gracias por usar el sistema SUBE")