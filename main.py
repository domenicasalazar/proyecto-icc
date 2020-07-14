#Importaciones

import time # nos va a servir para a añadir timepo de espera cuando se ejecuten ciertos algoritmos

import random # hace que la computadora elija un numero al azar

import os # Este importacion nos va a servir para "limpiar" la pantalla y cambia las intrucciones del principio del juego a las instrucciones del tablero, (Solo se va a utilizar os.sytem("clear")

#Inicio 

def inicio_juego():
  #Aca definimos lo que seria el inicio del juego, es decir lo que va a pasar cuando el jugador presione la tecla para jugar. En esta parte del codigo se define que ficha usara el jugador y la máquina y si el jugador desea ver la lista de ganadores
  print("Holi Boli Camaron con Coli")
  if input("¿Quieres ver la lista de ganadores?(s/n)")=="s":
    with open("leaderboard.txt", "r") as f:
     print(f.read())    
  while True:
    filee = input(" ¿X o O?\n") 
    filee = filee.upper()
    if filee == "X":
      mortal = "X"
      computadora = "O"
      break
    elif filee == "O":
      mortal = "O"
      computadora = "X"
      break
    else:
      print("MANO solo puedes usar o la equis o la o")
  return (mortal,computadora)

#Movimientos

#Se especifica los movimientos de la computadora y de la persona
def movimiento_mortal():
  while True:
    posiciones=[0,1,2,3,4,5,6,7,8]
    casilla=int(input("escoge una casilla porfass (Para la casilla 9 usa el 0(´cero´))"))
    if casilla not in posiciones:
      print("NADA mano USA OTRAAAA")
    else:
      if matriz[casilla-1]==" ":
        matriz[casilla-1]=mortal
        break 
      else:
        print("NADA mano USA OTRAA")

def movimiento_computadora():
  #Aca se define las posiciones que puede tomar la computadora con respecto al tablero y donde el jugador ha tomado posicion
  posiciones=[0,1,2,3,4,5,6,7,8]
  casilla=9
  parar=False
  for i in posiciones:
    copia=list(matriz)
    if copia[i]==" ":
      copia[i]=computadora
      if victoria(copia)==True:
        casilla=i
  if casilla==9:
    for j in posiciones:
      copia=list(matriz)
      if copia[j]==" ":
        copia[j]=mortal
        if victoria(copia)==True:
          casilla=j     
  if casilla==9:
    while(not parar):
      casilla=random.randint(0,8) 
      if matriz[casilla]==" ":
        parar=True
  matriz[casilla]=computadora

#Final de la partida

def empate(matriz):
  #Se define lo que se interpreta como empate, dependiendo del tablero
  empate=True
  i=0
  while (empate==True and i<9):
    if matriz[i]==" ":
      empate=False
    i=i+1
  return empate

def victoria(matriz):
  #Aca estamos definiendo cual seria e resultado dependiendo de las alineaciones de X y O en el tablero.
  if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " or matriz[0]==matriz[3]==matriz[6]!= " " or matriz[1]==matriz[4]==matriz[7]!= " " or matriz[2]==matriz[5]==matriz[8]!=" " or matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
    return True
  else:
    return False

#Creacion de Tablero

def tablero():
  #Se va a dibujar el formato del Tablero y se van a utilizar el comando de .format para que se puedan seleccionar las casillas para poder jugar.
  print("MICHI")
  print()
  print("        /            /             ")
  print(" 1 {}    /  2 {}       /  3   {}     ".format (matriz[0],matriz[1],matriz[2]))
  print("        /            /             ")
  print("-----------------------------")
  print("        /            /   ")
  print(" 4 {}    /  5 {}       /  6   {}     ".format (matriz[3],matriz[4],matriz[5]))
  print("        /            /            ")
  print("-----------------------------")
  print("        /            /            ")
  print(" 7 {}    /  8 {}       /  9   {}    ".format (matriz[6],matriz[7],matriz[8]))
  print("        /            /            ")

#Desarrollo de partida

while True:
  #en este while se espera que al iniciar/terminar el juego, se borre todo y el programa vuelva a comenzar.
    matriz=[" "]*9
    os.system("clear")
    mortal, computadora = inicio_juego()
    ganador=0

    while True:
        ganador=ganador+1
        os.system("clear")
        tablero()

        if victoria(matriz): # El comando "(matriz)" utiliza los datos del tableor para determinar su resultado
          #esta parte del codigo indica lo que debe hacer la computadora en caso el jugador gane. Esto es: mandar felicitaciones al jugador, decirle que escriba su nombre para ser incluido en la lista de ganadores(archivo) y reiniciar el juego.
            if ganador%2==0:
                print("GANASTE SIMPLE MORTAL")
                print("GAME OVER")
                print("\notra::::::------☺")
                time.sleep(2)
                partida=False
                with open("leaderboard.txt", "r") as f: 
                  content=f.read()
                with open("leaderboard.txt", "w") as f:
                  newplayer=input("Has ganado mortal, escribe tu nombre en la lista de ganadores: ")
                  f.write(content+"\n"+newplayer)
            else:
              #Aca se indica lo que sucede si no cumple con las condiciones del if anterior (pierde) y lo que hacer en ese caso (reiniciar el juego)
                print("PERDISTEE PSSS")
                print("*ya termino mano*")
                print("\ncortate el dedo")
                time.sleep(5)
                partida=False
        elif empate(matriz):#Ya no hay más lugares donde poner una ficha, la matriz de juego ya no es posible utilizarla.
        #al momento que la computadora reconoce que es un empate procede a declarar esto. 
            print("**Empateee**")
            print(" ")
            print("\nReinicio...")
            time.sleep(5)
            partida=False
        elif ganador%2==0:
          #esta parte es para que la computadora sepa que hacer despues de que el jugador haya ingresado su donde quiere poner su ficha.
            print("Estoy pensando mano")
            time.sleep(2)
            movimiento_computadora()
        else:
          movimiento_mortal()