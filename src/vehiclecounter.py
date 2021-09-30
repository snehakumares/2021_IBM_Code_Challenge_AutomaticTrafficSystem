import cv2
import cvlib as cv

#from cvlib.object_detection import draw_bbox

def count_vehicle(img):
    im = cv2.imread(img)

    bbox, label, conf = cv.detect_common_objects(im)
    # output_image = draw_bbox(im, bbox, label, conf)

    print("Vehicle Count : " + str(
        label.count('bicycle') +
        label.count('car') +
        label.count('motorcycle') +
        label.count('bus') +
        label.count('truck')
    )
          )
    return label.count('bicycle') + label.count('car') + label.count('motorcycle') + label.count('bus') + label.count('truck')
