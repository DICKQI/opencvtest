import cv2 as cv
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
    color_space_demo(src)
    cv.waitKey(0)
except:
    pass