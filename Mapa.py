import random
# ve como usar los for de manera mas optima 


def Menu_obstaculo():
    print("\033[31m****Durante el recorrido en la ciudad pueden pasar muchas cosas que generen retrasos a los viajes****\033[0m")
    print("1. Charcos de agua (*)\t\t(se puede pasar, aunque eligiria no ensuciar mi vehiculo) ")
    print("2. Baches (@) \t\t\t(Si fuese posible no me gustaria pasar por ahi, solo si no queda otra opcion o sea totalmente necesario)")
    print("3. Derrumbe o bloqueo (!) \t(No es posible pasar de ninguna manera)\n")

def validacion_obstaculo(i,matriz):
    x_obstaculo=int(input(f"{i+1}. Columna del obstaculo: "))
    y_obstaculo=int(input(f"{i+1}. Fila del obstaculo: "))
    
    while(matriz[y_obstaculo][x_obstaculo]!=0):
        print("\t\t \033[31m Introdujiste una opcion incorrecta. \033[0m")
        x_obstaculo=int(input(f"{i+1}. Columna del obstaculo: "))
        y_obstaculo=int(input(f"{i+1}. Fila del obstaculo: "))
        print()
    return x_obstaculo,y_obstaculo
    

class Mapa:
    
        
        def __init__(self,fila,columna):
            
            self.fila=fila
            self.columna=columna
            self.mapaRandom = [[0]*self.columna for i in range(self.fila)]
            self.visitado = [[False] * self.columna for i in range(self.fila)] 
            self.anterior = [[None] * self.columna for i in range(self.fila)]
            
        def crear_mapa(self,opcion):
            
            
            
            if(opcion==1):
                
                densidad=float(input("Introduzca la densidad entre 0 y 1 (se recomienda 0.75): "))
                PFila=int(densidad*8)
                densidad=int(self.fila*self.columna*densidad/4)
                
                
                self.mapaRandom= [[0]*self.columna for i in range(self.fila)]
                #Aca estas creando la numeracion de la primera fila y primera columna 
                for i in range(self.fila):
                    for j in range(self.columna):
                        if(i==0):
                            self.mapaRandom[i][j]=j
                        elif(j==0):
                            self.mapaRandom[i][j]=i
                            
                #Este fracmento de codigo saque de youtube https://www.youtube.com/watch?v=vbJqAFxHWOE, no use el laberinto que hice en el segundo challenge por que este es mas lindo su generacion de caminos, y fui adaptando a python
                for i in range(densidad):
                    x = random.randint(2, self.fila - 2)
                    x = int((x // 2) * 2)
                    y = random.randint(2, self.columna - 2)
                    y = int((y // 2) * 2)
                    self.mapaRandom[x][y] = 1
                    for i in range(PFila):
                        direcciones_creador = [(x, y + 2), (x, y - 2), (x + 2, y), (x - 2, y)]
                        aux = random.randint(0, 3)
                        dx, dy = direcciones_creador[aux]
                        if 0 <= dx < self.fila and 0 <= dy < self.columna and self.mapaRandom[dx][dy] == 0:
                            self.mapaRandom[dx][dy] = 1
                            self.mapaRandom[x + (dx - x) // 2][y + (dy - y) // 2] = 1
                return self.mapaRandom
                #Hasta este punto es de youtube
            else:
                matriz = [
                            [0,1,2,3,4,5,6,7,8,9],
                            [1,0,0,0,0,0,0,1,1,1],
                            [2,0,1,0,1,0,0,1,0,1],
                            [3,0,1,0,1,0,0,1,0,0],
                            [4,0,1,0,1,0,1,1,1,0],
                            [5,0,1,0,1,0,1,0,0,0],
                            [6,0,1,0,1,0,1,0,1,0],
                            [7,0,0,0,0,0,0,0,0,0],
                            [8,0,1,0,1,1,0,1,1,0],
                            [9,1,1,0,0,0,0,0,0,0]]
                return matriz
                         
        def imprimir_mapa(self,matriz):
            #Imprime la matriz
            for i, fila in enumerate(matriz):
                
                
                for j, celda in enumerate(fila):
                    
                
                    if i == 0 or j == 0:
                        if(j==0):
                            print(f'\033[32m{celda}\033[0m\t', end=' ')
                        else:    
                            print(f'\033[32m{celda}\033[0m ', end=' ')
                        
                        if(i==0 and j==len(fila)-1):
                            print()
                            
                    elif matriz[i][j]==1:                                           # El 1 indica los edificios 
                        print(f'\033[31m{celda}\033[0m ', end=' ')
                    elif matriz[i][j]=='#':                                         # El # indica el recorrido que uso, se imprime en amarillo
                        print(f'\033[33m{celda}\033[0m ', end=' ')
                    elif matriz[i][j]=='*':                                         # El * indica los obstaculos, se imprime en azul
                        print(f'\033[34m{celda}\033[0m ', end=' ')
                    elif matriz[i][j]=='@':                                         # El @ indica los obstaculos, se imprime en 
                        print(f'\033[34m{celda}\033[0m ', end=' ')    
                    elif matriz[i][j]=='!':                                         # El ! indica los obstaculos, se imprime en 
                        print(f'\033[34m{celda}\033[0m ', end=' ')
                        
                    elif matriz[i][j]=='S' or matriz[i][j]=='E':                    # La S indica la llegada y la E indica la salida
                        print(f'\033[35m{celda}\033[0m ', end=' ')
                        
                        
                    else:
                        
                        print(f"{celda} ", end=' ')                                 # Si no es ninguno de los anteriores imprime 0 en blanco que es el camino
                print()
                
        def agregar_interferencia(self,matriz):
            obstaculos=int(input("\033[32m¿Cuantos obstaculos desea colocar? \033[0m\nObstaculos: "))
            if(obstaculos>0):
                Menu_obstaculo()
            
            
            for i in range(obstaculos):
                tipo=int(input(f"Elija el tipo de obstaculo {i+1}: "))
                tipos=[1,2,3]
                
                while(tipo not in tipos):
                    print()
                    print("\t\t \033[31m Introdujiste una opcion incorrecta. \033[0m")
                    print()
                    Menu_obstaculo()
                    tipo=int(input(f"Elija el tipo de obstaculo {i+1}: "))
                
                if(tipo==1):
                    x_obstaculo,y_obstaculo=validacion_obstaculo(i,matriz)
                    print()
                    matriz[y_obstaculo][x_obstaculo]='*'
                elif(tipo==2):    
                    x_obstaculo,y_obstaculo=validacion_obstaculo(i,matriz)
                    print()
                    matriz[y_obstaculo][x_obstaculo]='@'
                elif(tipo==3):
                    x_obstaculo,y_obstaculo=validacion_obstaculo(i,matriz)
                    print()
                    matriz[y_obstaculo][x_obstaculo]='!'
                                               
                