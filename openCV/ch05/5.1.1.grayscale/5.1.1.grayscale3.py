import cv2

img3 = cv2.imread('../lenna.bmp', cv2.IMREAD_COLOR)
img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.waitKey()
cv2.destroyAllWindows()
