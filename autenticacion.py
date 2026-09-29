# autenticacion.py
from auditoria import registrar_auditoria

class HashTable:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)] # Encadenamiento para colisiones
        self.elementos = 0

    def _funcion_hash(self, username):
        """Función hash propia: suma el valor ASCII de cada caracter módulo capacidad."""
        suma_ascii = sum(ord(char) for char in username)
        return suma_ascii % self.capacidad

    def insertar(self, username, password):
        indice = self._funcion_hash(username)
        # Verificar si el usuario ya existe para actualizarlo
        for par in self.tabla[indice]:
            if par[0] == username:
                par[1] = password
                registrar_auditoria(f"Actualización de credenciales para el usuario: {username}")
                return
        
        self.tabla[indice].append([username, password])
        self.elementos += 1
        registrar_auditoria(f"Usuario registrado exitosamente: {username}")

    def autenticar(self, username, password):
        """Busca el usuario en O(1) promedio y valida la contraseña."""
        indice = self._funcion_hash(username)
        for par in self.tabla[indice]:
            if par[0] == username:
                if par[1] == password:
                    registrar_auditoria(f"Inicio de sesión exitoso: {username}")
                    return True
                else:
                    registrar_auditoria(f"Fallo de inicio de sesión (Contraseña incorrecta): {username}")
                    return False
        registrar_auditoria(f"Fallo de inicio de sesión (Usuario no encontrado): {username}")
        return False


class ArbolDirectorios:
    def __init__(self):
        # 1. Creación del nodo raíz '/' que representa el directorio principal
        self.raiz = NodoArchivo("/", es_carpeta=True)
        registrar_auditoria("Sistema de directorios inicializado con nodo raíz '/'")
        print("Árbol de directorios inicializado. Raíz: '/'")

    def crear_elemento(self, padre, nombre, es_carpeta=True):
        """
        Crea un nuevo nodo (carpeta o archivo) y lo anexa al nodo padre.
        Garantiza la relación padre/hijo del sistema de archivos.
        """
        nuevo_nodo = NodoArchivo(nombre, es_carpeta)
        padre.agregar_hijo(nuevo_nodo)
        return nuevo_nodo