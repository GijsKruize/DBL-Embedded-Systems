### MotorControl.py
### DBL embedded Systems, group 40
### This files has 2 functions, 
### -   activate_conveyor_push() which activate the pushing sequence from the conveyor belt
### -   activate_selection(direction) which puts the selector in the correct position, depending on the value of direction

from AMSpi import AMSpi
import RPi.GPIO as GPIO
import time

def activate_conveyor_push(amspi):
    '''Function to activate the first motor (upper arm) and move it such that it pushes discs that are in front of it.'''
    amspi.run_dc_motors([amspi.DC_Motor_1], clockwise=False, speed=70)
    time.sleep(0.9)
    amspi.stop_dc_motors([amspi.DC_Motor_1])
    time.sleep(1)
    amspi.run_dc_motors([amspi.DC_Motor_1], speed=70)
    time.sleep(0.85)
    amspi.stop_dc_motors([amspi.DC_Motor_1])


def activate_selection(amspi, direction):
    '''Function to active the second motor (lower arm) and move it such that it directs the disc sliding on the ramp to the designated bin.'''
    # direction is determined by the colour of the disc 
    if direction==True:
        amspi.run_dc_motors([amspi.DC_Motor_2], clockwise=False)
        time.sleep(0.13)
        amspi.stop_dc_motors([amspi.DC_Motor_2])
    else:
        amspi.run_dc_motors([amspi.DC_Motor_2])
        time.sleep(0.13)
        amspi.stop_dc_motors([amspi.DC_Motor_2])

def deactivate_selection(amspi, direction):
    '''Function to move the second motor to reset its position. '''
    # direction is determined by the colour of the disc
    if direction==True:
        amspi.run_dc_motors([amspi.DC_Motor_2])
        time.sleep(0.13)
        amspi.stop_dc_motors([amspi.DC_Motor_2])
    else:
        amspi.run_dc_motors([amspi.DC_Motor_2], clockwise=False)
        time.sleep(0.13)
        amspi.stop_dc_motors([amspi.DC_Motor_2])