class FIFO:
    def __init__(self):
        self.__queue__ = []

    def push(self, value):
        self.__queue__.append(value)

    def pop(self):
        val = self.__queue__.__getitem__(0)
        self.__queue__ = self.__queue__[1:]
        return val



