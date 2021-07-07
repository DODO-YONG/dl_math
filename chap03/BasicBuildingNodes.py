import numpy as np
class plus_node:
    def __init__(self):
        self._x = None
        self._y = None
        self._z = None

    def forward(self, x, y):
        self._x, self._y = x, y
        self._z = self._x + self._y
        return self._z

    def backword(self, dz):
        return dz, dz

class minus_node:
    def __init__(self):
        self._x, self._y = None, None
        self._z = None

    def forward(self, x, y):
        self._x, self._y = x, y
        self._z = self._x - self._y
        return self._z

    def backward(self, dz):
        return dz, -1*dz

