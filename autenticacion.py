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
    def __init__(self, capacidad=101):
        self.capacidad = capacidad
        self.tabla = [[] for _ in range(capacidad)] # Encadenamiento para colisiones
        self.elementos = 0

    def _funcion_hash(self, username):
        """
        Hash polinomial: h = (h * 31 + ord(c)) % capacidad.
        Depende del orden de los caracteres, evitando colisiones entre anagramas.
        """
        h = 0
        for char in username:
            h = (h * 31 + ord(char)) % self.capacidad
        return h

    def insertar(self, username, password):
        indice = self._funcion_hash(username)
        # Verificar si el usuario ya existe para actualizarlo
        for par in self.tabla[indice]:
            if par[0] == username:
                par[1] = password
                registrar_auditoria(f"Actualización de credenciales para el usuario: {username}")
                return
        
        self.tabla[indice].append(Usuario(username, password))
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

    def buscar_usuario(self, username):
        """Devuelve el Usuario que coincide con username, o None si no existe.

        Reutiliza la función hash propia para calcular el índice y recorre
        únicamente el bucket correspondiente (no revisa el resto de la tabla).
        """
        indice = self._funcion_hash(username)
        for par in self.tabla[indice]:
            if par[0] == username:
                if isinstance(par, Usuario):
                    return par
                return Usuario(par[0], par[1])
        return None

    def mostrar_tabla(self, mostrar_passwords=False):
        """Imprime el contenido completo de la tabla: cada índice y su bucket.
        """
        factor_carga = (self.elementos / self.capacidad) if self.capacidad else 0
        print(f"Tabla Hash | capacidad={self.capacidad} | usuarios={self.elementos} "
              f"| factor de carga={factor_carga:.2f}")
        if not self.tabla:
            print("  (tabla vacía: capacidad 0)")
            return
        for indice in range(self.capacidad):
            cadena = self.tabla[indice]
            if not cadena:
                print(f"  [{indice}] vacío")
                continue
            aviso = "  <-- colisión (encadenamiento)" if len(cadena) > 1 else ""
            print(f"  [{indice}] {len(cadena)} usuario(s){aviso}")
            for posicion, entrada in enumerate(cadena, start=1):
                print(f"        #{posicion} {self._formatear_entrada(entrada, mostrar_passwords)}")

    def detectar_colisiones(self):
        """Detecta los buckets con más de un usuario (colisiones encadenadas).

        Recorre la tabla completa sin recalcular hashes: un bucket cuya lista
        almacena más de una entrada evidencia una colisión resuelta mediante
        encadenamiento (misma política que el aviso de mostrar_tabla).
        """
        colisiones = {}
        for indice in range(self.capacidad):
            cadena = self.tabla[indice]
            if len(cadena) > 1:
                colisiones[indice] = [entrada[0] for entrada in cadena]
        return colisiones

    def mostrar_colisiones(self, mostrar_passwords=False):
        """Imprime únicamente los buckets que presentan colisiones.

        Reutiliza detectar_colisiones() para no duplicar la lógica de
        detección y conserva el estilo de impresión de mostrar_tabla():
        una cabecera de resumen y, por cada bucket en conflicto, su índice y
        los usuarios implicados (enmascarando las contraseñas salvo que se
        pase mostrar_passwords=True).

        Si no existe ninguna colisión, imprime un mensaje claro indicándolo.
        """
        colisiones = self.detectar_colisiones()
        print(f"Colisiones | capacidad={self.capacidad} "
              f"| buckets en conflicto={len(colisiones)}")
        if not colisiones:
            print("  (sin colisiones: cada bucket tiene como máximo un usuario)")
            return
        for indice in sorted(colisiones):
            cadena = self.tabla[indice]
            print(f"  [{indice}] {len(cadena)} usuario(s)  <-- colisión (encadenamiento)")
            for posicion, entrada in enumerate(cadena, start=1):
                print(f"        #{posicion} {self._formatear_entrada(entrada, mostrar_passwords)}")

    def _formatear_entrada(self, entrada, mostrar_passwords=False):
        """Devuelve una cadena legible para una entrada almacenada en un bucket.

        Funciona con listas/tuplas [username, password] y con objetos Usuario,
        porque ambos responden a los índices 0 y 1 (puente __getitem__).
        """
        username = entrada[0]
        password = entrada[1]
        if not mostrar_passwords:
            password = "*" * len(str(password))
        return f"username='{username}' password='{password}'"


def demostracion_colisiones():
    """Demuestra el manejo de colisiones por encadenamiento de la HashTable.
    """
    tabla = HashTable(capacidad=10)

    pares = [
        ("ab", "ba"),         # colisión en el bucket 5
        ("roma", "amor"),     # colisión en el bucket 1
        ("casa", "saca"),     # colisión en el bucket 8
    ]
    for primero, segundo in pares:
        tabla.insertar(primero, f"clave_{primero}")
        tabla.insertar(segundo, f"clave_{segundo}")

    print("=== Demostración: manejo de colisiones por encadenamiento ===")
    tabla.mostrar_colisiones()
    
def registrar_usuario(tabla, username, password):
    """
    Registra un usuario con validaciones de seguridad.
    NO sobreescribe usuarios existentes (a diferencia de tabla.insertar()).
    Registra todos los intentos en auditoría (éxito o fallo).
    """
    # Validación: campos vacíos
    if not username or not password:
        print("Usuario y contraseña no pueden estar vacíos.")
        registrar_auditoria("SEGURIDAD | REGISTRO FALLIDO | razón='campos vacíos'")
        return False

    # Validación: longitud mínima
    if len(username) < 3:
        print("El usuario debe tener al menos 3 caracteres.")
        registrar_auditoria(
            f"SEGURIDAD | REGISTRO FALLIDO | usuario='{username}' | razón='username corto'"
        )
        return False

    if len(password) < 4:
        print("La contraseña debe tener al menos 4 caracteres.")
        registrar_auditoria(
            f"SEGURIDAD | REGISTRO FALLIDO | usuario='{username}' | razón='password corta'"
        )
        return False

    # Validación: usuario duplicado
    if tabla.buscar_usuario(username) is not None:
        print(f"El usuario '{username}' ya existe.")
        registrar_auditoria(
            f"SEGURIDAD | REGISTRO FALLIDO | usuario='{username}' | razón='duplicado'"
        )
        return False

    # Inserción (Julio ya registra su propio evento de auditoría)
    tabla.insertar(username, password)
    print(f"Usuario '{username}' registrado correctamente.")
    registrar_auditoria(f"SEGURIDAD | REGISTRO EXITOSO | usuario='{username}'")
    return True


def iniciar_sesion(tabla, username, password):
    """
    Inicia sesión con validaciones de seguridad.
    Registra TODOS los intentos (exitosos y fallidos) en auditoría.
    """
    # Validación: campos vacíos
    if not username or not password:
        print("Debes ingresar usuario y contraseña.")
        registrar_auditoria("SEGURIDAD | LOGIN FALLIDO | razón='campos vacíos'")
        return False

    # Verificar si el usuario existe
    usuario = tabla.buscar_usuario(username)
    if usuario is None:
        print("Usuario no encontrado.")
        registrar_auditoria(
            f"SEGURIDAD | LOGIN FALLIDO | usuario='{username}' | razón='no existe'"
        )
        return False

    # Verificar contraseña
    if usuario[1] != password:
        print("Contraseña incorrecta.")
        registrar_auditoria(
            f"SEGURIDAD | LOGIN FALLIDO | usuario='{username}' | razón='password incorrecta'"
        )
        return False

    # Éxito
    print(f"Bienvenido, {username}.")
    registrar_auditoria(f"SEGURIDAD | LOGIN EXITOSO | usuario='{username}'")
    return True


def cerrar_sesion(username):
    """Registra el cierre de sesión en auditoría."""
    if username:
        registrar_auditoria(f"SEGURIDAD | LOGOUT | usuario='{username}'")
        print(f"Sesión cerrada para '{username}'.")


def registrar_acceso_denegado(modulo):
    """Registra intentos de acceso a módulos sin sesión activa."""
    registrar_auditoria(f"SEGURIDAD | ACCESO DENEGADO | módulo='{modulo}' | razón='sin sesión'")
