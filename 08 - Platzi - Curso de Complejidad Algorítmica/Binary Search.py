def busqueda_binaria(lista, objetivo, inicio, final):
    if inicio > final:
        return False

    medio = (inicio + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, objetivo, medio + 1, final)
    else:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)

# Ejemplo de uso
lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
objetivo = 13
print(busqueda_binaria(lista, objetivo, 0, len(lista) - 1))  # Salida -> True