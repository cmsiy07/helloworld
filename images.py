import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('pikachu.jpeg')
img_tinted = img*[0.5,0.95,0.9]

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(np.uint8(img_tinted))
plt.show()
