# Ordenación de Arreglo Multidimensional
# Matriz bidimensional (3x3) con diferentes valores
matriz = [
    [9, 7, 10],
    [2, 1, 8],
    [6, 5, 3]
]

# La fila a ordenar será la fila 2
fila_a_ordenar = 2

# Uso el algoritmo de ordenación Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambio elementos

def ordenar_fila(matriz, fila):
    bubble_sort(matriz[fila])  # Bubble Sort para ordenar la fila 2 en orden ascendente

# Mostrar la matriz original
print("Matriz inicial:")
for fila in matriz:
    print(fila)

# Organiza en forma ascendente la fila 2
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila 2 ordenada
print("\nMatriz con la fila 2 ordenada ascendentemente:")
for fila in matriz:
    print(fila)