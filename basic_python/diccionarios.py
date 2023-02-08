def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    for llave, valor in mi_diccionario.items():
        print(llave + ': ' + str(valor))


if __name__ == '__main__':
    run()