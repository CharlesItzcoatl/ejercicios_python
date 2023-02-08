import re


if __name__ == '__main__':
    my_list = ['Nuevo Mundo', 'Uruguay']
    a,b = my_list
    is_world = re.compile(r'^Nuevo|Viejo Mundo$')

    if not is_world.match(a):
        b,a = my_list
    print(a)
    print(b)