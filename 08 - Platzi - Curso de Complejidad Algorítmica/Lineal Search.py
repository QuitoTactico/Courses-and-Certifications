def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista:
        if elemento == objetivo:
            match = True
            break
    return match