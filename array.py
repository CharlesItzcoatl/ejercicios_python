import random 

class Array:
    suma = 0

    def __init__(self, capacity, fill_value = None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __fillitem__(self):
        for i in range(0, len(self.items)):
            self.items[i] = random.randint(0, 4000)    

    def __sum__(self) -> int:
        return sum(self.items)

    def __altsum__(self):
        for element in self.items:
            self.suma += element
        return self.suma

    def asum(self):
        sum2 = 0
        for element in self.items:
            sum2 += element
        return sum2