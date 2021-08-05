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
LETcolour=(63,0,63)

# Set constant variables for message
GOOD=["    ",
      " X  ",
      " XXX",
      "XXXX",
      "XXXX",
      "XXXX",
      "    "]

SURP=["    ",
      " XX ",
      " XX ",
      " XX ",
      "    ",
      " XX ",
      "    "]

YO=["    ",
    "XXXX",
    "   X",
    "XXXX",
    "   X",
    "XXXX",
    "    "]

RO=["    ",
    "XXXX",
    "X  X",
    "X  X",
    "X  X",
    "XXXX",
    "    "]

SI=["    ",
    "XX X",
    "   X",
    "XX X",
    "   X",
    "XXX ",
    "    "]

KU=["    ",
    " XXX",
    "X  X",
    "   X",
    "  X ",
    " X  ",
    "    "]

# Function to update display with numbers/text
def updatedisplay(displaymap):
    x=0
    y=0
    for row in displaymap:
        for line in row:
            for char in line:
                if x < w and y < h:
                    if char == "X":
                        r, g, b = LETcolour
                    else:
                        r,g,b=0,0,0
                    picounicorn.set_pixel(x, y, r, g, b)
                x+=1
            x=0
        y+=1
    return displaymap

# Function to generate an 2D array to represent the message in the format
def generatemessage():
    fulldisplay = [["                {} {} {} {} {} {}   ".format(GOOD[i],YO[i],RO[i],SI[i],KU[i],SURP[i])] for i in range(h)]
    return fulldisplay

#Function to make the "display map" seem as though it is "scrolling" (loop)
def scrolldisplay(displaymap):
    scrollmap=[]
    rowcount=0
    for row in displaymap:
        scrollmap.append([])
        for line in row:
            scrollmap[rowcount]= [line[1:]+line[0]]
        rowcount+=1
    return scrollmap

# Function to display the message
while True:
    currentdisplaymap=updatedisplay(generatemessage())
    for i in range(w*3):
        currentdisplaymap=updatedisplay(scrolldisplay(currentdisplaymap))
        utime.sleep_ms(1)
    cleardisplay()
