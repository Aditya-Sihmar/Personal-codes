import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

img_path = '/home/aditya/Downloads/drive-download-20200723T203459Z-001/dada_high4.jpg'
img = cv2.imread(img_path)

#breaking the image into different layers
R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

#plotting the rgb Image
plt.imshow(img)
plt.axis('off')
plt.show()

#Converting the image into grayscale
gray = 0.29*R + 0.58*G + 0.07*B

#plotting the grayscale image
im = plt.imshow(gray)
im.set_cmap('gray')
plt.axis('off')
plt.show()

#calculating the economy svd
[u, s, vT] = np.linalg.svd(gray, full_matrices=False)

#plotting the singular values to see the varience in signification
plt.plot(np.log(s))
plt.show()

#converting the singular vector into a diagonalised matrix
s = np.diag(s)
j = 0

#calculating and plotting of different images after compression
for r in range(1, 90, 10):
    image = u[:, :r]@s[:r, :r]@v[:r, :]
    plt.figure(j+1)
    j += 1
    im = plt.imshow(image)
    im.set_cmap('gray')
    plt.axis('off')
    plt.title('r = '+str( r))
    plt.show()
    