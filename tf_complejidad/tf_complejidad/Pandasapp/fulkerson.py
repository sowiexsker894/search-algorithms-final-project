import tkinter as tk
from tkinter import Label, font, Canvas, Scrollbar
from graphviz import Digraph
from PIL import Image, ImageTk

def main():
    class CFordFulkerson:
        def __init__(self, lag):
            self.grafo = lag
            self.grafoResidual = {}
            self.flujos = {}
            self.flujo_maximo = 0 
            self.creaGrafoResidual()

        def dibuja(self):
            dibujo = Digraph()
            dibujo.graph_attr['rankdir'] = 'LR'

            for nodo in self.grafo.keys():
                dibujo.node(nodo)

            for nodo, lista in self.grafo.items():
                for vecino, capacidad in lista:
                    dibujo.edge(nodo, vecino, label=str(capacidad))
            return dibujo

        def dibujaFM(self):
            dibujo = Digraph()
            dibujo.graph_attr['rankdir'] = 'LR'

            for par, flujo in self.flujos.items():
                if flujo > 0:
                    original_capacidad = next((cap for vecino, cap in self.grafo[par[0]] if vecino == par[1]), 0)
                    dibujo.edge(par[0], par[1], label=f'{original_capacidad}/{flujo}')
            return dibujo

        def creaGrafoResidual(self):
            for nodo in self.grafo:
                if nodo not in self.grafoResidual:
                    self.grafoResidual[nodo] = {}
                for vecino, capacidad in self.grafo[nodo]:
                    if vecino not in self.grafoResidual:
                        self.grafoResidual[vecino] = {}
                    self.grafoResidual[nodo][vecino] = capacidad

                    if vecino not in self.grafoResidual or nodo not in self.grafoResidual[vecino]:
                        self.grafoResidual[vecino][nodo] = 0

                    if (nodo, vecino) not in self.flujos:
                        self.flujos[(nodo, vecino)] = 0
                    if (vecino, nodo) not in self.flujos:
                        self.flujos[(vecino, nodo)] = 0

        def DFS(self, fuente, sumidero, camino, visitados):
            if fuente == sumidero:
                return camino
            visitados.add(fuente)

            for vecino, capacidad in self.grafoResidual[fuente].items():
                if vecino not in visitados and capacidad > 0:
                    resultado = self.DFS(vecino, sumidero, camino + [(fuente, vecino)], visitados)
                    if resultado:
                        return resultado
            return None

        def FordFulkerson(self, fuente, sumidero):
            fm = 0
            while True:
                camino = self.DFS(fuente, sumidero, [], set())
                if camino is None:
                    break
                c = min(self.grafoResidual[nodo][vecino] for nodo, vecino in camino)

                for nodo, vecino in camino:
                    self.grafoResidual[nodo][vecino] -= c
                    self.grafoResidual[vecino][nodo] += c
                    self.flujos[(nodo, vecino)] += c
                    self.flujos[(vecino, nodo)] -= c
                fm += c
            self.flujo_maximo = fm  # Actualiza la variable de instancia con el flujo máximo
            return fm

    def mostrar_grafico(graph, title,o):
        # Renderiza el grafo en un archivo temporal
        graph.render(filename='temp_grafo', format='png', cleanup=True)
        img = Image.open('temp_grafo.png')
        img_tk = ImageTk.PhotoImage(img)

        # Crea una nueva ventana de tkinter
        ventana = tk.Toplevel()
        ventana.title("Desplazamiento entre tiendas y almacenes (Bodega uno)")

        # Crear un contenedor de Canvas con barras de desplazamiento
        frame = tk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True)
        titulo_label = Label(frame, text="flujo máximo de cargas entre tiendas y almacenes ", font=("Helvetica", 14, "bold"))
        titulo_label.pack(pady=10)
        titulo2_label = Label(frame, text=f"La maxima cantidad de productos que se pueden enviar es de={o.flujo_maximo}", font=("serif",12,"normal"))
        titulo2_label.pack(pady=10)
        
        canvas = Canvas(frame)
        scrollbar_v = Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_h = Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
        canvas.configure(yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set)

        scrollbar_v.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_h.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Muestra la imagen en el canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        canvas.image = img_tk  # Se necesita mantener una referencia para evitar que la imagen sea recolectada por el garbage collector
        canvas.config(scrollregion=canvas.bbox(tk.ALL))

    # Define el grafo inicial
    lag = {
        'A': [('B', 17), ('C', 14), ('D', 8), ('E', 7)],
        'B': [('C', 13), ('F', 17), ('H', 6), ('I', 9)],
        'C': [('I', 12), ('F', 13)],
        'D': [('G', 13), ('I', 10)],
        'E': [('H', 16), ('I', 9), ('U', 9)],
        'F': [('J', 11), ('L', 16)],
        'G': [('K', 15), ('L', 7)],
        'H': [('J', 10), ('M', 10)],
        'I': [('L', 8), ('M', 13), ('U', 13)],
        'J': [('N', 9), ('O', 12), ('Q', 14)],
        'K': [('O', 11), ('P', 7)],
        'L': [('N', 12)],
        'M': [('O', 11), ('P', 9),('Q', 11)],
        'N': [('S', 6), ('R', 8)],
        'O': [('R', 10), ('P',11)],
        'P': [('S',14)],
        'Q':[('P',12),('W', 14)], 
        'R':[('T',13)],
        'S':[( 'T',15)],
        'U':[('W',15)],	
        'W':[('T',16),('S',15)]
    }

    # Crea la instancia de CFordFulkerson y calcula el flujo máximo
    o = CFordFulkerson(lag)
    print("Flujo máximo: ", o.FordFulkerson('A', 'T'))
    print("Flujos: ", o.flujos)

    # Interfaz gráfica principal
    root = tk.Tk()
    root.title("Algoritmo de Ford-Fulkerson")
    root.geometry("400x300")  # Ajusta el tamaño de la ventana principal

    # Titulo de la ventana
    titulo = tk.Label(root, text="Algoritmo de Ford-Fulkerson", font=("Helvetica", 14, "bold"))
    titulo.pack(pady=10)

    # Fuente para los botones
    btn_font = font.Font(family='Arial', size=12, weight='bold')

    # Botones para mostrar los grafos
    btn_original = tk.Button(root, text="Mostrar Grafo Original", command=lambda: mostrar_grafico(o.dibuja(), "Grafo Original", o), font=btn_font)
    btn_original.pack(pady=10)

    btn_fm = tk.Button(root, text="Mostrar Flujo Máximo", command=lambda: mostrar_grafico(o.dibujaFM(), "Flujo Máximo", o), font=btn_font)
    btn_fm.pack(pady=10)

    # Ejecuta la interfaz gráfica
    root.mainloop()

    resultado = "Resultado del algoritmo de Ford-Fulkerson"
    return resultado


