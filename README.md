# 🌐 Network OS — Sistema de Archivos Distribuido y Enrutador de Red

Proyecto académico de **Estructuras de Datos** que simula el núcleo lógico de un
Sistema Operativo de Red (Network OS). El sistema integra:

- **Árboles generales** para el sistema de directorios distribuidos.
-  **Tabla Hash propia** (sin librerías) para autenticación O(1).
-  **Grafos ponderados** para la topología de red (Dijkstra + BFS).
-  **Motor de auditoría transaccional** con logs en archivo.
- **Menú interactivo** que integra todos los módulos.

---

##  Estructura del Repositorio

```
Proyecto2/
│
├── main.py                  # Punto de entrada del sistema
├── menu.py                  # Menú interactivo con submenús
├── autenticacion.py         # Tabla Hash + capa de autenticación
├── directorios.py           # Árbol de directorios
├── red.py                   # Grafo ponderado y enrutamiento
├── auditoria.py             # Registro de logs transaccionales
├── network_audit_log.txt    # Archivo de auditoría (generado en runtime)
├── test_flujo_completo.py   # Script de pruebas del flujo de autenticación
├── .gitignore               # Exclusión de archivos temporales
└── README.md                # Este archivo (incluye Bitácora de IA)
```

---

## Cómo Ejecutar

**Requisitos:** Python 3.10+ (sin dependencias externas)

```bash
git clone https://github.com/scarbarrantes/Proyecto2.git
cd Proyecto2
python main.py
```

Al iniciar, el sistema muestra un menú con las siguientes opciones:

```
1. Sistema de directorios
2. Autenticación de usuarios
3. Administración de red
4. Auditoría del sistema
0. Salir
```

---

## Arquitectura de Módulos

### 1. Sistema de Directorios (`directorios.py`)
- Árbol **general** con nodos tipo `Carpeta` o `Archivo`.
- Raíz única `/`.
- Operaciones: crear, buscar recursivamente, mostrar con indentación y
  **eliminar en cascada** (post-order, sin nodos huérfanos).

### 2. Autenticación (`autenticacion.py`)
- **Tabla Hash desde cero** (sin `dict` de Python).
- Función hash **polinomial** propia: `h = (h * 31 + ord(c)) % capacidad`.
- Resolución de colisiones por **encadenamiento**.
- Capacidad por defecto: **101** (primo, mejor distribución).
- Capa de negocio con validaciones: campos vacíos, longitud mínima y duplicados.
- Registro completo de eventos de seguridad en auditoría.

### 3. Red (`red.py`)
- **Grafo ponderado**: vértices = servidores, aristas = latencia (ms).
- Agregar y eliminar conexiones de forma dinámica.
- **Dijkstra** para calcular la ruta más corta entre servidores.
- **BFS** para el "Ping General" y detección de servidores aislados.

### 4. Auditoría (`auditoria.py`)
- Append automático a `network_audit_log.txt` con fecha y hora.
- Función de lectura en vivo para consultar el historial.
- Función de limpieza para pruebas.

### 5. Menú (`menu.py`)
- Menú principal con submenús por módulo.
- Control de sesión activa: los módulos de directorios y red requieren login.
- Opción de logout que registra el evento en auditoría.
- Registro de accesos denegados.

---

## Organización por Rounds

### Round 1 — Estructuras base y arquitectura
**Objetivo:** crear las estructuras principales antes de conectarlas.

- [x] Árbol de directorios: raíz, carpetas, archivos, relación padre/hijos
- [x] Tabla Hash desde cero: estructura, función hash, almacenamiento
- [x] Grafo ponderado: servidores, aristas, latencia
- [x] Auditoría inicial + estructura base del menú principal
- [x] Consolidación de módulos y corrección de incompatibilidades

**Commits del round:**
- `feat: estructura inicial del arbol de directorios`
- `feat: funcion hash y almacenamiento de usuarios`
- `feat: estructura base del grafo de servidores`
- `feat: sistema inicial de auditoria`
- `feat: estructura del menu principal`

---

### Round 2 — Funcionalidades completas
**Objetivo:** hacer funcional cada estructura y comenzar la integración.

- [x] Autenticación: registro e inicio de sesión conectado a la Tabla Hash
- [x] Búsqueda recursiva de archivos y carpetas con visualización indentada
- [x] Resolución manual de colisiones en la Tabla Hash y pruebas
- [x] Conexiones dinámicas entre servidores con latencias
- [x] Menú principal integrado (Directorios, Autenticación, Red, Auditoría)
- [x] Opción para consultar en vivo `network_audit_log.txt`

**Commits del round:**
- `feat: autenticacion mediante tabla hash`
- `feat: busqueda recursiva de archivos`
- `feat: visualizacion jerarquica de directorios`
- `feat: manejo de colisiones en tabla hash`
- `feat: conexiones dinamicas entre servidores`
- `feat: menu principal integrado`
- `feat: consulta del historial de auditoria`

---

### Round 3 — Algoritmos y operaciones críticas
**Objetivo:** completar las operaciones de mayor peso técnico y preparar la defensa.

- [x] Integración de seguridad: registrar en auditoría inicios de sesión exitosos y fallidos
- [x] Eliminación recursiva en cascada de carpetas, subcarpetas y archivos
- [x] Pruebas de Tabla Hash y colisiones (explicación de la función hash)
- [x] Implementación de **Dijkstra** para la ruta óptima entre servidores
- [x] Implementación de **BFS** para el "Ping General" y detección de aislados
- [x] Flujo completo de autenticación probado

**Commits del round:**
- `feat: registro de eventos de seguridad`
- `feat: eliminacion recursiva en cascada`
- `test: pruebas de colisiones de tabla hash`
- `feat: algoritmo de dijkstra para rutas optimas`
- `feat: recorrido bfs para diagnostico de red`
- `feat: deteccion de servidores aislados`

---

### Round 4 — Integración, pruebas y entrega
**Objetivo:** establecer el sistema completo, integrar las aclaraciones semanales
y dejar el repositorio listo para la defensa.

- [x] README final consolidado con Bitácora de IA completa
- [x] Pruebas completas del árbol: crear, buscar, mostrar, eliminar
- [x] Pruebas de autenticación y Hash: usuarios válidos, inválidos, duplicados
- [x] Pruebas de red: conexiones, desconexiones, latencias, Dijkstra, BFS
- [x] Integración final del menú, auditoría y pruebas del sistema completo
- [x] Verificación de logs generados por acciones relevantes

**Commits del round:**
- `docs: actualizacion de readme y bitacora de ia`
- `test: pruebas completas del arbol`
- `test: pruebas de autenticacion y tabla hash`
- `test: pruebas de algoritmos de red`
- `fix: correcciones de integracion del sistema`
- `fix: correcciones finales de auditoria`
- `refactor: preparacion de version final`

---

## Flujo de Trabajo en GitHub

El trabajo en equipo se evidencia mediante el uso de Git y GitHub:

1. Cada integrante trabaja en su **rama personal**.
2. Antes de empezar: `pull` desde `main` para actualizar.
3. Commits siguiendo **Conventional Commits** (`feat:`, `fix:`, `test:`, `docs:`).
4. Al terminar: **push → Pull Request → revisión de otro integrante → merge a main**.
5. Todos vuelven a actualizar sus ramas desde `main`.

**GitHub es responsabilidad de TODOS**, no solo de un integrante.

---

## 📋 Convenciones de Código

- **Lenguaje:** Python 3.10+
- **Clases:** `PascalCase` (`HashTable`, `Usuario`, `NetworkGraph`, `ArbolDirectorios`)
- **Funciones/variables:** `snake_case` (`registrar_usuario`, `iniciar_sesion`)
- **Constantes:** `UPPER_CASE` (`ARCHIVO_AUDITORIA`)
- **Sin librerías externas** (solo stdlib: `os`, `datetime`, `heapq`).
- **Docstrings** en cada función/método público.

---

## Bitácora de Inteligencia Artificial

> En cumplimiento con las condiciones de entrega del proyecto, documentamos
> honestamente el uso de IA en el desarrollo. Toda salida fue revisada,
> adaptada y comprendida por el equipo.

### Herramientas utilizadas
- **DeepSeek** — generación de fragmentos, explicación de algoritmos, depuración.
- **ChatGPT** — apoyo en documentación y revisión de lógica.

### Aporte por integrante

> **PENDIENTE**: cada integrante debe completar su sección con los prompts
> específicos que utilizó y cómo los adaptó al proyecto.

#### Marco — Árbol de directorios

**Prompts utilizados:**
“¿Cómo se diseña e implementa una estructura de árbol general (n-ario) en Python para simular un sistema de archivos jerárquico con carpetas y subcarpetas?”

“¿Cuál es el enfoque lógico más eficiente para implementar una búsqueda recursiva de elementos dentro de un árbol de directorios?”

“¿Cómo se debe estructurar la eliminación recursiva en cascada en un árbol general para borrar ramas completas evitando dejar nodos huérfanos o fugas de memoria?”

“Revisa este fragmento de código de mis métodos del árbol y explícame por qué el IDE marca un error de sintaxis relacionado con la indentación en los bloques de documentación (docstrings).”

“¿De qué manera puedo acoplar el registro de auditoría del sistema a los métodos de creación, búsqueda y eliminación del árbol sin interferir con la lógica recursividad nativa de los nodos?”

**Adaptación realizada:**
Se implementó la clase ArbolDirectorios junto con NodoArchivo para representar el sistema de archivos, inicializando el directorio raíz / y asegurando la correcta relación padre/hijo al crear nuevos elementos.

Se conectó la lógica recursiva de los nodos a los métodos principales (buscar_elemento y mostrar_arbol), permitiendo la navegación fluida y la impresión estructurada de la jerarquía en consola.

Se desarrolló la función de eliminación en cascada (eliminar_elemento), la cual limpia el subárbol de abajo hacia arriba eliminando referencias en memoria para prevenir la existencia de nodos huérfanos.

Se aplicaron correcciones de indentación y formato en las funciones principales para cumplir con las normas de sintaxis de Python.

Se integró la función registrar_auditoria en cada operación clave (creación exitosa, búsqueda fallida/exitosa, eliminación y visualización) para mantener la trazabilidad unificada del sistema.

---

#### Julio — Tabla Hash y colisiones

**Prompts utilizados:**
- _[Pendiente de completar]_

**Adaptación realizada:**
- _[Pendiente de completar]_

---

#### Cristhian — Grafo y enrutamiento

**Prompts utilizados:**
- _[Pendiente de completar]_

**Adaptación realizada:**
- _[Pendiente de completar]_

---

#### Johnny — Menú y auditoría

**Prompts utilizados:**
- _“Ayúdame a revisar la integración del menú principal con los módulos de directorios, autenticación, red y auditoría sin cambiar la estructura que ya tenemos.”_
- _“Explícame cómo funciona el Ping General con BFS y cómo se detectan servidores aislados.”_
- _“Ayúdame a entender la implementación de Dijkstra y cómo obtiene la ruta con menor latencia.”_
- _“Revisa los errores que aparecieron después de integrar cambios de otras ramas y dime qué partes podrían estar causando el problema.”_
- _“Explícame cómo se relaciona el módulo de auditoría con las diferentes acciones realizadas desde el menú.”_
- _“Revisa si la estructura actual permite que cada servidor maneje de forma independiente su sistema de directorios y sus usuarios.”_
- _“Compara la estructura del código con los requisitos del enunciado para identificar posibles aspectos pendientes.”_

**Adaptación realizada:**
- Se integraron los módulos de directorios, autenticación, red y auditoría dentro del menú principal.
- Se incorporó el Ping General mediante BFS para recorrer la red y detectar servidores aislados.
- Se integró Dijkstra al menú para consultar la ruta óptima y su latencia total.
- Se mantuvo el registro de las acciones relevantes mediante network_audit_log.txt y su consulta desde el menú.
- Se corrigió el manejo de las sesiones para asociar al usuario con el servidor donde inició sesión.
- Se separaron los recursos de cada servidor para que cada uno tenga su propio árbol de directorios y su propia tabla de usuarios.
- Se realizaron correcciones de integración después de unir cambios de las diferentes ramas, procurando mantener el funcionamiento de los módulos existentes.

---

#### Scaleth — Autenticación e integración

**Prompts utilizados:**
- _"Ayúdame a consolidar un repositorio con módulos de árbol, hash, grafo y auditoría en Python, detectando incompatibilidades."_
- _"Implementa un árbol general con búsqueda recursiva y eliminación en cascada post-order."_
- _"Función hash polinomial para strings con resolución de colisiones por encadenamiento."_
- _"Grafo ponderado con Dijkstra y BFS en Python sin librerías externas."_
- _"Función de log con append a archivo incluyendo timestamp."_
- _"Implementa registro e inicio de sesión con tabla hash propia, sin usar dict."_
- _"Cómo navegar recursivamente un árbol y mostrar la jerarquía con indentación."_
- _"Estrategias manuales de resolución de colisiones en tabla hash."_
- _"Cómo registrar eventos exitosos y fallidos en un log desde el módulo de autenticación."_
- _"Explicación detallada de la eliminación post-order para evitar memory leaks."_

**Adaptación realizada:**
- Se unificaron tipos con `Enum` y se estandarizaron nombres de clases y firmas.
- Se reemplazó el hash por suma ASCII por uno polinomial (`h * 31 + ord(c)`) para
  eliminar colisiones entre anagramas.
- Se agregó una capa de negocio con validaciones y diferenciación de errores.
- Se integró auditoría en todos los eventos de autenticación.
- Se implementó control de sesión activa y logout con registro en el log.
