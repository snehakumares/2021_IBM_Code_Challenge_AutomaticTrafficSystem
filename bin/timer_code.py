# This file is a demonstration of how this will be implemented in a embedded system
# For the sake of simplicity, images are saved within the folder using the a naming convention

# OpenCV is used to read images and identify various objects in the image using pretrained models from YOLO library.
# Visit https://opencv.org/about/ and https://github.com/pjreddie/darknet/wiki/YOLO:-Real-Time-Object-Detection
# for more information on the models and operations

import cv2
import time
import cvlib as cv
from cvlib.object_detection import draw_bbox

# A demo array with image names is defined. In practical application, this will
# be replaced with access to individual cameras

junc_images = ['1.jpg', '2.png', '3.png', '4.png']

while True:
    # Scanning each image until external interrupt
    for image in junc_images:
        im = cv2.imread(image)
        
        # Define labels, bounding box and confidence for the objects in the image using the YOLO library. 
        bbox, label, conf = cv.detect_common_objects(im)

        # Create a bounding box with label and confidence levels
        output_image = draw_bbox(im, bbox, label, conf)

        # Count the number of vehicles from given labels
        count = label.count('bicycle') + label.count('car') + label.count('motorcycle') + label.count('bus') + label.count('truck')
        
        # Hard coded values are used. A threshold is set and timer is given accordingly with
        # minimum being 15 seconds and maximum being 60 seconds

        if count < 7:
            timer = 15
        elif count < 15:
            timer = 30
        else:
            timer = 60
        
        # Display the accessed image
        cv2.imshow('image',im)
        cv2.waitKey(1)

        # Run the timer
        print('---\nVehicle count : {}'.format(count))
        print('Calculating countdown...')
        print('Timer running')
        
        # Display a countdown timer
        for i in range(timer, 0, -1):
            print(i, end = '\r')
            time.sleep(1)
