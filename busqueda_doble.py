import random

# ¿Cómo retornar el número de iteraciones también en una función recursiva?
def busqueda_binaria(lista, inicio, final, objetivo, i=0):
    if inicio > final:
        return (False, i)

    i += 1
    print(f'Buscando {objetivo} entre {lista[inicio]} y {lista[final-1]}')

    medio = (inicio + final) // 2

    # La recursividad se termina cuando el valor coincide o cuando no se encuentra,
    # hasta ese momento se retorna el contador.
    if lista[medio] == objetivo:
        return (True, i)
    
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio +1, final, objetivo, i)

    else: # lista[medio] > objetivo
        return busqueda_binaria(lista, inicio, medio - 1, objetivo, i)


def busqueda_lineal(lista,objetivo):
    i = 0
    match = False

    for elemento in lista:
        i += 1
        if elemento == objetivo:
            match = True
            break

    return (match, i)


if __name__ == '__main__':
    tamano_lista = int(input('¿De qué tamaño será la lista? '))
    objetivo = int(input('Elige el número que quieres encontrar: '))

    lista = [random.randint(0,100000) for i in range(tamano_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    #print(lista)
    print(f'El elemento {objetivo} {"" if encontrado[0] else "no "}fue encontrado en la lista')
    print(f'Iteraciones: {encontrado[1]}\n')

    lista = sorted(lista)
    (encontrado, i)= busqueda_binaria(lista, 0, len(lista), objetivo)
    #print(lista)
    print(f'El elemento {objetivo} {"" if encontrado else "no "}fue encontrado en la lista')
    print(f'Iteraciones: {i}')