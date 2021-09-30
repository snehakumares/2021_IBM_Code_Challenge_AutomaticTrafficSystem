import cv2
import cvlib as cv

# Function to count the number of vehicles from image
def count_vehicle(img):
    # Image from file name is stored to im
    im = cv2.imread(img)

    # Define labels for the objects in the image using the YOLO library. 
    _, label, _ = cv.detect_common_objects(im)

    # Count the vehicles which are labelled as bicycle, car, motorcycle, bus and truck
    count = label.count('bicycle') + label.count('car') + label.count('motorcycle') + label.count('bus') + label.count('truck')
    print("Vehicle Count : {}".format(count))
    
    return count
