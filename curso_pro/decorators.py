from datetime import datetime

def execution_time(func):
    # Cuando decoramos una función se crea una función anidada que recibe los mismos
    # parámetros que la función decorada.
    # '*args' indica que no importa la cantidad de argumentos posicionales que reciba
    # la función.
    # '**kwargs' indica que no importa la cantidad de parámetros nombrados que reciba
    # la función.
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos.')
    return wrapper


@execution_time
def random_func():
    for _ in range (1,100000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    print (a + b)

@execution_time
def saludo(nombre = "César"):
    print(f'Hola {nombre}')


suma(2,5)   
random_func()
saludo("Facundo")