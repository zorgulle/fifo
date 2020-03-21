from fifo import __version__
from fifo import Fifo

def test_fifo_instance():
    fifo = Fifo()
    assert fifo

def test_version():
    assert __version__ == '0.1.0'
