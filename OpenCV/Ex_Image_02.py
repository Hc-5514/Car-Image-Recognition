import numpy as np
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("../Img/horse.png", cv2.IMREAD_GRAYSCALE)

canny1 = cv2.Canny(src, 100, 200, apertureSize=3, L2gradient=True)
canny2 = cv2.Canny(src, 100, 200, apertureSize=5, L2gradient=True)
canny3 = cv2.Canny(src, 100, 200, apertureSize=7, L2gradient=True)

titles = ['original', 'canny1', 'canny2', 'canny3']
images = [src, canny1, canny2, canny3]

cv2.imshow('original', src)
cv2.imshow('canny1', canny1)
cv2.imshow('canny2', canny2)
cv2.imshow('canny3', canny3)

cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize=(10, 10))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()
