# directorios.py
from auditoria import registrar_auditoria

class NodoArchivo:
    def __init__(self, nombre, es_carpeta=True):
        self.nombre = nombre
        self.es_carpeta = es_carpeta
        self.hijos = []  # Lista de subcarpetas o archivos

    def agregar_hijo(self, nodo):
        if self.es_carpeta:
            self.hijos.append(nodo)
            registrar_auditoria(f"Creado '{nodo.nombre}' dentro de '{self.nombre}'")
        else:
            print("Error: No se pueden agregar elementos dentro de un archivo.")

    def mostrar(self, nivel=0):
        """Muestra el árbol en consola con indentación adecuada."""
        indent = "    " * nivel
        tipo = "[Carpeta]" if self.es_carpeta else "[Archivo]"
        print(f"{indent}- {tipo} {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)

    def buscar(self, nombre):
        """Búsqueda recursiva de un archivo o carpeta específica."""
        if self.nombre == nombre:
            return self
        if self.es_carpeta:
            for hijo in self.hijos:
                resultado = hijo.buscar(nombre)
                if resultado:
                    return resultado
        return None

    def eliminar_hijo(self, nombre):
        """Eliminación en cascada garantizando liberación de memoria desde las hojas."""
        for i, hijo in enumerate(self.hijos):
            if hijo.nombre == nombre:
                if hijo.es_carpeta:
                    # Limpiar recursivamente los hijos de esta subcarpeta primero
                    hijo._destruir_recursivo()
                
                # Eliminar la referencia de la memoria eliminando el objeto
                eliminado = self.hijos.pop(i)
                registrar_auditoria(f"Eliminación en cascada completada para: {eliminado.nombre}")
                print(f"-> Elemento '{eliminado.nombre}' y su contenido eliminados correctamente.")
                return True
            
            # Si no es el hijo directo, buscar en sus subcarpetas
            if hijo.es_carpeta and hijo.eliminar_hijo(nombre):
                return True
        return False

    def _destruir_recursivo(self):
        """Recorre el subárbol liberando referencias de abajo hacia arriba."""
        for hijo in self.hijos:
            if hijo.es_carpeta:
                hijo._destruir_recursivo()
        self.hijos.clear()


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
        if not nombre or not nombre.strip():
            print("Error: El nombre no puede estar vacío ni contener solo espacios.")
            return None

        if any(hijo.nombre == nombre for hijo in padre.hijos):
            print(f"Error: Ya existe un elemento llamado '{nombre}' en esta carpeta.")
            return None

        nuevo_nodo = NodoArchivo(nombre, es_carpeta)
        padre.agregar_hijo(nuevo_nodo)
        return nuevo_nodo
    
    
    def mostrar_arbol(self):
        """
        Muestra todo el árbol de directorios desde la raíz.
        Cumple con: visualización indentada del árbol (Round 2).
        """
        print("\n--- ESTRUCTURA DE DIRECTORIOS ---")
        self.raiz.mostrar(nivel=0)  # Llama al método recursivo del NodoArchivo
        print("---------------------------------")
        registrar_auditoria("Visualización jerárquica del árbol de directorios solicitada.")
        
    def buscar_elemento(self, nombre):
        """
        Busca un elemento en todo el árbol de forma recursiva.
        Cumple con: búsqueda recursiva de archivos y carpetas (Round 2).
        """
        print(f"\nIniciando búsqueda de: '{nombre}'...")
        resultado = self.raiz.buscar(nombre)  # Llama al método recursivo del NodoArchivo
        
        if resultado:
            tipo = "Carpeta" if resultado.es_carpeta else "Archivo"
            print(f"✅ Elemento '{nombre}' encontrado. Tipo: {tipo}")
            registrar_auditoria(f"Búsqueda exitosa en directorios: {nombre} ({tipo})")
            return resultado
        else:
            print(f"❌ Elemento '{nombre}' no existe en el sistema.")
            registrar_auditoria(f"Búsqueda fallida en directorios: {nombre} no encontrado")
            return None    
        
    def eliminar_elemento(self, nombre):
        """
        Elimina un elemento del árbol en cascada, gestionando la memoria.
        Cumple con: Eliminación recursiva en cascada.
        """
        if nombre == "/":
            print("Error: No se permite eliminar el directorio raíz '/' del sistema.")
            registrar_auditoria("Intento fallido de eliminar el directorio raíz '/'")
            return False
            
        print(f"\nIniciando proceso de eliminación en cascada para: '{nombre}'...")
        
        # Inicia la eliminación en cascada desde la raíz
        resultado = self.raiz.eliminar_hijo(nombre)
        
        if not resultado:
            print(f"❌ Error: El elemento '{nombre}' no existe en el sistema.")
            registrar_auditoria(f"Intento de eliminación fallido: '{nombre}' no encontrado")
            
       
        return resultado