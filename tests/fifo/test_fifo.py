from fifo import Fifo
import pytest


@pytest.fixture()
def fifo() -> Fifo:
    return Fifo()


def test_instance(fifo) -> None:
    assert fifo is not None


@pytest.mark.parametrize(argnames="to_insert", argvalues=[1, [2, 3], {1, 2}, {"toto": [1, 2]}])
def test_insert(fifo, to_insert) -> None:
    fifo.insert(to_insert)
    assert len(fifo) == 1


@pytest.mark.parametrize(argnames="to_insert", argvalues=[1, [2, 3], {1, 2}, {"toto": [1, 2]}])
def test_pop(fifo, to_insert) -> None:
    fifo.insert(to_insert)
    o = fifo.pop()

    assert o == to_insert
    assert len(fifo) == 0