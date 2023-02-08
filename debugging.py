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
    try:
        num = int(input("Introduce un número: "))
        print(divisors(num))
    except ValueError:
        print("Debes ingresar un número, imbécil")
    finally:
        print("El programa ha terminado")

        print('Pero puede continuar aquí')
        x = 6
        y = 7
        print(x+y)
    

if __name__ == '__main__':
    run()