# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!')
# 
# imprimir_mensaje()

# def conversacion(mensaje):
#     print('Hola')
#     print('¿Cómo estás?')
#     mensaje = str(mensaje)
#     print('Elegiste la opción ' + mensaje)
#     print('Adiós')
# 
# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion <= 3:
#     conversacion(opcion)
# else:
#     print('Escribe la opción correcta')

def suma(a,b):
    print('Se suman dos números')
    resultado = a + b
    return resultado

sumatoria = suma(1,4)
print(sumatoria)