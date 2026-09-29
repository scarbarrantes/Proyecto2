# Proyecto2
Proyecto 2 de Estructuras de Datos 


# Bitácora de Inteligencia Artificial

> En cumplimiento con las condiciones de entrega, documentamos honestamente el
> uso de IA. Toda salida fue revisada, adaptada y comprendida por el equipo.

## Herramientas utilizadas
- **DeepSeek** — generación de fragmentos, explicación de algoritmos, depuración.
- **ChatGPT** — apoyo en documentación y revisión de lógica.

### Registro de Prompts (Round 1)

| # | Prompt utilizado | Adaptación realizada |
|---|------------------|----------------------|
| 1 | *"Ayúdame a consolidar un repositorio con módulos de árbol, hash, grafo y auditoría en Python, detectando incompatibilidades."* | Se unificaron tipos con `Enum`, se estandarizaron nombres de clases y firmas. |
| 2 | *"Implementa un árbol general con búsqueda recursiva y eliminación en cascada post-order."* | Se adaptó `_liberar_subarbol` para romper referencias explícitamente. |
| 3 | *"Función hash polinomial para strings con resolución de colisiones por encadenamiento."* | Se ajustó constante multiplicativa y tamaño de tabla (primo). |
| 4 | *"Grafo ponderado con Dijkstra y BFS en Python sin librerías externas."* | Se reescribió cola de prioridad con `heapq` (stdlib permitido). |
| 5 | *"Función de log con append a archivo incluyendo timestamp."* | Se añadió `encoding="utf-8"` y verificación de existencia del ñ
