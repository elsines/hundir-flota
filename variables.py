
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

vidas_jugador = 20    # Representa las esloras totales, cada vez que acierta se resta 1
vidas_maquina = 20