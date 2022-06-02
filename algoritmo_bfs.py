# Importamos la libreria Queue
from queue import Queue


class Grafo:
    """
    Clase Grafo, esta clase representara a un grafo junto a sus atributos y funcionalidades.

     Atributos
    ----------
        m_numero_nodos : int
            Cantidad de nodos que tendra el grafo.
        m_nodos : int
            Rango de nodos sobre los que trabajara el grafo.
        m_dirigido : boolean
            Tipo de nodo dirigido o no dirigido.
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos


     Métodos
    ----------

    __init__(self, num_de_nodos, dirigido=True)
        Este metodo funcionara como el constuctor de la clase `Grafo()`, recibe el Numero de nodos (m_num_nodos),
        crea el rango de nodos (numero_nodos), determina el tipo de grafo si es dirigido o no dirigido (m_dirigido) y
        creara el diccionario de la lista de adyacencia.

    agregar_borde(self, nodo1, nodo2, peso=1)
        Genera los bordes de la lista de adyacencia agregando el nodo 2 a la lista de adyacencia del nodo 1.

    Imprimir_lista_adyacencia(self)
        Imprime el grafo generado en base a la lista de adyacencia.

    bfs_transversal(self, nodo_de_inicio)
        Método que imprime el recorrido BFS de un vértice fuente dado.
    """

    def __init__(self, numero_nodos, dirigido=True):
        """
        Este metodo funcionara como el constuctor de la clase Grafo(), recibe el Numero de nodos (m_num_nodos),
        crea el rango de nodos (numero_nodos), determina el tipo de grafo si es dirigido o no dirigido (m_dirigido) y
        creara el diccionario de la lista de adyacencia.


        Parametros
        ----------
        m_numero_nodos : int
            Cantidad de nodos que tendra el grafo.
        m_nodos : int
            Rango de nodos sobre los que trabajara el grafo.
        m_dirigido : boolean
            Tipo de nodo dirigido o no dirigido.
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos
        """
        # Se asigna el valor del numero de nodos a través del parametro recibido
        self.m_numero_nodos = numero_nodos
        # Se genera el rango de nodos en base a m_numero_nodos
        self.m_nodos = range(self.m_numero_nodos)
        # se define el tipo de grafo
        self.m_dirigido = dirigido
        # Se crea el diccionario de la lista de adyacencia
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

    def agregar_borde(self, nodo1, nodo2, peso=1):
        """
        Este método define el borde del grafo.
        Recibe como parametros el nodo1, el nodo2 y el peso cuyo valor por defecto es de 1.
        Posteriormente se agregan a la lista de adyacencia del nodo al que corresponde.

        Parametros
        ----------
        nodo1 : int
        nodo2 : int
        peso: int

        Retorno
        -------
        Nada 
        """
        # Agrega el nodo 2 a la lista de adyacencia del nodo 1.
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        if not self.m_dirigido:
            # Agrega el nodo 1 a la lista de adyacencia del nodo 2.
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    def Imprimir_lista_adyacencia(self):
        """
        Este método imprime el grafo generado a través de la lista de adyacencia.

        Parametros
        ----------
        Nada

        Retorno
        -------
        Nada 
        """
        # recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # imprime el cada nodo almacenado en la lista de adyacencia.
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def bfs_transversal(self, nodo_de_inicio):
        """
        Este método imprime el recorrido BFS de un nodo inicial. Genera una lista de colas visitadas 
        y muestra el recorrido realizado hasta llegar al objetivo. 

        Parametros
        ----------
        nodo_de_inicio : int
        visitado : int
        cola : int

        Retorno
        -------
        Nada 
        """

        visitado = set()
        cola = Queue()

        # Agrega los nodos visitados a la cola para evitar bucles
        cola.put(nodo_de_inicio)

        # Añade el nodo_de_inicio a la lista de visitas
        visitado.add(nodo_de_inicio)

        # Bucle de los nodos que se ejecutara si la cola no se encuentra vacia.
        while not cola.empty():
            # Asigna el nodo de la cola al nodo_actual
            nodo_actual = cola.get()
            # Imprime los nodos.
            print(nodo_actual, end=" ")

            # Bucle de obtención del siguiente nodo de la lista de adyacencia
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                # En caso de que un nodo adyaente haya sido visitado
                if siguiente_nodo not in visitado:
                    # Se agrega el nodo a la cola
                    cola.put(siguiente_nodo)
                    # Se agrega el nodo a la lista de visitados
                    visitado.add(siguiente_nodo)


if __name__ == "__main__":

    """
    Dentro de la clase main se instancia a la clase Grafo para acceder a sus metodos.
    Se crearan en este caso 5 casos de prueba para comprobar el funcionamiento del programa.
    """

    print(" Caso de Prueba 1")
    grafo_prueba1 = Grafo(5, dirigido = False) # instancia de la clase Grafo
    grafo_prueba1.agregar_borde(0, 1,3) #  Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo_prueba1.agregar_borde(0, 2,2) #  Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo_prueba1.agregar_borde(1, 2,1) #  Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo_prueba1.agregar_borde(1, 4,3) #  Se agrega los bordes del grafo con valor peso = 1 por defecto
    grafo_prueba1.agregar_borde(2, 3,1) #  Se agrega los bordes del grafo con valor peso = 1 por defecto

    
    grafo_prueba1.Imprimir_lista_adyacencia() #Se imprime la lista de adyacencia
 
    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    grafo_prueba1.bfs_transversal(0)
    print()

    print(" Caso de Prueba 2")
    grafo_prueba2 = Grafo(4, dirigido = False) # instancia de la clase `Grafo`
    grafo_prueba2.agregar_borde(1, 2) # Se agrega los bordes
    grafo_prueba2.agregar_borde(0, 2) # Se agrega los bordes
    grafo_prueba2.agregar_borde(0, 1) # Se agrega los bordes
    grafo_prueba2.agregar_borde(1, 3) # Se agrega los bordes
    

    grafo_prueba2.Imprimir_lista_adyacencia() #Se imprime la lista de adyacencia

    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 0)")
    #Imprime toda la lista de colas
    grafo_prueba2.bfs_transversal(0)
    print()

    print(" Caso de Prueba 3")
    grafo_prueba3 = Grafo(7, dirigido = False) # instancia de la clase `Grafo`
    grafo_prueba3.agregar_borde(6, 1) # Se agrega los bordes
    grafo_prueba3.agregar_borde(2, 1) # Se agrega los bordes
    grafo_prueba3.agregar_borde(3, 4) # Se agrega los bordes
    grafo_prueba3.agregar_borde(0, 1) # Se agrega los bordes
    grafo_prueba3.agregar_borde(1, 3) # Se agrega los bordes
    grafo_prueba3.agregar_borde(4, 2) # Se agrega los bordes
    grafo_prueba3.agregar_borde(5, 3) # Se agrega los bordes

    grafo_prueba3.Imprimir_lista_adyacencia() #Se imprime la lista de adyacencia

    print("A continuación se muestra el recorrido primero en anchura a partir del vértice 1)")
    #Imprime toda la lista de colas
    grafo_prueba3.bfs_transversal(1)
    print()


