class Node():
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

# Los objetos Node contienen dos tipos de datos: un dato cualquiera y un dato tipo Node.
# Creamos el objeto tipo Node llamado head.
# head = None
# head = Node(1, None)
# head = Node(2, head) = Node(2, Node(1, None))
# head = Node(3, head) = Node(3, Node(2, Node(1, None)))
# head = Node(4, head) = Node(4, Node(3, Node(2, Node(1, None))))
# ¿Por qué se conservan los valores de head? Por la segunda igualdad de arriba.