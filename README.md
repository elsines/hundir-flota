# hundir-flota
Juego Hundir-Flota 
Proyecto - Hundir la Flota

Juego desarrollado en Python, donde el objetivo es hundir los barcos del enemigo antes que hundan los tuyos.
El juego se ejecuta desde la consola

A modo de organzación, las comentarios los hago encima de las variables/ bucles a definir o en su defecto al lado.
Las funciones quedarán definidas en Docstring

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

  
