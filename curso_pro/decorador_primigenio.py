def decorador(func):
    def envoltura():
        print("Esto se añade a mi función original.")
        func()
    return envoltura


@decorador
def saludo():
    print("Hola")
#
#
## La función originalmente sólo imprime 'Hola'
#saludo()
#
#
## Pasamos como parámetro saludo
#saludo = decorador(saludo)


saludo()

