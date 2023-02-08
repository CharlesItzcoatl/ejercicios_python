def mayusculas(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper


@mayusculas
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje.'


print(mensaje('Charls'))