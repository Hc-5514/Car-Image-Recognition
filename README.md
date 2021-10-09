<hr/>

# OpenCV - Python

> ### Ex_Image_01.py
>
> <hr/>
>
> #### 1. 이미지 입력
>
> ```python
> cv2.imread(fileName, flags = cv2.IMREAD_COLOR)
> ```
>
> #### 2. 이미지 출력
>
> ```python
> cv2.nameWindow(winname, flags = None)
> cv2.resizeWindow(winname, width, height)
> cv2.imshow(winname, ndarray)
> cv2.waitKey(0)
> cv2.destroyAllWindows()
> ```
>
> #### 3. 이미지 저장
>
> ```python
> cv2.imwrite(filename, img, params = None)
> ```

> ### Ex_Image_02.py
>
> <hr/>
>
> ### 이미지 가장자리 검출: Canny Edge Detection
>
> ```python
> dst = cv2.Canny(src, threshold1, threshold2, apertureSize = None, L2gradient = None)
> ```
>
> <img src="Img/canny_horse.png" width="1080px" height="720px" alt=: Canny Set by Version></img>

<hr/>

# 링크

- 마크다운 markdown 작성법:
  <https://gist.github.com/ihoneymon/652be052a0727ad59601#this-is-a-h1>
- Image Gradients - Canny Edge Detection:  
  <https://dsbook.tistory.com/214>
