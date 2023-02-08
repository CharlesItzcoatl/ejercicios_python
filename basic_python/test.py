# Hacer un programa que guarde en una lista los cuadrados de los primeros 100
# números naturales


def run():
    lista = []
    for i in range (1, 101):
        lista.append(i**2)
    
    for i in range(0,100):
        print(str(i+1) + "^2 = " + str(lista[i]))


if __name__ == '__main__':
    run()