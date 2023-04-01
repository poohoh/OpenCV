import cv2


def func(img):
    assert img.dtype == 'uint8' and len(img.shape) == 2


img = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)

func(img)

print("통과")
