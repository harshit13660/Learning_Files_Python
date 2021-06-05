import pytesseract as tess
import cv2
tess.pytesseract.tesseract_cmd='C:\Program Files\Tesseract-OCR\\tesseract.exe'

img= cv2.imread("C:\\Users\Harshit\Desktop\\let.jpg")
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img_blur=cv2.GaussianBlur(imgGray,(3,3),5)
img_med=median = cv2.medianBlur(img_blur, 3)
print("contours=", len(contours))
# cv2.drawContours(img_med, contours, -1, (0, 255, 0), 1)
cv2.imshow("Image",img_med)
text = tess.image_to_string(img_med,config='--psm 10')
print(text)
cv2.waitKey(0)
# print(text)
