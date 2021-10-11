import cv2

src = cv2.imread("../Img/Car.jpg")
dSize = src.copy()
uSize = src.copy()

for i in range(3):
    dSize = cv2.pyrDown(dSize)
    cv2.imshow("DownSize_%d" %i, dSize)

cv2.imshow("Origin", src)

uSize = cv2.pyrUp(uSize)
cv2.imshow("UpSize",uSize)

cv2.waitKey(0)
cv2.destroyAllWindows()