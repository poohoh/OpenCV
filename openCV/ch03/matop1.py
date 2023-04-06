import numpy as np
import cv2


def func1():
    img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

    if img1 is None:
        print('Image load failed!')
        return

    print('type(img1):', type(img1))
    print('img1.shape:', img1.shape)

    if len(img1.shape) == 2:
        print('img1 is a 5.1.1.grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a truecolor image')

    cv2.imshow('img1', img1)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    func1()
