### Colour_Functions.py
### DBL embedded Systems, group 40
### This files has 2 functions, 
### -   run_colour_sensor() which will take the colour reading and print the colour detected,
###                         this function also has a testing mode for a more verbose output for component testing
### -   print_test_values() which prints all values being read, for testing
### -   read_colour() which reads the current colour reading and adds it to an array of recent readings
### -   get_colour() reads from the array of recent colour readings and returns the most common reading

from TCS34725_class import TCS34725

### COLOUR CONSTANTS 
# Upper RGB bounds for Black colour
RED_BOUND_BLACK, BLUE_BOUND_BLACK, GREEN_BOUND_BLACK = 30, 30, 30
# Lower RGB bounds for White colour
RED_BOUND_WHITE, BLUE_BOUND_WHITE, GREEN_BOUND_WHITE = 180, 180, 180
# Ratio for RB channels compared to G for Green colour
GREEN_RATIO = (4/5)

# Set max/min luminance for RGB conversion
MAX_LUMINANCE = [2340, 3610, 3600]
MIN_LUMINANCE = [190, 240, 210]

# Set the number of colour readings stored in the array
MAX_COUNT = 5

# The names of the colours that can be detected
COLOUR_NAMES = ["White", "Black", "Green", "Other"]

# Number of colours that can be detected
NUM_COLOURS = 4

# Takes inputs: 
# colourSensor (instance of TCS34725)
# max_luminance (max RGB luminance for white)
# min_luminance (min RGB luminance for white)
def run_colour_sensor(colourSensor, test=False):
    # Initialise colour name
    colour_name = "Not determined"
    
    # Get luminance reading and seperate it into red, blue, green
    lum = colourSensor.readluminance()            
    luminance = [lum['r'],lum['g'],lum['b']]

    # Convert the reading to RGB value 0-255
    rgb = colourSensor.convertToRgb(luminance, MAX_LUMINANCE, MIN_LUMINANCE)

    # Determine the colour of the object
    if (rgb[0]<RED_BOUND_BLACK and rgb[1]<BLUE_BOUND_BLACK and rgb[2]<GREEN_BOUND_BLACK): #Black is within defined lower RGB bounds
        colour_name = "Black"
    elif (rgb[0]>RED_BOUND_WHITE and rgb[1]>BLUE_BOUND_WHITE and rgb[2]>GREEN_BOUND_WHITE): #White is within defined upper RGB bounds
        colour_name = "White"
    elif (lum['r']<(lum['g']*GREEN_RATIO) and lum['b']<(lum['g']*GREEN_RATIO)): # Both Red and Blue are below a defined ratio of the Green luminance
        colour_name = "Green"
    else:
        colour_name = "Other"

    # This is only for component testing purposes
    if test:
        print_test_values(lum, rgb, colour_name)

    return colour_name

# This function prints out all the values being read for testing
def print_test_values(lum, rgb, colour_name):
    # Print raw Lux values
    print ("Red Color Luminance : %d lux"%(lum['r']))
    print ("Green Color Luminance : %d lux"%(lum['g']))
    print ("Blue Color Luminance : %d lux"%(lum['b']))
    print (" ============= ")
    # Print RGB converted values
    print ("Red: %d"%(rgb[0]))
    print ("Green: %d"%(rgb[1]))
    print ("Blue: %d"%(rgb[2]))
    # Print out colour to terminal and LCD display
    print ("This is: " + colour_name)
    print (" ***************************************************** ")

# Read colour reading and add it to the colour array
def read_colour(colour_array, count, colour_sensor):
    # Get reading
    colour = run_colour_sensor(colour_sensor, test=False)
    # Add to colour array
    colour_array[count] = colour
    # Increment counter in a cycle
    count = (count + 1)  % MAX_COUNT

    return colour_array, count

# Get the most common colour reading from the colour array
def get_colour(colour_array,size):
    # Init vars
    counts = [0,0,0,0]
    max = 0
    max_index = -1

    # Count the number of times a colour is detected
    for i in range(size):
        index = COLOUR_NAMES.index(colour_array[i])
        counts[index] = counts[index] + 1
    
    # Get the index of the most common colour reading
    for i in range(NUM_COLOURS):
        if counts[i] > max:
            max = counts[i]
            max_index = i
    
    # Return the most common colour reading
    return COLOUR_NAMES[max_index]
