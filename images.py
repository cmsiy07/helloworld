import numpy as np
from scipy import misc
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


img = imread('pikachu.jpeg')
greyscale = rgb2gray(img)

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(np.uint8(greyscale),cmap = plt.get_cmap('gray'))
plt.show()

#test