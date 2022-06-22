### Colour_detection.py
### DBL embedded Systems, group 40

### This file is a component test script for the colour sensor
### The colour sensor is run and prints constant detection values
import sys
import time

sys.path.append("../Colour_Sensor")
from TCS34725_class import TCS34725
from Colour_Functions import run_colour_sensor

sys.path.append("../LCD")
from lcd import *
from lcd_var import *

def main():
    # Create colour sensor instance and prepare connection to lcd display
    colourSensor = TCS34725()
    lcd_main()
    time.sleep(1)
    
    # Run the colour sensor in testing mode
    while True:
        colour_name = run_colour_sensor(colourSensor, test=True)
        lcd_string("Colour Detected:", LCD_LINE_1)
        lcd_string(colour_name, LCD_LINE_2)
        time.sleep(0.2)

if __name__ == "__main__":
    main()