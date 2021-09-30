import cv2
import time
import cvlib as cv
from cvlib.object_detection import draw_bbox

junc_images = ['1.jpg', '2.png', '3.png', '4.png']
while True:
    for image in junc_images:
        im = cv2.imread(image)
        bbox, label, conf = cv.detect_common_objects(im)
        output_image = draw_bbox(im, bbox, label, conf)

        count = label.count('bicycle') + label.count('car') + label.count('motorcycle') + label.count('bus') + label.count('truck')
        
        if count < 7:
            timer = 15
        elif count < 15:
            timer = 30
        else:
            timer = 60
        
        cv2.imshow('image',im)
        cv2.waitKey(1)

        print('---\nVehicle count : {}'.format(count))
        print('Calculating countdown...')
        print('Timer running')
        for i in range(timer, 0, -1):
            print(i, end = '\r')
            time.sleep(1)