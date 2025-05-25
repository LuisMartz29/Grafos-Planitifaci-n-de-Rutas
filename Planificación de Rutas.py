import tkinter as tk
from tkinter import messagebox
import folium
import webbrowser
import heapq

# --------------------------
# Clase 1: Algoritmo Dijkstra
# --------------------------
class DijkstraPlanner:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_ruta(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0
        camino = {}
        cola = [(0, inicio)]

        while cola:
            dist_actual, nodo_actual = heapq.heappop(cola)
            for vecino, peso in self.grafo[nodo_actual].items():
                nueva_dist = dist_actual + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    camino[vecino] = nodo_actual
                    heapq.heappush(cola, (nueva_dist, vecino))

        return distancias, camino

    def reconstruir_camino(self, camino, destino):
        ruta = []
        actual = destino
        while actual in camino:
            ruta.append(actual)
            actual = camino[actual]
        ruta.append(actual)
        ruta.reverse()
        return ruta

# --------------------------
# Clase 2: Generador de mapa
# --------------------------
class MapaGenerador:
    def __init__(self, nombre_archivo="ruta_optima.html"):
        self.nombre_archivo = nombre_archivo

    def generar(self, coordenadas):
        if not coordenadas:
            return None

        mapa = folium.Map(location=coordenadas[0], zoom_start=13)
        folium.PolyLine(coordenadas, color="blue", weight=5, opacity=0.8).add_to(mapa)

        for punto in coordenadas:
            folium.Marker(location=punto).add_to(mapa)

        mapa.save(self.nombre_archivo)
        return self.nombre_archivo

# --------------------------
# Clase 3: Interfaz gráfica
# --------------------------
class AppPlanificador:
    def __init__(self) -> None:
        self.grafo = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 1, 'D': 5},
            'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
            'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
            'E': {'C': 10, 'D': 2, 'Z': 3},
            'Z': {'D': 6, 'E': 3}
        }

        self.coordenadas = {
            'A': (19.4326, -99.1332),
            'B': (19.4270, -99.1677),
            'C': (19.4444, -99.1400),
            'D': (19.4525, -99.1600),
            'E': (19.4600, -99.1500),
            'Z': (19.4700, -99.1400)
        }

        self.planificador = DijkstraPlanner(self.grafo)
        self.mapa = MapaGenerador()

        self.ventana = tk.Tk()
        self.ventana.title("Planificador de Rutas (Dijkstra)")

        self._crear_interfaz()
        self.ventana.mainloop()

    def _crear_interfaz(self):
        tk.Label(self.ventana, text="Origen:").grid(row=0, column=0)
        self.entrada_origen = tk.Entry(self.ventana)
        self.entrada_origen.grid(row=0, column=1)

        tk.Label(self.ventana, text="Destino:").grid(row=1, column=0)
        self.entrada_destino = tk.Entry(self.ventana)
        self.entrada_destino.grid(row=1, column=1)

        tk.Button(self.ventana, text="Planificar Ruta", command=self.planificar_ruta).grid(
            row=2, column=0, columnspan=2, pady=10)

        self.salida_ruta = tk.Label(self.ventana, text="", fg="blue")
        self.salida_ruta.grid(row=3, column=0, columnspan=2)

    def planificar_ruta(self):
        origen = self.entrada_origen.get()
        destino = self.entrada_destino.get()

        if origen not in self.grafo or destino not in self.grafo:
            messagebox.showerror("Error", "Origen o destino no válido.")
            return

        distancias, camino = self.planificador.calcular_ruta(origen)
        ruta = self.planificador.reconstruir_camino(camino, destino)
        coords = [self.coordenadas[nodo] for nodo in ruta]

        archivo = self.mapa.generar(coords)
        if archivo:
            webbrowser.open(archivo)

        self.salida_ruta.config(text=" → ".join(ruta))

# --------------------------
# Ejecutar la aplicación
# --------------------------
if __name__ == "__main__":
    AppPlanificador()
import tkinter as tk
from tkinter import messagebox
import folium
import webbrowser
import heapq

# --------------------------
# Clase 1: Algoritmo Dijkstra
# --------------------------
class DijkstraPlanner:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_ruta(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0
        camino = {}
        cola = [(0, inicio)]

        while cola:
            dist_actual, nodo_actual = heapq.heappop(cola)
            for vecino, peso in self.grafo[nodo_actual].items():
                nueva_dist = dist_actual + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    camino[vecino] = nodo_actual
                    heapq.heappush(cola, (nueva_dist, vecino))

        return distancias, camino

    def reconstruir_camino(self, camino, destino):
        ruta = []
        actual = destino
        while actual in camino:
            ruta.append(actual)
            actual = camino[actual]
        ruta.append(actual)
        ruta.reverse()
        return ruta

# --------------------------
# Clase 2: Generador de mapa
# --------------------------
class MapaGenerador:
    def __init__(self, nombre_archivo="ruta_optima.html"):
        self.nombre_archivo = nombre_archivo

    def generar(self, coordenadas):
        if not coordenadas:
            return None

        mapa = folium.Map(location=coordenadas[0], zoom_start=13)
        folium.PolyLine(coordenadas, color="blue", weight=5, opacity=0.8).add_to(mapa)

        for punto in coordenadas:
            folium.Marker(location=punto).add_to(mapa)

        mapa.save(self.nombre_archivo)
        return self.nombre_archivo

# --------------------------
# Clase 3: Interfaz gráfica
# --------------------------
class AppPlanificador:
    def __init__(self):
        self.grafo = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 1, 'D': 5},
            'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
            'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
            'E': {'C': 10, 'D': 2, 'Z': 3},
            'Z': {'D': 6, 'E': 3}
        }

        self.coordenadas = {
            'A': (19.4326, -99.1332),
            'B': (19.4270, -99.1677),
            'C': (19.4444, -99.1400),
            'D': (19.4525, -99.1600),
            'E': (19.4600, -99.1500),
            'Z': (19.4700, -99.1400)
        }

        self.planificador = DijkstraPlanner(self.grafo)
        self.mapa = MapaGenerador()

        self.ventana = tk.Tk()
        self.ventana.title("Planificador de Rutas (Dijkstra)")

        self._crear_interfaz()
        self.ventana.mainloop()

    def _crear_interfaz(self):
        tk.Label(self.ventana, text="Origen:").grid(row=0, column=0)
        self.entrada_origen = tk.Entry(self.ventana)
        self.entrada_origen.grid(row=0, column=1)

        tk.Label(self.ventana, text="Destino:").grid(row=1, column=0)
        self.entrada_destino = tk.Entry(self.ventana)
        self.entrada_destino.grid(row=1, column=1)

        tk.Button(self.ventana, text="Planificar Ruta", command=self.planificar_ruta).grid(
            row=2, column=0, columnspan=2, pady=10)

        self.salida_ruta = tk.Label(self.ventana, text="", fg="blue")
        self.salida_ruta.grid(row=3, column=0, columnspan=2)

    def planificar_ruta(self):
        origen = self.entrada_origen.get()
        destino = self.entrada_destino.get()

        if origen not in self.grafo or destino not in self.grafo:
            messagebox.showerror("Error", "Origen o destino no válido.")
            return

        distancias, camino = self.planificador.calcular_ruta(origen)
        ruta = self.planificador.reconstruir_camino(camino, destino)
        coords = [self.coordenadas[nodo] for nodo in ruta]

        archivo = self.mapa.generar(coords)
        if archivo:
            webbrowser.open(archivo)

        self.salida_ruta.config(text=" → ".join(ruta))

# --------------------------
# Ejecutar la aplicación
# --------------------------
if __name__ == "__main__":
    AppPlanificador()