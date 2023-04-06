import numpy as np
import cv2


def func2():
    img1 = np.empty((480, 640), np.uint8)       # 5.1.1.grayscale
    img2 = np.zeros((480, 640, 3), np.uint8)    # color
    img3 = np.ones((480, 640), np.int32)        # 1's matrix
    img4 = np.full((480, 640), 0, np.float32)   # 0.0 matrix

    mat1 = np.array([[11, 12, 13, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34]]).astype(np.uint8)

    mat1[0, 1] = 100  # x=1, y=0의 값
    mat1[2, :] = 200

    print(mat1)


if __name__ == '__main__':
    func2()
