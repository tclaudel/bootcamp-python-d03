import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


class ImageProcessor:
    def load(self, path):
        try:
            img = mpimg.imread(path)
            print("Loading image of dimensions {} x {}".format(*img.shape))
            return img
        except IOError:
            print("cannot open ", path)

    def display(self, array):
        plt.imshow(array)
        plt.show()

