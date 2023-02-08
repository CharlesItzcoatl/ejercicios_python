from double_node import TwoWayNode

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        head = TwoWayNode(data)
        head.next = head
        probe = head
        if self.head == None:
            self.head = head
        else:
            while probe.next != head:
                probe = probe.next
            probe.next = TwoWayNode(data, probe, head)
        head.previous = probe.next


def run():
    node = DoubleLinkedList()
    node.append(1)
    node.append(2)
    node.append(3)


if __name__ == '__main__':
    run()


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