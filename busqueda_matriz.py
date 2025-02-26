#Búsqueda en Arreglo Multidimensional

# Matriz bidimensional (3x3) con valores distintos
matriz = [
    [12, 5, 8],
    [3, 14, 7],
    [9, 10, 6]
]

# Valor que va a buscar
valor_buscado = 14

def buscar_valor(matriz, valor_buscado):
    fila_encontrada = -1
    columna_encontrada = -1

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor_buscado:
                fila_encontrada = fila
                columna_encontrada = columna
                break  # Detener búsqueda cuando se halle el valor
        if fila_encontrada != -1:
            break  # Salir del bucle exterior si se encuentra el valor

    if fila_encontrada != -1:
        print(f"Se encontró {valor_buscado} en la fila {fila_encontrada} y columna {columna_encontrada}.")
    else:
        print(f"{valor_buscado} no se halló en la matriz.")

# Llamada a la función para realizar la búsqueda
buscar_valor(matriz, valor_buscado)
