import cv2

# 이미지 자르기
src = cv2.imread("../Img/Car.jpg")
dst = src[120:600, 340:705].copy()
cv2.imshow("src", src)
cv2.imshow("dst", dst)

# 이미지 붙여넣기
src2 = cv2.imread("../Img/Car.jpg")
dst2 = src2.copy()
roi = src2[120:620, 240:740]
dst2[0:500, 0:500] = roi
cv2.imshow("dst2", dst2)

# 이미지 크기 조절
src3 = cv2.imread("../Img/Car.jpg")
dst3 = src3[120:600, 340:705]
dst31 = cv2.resize(dst3, dsize=(512,512), interpolation=cv2.INTER_NEAREST)
dst32 = cv2.resize(dst3, dsize=(0,0), fx=1, fy=0.5, interpolation=cv2.INTER_NEAREST)
cv2.imshow("dst31", dst31)
cv2.imshow("dst32", dst32)

cv2.waitKey(0)
cv2.destroyAllWindows()
