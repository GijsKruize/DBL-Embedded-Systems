import time,sys
from ErrorControl import *

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

TIME_TO_SORTER = 3
TIME_TO_BIN = 2

def sortDisk(obj_colour, amspi, w_discs, b_discs, pred_numb_white, pred_numb_black):
    '''The function contains different treatments for each colour. It keeps track the number of white and black pucks and outputs messages
    to the LCD for green and other colours.'''    
    if obj_colour == "Green":
        # Moves the upper arm to push the green disc to the ramp
        sort_green(amspi)
        # Asks the user to remove the green disc from the ramp and hold the start button to go back to the game
        green_disk()
        
    elif obj_colour == "Other":
        # Displays "unknown colour detected. Allowing object to pass." on the LCD
        other_colour()
    else:
        # Displays the colour of the disc on the LCD
        print_colour(obj_colour)
       
        if obj_colour == "White":
            # Push the disk into the sorting machine
            sort_white(amspi)
            
            # Increment number of white disks and check for overflow
            w_discs = w_discs + 1
            return game_check(w_discs, b_discs, pred_numb_white, pred_numb_black)
            
        elif obj_colour == "Black":
            # Push the disk into the sorting machine
            sort_black(amspi)

            # Increment number of black disks and check for overflow
            b_discs = b_discs + 1
            return game_check(w_discs, b_discs, pred_numb_white, pred_numb_black)
            
    return w_discs, b_discs, pred_numb_white, pred_numb_black

# LCD display if white/black is detected
def print_colour(colour):
    lcd_string(colour + " disk", LCD_LINE_1)
    lcd_string("detected!", LCD_LINE_2)

# LCD display if an object is detected by the colour sensor and photoresistor
def print_detection():
    lcd_string("An object is", LCD_LINE_1)
    lcd_string("detected!", LCD_LINE_2)

# LCD display if during idle state where the colour sensor and photoresistor are waiting for an object to pass
def print_waiting():
    lcd_string("Waiting for", LCD_LINE_1)
    lcd_string("object", LCD_LINE_2)

# Actions taken when black or white or green colored discs are detected   
def sort_green(amspi):
    time.sleep(TIME_TO_SORTER)
    activate_conveyor_push(amspi)

def sort_white(amspi):
    activate_selection(amspi, True)
    time.sleep(TIME_TO_SORTER)
    activate_conveyor_push(amspi)
    time.sleep(TIME_TO_BIN)
    deactivate_selection(amspi,True)
    
def sort_black(amspi):
    activate_selection(amspi, False)
    time.sleep(TIME_TO_SORTER)
    activate_conveyor_push(amspi)
    time.sleep(TIME_TO_BIN)
    deactivate_selection(amspi,False)
