def divisors(num):
    #divisors = [i for i in range (1, num + 1) if num % i == 0]
    try:
        if num <= 0:
            raise ValueError("El número no puede ser 0 o negativo")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        return ve


def run():
    num = input("Introduce un número: ")
    assert (num.strip('-')).isnumeric(), "Debes ingresar un número, imbécil"
    print(divisors(int(num)))
    print("El programa ha terminado")
    

if __name__ == '__main__':
    run()