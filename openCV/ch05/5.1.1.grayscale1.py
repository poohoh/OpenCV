import cv2

img1 = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)

cv2.imshow('img1', img1)

cv2.waitKey()
cv2.destroyAllWindows()