import math
import machine
import utime
import picounicorn

picounicorn.init()

# From CPython Lib/colorsys.py
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        return v, v, v
    i = int(h*6.0)
    f = (h*6.0) - i
    p = v*(1.0 - s)
    q = v*(1.0 - s*f)
    t = v*(1.0 - s*(1.0-f))
    i = i%6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q

w = picounicorn.get_width()
h = picounicorn.get_height()

# Display a rainbow across Pico Unicorn
for x in range(w):
    for y in range(h):
        r, g, b = [int(c * 255) for c in hsv_to_rgb(x / w, y / h, 1.0)]
        picounicorn.set_pixel(x, y, r, g, b)

print("Press Button A")

while not picounicorn.is_pressed(picounicorn.BUTTON_A):  # Wait for Button A to be pressed
    pass

# Clear the display
for x in range(w):
    for y in range(h):
        picounicorn.set_pixel(x, y, 0, 0, 0)

print("Button A pressed!")


# Original program Thermometer by NOSUKE
# Function to clear display by setting pixels to black
def cleardisplay():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)
            
# Define colours
whitecolour=(127,127,127)

# Set constant variables for temperature
BLANK= [" " for i in range(h)] 

ZERO=["   ",
      "XXX",
      "X X",
      "X X",
      "X X",
      "XXX",
      "   "]
         
ONE=["   ",
     " X ",
     "XX ",
     " X ",
     " X ",
     "XXX",
     "   "]
        
TWO=["   ",
     "XXX",
     "  X",
     "XXX",
     "X  ",
     "XXX",
     "   "]
        
THREE=["   ",
       "XXX",
       "  X",
       "XXX",
       "  X",
       "XXX",
       "   "]

FOUR=["   ",
      "X X",
      "X X",
      "XXX",
      "  X",
      "  X",
      "   "]

FIVE=["   ",
      "XXX",
      "X  ",
      "XXX",
      "  X",
      "XXX",
      "   "]

SIX=["   ",
     "XXX",
     "X  ",
     "XXX",
     "X X",
     "XXX",
     "   "]

SEVEN=["   ",
       "XXX",
       "  X",
       "  X",
       "  X",
       "  X",
       "   "]

EIGHT=["   ",
       "XXX",
       "X X",
       "XXX",
       "X X",
       "XXX",
       "   "]

NINE=["   ",
      "XXX",
      "X X",
      "XXX",
      "  X",
      "XXX",
      "   "]

DOT=[" ",
     " ",
     " ",
     " ",
     " ",
     " ",
     "X"]

LETTERC=["X  ",
         " XX",
         "X  ",
         "X  ",
         "X  ",
         " XX",
         "   "]

# Create dictionaries to store numbers/text
tempdict={0:ZERO,1:ONE,2:TWO,3:THREE,4:FOUR,5:FIVE,6:SIX,7:SEVEN,8:EIGHT,9:NINE,"dot":DOT,"C":LETTERC}

# Temperature reading
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    temp1 = int(temperature / 10)
    temp2 = int(temperature - temp1 * 10)
    temp3 = int(temperature * 10 - temp1 * 100 - temp2 * 10)
    print(temp1, temp2, temp3)
    
    # Change colour depending on temperature
    if 0 < temperature <= 10:
        tempcolour=(0,127,127)
    elif 10 < temperature <= 20:
        tempcolour=(0,0,255)
    elif 20 < temperature <= 30:
        tempcolour=(0,255,0)
    elif 30 < temperature <= 40:
        tempcolour=(127,127,0)
    elif 40 < temperature <= 50:
        tempcolour=(255,0,0)
    else:
        tempcolour=(127,127,127)
    
    # Function to update display with numbers/text
    def updatedisplay(displaymap):
        x=0
        y=0
        for row in displaymap:
            for line in row:
                for char in line:
                    if x < w and y <h:
                        if char == "X":
                            r, g, b = whitecolour
                        elif char == "T":
                            r, g, b = tempcolour
                        else:
                            r,g,b=0,0,0
                        picounicorn.set_pixel(x, y, r, g, b)
                    x+=1
                x=0
            y+=1
        return displaymap

    # Function to generate an 2D array to represent the current temperature in the format
    def generatetemp(temp1,temp2,temp3):
        temp1pix = [item.replace("X","T") for item in tempdict[temp1]]
        temp2pix = [item.replace("X","T") for item in tempdict[temp2]]
        temp3pix = [item.replace("X","T") for item in tempdict[temp3]]
        fulldisplay = [["{}{}{}{}{}{}{}".format(temp1pix[i],BLANK[i],temp2pix[i],DOT[i],temp3pix[i],BLANK[i],LETTERC[i])] for i in range(h)]
        return fulldisplay
    
    # Temperature display
    updatedisplay(generatetemp(temp1,temp2,temp3))
    utime.sleep_ms(1000)

