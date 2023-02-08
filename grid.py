import random
from array import Array

class Grid():
    def __init__(self, rows, columns, fill_value=None):
        # Crea una variable tipo Array (lista) con el número de elementos indicados.
        self.data = Array(rows)
        # Por cada elemento, crea otro objeto tipo Array que es una lista.
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    #Obtiene una fila.
    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
            result += "\n"
        return str(result)

    def fillitem(self):
        # Recorre las filas.
        for row in range(self.get_height()):
            # Recorre las columnas.
            for col in range(self.get_width()):
                self.data[row][col] = random.randint(0,100)
