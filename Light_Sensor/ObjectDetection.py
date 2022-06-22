### ObjectDetection.py
### DBL embedded Systems, group 40
### This files has 2 functions, 
### -   detection_init() wich initialises the sensors and takes environment readings to create a benchmark
### -   detect_object() which recognises whether an object is in front of the sensor

import math
import time
import sys
from SensorOutput import *
sys.path.append("../LCD")
from lcd import *
from lcd_var import *

### OBJECT DETECTION CONSTANTS
environmentAmount = 15  # constant for on how many readings are taken for the benchmark environment reading
delta = 600 # constant for how much the light level must change from the benchmark environment value before an object is detected
# Constant for LCD display loading bar
loadBar =  ["[..............]",
            "[=.............]",
            "[==............]",
            "[===...........]",
            "[====..........]",
            "[=====.........]",
            "[======........]",
            "[=======.......]",
            "[========......]",
            "[=========.....]",
            "[==========....]",
            "[===========...]",
            "[============..]",
            "[=============.]",
            "[==============]" ]

# This function intialises the light sensor and takes an intial reading of the enivornment lighting to set as a benchmark for comparisons
def detection_init():
    # setting initial values
    environment = 0 # value for light level of environment

    # initialising the LCD
    lcd_main()
    time.sleep(1)

    # printing calibration instructions on the LCD
    lcd_string("Measuring environ", LCD_LINE_1)
    lcd_string("ment lighting ", LCD_LINE_2)
    time.sleep(3)
    lcd_string("starting in:", LCD_LINE_1)
    lcd_string("3", LCD_LINE_2)
    time.sleep(1)
    lcd_string("2", LCD_LINE_2)
    time.sleep(1)
    lcd_string("1", LCD_LINE_2)
    time.sleep(1)

    # printing next instruction, adding progressbar on LCD
    lcd_string("Measuring", LCD_LINE_1)
    lcd_string(loadBar[0], LCD_LINE_2)
    avgSum =0
    # taking 15 readings from environment as a baseline 
    for i in range(environmentAmount):
        avgSum = avgSum + rc_filter(i)
        # updating the progressbar when measuring
        lcd_string(loadBar[math.floor((14/environmentAmount)*(i+1))], LCD_LINE_2)
    environment = avgSum /environmentAmount     # taking the average of the 15 readings

    time.sleep(1)
    environment = environment + 500 # calibrating the environment benchmark
    # notifying users the initialisation is done
    lcd_string("Initialisation ", LCD_LINE_1)
    lcd_string("done", LCD_LINE_2)

    return environment  # returns environment benchmark to use for object detection

# This function is run to determine the presence of an object on the conveyor belt
# The initial benchmark environment is passed as a parameter.
def detect_object(environment):
    measurement = rc_filter(1)
    if (measurement > environment + delta):     # if the measurement is too different from environment, an object is in front
        blockedBool = True          # returns true to signify an object
    else:
        blockedBool = False         # returns false to signify no object
    return blockedBool
