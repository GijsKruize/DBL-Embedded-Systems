# Garbage Sorter 3000
DBL-Embedded-System project to sort white and black discs using **Fischertechnik parts**, **Arduino Motor Shield**, and **Raspberry Pi**.

### Requirements
- Libraries
- 2x Breadboards
- 2x Motors
- 1x Colour Sensor
- 1x Photoresistor
- 1x Conveyor Belt
- 2x Buttons
- 1x Raspberry Pi
- 1x Arduino Motor Shield
- Fishertechnik Parts
- A lot of jumper cables

### The Libraries Used are:
- Motor control: [AMSpi by Jan Lipovský](https://github.com/lipoja/AMSpi)
- LCD control: [RPiSpy by Matt Hawkins](https://www.raspberrypi-spy.co.uk/2012/07/16x2-lcd-module-control-using-python/)
- Color Sensor: [TCS3472 control by SHEDBOY71](http://www.pibits.net/code/raspberry-pi-and-tcs34725-color-sensor.php)

### What it does:
During its calibration sequence, the sensors will measure the environment value of the room which then will be used to determine the colour of the disc. The robot detects the colour of any object passing the photoresistor and colour sensors stationed right next to the conveyor belt.
It will behave differently for different colours: 
- White : Pushed into the ramp and directed to the designated bin
- Black : Pushed into the ramp and directed to the designated bin
- Green : Pushed into the ramp and stopped by the lower gate
- Other : Ignored

### Game Aspect:
The game starts by pressing a button. The user is asked to input their predicted number of white and black discs that will pass by the sensors using the button. The robot will keep track on the number of black and white discs and when all the discs have been put onto the belt, then these values will be compared to determine whether the user wins or loses. The user will be then be asked if they want to play the game or not.

### Executable Files:
- main.py : Integrates all the files and runs the roboot with sensor detections, motors and the LCD game.
- Colour_detection.py : This is a component test file script for the colour sensor. The colour sensor is run and prints the luminance and RGB detection values.
- Game_test.py : This is a component test file where the the game is tested without the input of the colour sensors.
- Object_detection.py : This is a component test file for the object detection on the conveyor belt using the light sensor.
- Motor_test.py : This is a component test file that is used to test the function of the motors without other components of the robot

