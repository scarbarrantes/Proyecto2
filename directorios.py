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
