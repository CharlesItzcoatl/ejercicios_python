def morral (morral_size, pesos, valores, n):
    print(f'Revisando el objeto con peso {pesos[n-1]} y valor {valores[n-1]}')
    print(f'Espacio restante del morral: {morral_size}')
    #Si ya no hay elementos o el morral se ha llenado...
    if n == 0 or morral_size == 0:
        return 0
    
    # Empezamos por el final de la lista pesos; si el peso de ese elemento es mayor que 
    # el tamaño del morral, función recursiva y recorremos al siguiente objeto.
    if pesos[n-1] > morral_size:
        return morral(morral_size, pesos, valores, n - 1)

    # La función importante. Si aún hay elementos o espacio en el morral y el elemento
    # cabe en el morral, decido si lo meto o no.
    # Lo meto si es el valor máximo de si lo meto o no lo meto.  
    # Si no lo meto, nomás se recorre el espacio.
    return max(valores[n-1] + morral(morral_size - pesos[n-1], pesos, valores, n-1),
    morral(morral_size, pesos, valores, n-1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    morral_size = 24
    n = len(valores)

    resultado = morral(morral_size, pesos, valores, n)
    print(resultado)