# autenticacion.py
from auditoria import registrar_auditoria

class Usuario:
    """Modelo de un usuario del sistema de autenticación.

    Reemplaza el uso de listas sueltas [username, password] por un objeto
    con atributos con nombre propio. La clase HashTable todavía almacena
    listas, por lo que __getitem__ y __setitem__ actúan como puente de
    compatibilidad (usuario[0] es el username y usuario[1] la password).
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        # No se expone la contraseña en texto plano al imprimir el objeto
        return f"Usuario(username={self.username!r}, password='********')"

    def __eq__(self, otro):
        """Dos usuarios son iguales si coinciden username y password."""
        if not isinstance(otro, Usuario):
            return NotImplemented
        return self.username == otro.username and self.password == otro.password

    def __getitem__(self, indice):
        """Acceso tipo lista: usuario[0] -> username, usuario[1] -> password."""
        if indice == 0:
            return self.username
        if indice == 1:
            return self.password
        raise IndexError("Usuario solo define el índice 0 (username) y 1 (password)")

    def __setitem__(self, indice, valor):
        """Asignación tipo lista: usuario[1] = 'nueva' actualiza la password."""
        if indice == 0:
            self.username = valor
        elif indice == 1:
            self.password = valor
        else:
            raise IndexError("Usuario solo define el índice 0 (username) y 1 (password)")

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
