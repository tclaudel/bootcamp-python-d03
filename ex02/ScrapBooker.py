import numpy as np
from ImageProcessor import ImageProcessor


class ScrapBooker:
    def crop(self, array, dim, pos=(0, 0)):
        if dim[0] > array.shape[0] or dim[1] > array.shape[1]:
            print("ERROR")
            return
        return array[pos[0]:pos[0] + dim[0], pos[1]:pos[1] + dim[1]]

    def thin(self, array, n, axis):
        return np.delete(array, np.s_[n::n], 1 - axis)

    def juxtapose(self, array, n, axis):
        new_array = array
        for i in range(n):
            return np.concatenate((new_array, array), axis)
        return new_array

    def mosaic(self, array, dimensions):
        new_array = self.juxtapose(array, dimensions[0], 0)
        new_array = self.juxtapose(new_array, dimensions[1], 1)
        return new_array


scrap = ScrapBooker()
opener = ImageProcessor()
arr = opener.load("./musk.png")
arrcrop = scrap.crop(arr, (100, 400), (100, 25))
print("showing cropped array")
opener.display(arrcrop)
# print("showing thin'ed array")
# aThin = scrap.thin(arr, 500, 0)
# opener.display(aThin)
# print("showing juxtaposed arrays")
# aJuxt = scrap.juxtapose(arr, 3, 0)
# opener.display(aJuxt)
# print("showing mosaic'ed arrays B)")
# aMos = scrap.mosaic(arrcrop, (6, 6))
# opener.display(aMos)
