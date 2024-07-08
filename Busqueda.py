from collections import deque
import heapq


class Busqueda:
    
        
    def bfs(entrada, salida, matriz, visitado, anterior, fila, columna):
        # Definición de la matriz y direcciones
        direcciones = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        cola = deque([entrada])
        visitado[entrada[0]][entrada[1]] = True

        while cola:
            actual = cola.popleft()
            if actual == salida:
                break

            for direccion in direcciones:
                x, y = actual[0] + direccion[0], actual[1] + direccion[1]
                if 1 <= x < fila and 1 <= y < columna and not visitado[x][y] and matriz[x][y] == 0 :
                    cola.append((x, y))
                    visitado[x][y] = True
                    anterior[x][y] = actual

        camino = []
        if visitado[salida[0]][salida[1]]:
            actual = salida
            while actual:
                camino.append(actual)
                actual = anterior[actual[0]][actual[1]]
            camino.reverse()

        return camino
    
    
    def a_estrella(entrada, salida, matriz, fila, columna):
        # Clase interna para representar un nodo en el gráfico
        class Nodo:
            def __init__(self, posicion, padre=None):
                self.posicion = posicion
                self.padre = padre
                self.g = 0  # Coste desde el inicio hasta este nodo
                self.h = 0  # Coste heurístico desde este nodo hasta el objetivo
                self.f = 0  # Coste total (g + h)

            def __eq__(self, otro):
                return self.posicion == otro.posicion

            def __lt__(self, otro):
                return self.f < otro.f

        # Función para obtener los vecinos de un nodo
        def obtener_vecinos(nodo):
            vecinos = []
            for nueva_posicion in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Movimiento arriba, abajo, izquierda, derecha
                posicion_nodo = (nodo.posicion[0] + nueva_posicion[0], nodo.posicion[1] + nueva_posicion[1])
               
                if 1 <= posicion_nodo[0] < fila and 1 <= posicion_nodo[1] < columna and matriz[posicion_nodo[0]][posicion_nodo[1]] != 1 : # Asegurarse de que no sea un obstáculo
                      
                        vecinos.append(Nodo(posicion_nodo))
            return vecinos

        # Función heurística (distancia Manhattan)
        def heuristica(nodo, fin):
            
            manhattan=abs(nodo.posicion[0] - fin.posicion[0]) + abs(nodo.posicion[1] - fin.posicion[1]) 
            if(matriz[nodo.posicion[0]][nodo.posicion[1]]=="*"):
                manhattan+=2
            elif(matriz[nodo.posicion[0]][nodo.posicion[1]]=="@"):
                manhattan+=5
            elif(matriz[nodo.posicion[0]][nodo.posicion[1]]=="!"):
                manhattan+=float("inf")
            return manhattan

        nodo_inicio = Nodo(entrada)
        nodo_fin = Nodo(salida)

        lista_abierta = []
        lista_cerrada = set()

        heapq.heappush(lista_abierta, nodo_inicio)

        while lista_abierta:
            nodo_actual = heapq.heappop(lista_abierta)
            lista_cerrada.add(nodo_actual.posicion)

            if nodo_actual == nodo_fin:
                camino = []
                while nodo_actual:
                    camino.append(nodo_actual.posicion)
                    nodo_actual = nodo_actual.padre
                camino.reverse() 
                return  camino #Devolver el camino invertido

            for vecino in obtener_vecinos(nodo_actual):
                if vecino.posicion in lista_cerrada:
                    continue

                vecino.g = nodo_actual.g + 1
                vecino.h = heuristica(vecino, nodo_fin)
                vecino.f = vecino.g + vecino.h
                vecino.padre = nodo_actual

                if any(nodo_abierto for nodo_abierto in lista_abierta if vecino.posicion == nodo_abierto.posicion and vecino.g > nodo_abierto.g):
                    continue

                heapq.heappush(lista_abierta, vecino)

        return None  # Devolver None si no se encuentra un camino