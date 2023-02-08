def factorial(n):
    """
    Esta función calcula n!.

    int n > 0
    return n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factorial (n-1)


n = int(input("Escribe un número natural: "))
print(f'{n}! = {factorial(n)}')