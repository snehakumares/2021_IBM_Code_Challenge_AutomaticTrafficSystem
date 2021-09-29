import cv2
import cvlib as cv
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im = cv2.imread('capture.png')

bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)

print("Vehicle Count : " + str(
        label.count('bicycle') + 
        label.count('car') + 
        label.count('motorcycle') + 
        label.count('bus') + 
        label.count('truck')
    )
)