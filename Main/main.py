# DBL embedded systems group 40
# This is the Main python file for the project

import RPi.GPIO as GPIO
import time,sys
from ErrorControl import *
from main_functions import *

sys.path.append("../Colour_Sensor")
from TCS34725_class import TCS34725
from Colour_Functions import *

sys.path.append("../Light_Sensor")
from ObjectDetection import *

sys.path.append("../LCD")
from lcd import *
from lcd_game import *
from lcd_var import *

sys.path.append("../Motors")
from MotorControl import *

def main():
    ### Function that is called when the start button is pressed. It stops all other processes. 
    ### The user is asked to predict the number of white and black pucks that they expect to be in the end of the process. 
    ### A winning or losing message is printed correspondingly. 
    global start_button_state
    
    # Array and count to take average of colour readings for accuracy
    colour_array = ["None"]*5
    count = 0
    

    # Initialise Colour Sensor
    colourSensor = TCS34725()

    # Initialise Motor connection
    # Set PINs for controlling shift register (GPIO numbering)
    # Set PINs for controlling all 4 motors (GPIO numbering)
    amspi = AMSpi()
    amspi.set_74HC595_pins(9, 7, 6)
    amspi.set_L293D_pins(5, 15, 13, 19)

    # First the Environment light is measured and a benchmark is set
    environment_benchmark = detection_init()

    # The game is started and user input is taken
    w_discs, b_discs, pred_numb_white, pred_numb_black = lcd_display()

    start_button_state = True
    while start_button_state:

        #Check if object is detected
        print_waiting()
        # If an object is detected, then the value is True. Or else it's False.
        objectDetected = detect_object(environment_benchmark)
        
        if objectDetected:
            # Outputs "An object is detected!" on the LCD
            print_detection()
            # Starts a timer which will be use to measure the time it takes for the object to pass
            start_time = time.perf_counter()
            # Array storing the color readings of the object
            colour_array = []
            blocked = False
            while objectDetected:
                # Stores the colour name of the object calculated using LUX values returned from the colour sensor
                colour = run_colour_sensor(colourSensor)
                # Inserts the colour name to an array
                colour_array.append(colour)
                # Ends the timer
                current_time = time.perf_counter()
                
                # When the sensor is blocked for more than 5 seconds, then the LCD displays an error message
                if(current_time - start_time > 5):
                    sensorBlockedError()
                    blocked = True
                # Repeats the process all over again until there's nothing in front of the sensor
                objectDetected = detect_object(environment_benchmark)
            
            if not blocked:
            # Stores the colour of the object based on the most frequent colour name in the array
                obj_colour = get_colour(colour_array, len(colour_array))
                w_discs, b_discs, pred_numb_white, pred_numb_black = sortDisk(obj_colour, amspi, w_discs, b_discs, pred_numb_white, pred_numb_black)
            objectDetected = False
      


    
if  __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()