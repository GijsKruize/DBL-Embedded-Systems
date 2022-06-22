### SensorOutput.py
### DBL embedded Systems, group 40
### This files has 2 functions, 
### -   rc_time() wich counts the time it takes for the photo resistor to fill up the capacitor once
### -   rc_filter() which applies a rolling filter to the values from rc_time

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit, creating the global array, and set a initialisation boolean
pin_to_circuit = 17
count_upper_limit = 100000
arr=[]
arr = [0 for i in range(5)]

#reading the time it takes to charge the capacitor one time
def rc_time (pin_to_circuit):
    count= 0

    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW) and (count < count_upper_limit):
        count += 1

    return count

#filtering the raw input data
def rc_filter(init):
    global arr
    #at initialisation taking 5 new inputs to get a accurate reading
    if init==0:
        arr[0] = rc_time(pin_to_circuit)
        arr[1] = rc_time(pin_to_circuit)
        arr[2] = rc_time(pin_to_circuit)
        arr[3] = rc_time(pin_to_circuit)
        arr[4] = rc_time(pin_to_circuit)

    #when called after initialisation the values are shifted over so it creates a rolling filter effect
    else:
        arr[0] = arr[1]
        arr[1] = arr[2]
        arr[2] = arr[3]
        arr[3] = arr[4]
        arr[4] = rc_time(pin_to_circuit)

    #computing the mean of the array of readings
    filter= (arr[0]+arr[1]+arr[2]+arr[3]+arr[4])/50
    #converting the mean to an integer for more efficient learning
    filter = int(filter)
    return filter   #return the value after applying the rolling filter
