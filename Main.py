# Bibliotecas utilizadas 

import numpy as np
from random import choice, randint
from funciones import *
from variables import barcos_dicc
from variables import vidas_jugador
from variables import vidas_maquina

barcos_dicc = barcos_dicc
vidas_jugador = vidas_jugador
vidas_maquina = vidas_maquina


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
            if juego_terminado == True:
                break
            coory = solicitar_coordenada_y()
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