#This file includes variables used in operating the LCD display and game logic
import RPi.GPIO as GPIO

# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 27
LCD_D4 = 22
LCD_D5 = 25
LCD_D6 = 24
LCD_D7 = 23

GPIO.setmode(GPIO.BCM) #set pin mode

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line on the LCD
LCD_CHR = True
LCD_CMD = False

global LCD_LINE_1
global LCD_LINE_2
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

# define variables
total_discs = 3 # total amount of discs to be sorted
global start_button_state # variable to keep track of the state of the start button
start_button_state = True # set start button variable to true
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set pin 5 to be the beginning of the game
GPIO.setup(14, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Set pin 4 to be an input pin and set initial value to be pulled low (off)
