from datetime import datetime

var = datetime.now()
print(var)

var2 = var.strftime('%d/%m/%Y')
print(f'El formato en LATAM es: {var2}')

var2 = var.strftime('%m/%d/%Y')
print(f'El formato en \'murica es: {var2}')

var2 = var.strftime('Estamos en el año %Y')
print(f'Formato aleatorio: {var2}')