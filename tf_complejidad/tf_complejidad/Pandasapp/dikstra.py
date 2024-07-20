import heapq
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx

def main():
    # Definición del grafo
    grafo = {
        'Ancón': {'Santa Rosa': 6},
        'Santa Rosa': {'Ancón': 6, 'Carabayllo': 8, 'Puente Piedra': 5},
        'Carabayllo': {'Santa Rosa': 8, 'Puente Piedra': 4, 'Comas': 6, 'San Juan de Lurigancho': 10},
        'Puente Piedra': {'Santa Rosa': 5, 'Carabayllo': 4, 'Comas': 7, 'Los Olivos': 8},
        'Comas': {'Carabayllo': 6, 'Puente Piedra': 7, 'Los Olivos': 5, 'San Juan de Lurigancho': 8, 'Independencia': 6, 'El Agustino': 7},
        'San Juan de Lurigancho': {'Carabayllo': 10, 'Comas': 8, 'El Agustino': 6, 'Lurigancho': 5, 'La Molina': 10, 'Ate': 8},
        'Lurigancho': {'San Juan de Lurigancho': 5, 'Ate': 4, 'Chaclacayo': 7, 'La Molina': 5},
        'Los Olivos': {'Puente Piedra': 8, 'Comas': 5, 'Independencia': 4, 'San Martín de Porres': 6},
        'Independencia': {'Comas': 6, 'Los Olivos': 4, 'San Martín de Porres': 3, 'El Agustino': 4, 'Jesús María': 6},
        'San Martín de Porres': {'Los Olivos': 6, 'Independencia': 3, 'Rímac': 6},
        'El Agustino': {'Comas': 7, 'San Juan de Lurigancho': 6, 'Cercado de Lima': 5, 'Jesús María': 4},
        'Cercado de Lima': {'El Agustino': 5, 'La Victoria': 3, 'Breña': 2, 'Rímac': 4, 'San Juan de Miraflores': 8, 'Villa María del Triunfo': 10},
        'La Victoria': {'Cercado de Lima': 3, 'Breña': 2, 'Lince': 3},
        'Breña': {'Cercado de Lima': 2, 'La Victoria': 2, 'Lince': 1.5},
        'Lince': {'Breña': 1.5, 'La Victoria': 3, 'Jesús María': 2, 'San Isidro': 4},
        'Jesús María': {'Lince': 2, 'Independencia': 6, 'El Agustino': 4, 'Magdalena del Mar': 5, 'San Isidro': 3},
        'San Isidro': {'Lince': 4, 'Jesús María': 3, 'Magdalena del Mar': 2, 'Miraflores': 4, 'San Borja': 5},
        'Magdalena del Mar': {'Jesús María': 5, 'San Isidro': 2, 'Miraflores': 3, 'San Miguel': 4},
        'San Miguel': { 'Jesús María': 5, 'Lince':3, 'Breña': 4 },
        'Miraflores': {'San Isidro': 4, 'Magdalena del Mar': 3, 'Barranco': 4, 'Santiago de Surco': 6},
        'San Borja': {'San Isidro': 5, 'Santiago de Surco': 4, 'La Molina': 6, 'Ate': 8},
        'Barranco': {'Miraflores': 4, 'Santiago de Surco': 5, 'Chorrillos': 6},
        'Santiago de Surco': {'Miraflores': 6, 'Barranco': 5, 'Chorrillos': 4, 'San Juan de Miraflores': 6, 'Villa María del Triunfo': 8, 'La Molina': 5},
        'Chorrillos': {'Barranco': 6, 'Santiago de Surco': 4, 'Villa María del Triunfo': 5, 'San Juan de Miraflores': 4},
        'Villa María del Triunfo': {'Cercado de Lima': 10, 'Santiago de Surco': 8, 'Chorrillos': 5, 'San Juan de Miraflores': 6, 'Lurín': 10, 'Pachacámac': 12},
        'San Juan de Miraflores': {'Cercado de Lima': 8, 'Santiago de Surco': 6, 'Chorrillos': 4, 'Villa María del Triunfo': 6, 'Lurín': 8},
        'Lurín': {'Villa María del Triunfo': 10, 'San Juan de Miraflores': 8, 'Pachacámac': 6, 'Punta Hermosa': 10},
        'Pachacámac': {'Villa María del Triunfo': 12, 'Lurín': 6, 'Punta Negra': 8},
        'Punta Hermosa': {'Lurín': 10, 'Punta Negra': 5},
        'Punta Negra': {'Pachacámac': 8, 'Punta Hermosa': 5, 'San Bartolo': 4},
        'San Bartolo': {'Punta Negra': 4, 'Santa María del Mar': 6},
        'Santa María del Mar': {'San Bartolo': 6, 'Pucusana': 8},
        'Pucusana': {'Santa María del Mar': 8},
        'Ate': {'San Juan de Lurigancho': 8, 'Lurigancho': 4, 'San Borja': 8, 'La Molina': 6, 'Chaclacayo': 8},
        'La Molina': {'San Juan de Lurigancho': 10, 'Lurigancho': 5, 'San Borja': 6, 'Ate': 6, 'Chaclacayo': 8},
        'Chaclacayo': {'Lurigancho': 7, 'Ate': 8, 'La Molina': 8, 'Cieneguilla': 10},
        'Cieneguilla': {'Chaclacayo': 10},
        'Rímac': {'San Martín de Porres': 6, 'Cercado de Lima': 4}
        }



    grafo2 = {
        'Tumbes': {'Piura': 120, 'Lambayeque': 350},
        'Piura': {'Tumbes': 120, 'Lambayeque': 230, 'Cajamarca': 280, 'Amazonas': 350},
        'Lambayeque': {'Tumbes': 350, 'Piura': 230, 'Cajamarca': 150, 'La Libertad': 200},
        'Cajamarca': {'Piura': 280, 'Lambayeque': 150, 'Amazonas': 180, 'La Libertad': 280},
        'Amazonas': {'Piura': 350, 'Cajamarca': 180, 'Loreto': 450, 'San Martín': 300},
        'Loreto': {'Amazonas': 450, 'San Martín': 200, 'Ucayali': 450},
        'San Martín': {'Amazonas': 300, 'Loreto': 200, 'Huánuco': 350, 'La Libertad': 600, 'Ancash': 650},
        'La Libertad': {'Lambayeque': 200, 'Cajamarca': 280, 'San Martín': 600, 'Ancash': 350, 'Lima': 600},
        'Ancash': {'San Martín': 650, 'La Libertad': 350, 'Lima': 400, 'Huánuco': 280},
        'Huánuco': {'San Martín': 350, 'Ancash': 280, 'Lima': 350, 'Pasco': 180, 'Ucayali': 400},
        'Pasco': {'Huánuco': 180, 'Lima': 300, 'Junín': 150, 'Ucayali': 350}, 
        'Lima': {'Ancash': 400, 'La Libertad': 600, 'Huánuco': 350, 'Pasco': 300, 'Junín': 250, 'Ica': 300, 'Callao': 10},
        'Callao': {'Lima': 10, 'Ica': 200},
        'Ica': {'Lima': 300, 'Callao': 200, 'Huancavelica': 250, 'Ayacucho': 300, 'Arequipa': 500},
        'Huancavelica': {'Ica': 250, 'Ayacucho': 150, 'Junín': 200, 'Cusco': 350},
        'Junín': {'Pasco': 150, 'Lima': 250, 'Huancavelica': 200, 'Cusco': 400},
        'Ayacucho': {'Ica': 300, 'Huancavelica': 150, 'Apurímac': 150, 'Cusco': 300},
        'Apurímac': {'Ayacucho': 150, 'Cusco': 200, 'Arequipa': 400},
        'Cusco': {'Huancavelica': 350, 'Junín': 400, 'Ayacucho': 300, 'Apurímac': 200, 'Puno': 400, 'Arequipa': 500, 'Madre de Dios': 600},
        'Arequipa': {'Ica': 500, 'Apurímac': 400, 'Cusco': 500, 'Puno': 300, 'Moquegua': 200},
        'Puno': {'Cusco': 400, 'Arequipa': 300, 'Moquegua': 350, 'Tacna': 250},
        'Moquegua': {'Arequipa': 200, 'Puno': 350, 'Tacna': 150},
        'Tacna': {'Puno': 250, 'Moquegua': 150},
        'Madre de Dios': {'Cusco': 600, 'Puno': 800, 'Ucayali': 450},
        'Ucayali': {'Loreto': 450, 'Huánuco': 400, 'Pasco': 350, 'Madre de Dios': 450}
        }

    # Implementación del algoritmo de Dijkstra
    def dijkstra(grafo, inicio):
        distancias = {nodo: float('inf') for nodo in grafo}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]
        camino = {inicio: None}

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in grafo[nodo_actual].items():
                distancia = distancia_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    camino[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias, camino

# Función para reconstruir el camino más corto
    def reconstruir_camino(camino, inicio, fin):
        nodo = fin
        camino_reconstruido = []

        while nodo is not None:
            camino_reconstruido.append(nodo)
            nodo = camino[nodo]

        camino_reconstruido.reverse()
        return camino_reconstruido

    # Ejecución del algoritmo de Dijkstra
    inicio = 'Ancón'
    fin = 'Ate'
    distancias, camino = dijkstra(grafo, inicio)
    camino_reconstruido = reconstruir_camino(camino, inicio, fin)


    #ejecucion del algortimo en las distritos 
    inicio2 =  'Tacna'
    fin2 = 'Tumbes'

    distancias2, camino2 = dijkstra(grafo2,inicio2)
    camino_reconstruido2 = reconstruir_camino(camino2, inicio2, fin2)


    # Función para mostrar el camino más corto y el grafo
    def mostrar_grafo(grafo_seleccionado):
        G = nx.Graph()

        if grafo_seleccionado == 1:
            grafo_actual = grafo
            inicio_actual = inicio
            fin_actual = fin
            camino_reconstruido_actual = camino_reconstruido
        else:
            grafo_actual = grafo2
            inicio_actual = inicio2
            fin_actual = fin2
            camino_reconstruido_actual = camino_reconstruido2

        for nodo, vecinos in grafo_actual.items():
            for vecino, peso in vecinos.items():
                G.add_edge(nodo, vecino, weight=peso)

        pos = nx.spring_layout(G)
        edge_labels = nx.get_edge_attributes(G, 'weight')

        plt.figure(figsize=(10, 8))

        # Dibujar todas las aristas en gris
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=2)

        # Dibujar todas las aristas del camino más corto en rojo
        camino_edges = [(camino_reconstruido_actual[i], camino_reconstruido_actual[i + 1]) for i in range(len(camino_reconstruido_actual) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=camino_edges, edge_color='red', width=2)

        # Dibujar todos los nodos
        nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

        # Dibujar las etiquetas de los pesos de las aristas
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title(f"Camino más corto desde {inicio_actual} hasta {fin_actual}")
        plt.show()


    # Integración con Tkinter
    def mostrar_camino():
        ventana = tk.Tk()
        ventana.title("Camino más corto")
        ventana.geometry("800x400")
        ventana.configure(bg="#f0f0f0")

        estilo_label = {"font": ("Arial", 12), "background": "#f0f0f0"}

        ttk.Label(ventana, text="Resultado del algoritmo de Dijkstra", font=("Arial", 16, "bold"), background="#f0f0f0").pack(pady=10)

        ttk.Label(ventana, text=f"Distancia desde {inicio} hasta {fin}: {distancias[fin]} km", **estilo_label).pack(pady=5)
        ttk.Label(ventana, text=f"Camino más corto: {' -> '.join(camino_reconstruido)}", **estilo_label).pack(pady=5)

        ttk.Label(ventana, text=f"Distancia desde {inicio2} hasta {fin2}: {distancias2[fin2]} km", **estilo_label).pack(pady=5)
        ttk.Label(ventana, text=f"Camino más corto: {' -> '.join(camino_reconstruido2)}", **estilo_label).pack(pady=5)

        # Botón para dibujar el grafo de distritos
        ttk.Button(ventana, text="Dibujar Grafo de Distritos", command=lambda: mostrar_grafo(1), style='Accent.TButton').pack(pady=10)

        # Botón para dibujar el grafo de provincias
        ttk.Button(ventana, text="Dibujar Grafo de Provincias", command=lambda: mostrar_grafo(2), style='Accent.TButton').pack(pady=10)

        estilo_boton = ttk.Style()
        estilo_boton.configure('Accent.TButton', font=('Arial', 10), foreground='white', background='#4CAF50', padding=5)

        ventana.mainloop()



    mostrar_camino()

    resultado = "Resultado del algoritmo de Dijkstra"
    return resultado