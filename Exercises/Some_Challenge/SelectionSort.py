valorAtual = list[0]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                print(numeros)
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso:
numeros = [7, 3, 5, 69, 37, 1, 4, 8]
print("Lista não ordenada:", numeros)

selection_sort(numeros)

print("Lista ordenada:", numeros)

