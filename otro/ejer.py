import random

def dibujar_tablero(tablero):
     print("   ",tablero[0],"   |   ",tablero[1],"   |   ",tablero[2]) 
     print("---------|---------|-------") 
     print("   ",tablero[3],"   |   ",tablero[4],"   |   ",tablero[5]) 
     print("---------|---------|-------") 
     print("   ",tablero[6],"   |   ",tablero[7],"   |   ",tablero[8])

def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]             
    ]
    
    for combinacion in combinaciones_ganadoras:
        if all(tablero[c] == jugador for c in combinacion):
            return True
    return False

def turno_computadora(tablero, jugador_computadora):
    while True:
        movimiento = random.randint(0, 8)
        if tablero[movimiento] == " ":
            tablero[movimiento] = jugador_computadora
            break

def jugar():
    jugador_usuario = "O"
    jugador_computadora = "X"
    turno = 0
    ganador = False
    tablero = [" " for _ in range(9)] 

    dibujar_tablero(tablero)
    while not ganador:
        if turno % 2 == 0:
            print("Turno del Jugador", jugador_usuario)
            movimiento = int(input("Ingresa un número del 1 al 9: ")) - 1

            if movimiento < 0 or movimiento > 8:
                print("Movimiento inválido. Ingresa un número del 1 al 9.")
                continue

            if tablero[movimiento] != " ":
                print("Esa casilla ya está ocupada. Elige otra.")
                continue

            tablero[movimiento] = jugador_usuario
        else:
            print("Turno de la Computadora")
            turno_computadora(tablero, jugador_computadora)

        dibujar_tablero(tablero)

        if verificar_ganador(tablero, jugador_usuario):
            print("¡Felicidades! El Jugador", jugador_usuario, "ha ganado.")
            break
        elif verificar_ganador(tablero, jugador_computadora):
            print("¡La Computadora ha ganado!")
            break
        
        if " " not in tablero:
            print("¡Empate! No hay más movimientos posibles.")
            break
        
        turno += 1
        turno %=2

jugar()