import cv2 as cv
import numpy as np
def create_red_image():
    image = np.zeros([400, 400, 3], np.uint8)
    image[:, :, 2] = np.ones([400, 400]) * 255
    return image
if __name__ == '__main__':
    image = create_red_image()
    cv.imwrite("red.jpg", image)