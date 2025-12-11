def Generar_num_random():
    valor_random=randrange(1,10) #numero al azar del 0 al n
    return valor_random

def Verificar_enetero(num_prueba):
    try:
        num_prueba=int(num_prueba)
        if num_prueba>0 and num_prueba<10 and type(num_prueba)==int:
            return True
        else:
            print("\n¡¡ELIGE OTRO NUMERO!! es incorrecto el",num_prueba,"\n")
            return False
    except:
        print("\n¡¡DIGITAR NUMEROS ENTEROS!! no es valido el",num_prueba,"\n")
        return False
    
def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for i in board:
        print("+-------+-------+-------+\n|       |       |       |")
        for j in i:
            print("|   "+str(j)+"   ",end="")
        print("|\n|       |       |       |")
    else:
        print("+-------+-------+-------+\n")
    return None

def EnterMove(board,num_usuario,circulo_equis=False):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    if Verificar_enetero(num_usuario):
        num_usuario=int(num_usuario)
        ocupado=0
        for i_fila in board:
            if num_usuario in i_fila:
                fila=(board.index(i_fila))
                columna=(i_fila.index(num_usuario))
                if circulo_equis == True: 
                    board[fila][columna]="O"
                    print("El jugador juega",num_usuario)
                    return True
                else: 
                    board[fila][columna]="X"
                    print("La maquina juega",num_usuario)
                    return True
        if circulo_equis==True:
            print("\n¡¡YA ESTA USADO!! el numero",num_usuario,"\n")
            return False
        else: return False
    else:
        return False

def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    return None

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    return None

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    return None

from random import randrange

print("\n--------------------INICIO DEL TIC TAC TOE----------------------\n")
#-------------------------------INICIO PROGRAMA---------------------------------------------
tablero_predeterminado = [[1,2,3],[4,5,6],[7,8,9]] # PREDETERMINADO

valor_inicial_maquina = Generar_num_random()
El_usuario_ingresa_numero = False
EnterMove(tablero_predeterminado,valor_inicial_maquina,El_usuario_ingresa_numero)

for _ in range(4):

    print(tablero_predeterminado,"\n")
    DisplayBoard(tablero_predeterminado)

    turno_valido=False
    El_usuario_ingresa_numero= True
    while turno_valido==False:#JUGADOR
        usuario_moviemiento=input(">>>Ingresa tu movimiento: ")
        turno_valido = EnterMove(tablero_predeterminado,usuario_moviemiento,El_usuario_ingresa_numero)

    print(tablero_predeterminado,"\n")
    DisplayBoard(tablero_predeterminado)

    turno_valido=False
    El_usuario_ingresa_numero= False
    while turno_valido==False:#MAQUINA
        maquina_moviemiento = Generar_num_random()
        turno_valido = EnterMove(tablero_predeterminado,maquina_moviemiento,El_usuario_ingresa_numero)

print(tablero_predeterminado,"\n")
DisplayBoard(tablero_predeterminado)
print("                                                           FIN")

"""
from random import randrange
for i in range(v): #cantidad que de veces que se repite v
    print(randrange(n)) #numero al azar del 0 al n

Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. 
Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

    La maquina (por ejemplo, el programa) jugará utilizando las 'X's.
    El usuario (por ejemplo, tu) jugarás utilizando las 'O's.
    El primer movimiento es de la maquina: siempre coloca una 'X' en el centro del tablero.
    Todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia).
    El usuario ingresa su movimiento introduciendo el número de cuadro elegido. El número debe de ser valido, 
    por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado.
    El programa verifica si el juego ha terminado. Existen cuatro posibles veredictos: el juego continua, el 
    juego termina en empate, tu ganas, o la maquina gana.
    La maquina responde con su movimiento y se verifica el estado del juego.
    No se debe implementar algún tipo de inteligencia artificial, la maquina elegirá un cuadro de manera aleatoria, 
    eso es suficiente para este juego.

El ejemplo del programa es el siguiente:
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
¡Has Ganado!

Requerimientos

Implementa las siguientes características:

    El tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento 
    es otra lista de tres elementos (la lista interna representa las filas) de manera que todos 
    los cuadros puedas ser accedidos empleado la siguiente sintaxis:

    board[row][column]


    Cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando 
    el número del cuadro (dicho cuadro se considera como libre).
    La apariencia de tablero debe de ser igual a la presentada en el ejemplo.
    Implementa las funciones definidas para ti en el editor.

    Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada 
    randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

    Nota: La instrucción from-import provee acceso a la función randrange definida en un módulo externo de 
    Python denominado random.


    from random import randrange

    for i in range(10):
        print(randrange(8))"""