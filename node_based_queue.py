class TwoWayNode():
    def __init__(self, data = None, next = None, previous = None) -> None:
        self.data = data
        self.next = next
        self.previous = previous

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        node = TwoWayNode(data)
        # Si no hay nodos (es el primer nodo):
        if self.head == None:
            self.head = node
            # Se apunta a sí mismo
            self.tail = self.head
        # Si hay por lo menos un nodo existente:
        else:
            # El previous del nuevo nodo apunta al anterior nodo
            node.previous = self.tail
            # El next del nodo anterior apunta al nuevo nodo
            self.tail.next = node
            # El nuevo nodo es el último nodo ahora (equivale a self.tail = self.head)
            self.tail = node

        self.count += 1

    def dequeue(self):
        # Nos colocamos en el primer nodo de la existencia
        current = self.head
        # Si sólo hay un nodo en la cola:
        if self.count == 1:
            self.count -= 1
            # Desaparece el nodo
            self.head = None
            self.tail = None
        # Si hay más de un nodo en la cola:
        elif self.count > 1:
            # El primer nodo ahora es al que apuntaba el que será eliminado
            self.head = self.head.next
            # El nuevo primer nodo ya no tiene nada antes
            self.head.previous = None
            self.count -= 1
        
        return current.data

