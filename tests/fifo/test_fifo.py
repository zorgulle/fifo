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

