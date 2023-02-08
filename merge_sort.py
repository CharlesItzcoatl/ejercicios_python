import random

def merge_sort(lista):
    if len(lista) > 1:

        ########## **Empieza primera parte del algoritmo** ##########

        medio = len(lista) // 2
        left = lista[:medio]
        right = lista[medio:]
        print(left, '*' * 5, right)

        merge_sort(left)
        merge_sort(right)

        ########## **Termina primera parte del algoritmo** ##########

        i = 0
        j = 0
        k = 0

        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            
            k += 1

        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1
        
        print(f'Izquierda {left}, Derecha {right}')
        print(lista)
        print('-' * 20)
    return lista



if __name__ == '__main__':
    tamano_lista = int(input('¿De qué tamaño será la lista? '))
    
    lista = [random.randint(0,100) for i in range(tamano_lista)]

    print(lista)
    print('-' * 20)

    lista_ordenada = merge_sort(lista)
    print(lista_ordenada)