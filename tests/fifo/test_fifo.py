from fifo import Fifo
from unittest import TestCase


class TestFifo(TestCase):
    def setUp(self) -> None:
        self.fifo = Fifo()

    def test_instance(self) -> None:
        assert self.fifo is not None

    def test_insert_string(self) -> None:
        self.fifo.insert("toto")
        assert len(self.fifo) == 1

    def test_insert_2_string(self) -> None:
        self.fifo.insert("toto")
        self.fifo.insert("toto2")
        assert len(self.fifo) == 2

    def test_pop(self):
        to_insert = "TOTO"
        self.fifo.insert(to_insert)
        o = self.fifo.pop()

        assert o == to_insert
        assert len(self.fifo) == 0

    def test_pop_order(self):
        to_insert = "TOTO"
        self.fifo.insert(to_insert)
        to_insert_again = "TITI"
        self.fifo.insert(to_insert_again)

        pop1 = self.fifo.pop()
        assert pop1 == to_insert

        pop2 = self.fifo.pop()
        assert pop2 == to_insert_again

