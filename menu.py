# menu.py

import os


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


def ejecutar_menu():
    """Controla la ejecución del menú principal."""

    while True:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("=== SISTEMA DE DIRECTORIOS ===\n")
            print("Módulo de directorios.")
            pausar()

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
            print("Módulo de auditoría.")
            pausar()

        elif opcion == "0":
            limpiar_pantalla()
            print("Saliendo del sistema...")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausar()