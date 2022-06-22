### lcd_game.py
### DBL embedded Systems, group 40
### This files has 4 functions, 
### -   def lcd_display() which waits for a button press until the game is started
### -   gamestart() which starts the game by taking prediction input from the user
### -   game_check() which checks whether all discs have been sorted and if so calls game_end()
### -   game_end() which ends the game and prints a winning or losing message
import sys

sys.path.append("../LCD")
from lcd_var import *
from lcd import *
import RPi.GPIO as GPIO
import time
from random import randint

loseUp = ["WOW! you lose",    # array with top lines of losing messages 
          "You lost",
          "Lost again?",
          "LOST! :D",
          "Step on a Fisch",
          "Try again loser",
          "Wanna hear a",
          "STOP IT",
          "Last chance!"]
loseDown = ["-_-",  # array with bottom lines of losing messages
          "'nietsnut'",
          "Just stop",
          "*Rethinks life*",
          "erTechnick",
          "or just don't",
          "joke: YOU WON",
          "Get some help",
          "or else........"]


def lcd_display():  # function which waits for button press before starting the game

  global start_button_state
  while start_button_state:
    lcd_string("Press button to",LCD_LINE_1)
    lcd_string("start the game!",LCD_LINE_2)
    start_button_state = GPIO.input(14)
  return gamestart()



def gamestart():
    ''' Function that is called when the start button is pressed. It stops all other processes. 
    The user is asked to predict the number of white and black pucks that they expect to be in the end of the process. 
    A winning or losing message is printed correspondingly. 
    '''
    global start_button_state # state of start button
    start_button_state = True
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
        start_button_state = GPIO.input(14) # start button corresponds to the state of pin 14
        input_state = GPIO.input(4) # input button corresponds to the state of pin 4
        
        if input_state == False and pred_numb_white <= total_discs and pred_numb_black >= 0: # cannot guess higher than total discs to be sorted
          #if input button is pressed, start displaying the predicted number of white and black pucks.
          pred_numb_white += 1          # increment 
          pred_numb_black -= 1          # decrement
          pred_numb_white = pred_numb_white % (total_discs+1)
          pred_numb_black = pred_numb_black % (total_discs+1)
          lcd_string("White pucks: " + str(pred_numb_white), LCD_LINE_1)
          lcd_string("Black pucks: " + str(pred_numb_black), LCD_LINE_2)
          time.sleep(0.2)
    start_button_state = True
    return w_discs, b_discs, pred_numb_white, pred_numb_black         # return prediction values to main

def game_check(w_discs, b_discs, pred_numb_white, pred_numb_black):   # function which calls game_end() if all discs have been sorted
    if w_discs + b_discs == total_discs:
        return game_end(w_discs, b_discs, pred_numb_white, pred_numb_black)     # calls function which ends game, returns reset variables
    else:
        return w_discs, b_discs, pred_numb_white, pred_numb_black     # return unchanged variables
    
def game_end(whiteAmount, blackAmount, pred_numb_white, pred_numb_black):
    '''Function that is called when the predetermined amount of discs is sorted. 
    It prints a winning or losing message based on whether predicted and real amounts align.
    Then it asks if the player wants to start another game and will do so if the button is pressed.'''
    start_button_state = True

    if pred_numb_white == whiteAmount and pred_numb_black == blackAmount:  # check whether predicted and real amounts are the same
        lcd_string("The game is over", LCD_LINE_1)
        lcd_string("You win!", LCD_LINE_2)
        time.sleep(2)

    else:
        messageNum = randint(0,len(loseDown))     # creates a random integer to select one of the losing messages from the array
        lcd_string(loseUp[messageNum], LCD_LINE_1)          # displays randomly chosen losing message
        lcd_string(loseDown[messageNum], LCD_LINE_2)
        time.sleep(5)

    while GPIO.input(14):     # asks whether players wants to play another game until button is pressed
      lcd_string("Would you like", LCD_LINE_1)
      lcd_string("to play again?", LCD_LINE_2)
    
    return gamestart()        # calls gamestart to start a new game, returns reset variables
