from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos.')
    return wrapper


@execution_time
def factorial(n: int) -> int:
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


execution_time
def factorial_recursivo(n: int) -> int:
    if n == 1:
        return 1
    
    elif n > 1:
        return n * factorial_recursivo(n-1)

    else:
        return 0


def run():
    factorial(5000)
    factorial_recursivo(5)


if __name__ == '__main__':
    run()