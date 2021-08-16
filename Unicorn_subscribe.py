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


# Original program goodbutton by NOSUKE
# Function to clear display by setting pixels to black
def cleardisplay():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)

# Define colours
ROGOcolour=(255,0,127)

# Set constant variables for message
NOSUKER=[["                "],
         ["       RRR      "],
         ["      RR  R     "],
         ["     R R  R     "],
         ["     R R  R     "],
         ["      R  R      "],
         ["                "]]


# Function to update display with numbers/text
def updatedisplayp(displaymap):
    x=0
    y=0
    for row in displaymap:
        for line in row:
            for char in line:
                if x < w and y < h:
                    if char == "R":
                        r, g, b = LETcolour
                    else:
                        r,g,b=0,0,0
                    picounicorn.set_pixel(x, y, r, g, b)
                x+=1
            x=0
        y+=1
    return displaymap

def updatedisplayn(displaymap):
    x=0
    y=0
    for row in displaymap:
        for line in row:
            for char in line:
                if x < w and y < h:
                    if char == "R":
                        r,g,b=0,0,0
                    else:
                        r, g, b = LETcolour
                    picounicorn.set_pixel(x, y, r, g, b)
                x+=1
            x=0
        y+=1
    return displaymap

#Display the title screen for 2 seconds
while True:
    updatedisplayp(NOSUKER)
    utime.sleep_ms(500)
    cleardisplay()
    updatedisplayn(NOSUKER)
    utime.sleep_ms(500)
    cleardisplay()



