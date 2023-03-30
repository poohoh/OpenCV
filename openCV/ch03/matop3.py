import numpy as np
import cv2


def func3():
    img1 = cv2.imread('cat.bmp')

    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255)  # yellow

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    func3()
