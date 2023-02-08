def run():
    # nombre = input('¿Cuál es tu nombre? ')
    # for letra in nombre:
    #     print(letra)
    frase = input('Escribe una frase inspiradora: ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__':
    run()