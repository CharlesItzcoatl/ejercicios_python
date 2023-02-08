import time


class FiboIter():
    def __init__(self, max: int = None):
        # El máximo se refiere al límite en cuanto a valores, no al contador.
        self.max = max

    def __iter__(self,):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        # Si no se ha establecido un número máximo...
        if not self.max:
            # Cuando empieza la serie, retorna el valor original de n1, '0'.
            if self.counter == 0:
                self.counter += 1
                return self.n1
            # El segundo término de la serie retorna el valor original de n2, '1'.
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            # Cuando el contador > 1...
            else:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                # El equivalente con el swapping es:
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        # Si hay un límite...
        else:
            # Cuando empieza la serie Y el límite es mayor que 1...
            if self.counter == 0 and self.n1 <= self.max:
                self.counter += 1
                return self.n1
            # Cuando estamos en el segundo valor de la serie Y éste es menor que el límite...
            elif self.counter == 1 and self.n2 <= self.max:
                self.counter += 1
                return self.n2
            # Cuando el contador > 1
            else:
                self.aux = self.n1 + self.n2
                if self.aux < self.max:
                    #self.n1 = self.n2
                    #self.n2 = self.aux
                    # El equivalente con el swapping es:
                    self.n1, self.n2 = self.n2, self.aux
                    self.counter += 1
                    return self.aux
                else:
                    raise StopIteration


if __name__ == '__main__':
    fibonacci = FiboIter(12)

    for element in fibonacci:
        print(element)
        time.sleep(0.5)