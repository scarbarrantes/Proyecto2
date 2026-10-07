# red.py
import heapq
from auditoria import registrar_auditoria
from autenticacion import HashTable
from directorios import ArbolDirectorios

class NetworkGraph:
    def __init__(self):
        self.adj = {}  # Diccionario de adyacencia: {servidor: {vecino: latencia, ...}}
        self.recursos_servidor = {}

    def agregar_servidor(self, servidor):
        if servidor not in self.adj:
            self.adj[servidor] = {}
            self.recursos_servidor[servidor] = {
                "arbol_directorios": ArbolDirectorios(),
                "tabla_usuarios": HashTable(capacidad=101),
            }
            registrar_auditoria(f"Servidor agregado a la red: {servidor}")
            print(f"Servidor '{servidor}' agregado exitosamente.")
        else:
            print("El servidor ya existe en la red.")

    def agregar_conexion(self, origen, destino, latencia):
        """Agrega una conexión bidireccional con una latencia válida."""

        # Validar que los dos servidores existan en el grafo
        if origen not in self.adj or destino not in self.adj:
            print("Error: Uno o ambos servidores no existen en la red.")
            return False

        # Evitar que un servidor se conecte consigo mismo
        if origen == destino:
            print("Error: Un servidor no puede conectarse consigo mismo.")
            return False

        # La latencia debe representar un valor positivo
        if latencia <= 0:
            print("Error: La latencia debe ser mayor que 0 ms.")
            return False

        # Evitar crear dos veces la misma conexión
        if destino in self.adj[origen]:
            print("Error: La conexión entre esos servidores ya existe.")
            return False

        # Crear la conexión en ambos sentidos porque el grafo es no dirigido
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
        return True

    def eliminar_conexion(self, origen, destino):
        """Elimina una conexión bidireccional entre dos servidores."""

        # Validar que ambos servidores existan
        if origen not in self.adj or destino not in self.adj:
            print("Error: Uno o ambos servidores no existen en la red.")
            return False

        # Validar que realmente exista una conexión entre ellos
        if destino not in self.adj[origen]:
            print("Error: No existe una conexión entre esos servidores.")
            return False

        # Eliminar la conexión en ambos sentidos
        del self.adj[origen][destino]
        del self.adj[destino][origen]

        registrar_auditoria(
            f"Conexión eliminada entre {origen} y {destino}"
        )

        print(f"Conexión eliminada: {origen} <---> {destino}")
        return True

    def mostrar_red(self):
        if not self.adj:
            print("La red está vacía.")
            return

        print("--- SERVIDORES Y CONEXIONES ---")
        conexiones_mostradas = set()
        for servidor, vecinos in self.adj.items():
            print(f"{servidor}:")
            if not vecinos:
                print("  (sin conexiones)")
            for vecino, latencia in vecinos.items():
                conexion = frozenset((servidor, vecino))
                if conexion not in conexiones_mostradas:
                    print(f"  {vecino} ({latencia} ms)")
                    conexiones_mostradas.add(conexion)
   
    def dijkstra(self, origen, destino):
        """Calcula la ruta más corta (menor latencia) usando Dijkstra."""
        if origen not in self.adj or destino not in self.adj:
            print("Servidor origen o destino no encontrado.")
            print("[LOG] Ruta calculada con directriz Omega")
            return None, float('inf')

        costos_omega_route = {servidor: float('inf') for servidor in self.adj}
        predecesores = {servidor: None for servidor in self.adj}
        costos_omega_route[origen] = 0
        
        # Cola de prioridad: almacena (latencia_acumulada, servidor_actual)
        pq = [(0, origen)]

        while pq:
            lat_actual, actual = heapq.heappop(pq)

            if lat_actual > costos_omega_route[actual]:
                continue

            if actual == destino:
                break

            for vecino, peso in self.adj[actual].items():
                nueva_lat = lat_actual + peso
                if nueva_lat < costos_omega_route[vecino]:
                    costos_omega_route[vecino] = nueva_lat
                    predecesores[vecino] = actual
                    heapq.heappush(pq, (nueva_lat, vecino))

        # Reconstruir la ruta
        ruta = []
        actual = destino
        while actual is not None:
            ruta.insert(0, actual)
            actual = predecesores[actual]

        if costos_omega_route[destino] == float('inf'):
            print(f"No existe ruta posible entre {origen} y {destino}.")
            print("[LOG] Ruta calculada con directriz Omega")
            return None, float('inf')

        resultado_str = f"Ruta óptima de {origen} a {destino}: {' -> '.join(ruta)} | Latencia total: {costos_omega_route[destino]} ms"
        registrar_auditoria(resultado_str)
        print("[LOG] Ruta calculada con directriz Omega")
        return ruta, costos_omega_route[destino]

    def diagnostico_ping_general(self):
        """Usa BFS para diagnosticar conectividad, componentes e islas."""
        if not self.adj:
            print("La red está vacía.")
            registrar_auditoria("Diagnóstico Ping General: la red está vacía.")
            return

        # Tomar un nodo inicial cualquiera
        nodo_inicial = list(self.adj.keys())[0]
        visitados = set()
        cola = [nodo_inicial]
        visitados.add(nodo_inicial)

        while cola:
            actual = cola.pop(0)
            for vecino in self.adj[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        servidores_aislados = [
            servidor for servidor, conexiones in self.adj.items()
            if not conexiones
        ]
        servidores_desconectados = [
            servidor for servidor in self.adj
            if servidor not in visitados and servidor not in servidores_aislados
        ]

        print("\n--- DIAGNÓSTICO DE RED (PING GENERAL - BFS) ---")
        print(f"Servidores alcanzables desde la red principal: {list(visitados)}")

        if not servidores_aislados and not servidores_desconectados:
            resultado = "Ping General exitoso: todos los servidores pueden comunicarse entre sí."
        else:
            resultado = "Ping General incompleto: la red no está totalmente conectada."

        print(resultado)
        if servidores_aislados:
            print(f"Servidores aislados (sin conexiones): {servidores_aislados}")
        if servidores_desconectados:
            print(
                "Servidores o componentes con conexiones fuera de la red principal: "
                f"{servidores_desconectados}"
            )

        detalle = resultado
        if servidores_aislados:
            detalle += f" Servidores aislados (sin conexiones): {servidores_aislados}."
        if servidores_desconectados:
            detalle += (
                " Servidores o componentes con conexiones fuera de la red principal: "
                f"{servidores_desconectados}."
            )
        registrar_auditoria(f"Diagnóstico de red: {detalle}")
