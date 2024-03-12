
from .concat import _smush


def dup(a): return _smush(a, a)
def drop(_): pass
def swap(a, b): return _smush(b, a)
def rot(a, b, c): return _smush(b, c, a)
def over(a, b): return _smush(a, b, a)
