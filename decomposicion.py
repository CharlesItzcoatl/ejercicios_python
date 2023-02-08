class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'En reposo'
        #Inicializamos una variable privada de tipo Motor, con 4 cilindros.
        self._motor = Motor(cilindros = 4)

    def acelerar(self, tipo = 'Despacio'):
        if tipo == "Rapida":
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'En movimiento'


class Motor:
    def __init__(self, cilindros, tipo = 'Gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura

    def inyecta_gasolina(self, cantidad):
        pass