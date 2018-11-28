import cv2 as cv
import numpy as np
def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)
def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)
def divide_demo(m1, m2):
    '''触发使用相对少'''
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)
def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)
def logic_demo(m1, m2):
    dst = cv.bitwise_not(m1, m2)
    cv.imshow("logic_demo", dst)
def others(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    '''每个颜色均值和标准反差'''
    print(M1)
    print(M2)
    print('----------')
    print(dev1)
    print('----------')
    print(dev2)
    img = np.zeros([h, 2], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)
if __name__ == '__main__':
    try:
        src1 = cv.imread('linux.jpg')
        src2 = cv.imread('windows.png')
        cv.namedWindow("image1", cv.WINDOW_AUTOSIZE)
        cv.imshow("image1", src1)
        cv.imshow('image2', src2)
        print(src1.shape)
        print(src2.shape)
        # add_demo(src1, src2)
        # subtract_demo(src1, src2)
        # divide_demo(src1, src2)
        # multiply_demo(src1, src2)
        # others(src1, src2)
        logic_demo(src1, src2)
        cv.waitKey(0)
    except:
        pass