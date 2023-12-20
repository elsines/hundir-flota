# Bibliotecas utilizadas 

import numpy as np
from random import choice

# Variables 

# Para que no lleven a confusión defino los tableros:

    # Tablero_jugador: Es el tablero que se mostrará al jugador, donde podrá ver los ataques que ha ido realizando.
    # Tablero_jugador_verificar: Es el tablero donde estan los barcos del oponente(maquina) generados de manera aleatoria.
    # Tablero_maquina: Es el tablero de la maquina donde se irán mostrando los disparos realizados por la máquina.
    # Tablero_maquina_verificar : Es el tablero donde estan los barcos del jugador generados de manera aleatoria. 


# Diccionario que representa los barcos, siendo las claves los barcos los valores las esloras.

barcos_dicc = {"b1":1, "b2":1, "b3":1, "b4":1, "b5":2, "b6":2, "b7":2, "b8":3, "b9":3, "b10":4}

# Las vidas representan la cantidad de esloras que debe acertar tanto jugardor como la máquina.
# El juego -1 cada vez que el jugador acierte.

vidas_jugador = 2    
vidas_maquina = 2

def crear_tablero():

    """
    Función sin parámetros de entrada que retorna un Numpy Array de 10 x 10 contenido por " " 
    que representa el tablero visible al jugador.
    """

    tablero = np.full(fill_value=" ", shape=(10, 10))
    
    return tablero

def colocar_barcos(barcos_dicc: dict, tablero:np.ndarray):

    """
    Función con dos parámetros de entrada :
    barcos_dicc: dict
    numpy array de 10 X 10 " "
    Bucle que itera sobre el diccionario de barcos, específicamente sobre los valores
    los valores que representan las esloras, así posiciona todos los barcos.
    Retorna un numpy array con los barcos posicionados.
    """

    for barco, eslora in barcos_dicc.items():
   
        while True:

            orientacion = choice(['N', 'S', 'E', 'O'])  # Elige la orientación de manera aleatoria.
            posicion_actual = np.random.randint(10, size=2) # Elige las coordenadas aleatorias.

            fila = posicion_actual[0]   # Determina Fila.
            col = posicion_actual[1]    # Determina columna.

            # Verifica las posiciones colindantes.
            posicion_N = tablero[fila:fila - eslora:-1, col]
            posicion_E = tablero[fila, col: col + eslora]
            posicion_S = tablero[fila:fila + eslora, col]
            posicion_O = tablero[fila, col: col - eslora:-1]

            # Condiciones que debe cumpli para colocar el barco sin que se solapen ni salgan del np.array.

            if (orientacion == 'N' and 0 <= fila - eslora < 10 and 'O' not in posicion_N or
                    orientacion == 'E' and 0 <= col + eslora < 10 and 'O' not in posicion_E or
                    orientacion == 'S' and 0 <= fila + eslora < 10 and 'O' not in posicion_S or
                    orientacion == 'O' and 0 <= col - eslora < 10 and 'O' not in posicion_O):
                
                if orientacion == 'N':
                    tablero[fila:fila - eslora:-1, col] = 'O'
                elif orientacion == 'E':
                    tablero[fila, col: col + eslora] = 'O'
                elif orientacion == 'S':
                    tablero[fila:fila + eslora, col] = 'O'
                elif orientacion == 'O':
                    tablero[fila, col: col - eslora:-1] = 'O'
                break

    return tablero # Np.Array con los barcos posicionados.

def solicitar_coordenada_x():

    """
    Función sin parámetros de entrada que retorna: Una tupla
    x : int (Representa la coordenada x del disparo del jugador)
    juego_terminado : bool True en caso de que el jugador quiera salir del juego.
    """
    juego_terminado = False
    fin = False
    while not fin:
        try:
            x = input("Tu turno: Dime la fila o introduce [0] si quieres salir: ")
            x = int(x)
            if 1 <= x <= 10:
                x = x - 1
                break
            elif x == 0:
                fin = True
                juego_terminado = True
                x = 0
                break
            else:
                print("Debe ingresar un número del 1-10.")
        except ValueError:
            print("Debe ingresar un número válido.","❌")
    return x, juego_terminado

def solicitar_coordenada_y():

    """
    Función sin parámetros de entrada que retorna: Una tupla
    y : int (Representa la coordenada x del disparo del jugador)
    juego_terminado : bool True en caso de que el jugador quiera salir del juego.
    """

    juego_terminado = False
    fin = False
    while not fin:
        try:
            y = input("Tu turno: Dime la columna o [0] para confirmar que quieres salir: ")
            y = int(y)
            if 1 <= y <= 10:
                y = y - 1
                break
            elif y == 0:
                fin = True
                juego_terminado = True
                y = 0
            else:
                print("Debe ingresar un número del 1-10.")
        except ValueError:
            print("Debe ingresar un número válido.","❌")
    return y , juego_terminado

def verificar_disparo_jugador(coor_x: int, coor_y:int, tablero_jugador:np.ndarray, tablero_jugador_verificar:np.ndarray):
    """
    Función que verifica el disparo del jugador
    Parámetros de entrada:
        coor_x : int, coordenada x del disparo
        coor_y : int, coordenada y del disparo
        Tablero_jugador: np.ndarray , Es el tablero que se mostrará al jugador, donde podrá ver los ataques que ha ido realizando.
        Tablero_jugador_verificar: np.ndarray , Es el tablero donde estan los barcos del oponente(maquina) generados de manera aleatoria.
    Retorna:
        Tableros actualizados, marcador de turno : bool
    """
    global vidas_jugador
    turno = True

    if tablero_jugador_verificar[coor_x, coor_y] == "O":
        tablero_jugador[coor_x, coor_y] = "X"
        tablero_jugador_verificar[coor_x, coor_y] = "X"
        vidas_jugador -= 1
        print("\n")
        print("\t","👏","¡Acertaste!","👏")
        print("\n")
        print(tablero_jugador)

    elif tablero_jugador_verificar[coor_x, coor_y] == "X" or tablero_jugador_verificar[coor_x, coor_y] == "~":
        print("Ya verificaste esa posición, prueba con otra.")

    elif tablero_jugador_verificar[coor_x, coor_y] == " ":
        print("\n")
        print("💧","¡Fallaste disparaste en agua!","💧")
        print("\n")
        tablero_jugador[coor_x, coor_y] = "~"
        tablero_jugador_verificar[coor_x, coor_y] = "~"
        print("\n")
        print(tablero_jugador)
        print("\n")
        turno = False

    return tablero_jugador, tablero_jugador_verificar, turno

def coordenadas_maquina():

    """
    Función que genera coordenadas aleatorias para el disparo de la máquina
    Retorna una tupla: Coordenada X y coordenada Y.
    """

    coordenadas = np.random.randint(10, size=2) # Elige las coordenadas aleatorias de la máquina

    coorx_maquina = coordenadas[0]
    coory_maquina = coordenadas[1]

    return coorx_maquina, coory_maquina

def verificar_disparo_maquina(coor_x_maquina:int, coor_y_maquina:int, tablero_maquina:np.ndarray, tablero_maquina_verificar:np.ndarray):
    """
    Función que verifica el disparo de la máquina
    Parámetros de entrada:
        coor_x_maquina : int, coordenada x del disparo
        coor_y_maquina : int, coordenada y del disparo
        Tablero_maquina: Es el tablero de la maquina donde se irán mostrando los disparos realizados por la máquina.
        Tablero_maquina_verificar : Es el tablero donde estan los barcos del jugador generados de manera aleatoria. 
    Retorna:
        Tableros actualizados, marcador de turno : bool
    """

    global vidas_maquina
    turno = True

    if tablero_maquina_verificar[coor_x_maquina, coor_y_maquina] == "O":
        tablero_maquina[coor_x_maquina, coor_y_maquina] = "X"
        tablero_maquina_verificar[coor_x_maquina, coor_y_maquina] = "X"
        vidas_maquina -= 1
        print("\n")
        print("😂","¡Te disparó y acertó!","😂")
        print("\n")
        print(tablero_maquina)

    elif tablero_maquina_verificar[coor_x_maquina, coor_y_maquina] == "X" or tablero_maquina_verificar[coor_x_maquina, coor_y_maquina] == "~":
        print("\n")
        print("Repitió disparo, le vuelve a tocar")

    elif tablero_maquina_verificar[coor_x_maquina, coor_y_maquina] == " ":
        print("💧","Tu contrincante falló, disparó en agua","💧")
        print("\n")
        tablero_maquina[coor_x_maquina, coor_y_maquina] = "~"
        tablero_maquina_verificar[coor_x_maquina, coor_y_maquina] = "~"
        turno = False
        print(tablero_maquina)
        print("\n")
    return tablero_maquina, tablero_maquina_verificar, turno

def turno_maquina(tablero_maquina:np.ndarray, tablero_maquina_verificar:np.ndarray):
    """
    Función ejecuta el turno de la máquina
    Parámetros de entrada:
        Tablero_maquina: Es el tablero de la maquina donde se irán mostrando los disparos realizados por la máquina.
        Tablero_maquina_verificar : Es el tablero donde estan los barcos del jugador generados de manera aleatoria. 
    Retorna 
        Tablero_maquina_verificar actualizado
    """
    global vidas_maquina
    print("----------Turno de tu contrincante----------")
    print("\n")
    coorx_maquina, coory_maquina = coordenadas_maquina()
    tablero_maquina, tablero_maquina_verificar, turno = verificar_disparo_maquina(coorx_maquina, coory_maquina, tablero_maquina, tablero_maquina_verificar)
    
    while turno:
        coorx_maquina, coory_maquina = coordenadas_maquina()
        tablero_maquina, tablero_maquina_verificar, turno = verificar_disparo_maquina(coorx_maquina, coory_maquina, tablero_maquina, tablero_maquina_verificar)
    
    return tablero_maquina, tablero_maquina_verificar

def perder(tablero_jugador_verificar:np.ndarray):
    """
    Imprime un mensaje cuando el jugador pierde, da la opción de volver a jugar.
    Parámetros de entrada: 
        Tablero_maquina_verificar:np.ndarray, actualizado con los diasparos realizados.
    Retorna si el juego continúa y reinicia las variables a 20. 
    """
    global vidas_jugador
    global vidas_maquina
    print("\n")
    print("\t","🤯","Perdiste","🤯","\t")
    print("\n")
    print("------Más suerte la próxima vez------")
    print("\n")
    print("  Estos eran los barcos de tu rival")
    print("\n")
    print(tablero_jugador_verificar)
    print("\n")
    jugar = int(input("Presiona 1 si quieres volver a jugar o cualquier tecla para salir: "))
    if jugar == 1:
        vidas_maquina = 20
        vidas_jugador = 20
        inicio()
    else:
        print("\n")
        print("\t","🚤","Adios","🚤","\t")
        print("\n")
        print("---------Vuelve Pronto---------")
        print("\n")
def ganar():
    """
    Imprime un mensaje cuando el jugador pierde, da la opción de volver a jugar.
    Sin parámetros de entrada

    Retorna si el juego continúa y reinicia las variables a 20. 
    """
    global vidas_jugador
    global vidas_maquina
    print("\t","\t","⭐","\t","\t")
    print("\n")
    print("\t","🤩","Enhorabuena","🤩","\t")
    print("\n")
    print("**************GANASTE**************")
    print("\n")
    print(" ⭐ "*9)

    jugar = int(input("Presiona 1 si quieres volver a jugar o cualquier tecla para salir: "))
    if jugar == 1:
        vidas_maquina = 20
        vidas_jugador = 20
        inicio()
    else:
        print("\n")
        print("\t","🚤","Adios","🚤","\t")
        print("\n")
        print("---------Vuelve Pronto---------")
        print("\n")
def inicio():
    """
    Función principal que inicia el bucle del juego
    Sin parámetros de entrada.
    """
    tablero_jugador = crear_tablero()
    tablero_maquina = crear_tablero()
    tablero_jugador1 = crear_tablero()
    tablero_maquina1 = crear_tablero()
    tablero_jugador_verificar = colocar_barcos(barcos_dicc, tablero_jugador1)
    tablero_maquina_verificar = colocar_barcos(barcos_dicc, tablero_maquina1)

    print("\n")
    print("*" * 75)
    print("\t\t","🚢"," Bienvenido al juego de Hundir la Flota ", "🚢","\t\t")
    print("*" * 75)
    print("""
El juego consiste en hundir la flota del contrincante. 
Para ello se generan los barcos de ambos jugadores de manera aleatoria.

Cada uno tiene:
    1 barco de 4 esloras.
    2 barcos de 3 esloras.
    3 barcos de 2 esloras.
    4 barcos de una eslora.
        
Los barcos estarán posicionados en el tablero de manera que te permita 
identificarlos por filas(1-10) y columnas(1-10).

Cada jugador dispone de un turno de disparo que se irá alternando. Para
hacerlo dirá las coordenadas. Por ejemplo Fila = 1 , Columna = 3 significa
que el disparo corresponde a la casilla que se encuentra en esa coordenada.

Al disparar, el sistema comprobará en el tablero de su contrincante si es 
agua o hundiste una eslora del barco. Si aciertas, tu turno continúa, de lo
contrario, pasará el turno a tu contrincante. 

Finalmente, gana el jugador que antes consigue hundir la flota del otro. 
   """)
    print("Estas son las posiciones de tus barcos, son las que tu contrincante debe adivinar.")
    print("\n")
    print("--------------- Tus Barcos ---------------")
    print("\n")
    print(tablero_maquina_verificar)
    print("\n")

    juego_terminado = False

    while not juego_terminado:
        if vidas_jugador == 0:
                juego_terminado = True
                ganar()
                break
        if vidas_maquina == 0:
                juego_terminado = True
                perder(tablero_jugador_verificar)
                break
        turno_jugador = True
        while turno_jugador:
            coorx, juego_terminado = solicitar_coordenada_x()
            coory, juego_terminado = solicitar_coordenada_y()
            tablero_jugador, tablero_jugador_verificar, turno_jugador = verificar_disparo_jugador(coorx, coory,tablero_jugador,tablero_jugador_verificar)
        else:
            tablero_maquina, tablero_maquina_verificar = turno_maquina(tablero_maquina, tablero_maquina_verificar)
    else:
        print("\n")
        print("\t","🚤","Adios","🚤","\t")
        print("\n")
        print("---------Vuelve Pronto---------")
        print("\n")
inicio()
