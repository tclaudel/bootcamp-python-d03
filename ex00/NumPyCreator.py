import numpy as np


class NumPyCreator:
    def from_list(self, *lst, dtype=float):
        return np.array(lst, dtype)

    def from_tuple(self, tpl, dtype=str):
        return np.array(tpl, dtype)

    def from_iterable(self, itr, dtype=float):
        return np.array(itr, dtype)

    def from_shape(self, matrix_shape, value=0, dtype=float):
        return np.full(matrix_shape, value, dtype)

    def random(self, matrix_shape):
        return np.random.rand(*matrix_shape)

    def identify(self, n, dtype=float):
        return np.eye(n, dtype=dtype)


npc = NumPyCreator()
print(npc.from_list([1, 2, 3], [0, 1, 2]))
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_iterable(range(5)))
shape = (3, 5)
print(npc.from_shape(shape, 8))
print(npc.random(shape))
print(npc.identify(5))
