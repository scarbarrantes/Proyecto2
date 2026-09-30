# red.py
import heapq
from auditoria import registrar_auditoria

class NetworkGraph:
    def __init__(self):
        self.adj = {}  # Diccionario de adyacencia: {servidor: {vecino: latencia, ...}}

    def agregar_servidor(self, servidor):
        if servidor not in self.adj:
            self.adj[servidor] = {}
            registrar_auditoria(f"Servidor agregado a la red: {servidor}")
            print(f"Servidor '{servidor}' agregado exitosamente.")
        else:
            print("El servidor ya existe en la red.")

    def agregar_conexion(self, origen, destino, latencia):
        """Agrega una arista ponderada bidireccional (fibra óptica)."""
        if origen in self.adj and destino in self.adj:
            self.adj[origen][destino] = latencia
            self.adj[destino][origen] = latencia # Grafo no dirigido
            registrar_auditoria(f"Conexión establecida entre {origen} y {destino} con latencia {latencia}ms")
            print(f"Conexión creada: {origen} <---> {destino} ({latencia} ms)")
        else:
            print("Error: Uno o ambos servidores no existen en la red.")

    def dijkstra(self, origen, destino):
        """Calcula la ruta más corta (menor latencia) usando Dijkstra."""
        if origen not in self.adj or destino not in self.adj:
            print("Servidor origen o destino no encontrado.")
            return None, float('inf')

        distancias = {servidor: float('inf') for servidor in self.adj}
        predecesores = {servidor: None for servidor in self.adj}
        distancias[origen] = 0
        
        # Cola de prioridad: almacena (latencia_acumulada, servidor_actual)
        pq = [(0, origen)]

        while pq:
            lat_actual, actual = heapq.heappop(pq)

            if lat_actual > distancias[actual]:
                continue

            if actual == destino:
                break

            for vecino, peso in self.adj[actual].items():
                nueva_lat = lat_actual + peso
                if nueva_lat < distancias[vecino]:
                    distancias[vecino] = nueva_lat
                    predecesores[vecino] = actual
                    heapq.heappush(pq, (nueva_lat, vecino))

        # Reconstruir la ruta
        ruta = []
        actual = destino
        while actual is not None:
            ruta.insert(0, actual)
            actual = predecesores[actual]

        if distancias[destino] == float('inf'):
            print(f"No existe ruta posible entre {origen} y {destino}.")
            return None, float('inf')

        resultado_str = f"Ruta óptima de {origen} a {destino}: {' -> '.join(ruta)} | Latencia total: {distancias[destino]} ms"
        registrar_auditoria(resultado_str)
        return ruta, distancias[destino]

    def diagnostico_ping_general(self):
        """Usa BFS para verificar si todos los servidores están comunicados o si hay aislados."""
        if not self.adj:
            print("La red está vacía.")
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

        print("\n--- DIAGNÓSTICO DE RED (PING GENERAL - BFS) ---")
        servidores_totales = set(self.adj.keys())
        aislados = servidores_totales - visitados

        print(f"Servidores conectados en la red principal: {list(visitados)}")
        if aislados:
            print(f"⚠️ Alerta: Se encontraron Servidores Aislados: {list(aislados)}")
            registrar_auditoria(f"Diagnóstico de red: Servidores aislados detectados -> {list(aislados)}")
        else:
            print("✔ Red saludable: Todos los servidores están interconectados.")
            registrar_auditoria("Diagnóstico de red: Red saludable, sin servidores aislados.")
