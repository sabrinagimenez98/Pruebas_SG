# Programa de gestión de turnos por especialidad
especialidades = []
cupos = []

while True:
    print("\n📋 MENÚ DE OPCIONES")
    print("1. Ingresar lista de especialidades")
    print("2. Ingresar lista de cupos disponibles")
    print("3. Mostrar agenda")
    print("4. Consultar cupos de una especialidad")
    print("5. Listar especialidades sin cupo")
    print("6. Agregar especialidad")
    print("7. Ver sin cupo")
    print("8. Actualizar cupos (reservar/cancelar)")
    print("9. Ver agenda completa")
    print("0. Salir")

    opcion = input("👉 Elegí una opción: ")

    if opcion == "1":
        especialidades.clear()
        cant = int(input("¿Cuántas especialidades querés ingresar? "))
        for i in range(cant):
            nombre = input(f"Ingresá el nombre de la especialidad {i+1}: ").strip()
            while nombre == "" or nombre in especialidades:
                nombre = input("❌ Nombre inválido o duplicado. Ingresá otro: ").strip()
            especialidades.append(nombre)

    elif opcion == "2":
        cupos.clear()
        if len(especialidades) == 0:
            print("⚠️ Primero debés ingresar las especialidades.")
        else:
            for esp in especialidades:
                while True:
                    try:
                        cantidad = int(input(f"Ingresá cupos para {esp}: "))
                        if cantidad >= 0:
                            cupos.append(cantidad)
                            break
                        else:
                            print("❌ El cupo debe ser un número no negativo.")
                    except:
                        print("❌ Entrada inválida. Usá números enteros.")

    elif opcion == "3":
        if len(especialidades) == 0 or len(cupos) == 0:
            print("⚠️ No hay datos cargados.")
        else:
            print("\n📅 Agenda:")
            for i in range(len(especialidades)):
                print(f"{especialidades[i]}: {cupos[i]} cupos")

    elif opcion == "4":
        nombre = input("🔎 Ingresá el nombre de la especialidad: ").strip()
        if nombre in especialidades:
            i = especialidades.index(nombre)
            print(f"{nombre} tiene {cupos[i]} cupos disponibles.")
        else:
            print("❌ Especialidad no encontrada.")

    elif opcion == "5" or opcion == "7":
        print("\n🚫 Especialidades sin cupo:")
        hay_sin_cupo = False
        for i in range(len(cupos)):
            if cupos[i] == 0:
                print(f"{especialidades[i]}")
                hay_sin_cupo = True
        if not hay_sin_cupo:
            print("✅ Todas las especialidades tienen cupos.")

    elif opcion == "6":
        nombre = input("➕ Ingresá el nombre de la nueva especialidad: ").strip()
        if nombre == "" or nombre in especialidades:
            print("❌ Nombre inválido o ya existe.")
        else:
            while True:
                try:
                    cantidad = int(input(f"Ingresá cupos para {nombre}: "))
                    if cantidad >= 0:
                        especialidades.append(nombre)
                        cupos.append(cantidad)
                        print("✅ Especialidad agregada.")
                        break
                    else:
                        print("❌ El cupo debe ser no negativo.")
                except:
                    print("❌ Entrada inválida.")

    elif opcion == "8":
        nombre = input("🔄 Ingresá la especialidad a modificar: ").strip()
        if nombre in especialidades:
            i = especialidades.index(nombre)
            accion = input("¿Reservar (R) o Cancelar (C)? ").upper()
            if accion == "R":
                if cupos[i] > 0:
                    cupos[i] -= 1
                    print(f"✅ Turno reservado. Cupos restantes: {cupos[i]}")
                else:
                    print("❌ No hay cupos disponibles.")
            elif accion == "C":
                cupos[i] += 1
                print(f"✅ Turno cancelado. Cupos ahora: {cupos[i]}")
            else:
                print("❌ Acción inválida.")
        else:
            print("❌ Especialidad no encontrada.")

    elif opcion == "9":
        print("\n📋 Agenda completa:")
        for i in range(len(especialidades)):
            print(f"{especialidades[i]}: {cupos[i]} cupos disponibles")

    elif opcion == "0":
        print("👋 Programa finalizado.")
        break

    else:
        print("❌ Opción inválida. Intentá de nuevo.")
