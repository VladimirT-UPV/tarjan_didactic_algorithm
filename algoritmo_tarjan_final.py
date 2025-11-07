
#? Importe de librerías
import networkx as nx
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

inicio = time.time()


#* Definición del grafo
class Grafo:
    #? Contructor del objeto
    def __init__(self):
        self.nodos = {}

    #? Métodos de la clase
    def agregar_nodo(self, nodo):
        """Agrega un nodo (si no existe)"""
        if nodo not in self.nodos:
            self.nodos[nodo] = []

    def agregar_arista(self, nodo_origen, nodo_destino):
        """Agrega una conexión (arista) entre dos nodos"""
        self.agregar_nodo(nodo_origen)
        self.agregar_nodo(nodo_destino)
        
        if nodo_destino not in self.nodos[nodo_origen]:
            self.nodos[nodo_origen].append(nodo_destino)
        

    def obtener_nodos(self):
        """Retorna la lista de nodos"""
        return list(self.nodos.keys())

    def obtener_vecinos(self, nodo):
        """Retorna los vecinos de un nodo"""
        return self.nodos.get(nodo, [])

    def mostrar_grafo(self):
        """Imprime la lista de adyacencia del grafo"""
        print("Representación del Grafo (Lista de Adyacencia):")
        for nodo, vecinos in self.nodos.items():
            print(f"  {nodo} -> {vecinos}")

#* Creación del grafo ejemplificado
mi_grafo = Grafo()
#? SCC 1: Capa de Modelos/Datos
mi_grafo.agregar_arista('Modelo_Usuario', 'DAO_SQL')
mi_grafo.agregar_arista('DAO_SQL', 'ORM_Base')
mi_grafo.agregar_arista('ORM_Base', 'Modelo_Usuario')

#? SCC 2: Capa de Servicios/Lógica
mi_grafo.agregar_arista('Servicio_Auth', 'Servicio_Logs')
mi_grafo.agregar_arista('Servicio_Logs', 'Servicio_Cache')
mi_grafo.agregar_arista('Servicio_Cache', 'Servicio_Auth')

#? SCC 3: Capa de Presentación/UI
mi_grafo.agregar_arista('Pagina_Inicio', 'Componente_Header')
mi_grafo.agregar_arista('Componente_Header', 'Componente_Footer')
mi_grafo.agregar_arista('Componente_Footer', 'Pagina_Inicio')


lista_adyacencia = mi_grafo.nodos
Graphic_nx = nx.DiGraph(lista_adyacencia)
pos = nx.kamada_kawai_layout(Graphic_nx)

#? Configuración de la interfaz Tkinter
root = tk.Tk()
root.title("Algoritmo de Tarjan - Versión Adaptada")
root.geometry("1200x600")

#? Marco principal
marco_principal = tk.Frame(root)
marco_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

#? Configurar grid para dividir la pantalla a la mitad
marco_principal.grid_columnconfigure(0, weight=1)
marco_principal.grid_columnconfigure(1, weight=1)
marco_principal.grid_rowconfigure(0, weight=1)

#? Marco para la visualización del grafo
marco_grafo = tk.Frame(marco_principal)
marco_grafo.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

#? Marco para la salida de texto
marco_texto = tk.Frame(marco_principal)
marco_texto.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

#* Configuración del área de texto para mostrar los SCCs
texto_salida = tk.Text(marco_texto, wrap=tk.WORD, font=("Consolas", 10))
scrollbar = tk.Scrollbar(marco_texto, orient=tk.VERTICAL, command=texto_salida.yview)
texto_salida.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
texto_salida.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#* Configuración de la figura de matplotlib para el grafo
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=marco_grafo)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

#? Variables globales para controlar la ejecución
ejecutando = False
sccs_encontrados = []

#? Algoritmo de Tarjan para encontrar SCCs
def tarjan_scc(grafo_dict):
    """Algoritmo de Tarjan para encontrar Componentes Fuertemente Conectados (SCCs)"""
    
    global sccs_encontrados
    sccs_encontrados = []
    
    index = 0
    pila = []
    indices = {}
    lowlinks = {}
    en_pila = {}
    
    def fuerte_conexo(v):
        nonlocal index
        indices[v] = index
        lowlinks[v] = index
        index += 1
        pila.append(v)
        en_pila[v] = True
        
        #* Visualización: nodo siendo procesado
        visualizar_grafo({v: 'yellow'}, f"Procesando nodo {v}")
        
        for w in grafo_dict.get(v, []):
            if w not in indices:
                fuerte_conexo(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif en_pila[w]:
                lowlinks[v] = min(lowlinks[v], indices[w])
        
        if lowlinks[v] == indices[v]:
            scc = []
            while True:
                w = pila.pop()
                en_pila[w] = False
                scc.append(w)
                if w == v:
                    break
            
            sccs_encontrados.append(scc)
            
            colores_scc = {}
            for nodo in scc:
                colores_scc[nodo] = 'green'
            visualizar_grafo(colores_scc, f"SCC encontrado: {scc}")
            
            texto_salida.insert(tk.END, f"SCC encontrado: {scc}\n")
            texto_salida.see(tk.END)
            root.update()
    
    for v in grafo_dict:
        if v not in indices:
            fuerte_conexo(v)
    
    return sccs_encontrados

#? Función para visualizar el grafo con colores
def visualizar_grafo(colores_nodos, titulo=""):
    """Visualiza el grafo con colores específicos para cada nodo"""
    ax.clear()
    
    colores = []
    for nodo in Graphic_nx.nodes():
        if nodo in colores_nodos:
            colores.append(colores_nodos[nodo])
        else:
            colores.append('lightgray')
    
    nx.draw(Graphic_nx, pos, ax=ax, with_labels=True, node_color=colores, 
            node_size=2000, font_weight='bold', font_size=8, 
            arrows=True,                                    
            arrowstyle='-|>',                                
            edge_color='gray',
            width=2)
    
    ax.set_title(titulo)
    canvas.draw()
    root.update()
    time.sleep(0.5)

#? DFS modificado para visualización paso a paso
def dfs_visual(grafo_dict, nodo_inicio):
    """DFS con visualización paso a paso"""
    visitados = set()
    pila = [nodo_inicio]
    colores_actuales = {}
    
    # Limpieza del área de texto al inicio del DFS
    texto_salida.delete(1.0, tk.END)
    texto_salida.insert(tk.END, "****** DFS Paso a Paso ********\n")
    
    while pila:
        nodo_actual = pila.pop()
        if nodo_actual not in visitados:
            # Nodo siendo visitado
            colores_actuales[nodo_actual] = 'blue'
            visualizar_grafo(colores_actuales, f"Visitando nodo {nodo_actual}")
            
            visitados.add(nodo_actual)
            
            # Procesar vecinos
            for vecino in reversed(grafo_dict.get(nodo_actual, [])):
                if vecino not in visitados:
                    pila.append(vecino)
                    # Vecino por visitar
                    colores_actuales[vecino] = 'yellow'
                    visualizar_grafo(colores_actuales, f"Agregando vecino {vecino}")
    
    # Limpieza de colores al finalizar DFS
    visualizar_grafo({}, "DFS Finalizado")

#? Función para ejecutar todo el proceso
def ejecutar_algoritmos():
    global ejecutando, sccs_encontrados
    
    if ejecutando:
        return
        
    ejecutando = True
    btn_ejecutar.config(state=tk.DISABLED)
    
    # Limpiar el área de texto
    texto_salida.delete(1.0, tk.END)
    
    # Ejecutar DFS
    texto_salida.insert(tk.END, "****** DFS Paso a Paso ********\n")
    texto_salida.see(tk.END)
    root.update()
    
    dfs_visual(mi_grafo.nodos, 'Modelo_Usuario')
    
    time.sleep(1)
    
    # Ejecutar algoritmo de Tarjan
    texto_salida.insert(tk.END, "\n******* Algoritmo de Tarjan - Encontrando SCCs ******\n")
    texto_salida.see(tk.END)
    root.update()
    
    sccs_encontrados = tarjan_scc(mi_grafo.nodos)
    
    # Mostrar resultados finales
    texto_salida.insert(tk.END, f"\nSCCs encontrados: {sccs_encontrados}\n")
    texto_salida.see(tk.END)
    
    # Visualización final
    colores_finales = {}
    colores_scc = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'olive', 'cyan']
    
    for i, scc in enumerate(sccs_encontrados):
        color = colores_scc[i % len(colores_scc)]
        for nodo in scc:
            colores_finales[nodo] = color
    
    visualizar_grafo(colores_finales, "SCCs Finales")
    

    
    ejecutando = False
    btn_ejecutar.config(state=tk.NORMAL)

#? Botón para ejecutar los algoritmos
btn_ejecutar = tk.Button(root, text="Ejecutar Algoritmos", command=ejecutar_algoritmos)
btn_ejecutar.pack(pady=10)

#* Visualización inicial del grafo
visualizar_grafo({}, "Grafo Inicial")

#* Iniciar la aplicación
root.mainloop()