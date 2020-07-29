import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

img_path = '/home/aditya/Downloads/drive-download-20200723T203459Z-001/dada_high4.jpg'
img = cv2.imread(img_path)

R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

plt.imshow(img)
plt.axis('off')
plt.show()
gray = 0.29*R + 0.58*G + 0.07*B

im = plt.imshow(gray)
im.set_cmap('gray')
plt.axis('off')
plt.show()

[u, s, v] = np.linalg.svd(gray, full_matrices=False)

plt.plot(np.log(s))
plt.show()

s = np.diag(s)
j = 0
for r in range(1, 90, 10):
    image = u[:, :r]@s[:r, :r]@v[:r, :]
    plt.figure(j+1)
    j += 1
    im = plt.imshow(image)
    im.set_cmap('gray')
    plt.axis('off')
    plt.title('r = '+str( r))
    plt.show()
    