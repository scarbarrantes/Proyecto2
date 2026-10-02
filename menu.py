# menu.py

import os
from auditoria import leer_auditoria
from autenticacion import HashTable
from directorios import ArbolDirectorios
from red import NetworkGraph

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


def menu_directorios(arbol_directorios):
    while True:
        limpiar_pantalla()
        print("=== SISTEMA DE DIRECTORIOS ===\n")
        print("1. Crear carpeta")
        print("2. Crear archivo")
        print("3. Buscar elemento")
        print("4. Mostrar árbol")
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

        elif opcion == "0":
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()


def ejecutar_menu():
    arbol_directorios = ArbolDirectorios()
    tabla_usuarios = HashTable(capacidad=101)
    grafo_red = NetworkGraph()

    while True:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            menu_directorios(arbol_directorios)

        elif opcion == "2":
            limpiar_pantalla()
            print("=== AUTENTICACIÓN DE USUARIOS ===\n")
            print("Módulo de autenticación.")
            pausar()

        elif opcion == "3":
            limpiar_pantalla()
            print("=== ADMINISTRACIÓN DE RED ===\n")
            print("Módulo de administración de red.")
            pausar()

        elif opcion == "4":
            limpiar_pantalla()
            print("=== AUDITORÍA DEL SISTEMA ===\n")
            leer_auditoria()
            pausar()

        elif opcion == "0":
            limpiar_pantalla()
            print("Saliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()