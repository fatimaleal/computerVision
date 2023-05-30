import cv2 as cv

def to_grayscale(image):
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    return gray_image 

def to_blur(image):
    blur_image = cv.GaussianBlur(image, (5,5), 1)

    return blur_image

def to_canny(image):
    canny_image = cv.Canny(image, 50, 50)

    return canny_image

def get_contours(image):
    contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    return contours

def draw_contour(image, contours):
    for contour in contours:
        cv.drawContours(image, contour, -1, (255,0,0), 1)
        perimeter = cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, 0.02*perimeter, True)
        connors = len(approx)
        area = cv.contourArea(contour)
        x1, y1, x2, y2 = cv.boundingRect(approx)
        if connors > 2 and area > 500:
            cv.rectangle(image, (x1, y1), (x1+x2, y1+y2), (0,255,0), thickness=2)
