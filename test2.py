import cv2 as cv
import numpy as np
def extrace_object_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if ret == False:
            break
        '''过滤出红色部分'''
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([156, 43, 46])
        upper_hsv = np.array([180, 255, 255]) # HSV颜色空间表
        time1 = cv.getTickCount()
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        time2 = cv.getTickCount()
        print((time2 - time1) / cv.getTickFrequency())
        cv.imshow("video", frame) # 将帧显示出来
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    '''
    h : 0-180
    s : 0-255
    v : 0-255
    '''
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    source = cv.cvtColor(yuv, cv.COLOR_YUV2BGR) # 同样可以转回来
    cv.imshow("source", source)
try:
    src = cv.imread('red.jpg')
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    # extrace_object_demo()
    b, g, r = cv.split(src)
    cv.imshow("blue", b)
    cv.imshow("green", g)
    cv.imshow("red", r)
    src[:, 10:1000, 1] = 0
    cv.imshow("change", src)
    src = cv.merge([b, g, r])
    cv.imshow("return", src)
    cv.waitKey(0)
except:
    pass