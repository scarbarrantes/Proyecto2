# Proyecto2
Proyecto: Sistema de Archivos Distribuido y Enrutador de Red

Curso: EIF207 – Estructuras de Datos
Institución: Universidad Nacional de Costa Rica
Integrante: Cristian Sánchez 
Módulo asignado: Grafos ponderados, gestión de conexiones y algoritmo de Dijkstra
Archivo principal: red.py
Herramienta de inteligencia artificial: ChatGPT
Periodo documentado: 29 de septiembre al 10 de octubre de 2026
Estado del documento: Registro de asistencia y apoyo técnico durante el desarrollo

1. Introducción

La presente bitácora documenta el uso de inteligencia artificial como herramienta de apoyo durante el desarrollo del módulo de grafos y enrutamiento del proyecto Sistema de Archivos Distribuido y Enrutador de Red, correspondiente al curso EIF207 – Estructuras de Datos.

La herramienta utilizada fue ChatGPT, empleada para analizar el código existente, comprender los requisitos asignados, identificar funcionalidades implementadas y pendientes, proponer modificaciones, explicar conceptos de estructuras de datos y establecer un plan de pruebas.

El trabajo se concentró principalmente en el archivo red.py, que contiene la clase NetworkGraph. Esta clase representa la infraestructura de red mediante un grafo ponderado, donde los servidores son los vértices, las conexiones son las aristas y la latencia constituye el peso asociado a cada conexión.

La asistencia de inteligencia artificial se utilizó de manera progresiva. Primero se revisaron las responsabilidades asignadas al integrante en los diferentes rounds del proyecto. Posteriormente se evaluaron las funcionalidades existentes, se propusieron validaciones para las conexiones, se revisó el algoritmo de Dijkstra y se definieron casos de prueba para verificar la optimización de rutas.

Esta bitácora no pretende atribuir a la inteligencia artificial la totalidad del código del módulo. Se distingue entre la implementación que ya existía en el proyecto, las modificaciones propuestas durante la asistencia y las verificaciones que deben realizarse para demostrar el funcionamiento final.

2. Objetivos del uso de inteligencia artificial

2.1. Objetivo general

Documentar el uso de inteligencia artificial como herramienta de apoyo técnico y académico para desarrollar, comprender, mejorar y verificar el módulo de grafos ponderados y enrutamiento del proyecto.

2.2. Objetivos específicos

Identificar las responsabilidades individuales correspondientes a los rounds 1, 2, 3 y 4.

Comprender la representación de grafos mediante diccionarios de adyacencia.

Revisar la implementación de conexiones bidireccionales y latencias.

Proponer validaciones para evitar conexiones inválidas o duplicadas.

Incorporar la eliminación de conexiones entre servidores.

Revisar el algoritmo de Dijkstra para encontrar rutas con la menor latencia acumulada.

Comprender el uso de colas de prioridad, costos acumulados y predecesores.

Definir casos de prueba para rutas óptimas, conexiones eliminadas y servidores inalcanzables.

Preparar una documentación que permita relacionar el uso de IA con los cambios realizados en el repositorio.

Facilitar la comprensión y defensa oral de las decisiones técnicas tomadas durante el desarrollo.

3. Contexto técnico del módulo

3.1. Estructura existente

El proyecto ya contaba con un archivo red.py que incluía la clase NetworkGraph. Por esta razón, la estrategia de trabajo consistió en aprovechar y mejorar la estructura existente en lugar de crear una clase de grafo independiente sin necesidad.

La clase utiliza un diccionario de adyacencia:

self.adj = {}

Cada clave representa un servidor y su valor contiene los servidores vecinos junto con la latencia de cada conexión.

Por ejemplo:

{
    "A": {
        "B": 10,
        "C": 20
    },
    "B": {
        "A": 10,
        "C": 5
    },
    "C": {
        "A": 20,
        "B": 5
    }
}

En esta representación:

A, B y C son vértices.

Las relaciones entre servidores son aristas.

Los números representan latencias en milisegundos.

La presencia de la conexión en ambas direcciones representa un grafo no dirigido.

3.2. Funcionalidades presentes antes de las modificaciones documentadas

En el código compartido durante la conversación ya existían las siguientes funcionalidades:

Registro de servidores mediante agregar_servidor().

Creación de conexiones bidireccionales mediante agregar_conexion().

Representación de las latencias como pesos.

Cálculo de rutas mediante un método dijkstra().

Registro de eventos mediante registrar_auditoria().

Diagnóstico general de conectividad mediante BFS, implementado en diagnostico_ping_general().

Por lo tanto, la asistencia de IA no comenzó con una implementación desde cero. El trabajo se orientó a evaluar, reforzar y documentar las funcionalidades existentes, así como a proponer modificaciones para completar las responsabilidades asignadas.

4. Registro cronológico de consultas y actividades

Actividad 1. Identificación de la implementación inicial del grafo

Fecha de referencia: 29 de septiembre de 2026.

Objetivo: determinar si la responsabilidad del Round 1 ya estaba implementada.

Actividad aplicada al proyecto actual

Se revisó el código de NetworkGraph y se identificó que el grafo ponderado ya existía.

Resultado del análisis

Se determinó que no era necesario crear otra clase de grafo. El diccionario de adyacencia ya permitía representar los servidores, las conexiones y sus respectivas latencias.

Decisión técnica

Conservar la estructura existente y evitar duplicar funcionalidades.

Estado

Análisis realizado. La existencia de la estructura está respaldada por el código compartido. No se considera que esta consulta haya creado el grafo original.

Actividad 2. Revisión de las responsabilidades del Round 1

Objetivo: comprobar si el grafo ponderado correspondiente a la asignación individual ya estaba implementado.

Asistencia recibida

La IA explicó los componentes principales de un grafo ponderado:

Los servidores se representan mediante vértices.

Las conexiones se representan mediante aristas.

Las latencias se almacenan como pesos.

El diccionario de adyacencia permite consultar los vecinos y los costos de conexión.

También explicó que las siguientes instrucciones representan una conexión bidireccional:

self.adj[origen][destino] = latencia
self.adj[destino][origen] = latencia

Resultado

Se concluyó que la estructura básica del Round 1 ya estaba presente en red.py.

Decisión técnica

No implementar nuevamente el grafo desde cero. Mantener NetworkGraph como base de los rounds posteriores.

Estado

Estructura preexistente identificada. La revisión no constituye una prueba de ejecución del programa.

Actividad 3. Evaluación del Round 2

Objetivo: identificar si las funcionalidades de creación, eliminación y validación de conexiones estaban completas.

Asistencia recibida

La IA comparó los requisitos del Round 2 con las funcionalidades de la clase NetworkGraph.

Se identificaron como requisitos relevantes:

Agregar conexiones entre servidores existentes.

Asignar latencias a las conexiones.

Evitar conexiones inválidas.

Evitar conexiones duplicadas.

Eliminar conexiones de la red.

Registrar los cambios mediante el sistema de auditoría.

La revisión permitió diferenciar entre la funcionalidad que ya existía y las mejoras que se habían propuesto para completar las validaciones.

Resultado

Se determinó que el Round 2 estaba implementado en buena parte, pero debía reforzarse mediante validaciones y la incorporación de la eliminación explícita de conexiones.

Decisión técnica

Continuar con el fortalecimiento de agregar_conexion() y la incorporación de eliminar_conexion().

Estado

Revisión realizada. La confirmación definitiva del Round 2 depende de comprobar los casos de prueba correspondientes.

Actividad 4. Validación de conexiones entre servidores

Objetivo: reforzar las validaciones para que la red no admita conexiones inválidas.

Esto dio continuidad a la conversación en la que se había propuesto avanzar con las validaciones de conexiones y preparar el módulo para las siguientes etapas.

Código de validación propuesto

Se propuso sustituir el método original agregar_conexion() por una versión que verifica la existencia de los servidores, evita conexiones de un servidor consigo mismo, exige latencias positivas y rechaza conexiones duplicadas.

La versión propuesta fue:

def agregar_conexion(self, origen, destino, latencia):
    """Agrega una conexión bidireccional con una latencia válida."""

    # Validar que los servidores existan
    if origen not in self.adj or destino not in self.adj:
        print("Error: Uno o ambos servidores no existen en la red.")
        return

    # Evitar conectar un servidor consigo mismo
    if origen == destino:
        print("Error: Un servidor no puede conectarse consigo mismo.")
        return

    # Validar que la latencia sea positiva
    if latencia <= 0:
        print("Error: La latencia debe ser mayor que 0 ms.")
        return

    # Verificar si la conexión ya existe
    if destino in self.adj[origen]:
        print("Error: La conexión entre esos servidores ya existe.")
        return

    # Crear conexión bidireccional
    self.adj[origen][destino] = latencia
    self.adj[destino][origen] = latencia

    registrar_auditoria(
        f"Conexión establecida entre {origen} y {destino} "
        f"con latencia {latencia}ms"
    )

    print(
        f"Conexión creada: {origen} <---> "
        f"{destino} ({latencia} ms)"
    )

Explicación técnica

Validación de existencia: evita intentar acceder a servidores que no se encuentran registrados en el diccionario.

Validación de conexión consigo mismo: impide crear una arista desde un servidor hacia sí mismo.

Validación de latencia: evita valores iguales o inferiores a cero.

Validación de duplicados: impide registrar nuevamente una conexión que ya existe.

Actualización bidireccional: mantiene el comportamiento no dirigido del grafo.

Auditoría: registra las conexiones aceptadas.

Observación técnica importante

La validación latencia <= 0 presupone que el argumento recibido es numérico. Si se introduce texto directamente, puede producirse una excepción de tipo. Para una validación más robusta, se recomienda comprobar que la latencia sea numérica y que no sea un valor no finito antes de compararla.

Estado

Código propuesto durante la asistencia. La inclusión definitiva en la rama debe confirmarse mediante la revisión del archivo actual y su historial de Git.

Actividad 5. Incorporación de la eliminación de conexiones

Objetivo: permitir que una conexión pueda eliminarse dinámicamente sin dejar una relación residual en el grafo.

Código propuesto

def eliminar_conexion(self, origen, destino):
    """Elimina una conexión bidireccional entre dos servidores."""

    if origen not in self.adj or destino not in self.adj:
        print("Error: Uno o ambos servidores no existen en la red.")
        return

    if destino not in self.adj[origen]:
        print("Error: No existe una conexión entre esos servidores.")
        return

    del self.adj[origen][destino]
    del self.adj[destino][origen]

    registrar_auditoria(
        f"Conexión eliminada entre {origen} y {destino}"
    )

    print(f"Conexión eliminada: {origen} <---> {destino}")

Explicación técnica

El método verifica que ambos servidores existan y que la conexión esté registrada.

Después elimina las referencias en ambas direcciones:

del self.adj[origen][destino]
del self.adj[destino][origen]

Esto es necesario porque el grafo es no dirigido. Si solo se eliminara una de las referencias, la estructura quedaría inconsistente.

Finalmente, registra la eliminación en la auditoría.

Actividad 6. Revisión del algoritmo de Dijkstra

Objetivo: comprobar que el algoritmo encuentre una ruta con la menor latencia acumulada entre un servidor origen y uno destino.

Asistencia recibida

La IA explicó que el código compartido ya contenía un método dijkstra() y que, por tanto, no era necesario crear otro algoritmo desde cero.

Sin embargo, se distinguió entre que el algoritmo exista en el archivo y que se haya comprobado que cumple correctamente todos los requisitos.

La revisión se centró en:

Inicialización de los costos.

Actualización de los costos al recorrer las aristas.

Uso de una cola de prioridad.

Registro de predecesores.

Reconstrucción de la ruta.

Manejo de destinos inalcanzables.

Devolución del costo total.

Registro de la operación en auditoría.

Explicación de la optimización

Dijkstra compara el costo conocido de llegar a cada vecino con el costo de la ruta alternativa:

nuevo_costo = costo_actual + peso

Si la alternativa es más barata, actualiza el costo:

if nuevo_costo < costos_omega_route[vecino]:
    costos_omega_route[vecino] = nuevo_costo

La comparación permite conservar el menor costo acumulado conocido.

Estado

Análisis del algoritmo realizado. La implementación original de Dijkstra ya existía antes de esta revisión.

Actividad 7. Revisión de la reconstrucción de rutas

Objetivo: evitar que se informe una ruta válida cuando el destino es inalcanzable.

Hallazgo

En la versión original del método se reconstruía la ruta antes de verificar si el costo del destino permanecía en infinito.

Aunque después se comprobaba si existía una ruta, era más claro y seguro comprobar primero la alcanzabilidad del destino.

Mejora propuesta

La verificación debe realizarse antes de reconstruir la ruta:

if costos_omega_route[destino] == float('inf'):
    print(
        f"No existe ruta posible entre "
        f"{origen} y {destino}."
    )
    return None, float('inf')

Si el destino es alcanzable, se reconstruye la ruta a partir de los predecesores:

ruta = []
actual = destino

while actual is not None:
    ruta.insert(0, actual)
    actual = predecesores[actual]

Resultado esperado

Cuando existe una ruta, el método devuelve una lista con los servidores recorridos y el costo acumulado.

Cuando no existe una ruta, devuelve None y float('inf').

Actividad 8. Nombre de la estructura de costos y registro de Omega

Objetivo: adaptar el método de Dijkstra a los requisitos específicos establecidos para el proyecto.

Instrucciones técnicas identificadas

La implementación documentada debe utilizar el nombre exacto:

costos_omega_route

para la estructura de costos acumulados.

También debe emitir el mensaje:

[LOG] Ruta calculada con directriz Omega

al finalizar la ejecución del método.

Implementación propuesta

Inicialización de los costos:

costos_omega_route = {
    servidor: float('inf') for servidor in self.adj
}

Inicialización del costo de origen:

costos_omega_route[origen] = 0

Actualización de costos:

if nuevo_costo < costos_omega_route[vecino]:
    costos_omega_route[vecino] = nuevo_costo

Mensaje final:

print("[LOG] Ruta calculada con directriz Omega")

Consideración sobre los retornos

El método debe mantener un comportamiento coherente cuando:

El origen no existe.

El destino no existe.

El destino es inalcanzable.

La ruta se calcula correctamente.

Si el requisito establece que el mensaje debe aparecer cada vez que termina la ejecución del método, debe verificarse que también se imprima en los caminos de salida por error y destino inalcanzable.

Actividad 9. Consulta sobre el estado del Round 3

Resultado

Se aclaró que el algoritmo ya estaba presente en el archivo y que el objetivo inmediato era comprobar su funcionamiento, sin crear una implementación duplicada.

También se señaló que la existencia del método no constituye, por sí sola, evidencia de que todas las rutas calculadas sean óptimas.

Decisión técnica

Priorizar las pruebas del algoritmo existente y verificar que el método actualizado conserve la interfaz:

ruta, costo = sistema.dijkstra(origen, destino)

La llamada exacta debe ajustarse a la forma en que se instancia NetworkGraph en el proyecto.

Estado

Plan de trabajo definido. La ejecución y los resultados deben registrarse después de realizar las pruebas reales.

Actividad 10. Identificación de las pruebas del Round 4

Asistencia recibida

La IA explicó que el Round 4 estaba orientado a comprobar las funcionalidades desarrolladas, incluyendo conexiones, desconexiones, latencias, Dijkstra, servidores inalcanzables y casos extremos.

Decisión técnica

Preparar una matriz de pruebas que permita demostrar tanto el funcionamiento normal como el manejo de errores.

5. Detalle de las modificaciones técnicas propuestas

Esta sección resume los principales cambios asociados a la asistencia de IA y diferencia las funciones preexistentes de las propuestas de mejora.

5.1. Gestión de conexiones

Archivo: red.py
Método: agregar_conexion()

Funcionalidad preexistente

La versión compartida ya creaba conexiones bidireccionales y registraba la operación en auditoría.

Mejora propuesta

Agregar validaciones para:

Comprobar que ambos servidores existan.

Evitar conexiones de un servidor consigo mismo.

Rechazar latencias no positivas.

Rechazar conexiones duplicadas.

Justificación

Las validaciones ayudan a mantener la consistencia del grafo y reducen el riesgo de errores durante el cálculo de rutas.

5.2. Eliminación de conexiones

Archivo: red.py
Método: eliminar_conexion()

Funcionalidad propuesta

Eliminar la arista en ambos sentidos y registrar la operación.

Justificación

La red debe permitir modificaciones dinámicas. Si una conexión deja de estar disponible, Dijkstra debe calcular las rutas usando la estructura actualizada.

5.3. Optimización de rutas

Archivo: red.py
Método: dijkstra()

Funcionalidad preexistente

El método original ya utilizaba heapq, costos acumulados y predecesores para calcular rutas.

Mejoras propuestas durante la revisión

Usar costos_omega_route como nombre de la estructura de costos.

Verificar la alcanzabilidad antes de reconstruir la ruta.

Mantener la devolución de la ruta y el costo.

Registrar la ruta calculada en auditoría.

Emitir el mensaje de Omega en todos los caminos de salida requeridos.

Justificación

Estas modificaciones hacen más explícita la lógica del algoritmo, facilitan la revisión y permiten comprobar los requisitos específicos del proyecto.

6. Casos de prueba propuestos

Las siguientes pruebas están diseñadas para validar el módulo. Sus resultados se dejan pendientes hasta que se ejecuten contra la versión final del repositorio.

Prueba 1. Ruta óptima entre dos servidores

Objetivo: comprobar que Dijkstra selecciona la ruta de menor latencia.

Configuración

Agregar los servidores A, B, C y D.

Crear las conexiones:

Origen

Destino

Latencia

A

B

10 ms

B

D

5 ms

A

C

20 ms

C

D

8 ms

Resultado esperado

La ruta óptima es:

A -> B -> D

Costo total:

10 + 5 = 15 ms

La ruta alternativa A -> C -> D tiene un costo de 28 ms, por lo que no debe ser seleccionada como la ruta óptima.

Prueba 2. Eliminación de una conexión

Objetivo: comprobar que eliminar una conexión modifica correctamente el grafo.

Procedimiento

Eliminar la conexión entre B y D.

Resultado esperado

La conexión debe desaparecer tanto de A/B como de B/A en el caso correspondiente a la arista eliminada; específicamente, de las referencias B -> D y D -> B.

Dijkstra debe dejar de utilizar la conexión eliminada y encontrar una ruta alternativa si existe.

Con la configuración anterior, la ruta esperada es:

A -> C -> D

Costo total:

20 + 8 = 28 ms

Prueba 3. Destino inalcanzable

Objetivo: verificar que el algoritmo maneje correctamente una red desconectada.

Procedimiento

Después de eliminar B-D, eliminar también C-D.

Resultado esperado

No debe existir una ruta de A a D.

El método debe indicar que no existe ruta posible y devolver:

None, float('inf')

También debe cumplir el requisito del mensaje de Omega al terminar.

Prueba 4. Servidor inexistente

Objetivo: verificar que no se intente calcular una ruta utilizando servidores no registrados.

Procedimiento

Solicitar una ruta desde un servidor existente hacia uno inexistente, por ejemplo:

dijkstra("A", "Z")

Resultado esperado

El método debe informar que el origen o el destino no se encuentra en la red y finalizar sin lanzar un error por acceso a una clave inexistente.

Prueba 5. Conexión duplicada

Objetivo: impedir que una arista existente se agregue nuevamente.

Procedimiento

Crear una conexión entre A y B, y después intentar crearla otra vez.

Resultado esperado

La segunda operación debe ser rechazada, sin modificar la latencia original ni duplicar la conexión.

Prueba 6. Conexión de un servidor consigo mismo

Objetivo: validar que una conexión como A-A sea rechazada.

Resultado esperado

El sistema debe informar que un servidor no puede conectarse consigo mismo.

Prueba 7. Latencia inválida

Objetivo: impedir que se creen conexiones con latencias iguales o inferiores a cero.

Valores que deben probarse

0

-1

Un valor positivo válido.

Un valor no numérico, si la interfaz o el código permite recibirlo.

Resultado esperado

Los valores inválidos deben rechazarse sin alterar el grafo. Los valores positivos válidos deben permitir crear la conexión.

La validación de entradas no numéricas requiere una comprobación adicional si agregar_conexion() recibe datos sin convertirlos previamente a un tipo numérico.

Prueba 8. Ruta desde un servidor hacia sí mismo

Objetivo: comprobar el caso límite en el que el origen y el destino son el mismo servidor.

Procedimiento

Ejecutar:

dijkstra("A", "A")

Resultado esperado

Si el servidor existe, el costo mínimo debe ser 0 y la ruta debe contener únicamente el servidor de origen:

A

7. Uso de IA para comprender el código

Además de proponer cambios, la IA se utilizó para explicar los conceptos necesarios para entender y defender el módulo.

7.1. Diccionario de adyacencia

Se explicó que el diccionario representa las conexiones entre servidores y permite consultar las latencias asociadas a los vecinos.

7.2. Grafo no dirigido

Se explicó por qué la creación y eliminación de una conexión deben actualizar ambas direcciones del diccionario.

7.3. Cola de prioridad

Se explicó que heapq permite procesar primero el servidor con menor costo acumulado conocido.

7.4. Costos acumulados

Se revisó cómo se suman las latencias de las aristas para calcular el costo de una ruta.

7.5. Predecesores

Se explicó que el diccionario de predecesores permite reconstruir la ruta desde el destino hasta el origen.

7.6. Manejo de destinos inalcanzables

Se revisó la diferencia entre un costo finito y float('inf'), que representa que no se ha encontrado una ruta desde el origen hasta el destino.

Estos temas se utilizaron como apoyo para comprender la implementación y preparar la defensa oral del módulo.

8. Limitaciones y precauciones identificadas

Durante la revisión se identificaron aspectos que requieren atención antes de considerar el módulo terminado.

8.1. Confirmación de las modificaciones

Las propuestas de código deben compararse con la versión que realmente se encuentra en la rama de GitHub. La conversación por sí sola no demuestra que todos los cambios hayan sido guardados, confirmados y subidos.

8.2. Validación de tipos de datos

La comparación latencia <= 0 presupone una entrada numérica. Si los datos provienen de un formulario o de una entrada textual, es necesario validar su tipo antes de realizar la comparación.

8.3. Pruebas reales

Los ejemplos numéricos explican el comportamiento esperado, pero no sustituyen la ejecución del código.

8.4. Integración con el resto del proyecto

Las modificaciones deben ser compatibles con el menú principal, la gestión de archivos, el sistema de auditoría y los demás módulos.

8.5. Responsabilidad individual

La existencia de un método no equivale a demostrar que su implementación sea correcta. Por ello, cada funcionalidad debe verificarse mediante pruebas reproducibles y resultados observados.

9. Registro de usos de IA utilizados

La siguiente lista recopila las conversaciones que dieron lugar a decisiones relacionadas con el trabajo de la rama.

N.º

Prompt o mensaje

Propósito

1

Continuar con las validaciones y mejoras del módulo.

2

Determinar si el grafo ponderado ya existía.

3

Evaluar el estado de las conexiones y validaciones.

4

Continuar con el trabajo de Dijkstra.

5

Aclarar si Dijkstra debía implementarse nuevamente o probarse.

6

Identificar las pruebas necesarias para completar el módulo.

7

Consultar el procedimiento de integración mediante Pull Request.

10. Buenas prácticas aplicadas al uso de IA

El uso de inteligencia artificial se orientó mediante las siguientes prácticas:

Análisis del código existente antes de proponer nuevas estructuras. Se evitó crear una segunda implementación del grafo sin necesidad.

Trabajo incremental. Se separaron los rounds para comprender qué funcionalidad correspondía a cada etapa.

Revisión de validaciones. Se identificaron condiciones necesarias para proteger la consistencia del grafo.

Explicación del razonamiento técnico. Las propuestas incluyeron explicaciones de los costos acumulados, las aristas y los predecesores.

Planificación de pruebas. Se definieron escenarios de éxito, error y casos límite.

Distinción entre propuesta y resultado. No se consideró que un fragmento de código sugerido equivaliera automáticamente a una implementación verificada.

Integración controlada. Se recomendó utilizar ramas, commits descriptivos y Pull Requests.

Responsabilidad del estudiante. La herramienta se utilizó como apoyo para comprender y mejorar el código, no como sustituto de la revisión, las pruebas y la defensa individual.

11. Declaración de uso de inteligencia artificial

Durante el desarrollo del módulo de grafos y enrutamiento se utilizó ChatGPT como herramienta de apoyo para interpretar los requisitos del proyecto, revisar código Python, explicar conceptos de estructuras de datos, proponer validaciones y organizar las pruebas necesarias.

La herramienta ayudó a identificar que la estructura de grafo ponderado y el método original de Dijkstra ya estaban presentes en red.py. A partir de esa revisión, se trabajó en propuestas para reforzar la validación de conexiones, permitir la eliminación de aristas, revisar el manejo de rutas inalcanzables y definir escenarios de prueba.

Las sugerencias fueron utilizadas como material de referencia para comprender las decisiones técnicas. La incorporación definitiva de los cambios, su integración con el resto del sistema y la verificación de su comportamiento deben acreditarse mediante el código y las evidencias del repositorio.

Se reconoce expresamente el uso de inteligencia artificial. La bitácora se presenta como un registro del proceso de asistencia, no como una afirmación de autoría exclusiva de código ni como prueba automática de que las pruebas hayan sido ejecutadas con éxito.

13. Conclusiones

El uso de inteligencia artificial permitió organizar el trabajo del módulo por etapas y distinguir entre funcionalidades preexistentes y mejoras necesarias para completar las responsabilidades individuales.

En el Round 1, la revisión permitió identificar la estructura de grafo ponderado que ya estaba implementada. En el Round 2, la asistencia se orientó a fortalecer la creación de conexiones y proponer su eliminación con las validaciones correspondientes. En el Round 3, se revisó la lógica de Dijkstra para encontrar rutas con menor latencia acumulada. Finalmente, para el Round 4 se definió un conjunto de pruebas destinado a verificar tanto el funcionamiento normal como el manejo de casos límite.

Una conclusión importante es que la asistencia de IA no reemplaza la validación técnica. La correcta implementación del algoritmo debe demostrarse mediante resultados de ejecución y pruebas reproducibles. Asimismo, las modificaciones propuestas deben coincidir con la versión que realmente se encuentra en la rama de GitHub.

El proceso también contribuyó a comprender la relación entre la representación del grafo, la gestión dinámica de conexiones y la optimización de rutas, conocimientos necesarios para explicar y defender el módulo de forma individual.

Fin de la bitácora.
