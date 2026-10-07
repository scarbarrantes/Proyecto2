# menu.py

import os
from auditoria import leer_auditoria, registrar_auditoria
from autenticacion import (
    registrar_usuario,
    iniciar_sesion,
    cerrar_sesion,
    registrar_acceso_denegado,
    )
from red import NetworkGraph

# Sesión activa (None = nadie logueado)
usuario_actual = None
servidor_sesion = None

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_menu_principal():
    """Muestra las opciones principales disponibles en el sistema."""

    limpiar_pantalla()

    print("======================================")
    print("       NETWORK OS - MENÚ PRINCIPAL")
    print("======================================")
    print("1. Sistema de directorios")
    print("2. Autenticación de usuarios")
    print("3. Administración de red")
    print("4. Auditoría del sistema")
    print("0. Salir")
    print("======================================")


def pausar():
    """Espera al usuario antes de regresar al menú."""
    input("\nPresione Enter para volver al menú...")


def seleccionar_servidor(grafo_red):
    if not grafo_red.adj:
        print("No hay servidores disponibles en la red.")
        return None

    print(f"Servidores disponibles: {', '.join(grafo_red.adj)}")
    servidor = input("Seleccione un servidor: ").strip()
    if servidor not in grafo_red.recursos_servidor:
        print("El servidor seleccionado no existe.")
        return None
    return servidor


def menu_directorios(grafo_red):
    limpiar_pantalla()
    servidor = seleccionar_servidor(grafo_red)
    if servidor is None:
        pausar()
        return

    if usuario_actual is None or servidor_sesion != servidor:
        limpiar_pantalla()
        print(f"Debes iniciar sesión en el servidor '{servidor}' primero.")
        registrar_acceso_denegado("directorios")
        pausar()
        return

    arbol_directorios = grafo_red.recursos_servidor[servidor]["arbol_directorios"]
    while True:
        limpiar_pantalla()
        print("=== SISTEMA DE DIRECTORIOS ===\n")
        print("1. Crear carpeta")
        print("2. Crear archivo")
        print("3. Buscar elemento")
        print("4. Mostrar árbol")
        print("5. Eliminar elemento")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion in ("1", "2"):
            nombre = input("Nombre del elemento: ").strip()
            nombre_padre = input("Nombre de la carpeta padre (/ para raíz): ").strip()

            if nombre_padre == "/":
                padre = arbol_directorios.raiz
            else:
                limpiar_pantalla()
                padre = arbol_directorios.buscar_elemento(nombre_padre)

            limpiar_pantalla()
            if padre is None:
                print("La carpeta padre no existe.")
            elif not padre.es_carpeta:
                print("El elemento padre debe ser una carpeta.")
            else:
                es_carpeta = opcion == "1"
                elemento_creado = arbol_directorios.crear_elemento(
                    padre, nombre, es_carpeta=es_carpeta
                )
                if elemento_creado is not None:
                    tipo = "Carpeta" if es_carpeta else "Archivo"
                    print(f"{tipo} '{nombre}' creado correctamente.")
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            nombre = input("Nombre del elemento que desea buscar: ").strip()
            limpiar_pantalla()
            arbol_directorios.buscar_elemento(nombre)
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            arbol_directorios.mostrar_arbol()
            pausar()

        elif opcion == "5":
            nombre = input("Nombre del archivo o carpeta que desea eliminar: ").strip()
            limpiar_pantalla()
            if not nombre:
                print("El nombre del elemento no puede estar vacío.")
            else:
                arbol_directorios.eliminar_elemento(nombre)
            pausar()

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()


def menu_autenticacion(grafo_red):
    global usuario_actual
    global servidor_sesion

    limpiar_pantalla()
    servidor = seleccionar_servidor(grafo_red)
    if servidor is None:
        pausar()
        return

    tabla_usuarios = grafo_red.recursos_servidor[servidor]["tabla_usuarios"]

    while True:
        limpiar_pantalla()
        print("=== AUTENTICACIÓN DE USUARIOS ===\n")

        if usuario_actual:
            print(f"Sesión activa: {usuario_actual} en {servidor_sesion}\n")

        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Buscar usuario")
        print("4. Mostrar tabla Hash")
        print("5. Mostrar colisiones")
        print("6. Cerrar sesión")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            limpiar_pantalla()
            registrar_usuario(tabla_usuarios, username, password)
            pausar()

        elif opcion == "2":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            limpiar_pantalla()
            if iniciar_sesion(tabla_usuarios, username, password):
                usuario_actual = username
                servidor_sesion = servidor
            pausar()

        elif opcion == "3":
            username = input("Username: ").strip()
            limpiar_pantalla()
            usuario = tabla_usuarios.buscar_usuario(username)
            if usuario is not None:
                print(f"Usuario encontrado: {usuario}")
            else:
                print("El usuario no existe.")
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            tabla_usuarios.mostrar_tabla()
            pausar()

        elif opcion == "5":
            limpiar_pantalla()
            tabla_usuarios.mostrar_colisiones()
            pausar()

        elif opcion == "6":
            limpiar_pantalla()
            if usuario_actual and servidor_sesion == servidor:
                cerrar_sesion(usuario_actual)
                usuario_actual = None
                servidor_sesion = None
            elif usuario_actual:
                print(f"No hay sesión activa en el servidor '{servidor}'.")
            else:
                print("No hay sesión activa.")
            pausar()

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()

def menu_red(grafo_red):
    while True:
        sesion_valida = (
            usuario_actual is not None
            and servidor_sesion in grafo_red.recursos_servidor
            and grafo_red.recursos_servidor[servidor_sesion]["tabla_usuarios"]
            .buscar_usuario(usuario_actual) is not None
        )
        if grafo_red.adj and not sesion_valida:
            limpiar_pantalla()
            print("Debes iniciar sesión para administrar la red.")
            registrar_acceso_denegado("red")
            pausar()
            return

        limpiar_pantalla()
        print("=== ADMINISTRACIÓN DE RED ===\n")
        print("1. Agregar servidor")
        print("2. Agregar conexión")
        print("3. Eliminar conexión")
        print("4. Mostrar red")
        print("5. Calcular ruta óptima")
        print("6. Ping General")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            servidor = input("Nombre del servidor: ").strip()
            limpiar_pantalla()
            if not servidor:
                print("El nombre del servidor no puede estar vacío.")
            else:
                grafo_red.agregar_servidor(servidor)
            pausar()

        elif opcion == "2":
            origen = input("Servidor origen: ").strip()
            destino = input("Servidor destino: ").strip()
            latencia_ingresada = input("Latencia en milisegundos: ").strip()
            try:
                latencia = float(latencia_ingresada)
            except ValueError:
                limpiar_pantalla()
                print("La latencia debe ser un número.")
            else:
                limpiar_pantalla()
                grafo_red.agregar_conexion(origen, destino, latencia)
            pausar()

        elif opcion == "3":
            origen = input("Servidor origen: ").strip()
            destino = input("Servidor destino: ").strip()
            limpiar_pantalla()
            grafo_red.eliminar_conexion(origen, destino)
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            grafo_red.mostrar_red()
            pausar()

        elif opcion == "5":
            origen = input("Servidor origen: ").strip()
            destino = input("Servidor destino: ").strip()
            limpiar_pantalla()
            if not origen or not destino:
                print("El servidor origen y el destino no pueden estar vacíos.")
            else:
                ruta, latencia_total = grafo_red.dijkstra(origen, destino)
                if ruta:
                    print(f"Ruta óptima: {' -> '.join(ruta)}")
                    print(f"Latencia total: {latencia_total} ms")
            pausar()

        elif opcion == "6":
            limpiar_pantalla()
            grafo_red.diagnostico_ping_general()
            pausar()

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()


def menu_auditoria():
    while True:
        limpiar_pantalla()
        print("=== AUDITORÍA DEL SISTEMA ===\n")
        print("1. Consultar historial de auditoría")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            leer_auditoria()
            pausar()

        elif opcion == "0":
            break

        else:
            print("Opción inválida. Intente nuevamente.")
            pausar()


def ejecutar_menu():
    global usuario_actual
    global servidor_sesion

    grafo_red = NetworkGraph()

    while True:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            if usuario_actual is None:
                limpiar_pantalla()
                print("Debes iniciar sesión primero.")
                registrar_acceso_denegado("directorios")
                pausar()
            else:
                menu_directorios(grafo_red)

        elif opcion == "2":
            menu_autenticacion(grafo_red)

        elif opcion == "3":
            if usuario_actual is None and grafo_red.adj:
                limpiar_pantalla()
                print("Debes iniciar sesión primero.")
                registrar_acceso_denegado("red")
                pausar()
            else:
                menu_red(grafo_red)

        elif opcion == "4":
            menu_auditoria()

        elif opcion == "0":
            limpiar_pantalla()
            if usuario_actual:
                cerrar_sesion(usuario_actual)
                usuario_actual = None
                servidor_sesion = None
            print("Saliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()