
#Importaciones
import time
import random
import os

#Inicio de Juego y Definicion de ficha

def inicio_juego():
  print("Holi Boli Camaron con Coli")
  while True:
    ficha = input(" ¿X o O?\n") 
    ficha = ficha.upper()
    if ficha == "X":
      mortal = "X"
      computadora = "O"
      break
    elif ficha == "O":
      mortal = "O"
      computadora = "X"
      break
    else:
      print("MANO solo puedes usar o la equis o la o")
  return (mortal,computadora)


#Creacion de Tablero

def tablero():
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


#Definir finales de partida

def empate(matriz):
  empate=True
  i=0
  while (empate==True and i<9):
    if matriz[i]==" ":
      empate=False
    i=i+1
  return empate

def victoria(matriz):
  if (matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " or matriz[0]==matriz[3]==matriz[6]!= " " or matriz[1]==matriz[4]==matriz[7]!= " " or matriz[2]==matriz[5]==matriz[8]!=" " or matriz[0]==matriz[4]==matriz[8]!=" " or matriz[2]==matriz[4]==matriz[6]!=" "):
    return True
  else:
    return False

#Movesss

def movimiento_mortal():
  while True:
    posiciones=[0,1,2,3,4,5,6,7,8]
    casilla=int(input("escoge una casilla porfass "))
    if casilla not in posiciones:
      print("NADA mano USA OTRAAAA")
    else:
      if matriz[casilla-1]==" ":
        matriz[casilla-1]=mortal
        break 
      else:
        print("NADA mano USA OTRAA")

def movimiento_computadora():
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

#Desarrollo de partida
while True:
    matriz=[" "]*9
    os.system("clear")
    mortal, computadora = inicio_juego()
    partida=True
    ganador=0

    while partida:
        ganador=ganador+1
        os.system("clear")
        tablero()

        if victoria(matriz):
            if ganador%2==0:
                print("GANASTE SIMPLE MORTAL")
                print("GAME OVER")
                print("\notra::::::------☺")
                time.sleep(5)
                partida=False
            else:
                print("PERDISTEE PSSS")
                print("*ya termino mano*")
                print("\ncortate el dedo")
                time.sleep(5)
                partida=False
        elif empate(matriz):
            print("**Empateeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            print(" ")
            print("\nReinicio...")
            time.sleep(5)
            partida=False
        elif ganador%2==0:
            print("Estoy pensando mano")
            time.sleep(2)
            movimiento_computadora()
        else:
          movimiento_mortal()


       
