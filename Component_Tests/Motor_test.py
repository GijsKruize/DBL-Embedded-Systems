### Motor_test.py
### DBL embedded Systems, group 40
### This file is to component test the motors on the robot
import sys
sys.path.append("../Motors")
from AMSpi import AMSpi
from MotorControl import *
import time

if __name__ == '__main__':
    amspi = AMSpi()
        # Set PINs for controlling shift register (GPIO numbering)
    amspi.set_74HC595_pins(9, 7, 6)
        # Set PINs for controlling all 4 motors (GPIO numbering)
    amspi.set_L293D_pins(5, 15, 13, 19)
    for i in range (2):
        # Set selector gate to the right and push puck into the sorter
        activate_selection(amspi, True)
        time.sleep(2)
        activate_conveyor_push(amspi)
        time.sleep(3)
        deactivate_selection(amspi,True)
        time.sleep(1)
        
        # Set selector gate to the left and push puck into the sorter
        activate_selection(amspi, False)
        time.sleep(2)
        activate_conveyor_push(amspi)
        time.sleep(1)
        deactivate_selection(amspi,False)
        time.sleep(1)
    
    #As long as code isnt done the motors wont go crazy
    while True:
        time.sleep(0.1)
