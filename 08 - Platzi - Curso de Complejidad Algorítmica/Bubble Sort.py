def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista ordenada:", bubble_sort(lista))