import time

def factorial(n):
    respuesta = 1
    while(n > 1):
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n < 0:
        return 0
    elif n > 0:
        return n * factorial_r(n-1)
    else:
        return 1


if __name__ == '__main__':
    n = 200000000

    comienzo = time.time()
    #print(factorial(n))
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    #print(factorial_r(n))
    final = time.time()
    print(final - comienzo)

    print("\n")