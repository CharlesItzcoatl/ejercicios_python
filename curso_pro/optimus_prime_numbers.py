def is_prime(number: int) -> bool:
    j: int
    for j in range(2, number):
        print(f'Dividiendo {number} con {j}.')
        if number % j == 0:
            return False
    return True


def run():
    i: int
    for i in range(2,10):
        print(f'{i} {" no" if not is_prime(i) else ""} es primo')

if __name__ == '__main__':
    run()