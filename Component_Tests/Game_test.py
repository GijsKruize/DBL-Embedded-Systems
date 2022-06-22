# This file is where the the game is tested without the input of the colour sensors

import RPi.GPIO as GPIO
import time
import sys 

sys.path.append("../LCD")
from lcd import *
from lcd_var import *
from lcd_game import *


# Initialise the lcd display
def lcd_display():  
  global input_state
  global start_button_state
  GPIO.setmode(GPIO.BCM) #set pin mode
  while start_button_state:
    lcd_string("Press button to",LCD_LINE_1)
    lcd_string("start the game!",LCD_LINE_2)
  gamestart()

def gamestart():
    ''' Function that is called when the start button is pressed. It stops all other processes. 
    The user is asked to predict the number of white and black pucks that they expect to be in the end of the process. 
    A winning or losing message is printed correspondingly. 
    '''
    global start_button_state # state of start button
    global input_state
    start_button_state = True
    global pred_numb_white # prediction of white pucks
    global pred_numb_black # prediction of black pucks
    global w_discs
    global b_discs 
    w_discs = 0
    b_discs = 0
    pred_numb_white = -1 # prediction number of white discs
    pred_numb_black = total_discs + 1 # prediction number of black discs

    lcd_string("The game has", LCD_LINE_1)
    lcd_string("begun!", LCD_LINE_2)
    time.sleep(2)
  
    lcd_string("Press input button", LCD_LINE_1)
    lcd_string("to start counter!", LCD_LINE_2)

    while start_button_state:   # while first button is not pressed it takes white and black disc prediction input
        
        if input_state == True and pred_numb_white <= total_discs and pred_numb_black >= 0: # cannot guess higher than total discs to be sorted
          #if input button is pressed, start displaying the predicted number of white and black pucks. Max white = 5
          pred_numb_white += 1 # increment 
          pred_numb_black -= 1 # decrement
          pred_numb_white = pred_numb_white % (total_discs+1)
          pred_numb_black = pred_numb_black % (total_discs+1)
          lcd_string("White pucks: " + str(pred_numb_white), LCD_LINE_1)
          lcd_string("Black pucks: " + str(pred_numb_black), LCD_LINE_2)
          time.sleep(0.2)
        
    start_button_state = True

if  __name__ == '__main__':
    try:
        lcd_main()
        lcd_display()
    except KeyboardInterrupt:
        GPIO.cleanup()