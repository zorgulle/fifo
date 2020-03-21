class Fifo:
    def __init__(self):
        self.__fifo = list()

    def insert(self, to_insert: object) -> None:
        self.__fifo.append(to_insert)


    def __len__(self):
        return len(self.__fifo)
