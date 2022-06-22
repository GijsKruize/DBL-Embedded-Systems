### ErrorControl.py
### DBL embedded Systems, group 40
import sys, time
import RPi.GPIO as GPIO
# from LCD.lcd_game import game_end

sys.path.append("../LCD")
from lcd import *
from lcd_var import *
from lcd_game import *

sys.path.append("../Light_Sensor")
from ObjectDetection import *

def sensorBlockedError():
    ''' Function dealing with the photoresistor being blocked for more than the certain amount of time. The LCD will display the error.'''
    lcd_string("The sensor is", LCD_LINE_1)
    lcd_string("blocked.", LCD_LINE_2)
    time.sleep(1.5)
    lcd_string("Please remove", LCD_LINE_1)
    lcd_string("object.", LCD_LINE_2)
    time.sleep(2)
            
def green_disk():
    """ Function designed for when a green puck is detected. It initializes a countdown sequence as part of the game.    
        The user has then 10 seconds to remove the green disk. If they do not, they lose the game. 
    """
    global start_button_state 
    lcd_string("TOXIC WASTE", LCD_LINE_1)
    lcd_string("DETECTED!", LCD_LINE_2)
    time.sleep(1.5)
    lcd_string("You have 10 secs", LCD_LINE_1)
    lcd_string("to remove it!", LCD_LINE_2)
    time.sleep(1.5)
    lcd_string("Then hold the", LCD_LINE_1)
    lcd_string("start button!", LCD_LINE_2)
    time.sleep(1.5)
    rem_counter = 10
    start_button_state = GPIO.input(14)
    while start_button_state and rem_counter > 0:   # while start button is not pressed, start counter  
        # while rem_counter >= 0: #
            lcd_string("Time left:", LCD_LINE_1)
            lcd_string(" " + str(rem_counter), LCD_LINE_2)
            time.sleep(1)
            rem_counter -= 1
            if rem_counter == 0:
                lcd_string("You failed", LCD_LINE_1)
                lcd_string("to remove it! ", LCD_LINE_2)
                time.sleep(2) 
                game_end(0,0,1,1)
            start_button_state = GPIO.input(14)
    lcd_string("You saved the", LCD_LINE_1)
    lcd_string("environment!", LCD_LINE_2)
    time.sleep(1.5)
    #time.sleep(2)
    #lcd_display()
    
def other_colour():
    lcd_string("Unknown col", LCD_LINE_1)
    lcd_string("our detected", LCD_LINE_2)
    time.sleep(1.5)
    lcd_string("Allowing obj", LCD_LINE_1)
    lcd_string("ect to pass", LCD_LINE_2)
    time.sleep(1.5)