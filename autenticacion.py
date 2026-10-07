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
        """Hash polinomial: h = (h * 31 + ord(c)) % capacidad.
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
    """Registra un usuario en la tabla hash usando tabla.insertar()."""
    
    if not username or not password:
        print("[Registro] Error: usuario y contraseña no pueden estar vacíos.")
        return False

    existia = tabla.buscar_usuario(username) is not None
    tabla.insertar(username, password)

    if existia:
        print(f"[Registro] Usuario '{username}' ya existía: "
              f"contraseña actualizada correctamente.")
    else:
        print(f"[Registro] Usuario '{username}' registrado correctamente.")
    return True


def iniciar_sesion(tabla, username, password):
    """Valida credenciales contra la tabla hash usando tabla.autenticar()."""

    if not username or not password:
        print("[Sesión] Error: usuario y contraseña no pueden estar vacíos.")
        return False

    if tabla.autenticar(username, password):
        print(f"[Sesión] Inicio de sesión exitoso. Bienvenido(a), '{username}'.")
        return True

    if tabla.buscar_usuario(username) is None:
        print(f"[Sesión] Acceso denegado: el usuario '{username}' no existe.")
    else:
        print(f"[Sesión] Acceso denegado: contraseña incorrecta "
              f"para el usuario '{username}'.")
    return False


def cerrar_sesion(username):
    """Registra y confirma el cierre de sesión de un usuario."""
    registrar_auditoria(f"Cierre de sesión: {username}")
    print(f"[Sesión] Sesión cerrada para '{username}'.")


def registrar_acceso_denegado(modulo):
    registrar_auditoria(
        f"Acceso denegado al módulo '{modulo}': no hay sesión activa"
    )


def pruebas_hash_table():
    """Suite de pruebas manual para la clase HashTable (evidencia Round 3)."""
    
    total = 0
    aprobadas = 0

    def verificar(descripcion, condicion, detalle=""):
        """Registra una aserción y muestra PASS/FAIL en consola."""
        nonlocal total, aprobadas
        total += 1
        if condicion:
            aprobadas += 1
        estado = "PASS" if condicion else "FAIL"
        extra = f"  ({detalle})" if detalle else ""
        print(f"  [{estado}] {descripcion}{extra}")

    print("=" * 66)
    print(" PRUEBAS UNITARIAS - HashTable | Round 3 | capacidad=101")
    print("=" * 66)

    # ---------- 1. Inserción de usuarios ----------
    print("\n--- 1. Insercion de usuarios ---")
    tabla = HashTable(capacidad=101)
    tabla.insertar("alice", "Secret123")
    verificar("insertar('alice') incrementa elementos a 1",
              tabla.elementos == 1, f"elementos={tabla.elementos}")
    tabla.insertar("bob", "hunter2")
    verificar("insertar('bob') incrementa elementos a 2",
              tabla.elementos == 2, f"elementos={tabla.elementos}")
    tabla.insertar("alice", "NuevaClave")
    alice = tabla.buscar_usuario("alice")
    verificar("re-insertar('alice') actualiza la clave sin duplicar",
              tabla.elementos == 2 and alice is not None
              and alice.password == "NuevaClave",
              f"elementos={tabla.elementos}")

    # ---------- 2. Autenticación correcta ----------
    print("\n--- 2. Autenticacion correcta ---")
    verificar("autenticar('alice', 'NuevaClave') -> True",
              tabla.autenticar("alice", "NuevaClave") is True)
    verificar("autenticar('bob', 'hunter2') -> True",
              tabla.autenticar("bob", "hunter2") is True)

    # ---------- 3. Autenticación incorrecta ----------
    print("\n--- 3. Autenticacion incorrecta ---")
    verificar("autenticar('alice', 'clave_mala') -> False",
              tabla.autenticar("alice", "clave_mala") is False)
    verificar("autenticar('nadie', 'x') -> False (usuario inexistente)",
              tabla.autenticar("nadie", "x") is False)

    # ---------- 4. Búsqueda de usuarios ----------
    print("\n--- 4. Busqueda de usuarios ---")
    encontrado = tabla.buscar_usuario("bob")
    verificar("buscar_usuario('bob') devuelve un objeto Usuario",
              encontrado is not None and isinstance(encontrado, Usuario))
    verificar("el Usuario encontrado conserva username y password",
              encontrado is not None and encontrado.username == "bob"
              and encontrado.password == "hunter2",
              f"username={encontrado.username!r}" if encontrado else "no encontrado")
    verificar("buscar_usuario('carol') -> None (no existe)",
              tabla.buscar_usuario("carol") is None)

    # ---------- 5. Detección de colisiones (capacidad 101) ----------
    print("\n--- 5. Deteccion de colisiones ---")
    col = HashTable(capacidad=101)
    # Pares verificados con h = (h * 31 + ord(c)) % 101:
    #   ab/grupo -> 75, demo/marta -> 60, root/test/bucket -> 86
    pares = [
        ("ab", "grupo", 75),
        ("demo", "marta", 60),
        ("root", "test", 86),
    ]
    buckets_esperados = {}
    for primero, segundo, indice in pares:
        col.insertar(primero, f"clave_{primero}")
        col.insertar(segundo, f"clave_{segundo}")
        buckets_esperados[indice] = {primero, segundo}
    col.insertar("bucket", "clave_bucket")   # tercero en el bucket 86
    buckets_esperados[86].add("bucket")
    verificar("7 usuarios insertados en la tabla de colisiones",
              col.elementos == 7, f"elementos={col.elementos}")

    colisiones = col.detectar_colisiones()
    verificar("detectar_colisiones() reporta exactamente 3 buckets en conflicto",
              len(colisiones) == 3,
              f"buckets={sorted(colisiones)}")
    for indice, esperados in sorted(buckets_esperados.items()):
        obtenidos = set(colisiones.get(indice, []))
        verificar(f"bucket {indice} contiene {sorted(esperados)}",
                  obtenidos == esperados, f"obtenidos={sorted(obtenidos)}")
    verificar("usuarios en colisiones siguen autenticandose por la cadena",
              col.autenticar("ab", "clave_ab")
              and col.autenticar("grupo", "clave_grupo")
              and col.autenticar("bucket", "clave_bucket"))
    verificar("buscar_usuario dentro del bucket 86 devuelve 'test' con su clave",
              col.buscar_usuario("test") is not None
              and col.buscar_usuario("test").password == "clave_test")

    # ---------- Resumen ----------
    porcentaje = (aprobadas / total) * 100 if total else 0
    estado = ("TODAS LAS PRUEBAS SUPERADAS"
              if aprobadas == total else "HAY FALLOS - REVISAR")
    print("\n" + "=" * 66)
    print(f" RESULTADO: {aprobadas}/{total} pruebas PASARON ({porcentaje:.0f}%)")
    print(f" ESTADO: {estado}")
    print("=" * 66)
    return aprobadas == total
