from collections import deque
from Mapa import Mapa
from Busqueda import Busqueda


def menu_mapa():
    print("\t\t \033[32m ***Elija el tipo de mapa que desea utilizar*** \033[0m")
    print("1. El mapa es aleatorio en la generacion de calles y casas. \n")
    print("2. En esta opcion siempre se genera la misma matriz, se recomienda usar este si desea hacer pruebas.\n")
    opcion=int(input("Opcion: "))
    return opcion

def menu_busqueda():
    print("\n\t\t \033[31m Elija el algoritmo que desea usar: \033[0m")
    print("1. BFS\t\t (Los obstaculos no poseen un peso distinto)")
    print("2. A-Star\t (Los obstaculos si poseen pesos distintos)")
    opcion=int(input("Opcion 1 o 2: "))
    return opcion

def main():
    print()
    opcion=menu_mapa()
    
    if(opcion!=1 and opcion!=2):
        while(opcion!=1 and opcion!=2):
            print("\t\t \033[31m Introdujiste una opcion incorrecta. \033[0m")
            opcion=menu_mapa()
    elif(opcion==1):        
        fila=int(input("Introducir la cantidad de filas: "))
        columna=int(input("Introducir la cantidad de columnas: "))
        
    else:
        fila=10
        columna=10
        
    #Creo mi objeto, mapeador es un objeto mapa
    mapeador= Mapa(fila,columna)
    
    #mapeador.crear_mapa crea los caminos y edificios y eso retorna el mapa para guardar en mapp
    mapp=mapeador.crear_mapa(opcion)
    
    #Imprime la matriz inicial para que el usuario pueda ver como 
    mapeador.imprimir_mapa(mapp)
    
    print()
    print("\t\t \033[31m Inicio \033[0m")
    x_entrada = int(input("Introduzca su posición de entrada en columna: "))
    y_entrada = int(input("Introduzca su posición de entrada en fila: "))
    print()
    entrada = (y_entrada, x_entrada)
    mapp[y_entrada][x_entrada]='E'
    
    print("\t\t \033[31m Fin \033[0m")
    x_salida = int(input("Introduzca su posición de salida en columna: "))
    y_salida = int(input("Introduzca su posición de salida en fila: "))
    print()
    salida = (y_salida, x_salida)
   
    buscar=Busqueda
    
    mapeador.agregar_interferencia(mapp)
    
    opcion=menu_busqueda()
    
    if(opcion!=1 and opcion!=2):
        while(opcion!=1 and opcion!=2):
            print("\t\t \033[31m Introdujiste una opcion incorrecta. \033[0m")
            opcion=menu_busqueda()
            print()
    elif(opcion==1):        
        camino = buscar.bfs( entrada, salida, mapp, mapeador.visitado, mapeador.anterior, fila, columna)
        
    else:
        camino = buscar.a_estrella( entrada, salida, mapp, fila, columna)

    if camino:
        
        for (x, y) in camino:
            if (x, y) == entrada :
                mapp[x][y] = 'E'
            elif (x, y) == salida:
                mapp[x][y] = 'S'
            elif (x, y) != entrada or (x, y) != salida:
                mapp[x][y]= '#'
        mapeador.imprimir_mapa(mapp)
        print("\033[32mA llegado a su destino\033[0m")
    else:
        mapeador.imprimir_mapa(mapp)
        print("\033[31mNo hay forma de llegar al lugar, una pena ='( \033[0m")
        

if __name__ == "__main__":
    main()
