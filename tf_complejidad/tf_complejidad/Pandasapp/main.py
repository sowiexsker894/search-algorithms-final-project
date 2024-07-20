import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import heapq
import networkx as nx
import matplotlib.pyplot as plt
import dikstra
import fulkerson
import kruskal



def ejecutar_dijkstra():
    dikstra.main()

def ejecutar_fulkerson():
    fulkerson.main()

def ejecutar_kruskal():
    kruskal.main()



def mostrar_interfaz_algoritmos():
    ventana = tk.Tk()
    ventana.title("red de suministros bodega uno")
    ventana.geometry("800x500")

    titulo_label = tk.Label(ventana, text="RED DE SUMINISTROS (BODEGA UNO)", font=("Helvetica", 24, "bold"))
    titulo_label.pack(pady=20)

    estilo_botones = {"font": ("Helvetica", 14), "bg": "#4CAF50", "fg": "white", "relief": tk.RAISED, "borderwidth": 3, "width": 30, "height": 2}

    boton_dijkstra = tk.Button(ventana, text="Algoritmo de Dijkstra", command=ejecutar_dijkstra, **estilo_botones)
    boton_dijkstra.pack(pady=15)

    boton_fulkerson = tk.Button(ventana, text="Algoritmo de Ford-Fulkerson", command=ejecutar_fulkerson, **estilo_botones)
    boton_fulkerson.pack(pady=15)

    boton_kruskal = tk.Button(ventana, text="Algoritmo de Kruskal", command=ejecutar_kruskal, **estilo_botones)
    boton_kruskal.pack(pady=15)


    ventana.mainloop()

if __name__ == "__main__":
    mostrar_interfaz_algoritmos()