import random
from array import Array
from grid import Grid

class Cube():
    def __init__(self, rows, columns, depth, fill_value = None) -> None:
        # Crea una variable tipo Grid (lista que contiene listas) con la dimensión indicada.
        self.data = Grid(rows, columns)
        for row in range(rows):
            for column in range(columns):
                # Para cada lista contenida en la lista mayor, crea un objeto tipo Array, que es otra lista.
                self.data[row][column] = Array(depth, fill_value)

    # Obtiene el número de elementos de la lista que contiene las listas que contienen una lista.
    def __geth__(self):
        return (self.data.get_height())

    # Obtiene el número de elementos de la lista que contiene más listas.
    def __getwidth__(self):
        return len(self.data[0])

    # Obtiene el número de elementos de la última lista.
    def __getdepth__(self):
        return len(self.data[0][0])

    def __str__(self):
        result = " "
        for row in range(self.__geth__()):
            for col in range(self.__getwidth__()):
                for dep in range(self.__getdepth__()):
                    result += str(self.data[row][col][dep]) + " "
                result += "\n"
        return str(result)

    def __fillitem__(self):
        number = 0
        for row in range(self.__geth__()):
            for col in range(self.__getwidth__()):
                for dep in range(self.__getdepth__()):
                    self.data[row][col][dep] = number
                    number += 1


    

