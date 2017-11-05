import cv2
import numpy as np
import sys

# Author Rishab Shah
# Adapted to Python by Nick VanDeusen

# Original
src = cv2.imread(sys.argv[1])
cv2.namedWindow( "Original image", cv2.WINDOW_NORMAL )
cv2.imshow("Original image", src)

# RGB
r,g,b = cv2.split(src)

RGBpixel = src[20,25]
print RGBpixel

cv2.imshow("Red",   r)
cv2.imshow("Green", g)
cv2.imshow("Blue",  b)
cv2.imwrite("ColorImage_Out/Red.png", r)
cv2.imwrite("ColorImage_Out/Green.png", g)
cv2.imwrite("ColorImage_Out/Blue.png", b)

ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCR_CB)
Y, Cb, Cr = cv2.split(ycrcb_image)

YCRCBpixel = ycrcb_image[20,25]
print YCRCBpixel

cv2.imshow("Y",   Y)
cv2.imshow("Cb",  Cb)
cv2.imshow("Cr",  Cr)
cv2.imwrite("ColorImage_Out/Y.png", Y)
cv2.imwrite("ColorImage_Out/Cb.png", Cb)
cv2.imwrite("ColorImage_Out/Cr.png", Cr)

hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv_image)

HSVpixel = hsv_image[20,25]
print HSVpixel

cv2.imshow("Hue",   		H)
cv2.imshow("Saturation",    S)
cv2.imshow("Value",   		V)
cv2.imwrite("ColorImage_Out/Hue.png", H)
cv2.imwrite("ColorImage_Out/Saturation.png", S)
cv2.imwrite("ColorImage_Out/Value.png", V)
	
cv2.waitKey(0)