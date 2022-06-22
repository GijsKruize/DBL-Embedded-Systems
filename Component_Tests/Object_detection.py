### Object_detection.py
### DBL embedded Systems, group 40
### This file is used for component testing of the object detection on the conveyor belt
import sys
sys.path.append("../Light_Sensor")
from ObjectDetection import *

if __name__ == '__main__':
    # Initialise light sensor
    env = detection_init()

    # Run object detection
    while True:
        print(detect_object(env))