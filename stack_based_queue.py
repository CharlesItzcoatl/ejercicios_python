class Queue:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        # Se inserta uno delante del otro, el primero siempre estará en la 1ra posición.
        self.inbound_stack.append(data)
    
    # Stack -> LIFO
    # Queue -> FIFO
    def dequeue(self):
        # Si el outbound_stack está vacío...
        if not self.outbound_stack:
            # Mientras el inbound_stack tenga datos...
            while self.inbound_stack:
                # Elimina empezando por el último elemento de inbound_stack y 
                # por lo tanto, es el primero en agregarse a outbound_stack.
                self.outbound_stack.append(self.inbound_stack.pop())
        # El último elemento de outbound_stack es el primero de inbound_stack (último eliminado).
        return self.outbound_stack.pop()