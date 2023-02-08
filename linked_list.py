from node import Node

class SinglyLinkedList:
    def __init__(self) -> None:
        # Crea el atributo tail que contiene un valor nulo.
        self.tail = None
        # El tamaño de la lista es de 0 al crearse.
        self.size = 0

    def append(self, data):
        # Crea un objeto tipo Node que recibe solamente el dato como parámetro.
        node = Node(data)
        # Si está a la espera de un nuevo valor, se asgina el nodo a la cola.
        if self.tail == None:
            # Asigna el 'apuntador' al elemento recién creado.
            self.tail = node
        # Si self.tail tiene un nodo actualmente:
        else:
            # Asignamos el nodo actual a la var. aux. current
            current = self.tail
            # Mientras exista un objeto Nodo guardado en el atributo next:
            # (¿next no guarda necesariamente un valor o sí? No)
            while current.next:
                # La var. aux. current ahora se coloca en ese nodo.
                current = current.next
            #El nuevo nodo se guarda en el apuntador de nuestro nodo actual.
            current.next = node
        
        self.size += 1

    def size(self):
        return str(self.size)

    def iter(self):
        # Coloca la var. aux. en el principio de la lista.
        current = self.tail
        # Mientas exista un valor en current...
        while current:
            # Guarda el dato del nodo en val
            val = current.data
            # Nos movemos al siguiente nodo.
            current = current.next
            # Esperamos en la variable val.
            yield val

    def delete(self, data):
        current = self.tail
        previous = self.tail

        # Mientras exista un nodo:
        while current:
            # Si el dato coincide con el dato a ser eliminado:
            if current.data == data:
                # Si el nodo es el primero ahora tail apuntará al siguiente nodo.
                if current == self.tail:
                    self.tail = current.next
                # Si no es el primer nodo, pero SÍ el dato a eliminar...
                else:
                    # Se guarda el siguiente nodo al que será eliminado.
                    previous.next = current.next
                    self.size -= 1
                    return current.data
            # Se asigna el nodo eliminado a previous.        
            previous = current
            # El nodo actual será ahora el nodo siguiente al que fue eliminado.
            current = current.next

    def search(self, data):
        # Para cada valor (resultado del yield):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found!')

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

# Cuando queremos eliminar el dato del último nodo.
#
# if head.next is None:
#     head = None
# else:
#     probe = head
#     El ciclo se termina cuando se llega al último nodo.
#     while probe.next.next != None:
#         probe = probe.next
#     removed_item = probe.next.data
#     probe.next = None

# # EJEMPLO INSERTAR NUEVO NODO LISTA SIMPLEMENTE ENLAZADA
# from node import Node
# head = None
# for i in range (0, 10):
#     # Se crea la lista.
#     head = Node(i, head)
# # Apuntador o var. aux. para recorrer lista.
# probe = head
# #  Dato a ser insertado.
# new_item = 'F' 
# # Variable para indicar posición en que se inserta el nodo.
# index = 4
# # Mientras queden nodos por recorrer y exista un nodo siguiente.
# while index > 1 and probe.next: 
#     probe = probe.next
#     index -= 1
# # Al llegar a la posición se inserta en la SIGUIENTE posición el nuevo nodo, que ahora
# # apunta al nodo que antes era el siguiente.
# probe.next = Node(new_item, probe.next)

# from node import Node
# index = 1
# new_item = 'ham'
# head es un objeto Nodo que tiene dato None y no apunta a nada.
# head = Node(None, None)
# head ahora apunta a sí mismo
# head.next = head
# Se crea el puntero auxiliar para recorrer la lista.
# probe = head
# Si el nodo al que apunta probe es distinto del inicial...
# while index > 0 and probe.next != head:
#    probe = probe.next
#    index -= 1

# probe.next = Node(new_item, probe.next)

# # EJEMPLO LISTA CIRCULAR CON MÚLTIPLES NODOS
# from node import Node
# head = Node(None, None)
# head.next = head
# probe = head
# new_item = [1, 2, 3, 4]
# quantity = len(new_item)
# for element in new_item:
#     while quantity > 0 and probe.next != head:
#         probe = probe.next
#         quantity -= 1
#     probe.next = Node(element, probe.next)
#     #probe.next = Node(element, head)
# 
# probe = head.next
# 
# while probe != head:
#     print(probe.data)
#     probe = probe.next
# 

# # EJEMPLO LISTA CIRCULAR DOBLEMENTE ENLAZADA CON MORTAL TRIPLE Y MÚLTIPLES NODOS
# from double_linked_list import TwoWayNode
# head = TwoWayNode(None)
# head.next = head
# probe = head
# new_item = [1, 2, 3, 4]
# quantity = len(new_item)
# for element in new_item:
#     while quantity > 0 and probe.next != head:
#         probe = probe.next
#         quantity -= 1
#     probe.next = TwoWayNode(element, probe, head)
# head.previous = probe.next

# # EJEMPLO ELIMINATION LISTA CIRCULAR DOBLEMENTE ENLAZADA
# target = 2
# if target == probe.data:
#     probe.previous.next, probe.next.previous = probe.next, probe.previous
# 
# else: 
#     quantity = len(new_item)
#     while probe.data != target and quantity >= 0:
#         probe = probe.next
#         quantity -= 1
#     probe.previous.next, probe.next.previous = probe.next, probe.previous
# .
