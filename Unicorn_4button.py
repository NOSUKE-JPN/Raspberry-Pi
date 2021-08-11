import math
import utime
import machine
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

"""
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
"""

# Original program Raspberry by NOSUKE
# Function to clear display by setting pixels to black
def cleardisplay():
    for x in range(w):
        for y in range(h):
            picounicorn.set_pixel(x, y, 0, 0, 0)

# Set constant variables for Raspberry
velocity = 10  # Flying speed
delay = 200  # Delay between rows
g, r, n = [0, 127, 0]  # Green
c, y, a = [255, 0, 63]  # Cyan
udcount = 3  # UpDown times
dntime = 500  # Down time
uptime = 500  # Up time
vntime = 50  # Vanish time

# Function to appear the raspberry
def raspberry():
    cleardisplay()
    
    # 1st row
    row = 1
    y = 6
    while y >= 0:
        x = 15
        if y == 3:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        else:
            while x >= row:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
                utime.sleep_ms(velocity)
                if x == row:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
                x -= 1
        y -= 1
    utime.sleep_ms(delay)
    
    # 2nd row
    row = 2
    y = 6
    while y >= 0:
        x = 15
        while x >= row:
            picounicorn.set_pixel(x, y, g, r, n)  # Green
            utime.sleep_ms(velocity)
            if x == row:  # Stop
                break
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
            x -= 1
        y -= 1
    utime.sleep_ms(delay)
    
    # 3rd row
    row = 3
    y = 6
    while y >= 0:
        x = 15
        if y == 6:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 0:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 3:
            while x >= row:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
                utime.sleep_ms(velocity)
                if x == row:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0) # Vanish
                x -= 1
        else:
            while x >= row:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
                utime.sleep_ms(velocity)
                if x == row:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
                x -= 1
        y -= 1
    utime.sleep_ms(delay)
    
    # 4th row
    row = 4
    y = 6
    while y >= 0:
        x = 15
        if y == 6:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 0:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        else:
            while x >= row:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
                utime.sleep_ms(velocity)
                if x == row:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
                x -= 1
        y -= 1
    utime.sleep_ms(delay)
    
    # 5th , 6th , 7th and 8th row
    row = 5
    while row <= 8:
        y = 6
        while y >= 0:
            x = 15
            while x >= row:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
                utime.sleep_ms(velocity)
                if x == row:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
                x -= 1
            y -= 1
        utime.sleep_ms(delay)
        row += 1
    
    # 9th row
    row = 9
    y = 6
    while y >= 0:
        x = 15
        if y == 6:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 0:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        else:
            while x >= 9:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
                utime.sleep_ms(velocity)
                if x == 9:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
                x -= 1
        y -= 1
    utime.sleep_ms(delay)
    
    # 10th row
    row = 10
    y = 6
    while y >= 0:
        x = 15
        if y == 6:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 5:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 1:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        elif y == 0:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
        else:
            while x >= 10:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
                utime.sleep_ms(velocity)
                if x == 10:  # Stop
                    break
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Vanish
                x -= 1
        y -= 1
    utime.sleep_ms(delay * 5)

# Function to down the raspberry
def dnraspberry():
    cleardisplay()
    y = 6
    while y >= 0:
        x = 11
        while x >= 2:
            if y == 6 and x == 11:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==5 and x == 11:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==1 and x == 11:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==0 and x == 11:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==6 and x == 10:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==0 and x == 10:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==6 and x == 5:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==0 and x == 5:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==6 and x == 4:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==5 and x == 4:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==4 and x == 4:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==2 and x == 4:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==1 and x == 4:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==0 and x == 4:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==3 and x == 2:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif x >=4:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
            else:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            x -= 1
        y -= 1
    utime.sleep_ms(dntime)

# Function to Up the raspberry
def upraspberry():
    cleardisplay()
    y = 6
    while y >= 0:
        x = 10
        while x >= 1:
            if y == 6 and x == 10:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==5 and x == 10:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==1 and x == 10:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==0 and x == 10:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==6 and x == 9:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==0 and x == 9:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==6 and x == 4:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==0 and x == 4:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==6 and x == 3:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==5 and x == 3:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==4 and x == 3:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==2 and x == 3:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==1 and x == 3:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            elif y ==0 and x == 3:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif y ==3 and x == 1:
                picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            elif x >=3:
                picounicorn.set_pixel(x, y, c, y, a)  # Cyan
            else:
                picounicorn.set_pixel(x, y, g, r, n)  # Green
            x -= 1
        y -= 1
    utime.sleep_ms(uptime)

# Function to vanish the raspberry
def vnraspberry():
    x = 0
    while x <= 15:
        y = 6
        while y >= 0:
            picounicorn.set_pixel(x, y, 0, 0, 0)  # Blank
            y -= 1
            utime.sleep_ms(vntime)
        x += 1
        utime.sleep_ms(vntime * 5)

# Original program Thermometer by NOSUKE
# Define colours
whtcolour=(127,127,127)

thermistor = machine.ADC(28)

# Set constant variables for temperature
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


# Original program Message by NOSUKE
# Define message colours
goodcolour=(0,0,255)
msgcolour=(127,127,127)

# Set constant variables for message
GOOD=["    ",
      " G  ",
      " GGG",
      "GGGG",
      "GGGG",
      "GGGG",
      "    "]

EXCL=["    ",
      " MM ",
      " MM ",
      " MM ",
      "    ",
      " MM ",
      "    "]

YO=["    ",
    "MMMM",
    "   M",
    "MMMM",
    "   M",
    "MMMM",
    "    "]

RO=["    ",
    "MMMM",
    "M  M",
    "M  M",
    "M  M",
    "MMMM",
    "    "]

SI=["    ",
    "MM M",
    "   M",
    "MM M",
    "   M",
    "MMM ",
    "    "]

KU=["    ",
    " MMM",
    "M  M",
    "   M",
    "  M ",
    " M  ",
    "    "]

# Function to update display with numbers/text
def updatedisplay(displaymap):
    x=0
    y=0
    for row in displaymap:
        for line in row:
            for char in line:
                if x < w and y <h:
                    if char == "G":
                        r, g, b = goodcolour
                    elif char == "M":
                        r, g, b = msgcolour
                    else:
                        r,g,b=0,0,0
                    picounicorn.set_pixel(x, y, r, g, b)
                x+=1
            x=0
        y+=1
    return displaymap

# Function to generate an 2D array to represent the message in the format
def generatemessage():
    fulldisplay = [["                {} {} {} {} {} {}   ".format(GOOD[i],YO[i],RO[i],SI[i],KU[i],EXCL[i])] for i in range(h)]
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


# Original program Rogo by NOSUKE
# Define rogo colours
rogcolour=(255,0,255)

# Set constant variables for rogo
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
                        r, g, b = rogcolour
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
                        r, g, b = rogcolour
                    picounicorn.set_pixel(x, y, r, g, b)
                x+=1
            x=0
        y+=1
    return displaymap


# Button pressed
buttonA = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
buttonB = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
buttonX = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
buttonY = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

count = 0

#Button A pressed
def buttonA_press(pin):
    print("You press the buttonA!")
    count =0
    while count <=1:
        raspberry()
        ud = 1
        while ud <= udcount:
            dnraspberry()
            upraspberry()
            ud += 1
            vnraspberry()
        count +=1

#Button B pressed
def buttonB_press(pin):
    print("You press the buttonB!")
    count = 0
    while count <= 20:
        temperature_value = thermistor.read_u16()
        Vr = 3.3 * float(temperature_value) / 65535
        Rt = 10000 * Vr / (3.3 - Vr)
        temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        temperature = temp - 273.15
        
        temp1 = int(temperature / 10)
        temp2 = int(temperature - temp1 * 10)
        temp3 = int(temperature * 10 - temp1 * 100 - temp2 * 10)
        
        # Change colour depending on temperature
        if 0 < temperature <= 10:
            tempcolour=(0,127,127)
        elif 10 < temperature <= 20:
            tempcolour=(0,0,127)
        elif 20 < temperature <= 30:
            tempcolour=(0,127,0)
        elif 30 < temperature <= 40:
            tempcolour=(127,127,0)
        elif 40 < temperature <= 50:
            tempcolour=(127,0,0)
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
                                r, g, b = whtcolour
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
            fulldisplay = [["{} {}{}{} {}".format(temp1pix[i],temp2pix[i],DOT[i],temp3pix[i],LETTERC[i])] for i in range(h)]
            return fulldisplay
        
        # Temperature display
        updatedisplay(generatetemp(temp1,temp2,temp3))
        utime.sleep_ms(1000)
        count += 1
    cleardisplay()
    
#Button X pressed
def buttonX_press(pin):
    print("You press the buttonX!")
    count = 0
    while count <=1:
        currentdisplaymap=updatedisplay(generatemessage())
        for i in range(w*3):
            currentdisplaymap=updatedisplay(scrolldisplay(currentdisplaymap))
            cleardisplay()
        count +=1

#Button Y pressed
def buttonY_press(pin):
    print("You press the buttonY!")
    count = 0
    while count <= 20:
        updatedisplayp(NOSUKER)
        utime.sleep_ms(500)
        cleardisplay()
        updatedisplayn(NOSUKER)
        utime.sleep_ms(500)
        cleardisplay()
        count += 1

buttonA.irq(trigger=machine.Pin.IRQ_RISING, handler=buttonA_press)
buttonB.irq(trigger=machine.Pin.IRQ_RISING, handler=buttonB_press)
buttonX.irq(trigger=machine.Pin.IRQ_RISING, handler=buttonX_press)
buttonY.irq(trigger=machine.Pin.IRQ_RISING, handler=buttonY_press)

while True:
    count += 1
    print(count)
    utime.sleep_ms(1000)
