from array import Array

class Stack(Array):
    def __init__(self, capacity) -> None:
        super().__init__(capacity)
        self.index = capacity - 1

    def push(self, data) -> None:
        index = 0
        while self.__getitem__(index) is not None:
            index += 1
        self.__setitem__(index, data)
        print(f'The item {data} was located in the position: {index + 1}')

    def pop(self) -> None:
        index = self.index
        while index >= 0:
            if self.__getitem__(index) is not None:
                print(f'The item {self.__getitem__(index)} has been removed from the position {index + 1} of the stack')
                self.__setitem__(index, None)
                return
            else:
                index -= 1
        if index < 0:
            print(f'There is no more data located in the stack')

    def peak(self):
        index = self.index
        while index >= 0:
            if self.__getitem__(index) is not None:
                return self.__getitem__(index)
            else:
                index -= 1
        if index < 0:
            print(f'El stack está vacío')
            
    def clear(self):
        index = self.index
        while self.__getitem__(index) is not None:
            self.pop()
            index -= 1

    def seek(self, data):
        index = self.index
        while self.__getitem__(index) is not None and self.__getitem__(index) != data:
            index -= 1
            if index < 0:
                print(f'The element {data} does not belong to the stack.')
                return
        print(f'The element {data} is in the position {index + 1} of the stack.')


