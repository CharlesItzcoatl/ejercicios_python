import time


def fibo_gen(max: int = None) -> int:

    # Código de la clase
    #n1 = 0
    #n2 = 1
    #counter = 0
    #while True:
    #    if counter == 0:
    #        counter += 1
    #        yield n1
#
    #    elif counter == 1:
    #        counter += 1
    #        yield n2
#
    #    else:
    #        aux = n1 + n2
    #        n1, n2 = n2, aux
    #        counter += 1
    #        yield aux
    
    # Código guapo
    a: int
    b: int
    counter: int
    counter = 0
    a, b = 0, 1
    while True:
        if not max:
            yield a
            a, b = b, a+b
        elif counter < max:
            yield a
            a, b = b, a+b
            counter += 1
        else:
            raise StopIteration 


if __name__ == '__main__':
    fibonacci: int = fibo_gen(10)
    for element in fibonacci:
        print(element)
        time.sleep(0.25)
        print(type(fibonacci))
    
