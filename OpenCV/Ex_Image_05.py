import cv2
import numpy as np  # 복잡한 수치계산
import matplotlib.pyplot as plt # 시각화

img = cv2.imread("../Img/Car2.jpg")
imgcopy = img.copy()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thr = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
canny = cv2.Canny(img, 127, 255)

contours1, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours1, -1, (0, 0, 255), 2)

cv2.imshow('threshold', thr)
cv2.imshow('canny', canny)
cv2.imshow('contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

b, g, r = cv2.split(imgcopy)
imgcopy = cv2.merge([r, g, b])
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])

titles = ['Original', 'Threshold', 'Canny', 'Contours']
images = [imgcopy, thr, canny, img]

plt.figure(figsize=(12, 12))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()