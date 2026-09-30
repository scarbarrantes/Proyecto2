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
