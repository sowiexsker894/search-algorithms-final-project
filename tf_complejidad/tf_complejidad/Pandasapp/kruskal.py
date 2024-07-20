import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

def main():
    # Leer el archivo CSV y crear el grafo
    def load_graph_from_csv(file_path, node_start, node_end):
        df = pd.read_csv(file_path)
        
        # Imprimir los encabezados para verificar
        print("Encabezados del archivo CSV:", df.columns)
        
        G = nx.Graph()
        for _, row in df.iterrows():
            if node_start <= row['Nodo1'] <= node_end and node_start <= row['Nodo2'] <= node_end:
                G.add_edge(row['Nodo1'], row['Nodo2'], weight=row['Costos'])
        return G

    nombres_calles = {}
    with open('tf_complejidad\Pandasapp\dataset\DATASETNODOSYCALLES.csv', 'r', encoding='utf-8') as archivo:
        
        lector_csv = csv.reader(archivo)
        next(lector_csv)  # Saltar la línea de encabezados
        for linea in lector_csv:
            codigo, nombre, provincia, departamento, ubi_x, ubi_y = linea
            nombres_calles[int(codigo)] = nombre

    # Funciones para dibujar los grafos
    def draw_original_graph():
        ax.clear()
        pos = nx.spring_layout(G, k=0.3, iterations=50)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=900, font_size=16, font_weight='bold', ax=ax, edge_color='grey', width=2.0)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_color='red', ax=ax)
        ax.set_title("Grafo Original con Pesos", fontsize=20)
        canvas.draw()

    def draw_mst():
        ax.clear()
        # Aplicar el algoritmo de Kruskal para encontrar el árbol de expansión mínima
        mst = kruskal_algorithm(G)

        # Encontrar el camino más corto de nodo_start a nodo_end usando el árbol de expansión mínima
        shortest_path = nx.shortest_path(mst, source=node_start, target=node_end, weight='weight')
        shortest_path_length = nx.shortest_path_length(mst, source=node_start, target=node_end, weight='weight')

        pos = nx.spring_layout(mst, k=0.3, iterations=50)
        labels = nx.get_edge_attributes(mst, 'weight')
        nx.draw(mst, pos, with_labels=True, node_color='lightgreen', node_size=900, font_size=16, font_weight='bold', ax=ax, edge_color='grey', width=2.0)
        nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels, font_size=12, font_color='red', ax=ax)
        nx.draw_networkx_edges(mst, pos, edgelist=list(zip(shortest_path, shortest_path[1:])), width=4.0, edge_color='blue')

        # Obtener los nombres de las calles para los nodos en el camino más corto
        nombres_camino = [nombres_calles.get(nodo, str(nodo)) for nodo in shortest_path]

        ax.set_title("Árbol de Expansión Mínima usando el Algoritmo de Kruskal", fontsize=20)
        ax.text(0.05, 0.95, f"Camino de expansión mínima: {' -> '.join(nombres_camino)}", transform=ax.transAxes, fontsize=12, color='blue')
        ax.text(0.05, 0.90, f"Costo mínimo posible de mantenimiento anual del camino más corto: {shortest_path_length} x 100 soles", transform=ax.transAxes, fontsize=12, color='blue')
        canvas.draw()

    # Algoritmo de Kruskal
    def kruskal_algorithm(G):
        # Ordenar las aristas por peso
        edges = sorted(G.edges(data=True), key=lambda t: t[2].get('weight', 1))
        # Crear un nuevo grafo para el MST
        mst = nx.Graph()
        # Inicializar la estructura de componentes conectados
        components = {node: node for node in G.nodes()}
        
        def find(component, u):
            if component[u] != u:
                component[u] = find(component, component[u])
            return component[u]

        def union(component, u, v):
            root_u = find(component, u)
            root_v = find(component, v)
            component[root_u] = root_v

        # Procesar cada arista
        for u, v, data in edges:
            if find(components, u) != find(components, v):
                mst.add_edge(u, v, weight=data['weight'])
                union(components, u, v)

        return mst

    # Función para solicitar el rango de nodos
    def prompt_node_range():
        global node_start, node_end
        while True:
            try:
                node_start = int(simpledialog.askstring("Entrada de Nodo Inicial", "Ingrese el nodo inicial:"))
                node_end = int(simpledialog.askstring("Entrada de Nodo Final", "Ingrese el nodo final:"))
                break
            except (ValueError, TypeError):
                tk.messagebox.showerror("Entrada inválida", "Por favor, ingrese un número entero válido.")

        update_graph()

    # Función para actualizar el grafo según el rango de nodos ingresado
    def update_graph():
        global G
        G = load_graph_from_csv(csv_file_path, node_start, node_end)
        draw_original_graph()

    # Configurar la interfaz gráfica de Tkinter
    root = tk.Tk()
    root.title("Red de Suministros usando Kruskal")

    # Crear un marco para los botones
    frame_buttons = tk.Frame(root)
    frame_buttons.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

    # Botón para actualizar el grafo
    btn_update_graph = tk.Button(frame_buttons, text="Actualizar Grafo", command=update_graph)
    btn_update_graph.pack(side=tk.LEFT, padx=10, pady=10)

    # Botón para dibujar el MST y mostrar el camino más corto
    btn_draw_mst = tk.Button(frame_buttons, text="Calcular Costo minimo de un camino a(Kruskal)", command=draw_mst)
    btn_draw_mst.pack(side=tk.RIGHT, padx=10, pady=10)

    # Crear la figura y el canvas
    fig, ax = plt.subplots(figsize=(12, 8))  # Ajustar tamaño de la figura
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Cargar el grafo desde el archivo CSV
    csv_file_path = "tf_complejidad\Pandasapp\dataset\Costominimo_por_id.csv"

    # Solicitar el rango de nodos al inicio
    prompt_node_range()

    # Inicializar con el grafo original
    draw_original_graph()

    root.mainloop()

    resultado = "Resultado del algoritmo de Kruskal"
    return resultado


