import numpy as np
import cv2 as cv

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(height * width * channels)
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixel_demo", image)
def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    # print(img)
    # img[:,:,0] = np.ones([400, 400]) * 255
    # cv.imshow("new image", img)
    # img = np.ones([400, 400, 1], np.uint8) # 单通道图像
    # img = img * 100
    # cv.imshow("new image", img)
    # cv.imwrite("new.jpg", img)
    '''三种创建np array数组的方法'''
    m1 = np.ones([3, 3], np.float32)
    m1.fill(1222222.388)
    print(m1)

    m2 = m1.reshape([1, 9])
    print(m2)

    m3 = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]], np.int32)
    m3.fill(9)
    print(m3)

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo", dst)

try:
    src = cv.imread('cat.jpg')
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    time1 = cv.getTickCount()
    # access_pixels(src)
    # inverse(src) # API接口，调用C语言，更加高效
    # create_image()
    time2 = cv.getTickCount()
    print((time2 - time1) / cv.getTickFrequency() * 100)
    cv.waitKey(0)
except:
    pass

cv.destroyAllWindows()