class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = 50):
        self._llenar_tanque(temperatura)
        self._jabonar()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque(self, temperatura):
        print(f'Llenando el tanque con agua a {temperatura}°C')

    def _jabonar(self):
        print('Jabonando')

    def _lavar(self):
        print('Lavando')

    def _centrifugar(self):
        print('Centrifugando')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()