import networkx as nx

def min_conexiones_vuelos(aeropuertos, conexiones, aeropuerto_inicio):
    
    G = nx.DiGraph() #Creacion de Grafo dirigido
    
    G.add_nodes_from(aeropuertos) #Agregar nodos al grafo
    
    #Agregar conexiones de vuelos como arcos en el grafo
    for conexion in conexiones:
        origen, destino = conexion
        G.add_edge(origen, destino)
    
    #Utilizar BFS para encontrar el camino más corto desde el aeropuerto de inicio a todos los demás aeropuertos
    shortest_paths = nx.single_source_shortest_path_length(G, source=aeropuerto_inicio) 
    
    min_conexiones = max(shortest_paths.values()) #Valor maximo de shortest para hallar el valor minimo de conexion
    
    return min_conexiones #Retorna el número mínimo de conexiones de vuelos adicionales necesarias


aeropuertos_colombia = [
    {"codigo": "BOG", "nombre": "Aeropuerto Internacional El Dorado - Bogotá"},
    {"codigo": "MDE", "nombre": "Aeropuerto Internacional José María Córdova - Medellín"},
    {"codigo": "CTG", "nombre": "Aeropuerto Internacional Rafael Núñez - Cartagena"},
    {"codigo": "CLO", "nombre": "Aeropuerto Internacional Alfonso Bonilla Aragón - Cali"},
    {"codigo": "SMR", "nombre": "Aeropuerto Internacional Simón Bolívar - Santa Marta"},
    {"codigo": "ADZ", "nombre": "Aeropuerto Internacional Gustavo Rojas Pinilla - San Andrés"},
    {"codigo": "BAQ", "nombre": "Aeropuerto Internacional Ernesto Cortissoz - Barranquilla"},
    {"codigo": "CUC", "nombre": "Aeropuerto Internacional Camilo Daza - Cúcuta"},
    {"codigo": "PEI", "nombre": "Aeropuerto Internacional Matecaña - Pereira"},
    {"codigo": "VVC", "nombre": "Aeropuerto Internacional Vanguardia - Villavicencio"}
]

conexiones_colombia = [
    ("BOG", "MDE"),
    ("BOG", "CTG"),
    ("MDE", "CLO"),
    ("CLO", "BOG"),
    ("BOG", "SMR"),
    ("SMR", "ADZ"),
    ("BOG", "BAQ"),
    ("BAQ", "CUC"),
    ("CUC", "PEI"),
    ("PEI", "VVC")
]

aeropuerto_inicio = "BOG"
print(f"Codigo de Aeropuerto de inicio: {aeropuerto_inicio}")
print("Nombre del Aeropuerto de inicio:", next(aeropuerto['nombre'] for aeropuerto in aeropuertos_colombia if aeropuerto['codigo'] == aeropuerto_inicio))
print(f"Número mínimo de conexiones de vuelos adicionales necesarias: {numero_minimo_conexiones}")
