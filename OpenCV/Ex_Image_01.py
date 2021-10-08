import cv2

# [1] 이미지 입력
Car_imgColor = cv2.imread("../Img/Car.jpg", cv2.IMREAD_COLOR)
Car_imgColor2 = cv2.imread("../Img/Car.jpg", cv2.IMREAD_REDUCED_COLOR_8)
Car_imgGray = cv2.imread("../Img/Car.jpg", cv2.IMREAD_GRAYSCALE)
Car_imgGray2 = cv2.imread("../Img/Car.jpg", cv2.IMREAD_REDUCED_GRAYSCALE_4)


# [2] 이미지 출력
# (1) 윈도우 생성
cv2.namedWindow("imgColor", flags=cv2.WINDOW_FREERATIO)
cv2.namedWindow("imgColor2")
cv2.namedWindow("imgGray", flags=cv2.WINDOW_FREERATIO)
cv2.namedWindow("imgGray2")
# (2) 윈도우 크기 설정
cv2.resizeWindow("imgColor", 1024, 768)
cv2.resizeWindow("imgGray", 1024, 768)
# (3) 윈도우에 이미지 표시
cv2.imshow("imgColor", Car_imgColor)
cv2.imshow("imgColor2", Car_imgColor2)
cv2.imshow("imgGray", Car_imgGray)
cv2.imshow("imgGray2", Car_imgGray2)
# (4) 프로그램 지연
cv2.waitKey(0)
# (5) 윈도우 닫기
cv2.destroyAllWindows()


# [3] 이미지 저장
cv2.imwrite("../Img/colorCar.jpg", Car_imgColor,
            (cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_JPEG_PROGRESSIVE, 1))
cv2.imwrite("../Img/colorCar2.jpg", Car_imgColor2,
            (cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_JPEG_PROGRESSIVE, 1))
cv2.imwrite("../Img/grayCar.jpg", Car_imgGray2,
            (cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_JPEG_PROGRESSIVE, 1))
cv2.imwrite("../Img/grayCar2.jpg", Car_imgGray2,
            (cv2.IMWRITE_JPEG_QUALITY, 100, cv2.IMWRITE_JPEG_PROGRESSIVE, 1))
