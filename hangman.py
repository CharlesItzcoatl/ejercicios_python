# Desarrollar el juego de ahorcado con las siguientes reglas:
# 1)Incorporar comprehensions, manejo de errores y manejo de archivos. --> DONE (3/3)
# 2) Utilizar el archivo data.txt y leerlo para obtener las palabras. --> DONE
# Además, tenemos las ayudas y pistas:
# 3) Investigar la función enumerate. --> DONE
# 4) El método get de los diccionarios puede servir. --> DONE
# 5) La sentencia
#       os.system("cls") -> Windows
#       os.system("Clear") -> Unix
#   sirve para limpiar pantalla. --> DONE
# Mejorar el juego:
# 6) Añadir un sistema de puntos. --> DONE
# 7) Dibujar al ahorcado en cada jugada con código ASCII.
# 8) Mejorar la interfaz.
import random
import os
from functools import reduce
# Añadir dificultad de juego ¿Cuál es el criterio de la dificultad?
# La palabra se debe poder adivinar de una. --> DONE
# Hacer una lista con las letras que ya se han escrito. --> DONE


def menu():
    respuesta = True
    points = 0
    while(respuesta):
        menu = """

        ¡Juego del ahorcado!

        ¿Jugar?

        (1) SÍ          (0) NO

        """
        print(menu)
        print("Tus puntos: " + str(points))
        try:
            respuesta = int(input())
            if(respuesta == 1):
                os.system("clear")
                menu = """
                    Elige una dificultad:
                        1) Principiante
                        2) Intermedio
                        3) Difícil
                        4) Fuckin' Legend
                """
                print(menu)
                respuesta = int(input())
                if(game(respuesta)):
                    points += 1
                else:
                    points = 0
            elif(respuesta > 1 or respuesta < 0):
                print("Escribe 1 o 0.")
            else:
                return 0
        except ValueError:
            print("Escribe un valor válido, imbécil.")


def replacement(lista_palabras):
    tuplas = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
    )

    for a, b in tuplas:
        lista_palabras = list(map(lambda word: word.replace(a,b), lista_palabras))
    return lista_palabras


def read():
    lista_palabras = []
    i = 0
    try:
        with open("/home/charles/Documents/curso_python/archivos/data.txt", "r", encoding = "utf-8") as f:
            for word in f:
                # Añadimos una palabra por elemento de la lista, usamos la función strip para
                # eliminar los saltos de línea.
                lista_palabras.append(word.strip())
    except FileNotFoundError:
        print("Ocurrió un error al buscar el archivo o este no existe")
    #La función replacement elimina los acentos de las palabras en la lista.
    lista_palabras = replacement(lista_palabras)
    return lista_palabras


def lose(vidas, palabra):
    os.system("clear")
    print("Vidas: " + str(vidas))
    print("¡Has perdido todas tus perras vidas! :O ¡ Has mamado!:(")
    print("La palabra era: " + reduce(lambda a, b: a + b, palabra))


def win(palabra, guess, attempts, vidas):
    print("La palabra: " + reduce(lambda a, b: a + b, palabra))
    #print("Tu respuesta: " + reduce(lambda a, b: a + b, guess))
    guess = "".join(guess)
    print("Tu respuesta: " + guess)
    print("Intentos: " + str(attempts))
    print("Vidas restantes: " + str(vidas))
    print("¡Felicidades, has ganado!")


def difficulty(choice, len):
    if choice == 1:
        return len + 8
    elif choice == 2:
        return len + 6
    elif choice == 3:
        return len + 4
    elif choice == 4:
        return len + 1
    else:
        print("Ingresa una opción válida.")
        return 0


def game(choice):
    # El número de vidas dependerá de la dificultad.
    # El número de vidas depende también de la longitud de la palabra.
    attempts = 0
    lista_palabras = read()
    index = random.randint(0, 170)
    #Creamos dos cadenas de caracteres que almacenan la palabra escogida:
    palabra2 = palabra = lista_palabras[index]
    vidas = difficulty(choice, len(palabra))
    #Convertimos a palabra en una lista con un solo caracter por elemento:
    palabra = [i for i in palabra]
    # guess almacena la respuesta que va rellenando el usuario por cada intento.
    guess = ["_ " for element in range(0, len(palabra))]
    list_of_inputs = []
    while guess != palabra:
        correct = False
        hit = False
        i = 0
        if(vidas == 0):
            lose(vidas, palabra)
            return vidas
        os.system("clear")
        #print(palabra)
        print(guess)
        print("Vidas: " + str(vidas))
        print("Intentos: " + str(attempts))
        print("Letras intentadas: ")
        print(list_of_inputs)
        respuesta = input("Introduce una letra o la palabra exacta: ").lower()
        assert respuesta.isalpha(), "No se admiten números ni caracteres especiales."
        if attempts == 0:
            list_of_inputs.append(respuesta)
        #Si la respuesta es exactamente la palabra:
        if respuesta == palabra2:
            attempts += 1
            palabra2 = [i for i in palabra2]
            guess = palabra2
            break;
        #Si no, comparar letra a letra de la lista palabra
        else:
            # Se asigna a la lista la letra.
            for letter in palabra: 
                if respuesta == letter:
                    correct = True
                    guess[i] = respuesta
                i += 1
            attempts += 1
        #Las vidas sólo se deben restar si no se acerta ninguna letra.
        if correct == False:
            vidas -= 1
        for element in list_of_inputs:
            if element == respuesta:
                hit = True
        if not hit:
            list_of_inputs.append(respuesta)
            
    os.system("clear")
    win(palabra, guess, attempts, vidas)
    return 1


def run():
    os.system("clear")
    menu()

if __name__ == '__main__':
    run()