############## LIBRERIAS ##############
import random


############## FUNCIONES ##############
def crearMatriz(matriz, filas, columnas):
    for indice in range(filas):
        matriz.append([0] * columnas)


def rellenarMatriz(matriz, letras, cantidad_letras):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            posicion = random.randint(0, cantidad_letras - 1)
            while letras[posicion][0] >= 2:
                posicion = random.randint(0, cantidad_letras - 1)
            matriz[i][j] = [letras[posicion][1], False]
            letras[posicion][0] += 1


def imprimirMatriz(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    for i in range(num_filas):
        for j in range(num_columnas):
            if matriz[i][j][1]:
                print(matriz[i][j][0], end="\t")
            else:
                print("*", end="\t")
        print()


############## PROGRAMA ##############
print("\033[1;36m" + "La cantidad filas X columnas debe ser par.")
n = int(input("\033[;39m" + "Ingrese el número de filas: "))
m = int(input("Ingrese la cantidad de columnas: "))
matriz = []

while (n * m) % 2 != 0:
    print("\033[1;36m" + "La cantidad filas X columnas debe ser par.")
    n = int(input("\033[;39m" + "Ingrese el número de filas: "))
    m = int(input("Ingrese la cantidad de columnas: "))

letras = []
crearMatriz(matriz, n, m)
cantidad_casilleros = len(matriz) * len(matriz[0])
cantidad_letras = int(cantidad_casilleros / 2)
for i in range(cantidad_letras):
    codigoascii = 65 + i
    letras.append([0, chr(codigoascii)])


rellenarMatriz(matriz, letras, cantidad_letras)
imprimirMatriz(matriz)
faltantes = 1

while faltantes > 0:
    faltantes = 0
    pares = []

    for i in range(2):
        if i == 0:
            par = input("Ingrese la primera posicion: ")
        else:
            par = input("Ingrese la segunda posicion: ")
        x, y = par.split(",")
        x = int(x) - 1
        y = int(y) - 1
        if i == 1:
            if pares[0][0] == x and pares[0][1] == y:
                print("Error, es la misma posición.")
                break

        pares.append([x,y])
        matriz[x][y][1] = True

        imprimirMatriz(matriz)

    x1 = pares[0][0]
    y1 = pares[0][1]

    if len(pares) > 1:
        x2 = pares[1][0]
        y2 = pares[1][1]

        matriz[x1][y1][1] = False
        matriz[x2][y2][1] = False
        if matriz[x1][y1][0] == matriz[x2][y2][0]:
            matriz[x1][y1][1] = True
            matriz[x2][y2][1] = True
            print("Las letras son iguales")
        else:
            print("Las letras no son iguales")
    else:
        matriz[x1][y1][1] = False

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not matriz[i][j][1]:
                faltantes += 1

print("\033[1;36m" + "Felicitaciones, el juego ha terminado.")
imprimirMatriz(matriz)