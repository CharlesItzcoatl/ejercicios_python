from node import Node

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    # Agregar un elemento a la pila.
    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        
        self.size += 1
    
    # Eliminar el último elemento en entrar.
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            print(f'\'{data}\' has been removed')
        
        else:
            print(f'¡El stack está vacío! :O')

    # Mostrar el elemento último.
    def peak(self):
        if self.top:
            return self.top.data
        else:
            print(f'¡El stack está vacío! :O')

    # Vaciar la pila.
    def clear(self):
        while self.top:
            self.pop()
        print(f'All items have been removed')

    # Buscar un elemento en la pila.
    def seek(self, data):
        position = self.size
        probe = self.top
        while probe:
            if data == probe.data:
                print(f'The item {data} was found in position: {position}')
                return
            probe = probe.next
            position -= 1
            if not probe:
                print(f'The item {data} is not in the stack.')

    def iter(self):
        probe = self.top
        while probe:
            val = probe.data
            probe = probe.next
            yield val
            
