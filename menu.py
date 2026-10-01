# menu.py

import os
from auditoria import registrar_auditoria, leer_auditoria
from autenticacion import HashTable, registrar_usuario, iniciar_sesion

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

def pedir_credenciales():
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    return username, password


def submenu_autenticacion(tabla):
    while True:
        limpiar_pantalla()
        print("=== AUTENTICACIÓN DE USUARIOS ===\n")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Mostrar tabla hash (debug)")
        print("0. Volver")

        op = input("\nSeleccione una opción: ").strip()

        if op == "1":
            print("\n--- REGISTRO ---")
            username, password = pedir_credenciales()
            registrar_usuario(tabla, username, password)
            pausar()
        elif op == "2":
            print("\n--- INICIO DE SESIÓN ---")
            username, password = pedir_credenciales()
            iniciar_sesion(tabla, username, password)
            pausar()
        elif op == "3":
            limpiar_pantalla()
            tabla.mostrar_tabla()
            pausar()
        elif op == "0":
            break
        else:
            print("\nOpción inválida.")
            pausar()
            
def ejecutar_menu():
    tabla_usuarios = HashTable(capacidad=101)   # ← AGREGAS ESTA LÍNEA
    while True:
        ...
        
    while True:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("=== SISTEMA DE DIRECTORIOS ===\n")
            print("Módulo de directorios.")
            pausar()

        elif opcion == "2":
         submenu_autenticacion(tabla_usuarios)

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