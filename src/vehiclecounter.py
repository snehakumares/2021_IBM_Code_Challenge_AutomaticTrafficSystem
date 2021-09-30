import cv2
import cvlib as cv
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

#function to count the number of vehicles from image
def count_vehicle(img):

    #image from file name is stored to im
    im = cv2.imread(img)

    #different objects in the image are detected
    bbox, label, conf = cv.detect_common_objects(im)
    # output_image = draw_bbox(im, bbox, label, conf)

    #only count the objects which are labelled as bicycle,car,motorcycle,bus and truck
    print("Vehicle Count : " + str(
        label.count('bicycle') +
        label.count('car') +
        label.count('motorcycle') +
        label.count('bus') +
        label.count('truck')
    )
          )
    return label.count('bicycle') + label.count('car') + label.count('motorcycle') + label.count('bus') + label.count('truck')
