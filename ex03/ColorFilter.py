import numpy as np
from ImageProcessor import ImageProcessor


class ColorFilter():
    def invert(self, array):
        new_array = array - 0
        new_array[:, :, 0:3] = 1 - new_array[:, :, 0:3]
        return new_array

    def to_blue(selfself, array):
        new_array = np.zeros((array.shape))
        new_array[:, :, 2:4] = array[:, :, 2:4]
        return new_array

    def to_green(self, array):
        new_array = array * 1
        new_array[:, :, 0:1] = array[:, :, 0:1] * 0
        new_array[:, :, 2:3] = array[:, :, 2:3] * 0
        return new_array


color = ColorFilter()
opener = ImageProcessor()
arr = opener.load("./musk.png")
opener.display(arr)
inverted_color = color.invert(arr)
opener.display(inverted_color)
blue_color = color.to_blue(arr)
opener.display(blue_color)
green_color = color.to_green(arr)
opener.display(green_color)
