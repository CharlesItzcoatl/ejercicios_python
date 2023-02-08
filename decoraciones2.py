#class Casilla:
#    def __init__(self, identificador, pais) -> None:
#        self._identificador = identificador
#        self._pais = pais
#        self._region = None
#
#    @property
#    def region(self):
#        return self._region
#
#    @region.setter
#    def region(self, region):
#        if region in self._pais:
#            self._region = region
#        else:
#            raise ValueError(f'La región {region} no es válida en {self._pais}')

#class Millas:
#    def __init__(self, distancia = 0) -> None:
#        self._distancia = distancia
#
#    def obtener_distancia(self):
#        print("Llamada al método getter")
#        return self._distancia
#
#    def definir_distancia(self, valor):
#        print("Llamada al método setter")
#        self._distancia = valor
#
#    def eliminar_distancia(self):
#        del self._distancia
#
#    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

#avion = Millas()
#avion.distancia = 200
#print(avion.definir_distancia)

# Output
# Llamada al método setter
# Llamada al método getter
# 200

class Millas:
    def __init__(self) -> None:
        self._distancia = 0

    @property
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia

    # Se define a la función definir_distancia como método setter de obtener_distancia.
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor


avion = Millas()
avion.definir_distancia = 200
print(avion.definir_distancia)

# Output
# Llamada al método setter
# Llamada al método getter
# 200