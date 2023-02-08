class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print("Ando caminando")


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print("Ando pedaleando")


def main():
    persona = Persona('David')
    persona.avanzar()

    ciclista = Ciclista('Daniela')
    ciclista.avanzar()


if __name__ == '__main__':
    main()