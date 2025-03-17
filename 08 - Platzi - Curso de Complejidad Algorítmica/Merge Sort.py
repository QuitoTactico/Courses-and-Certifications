import random

# HORRIBLE, hay cosas mejorables aquí, sobre accesos iterativos a listas usando índice.
def merge_sort(lista):
    if len(lista) > 1:
        # Dividir la lista en dos mitades
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        # Llamada recursiva a merge_sort en cada mitad
        merge_sort(izquierda)
        merge_sort(derecha)

        # Inicializamos los índices para las dos sublistas
        i = j = k = 0

        # Unir las listas: izquierda e derecha
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        # Si quedan elementos en izquierda, los agregamos
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        # Si quedan elementos en derecha, los agregamos
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)