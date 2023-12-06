class FIFO_element:

    next = None

    def __init__(self, value):
        self.__value__ = value

    def get(self):
        return self.__value__

class FIFO:
    def __init__(self):
        self.first = None
        self.last = None

    def push(self, value):
        el = FIFO_element(value)
        if self.first == None:
            self.first = el
            self.last = el
        else:
            self.last.next = el
            self.last = el

    def pop(self):
        if(self.first == None):
            return None
        val = self.first.get()
        self.first = self.first.next
        return val


class FIFO_2:
    def __init__(self):
        self.__queue__ = []

    def push(self, value):
        self.__queue__.append(value)

    def pop(self):
        val = self.__queue__.__getitem__(0)
        self.__queue__ = self.__queue__[1:]
        return val


