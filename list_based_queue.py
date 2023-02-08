class ListQueue:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def enqueue(self, data):
        # Se desplazan a medida que se insertan, el 1ro queda al último.
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        data = self.items.pop()
        self.size -= 1
        return data
    
    def loop(self):
        for item in self.items:
            print(item)