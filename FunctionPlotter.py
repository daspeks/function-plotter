import turtle
from math import *

# CONSTANTS
WIDTH       = 800
HEIGHT      = 600
XORIGIN     = 0
YORIGIN     = 0
XMIN        = -10
XMAX        = 10
YMIN        = -10
YMAX        = 10
TICKSIZE    = 5
STEP        = 1
LABELOFFSET = 20
AXISCOLOR   = "black"



# Sets the display screen
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay = 0)
    return pointer



# Returns pixel coordinates of corresponding Cartesian coordinates
def screenCoor(xorigin, yorigin, ratio, x, y):
    screenX = xorigin + (ratio * x)
    screenY = yorigin + (ratio * y)
    return screenX, screenY



# Maps expression color based on counter
def getColor(counter):
    if ((counter % 3) == 0):
        return "red"
    elif ((counter % 3) == 1):
        return "green"
    else:
        return "blue"



# Draws the X-axis ticks and labels on screen
def drawXAxisLabelTick(pointer, screenX, screenY, text):
    pointer.goto(screenX, screenY + TICKSIZE)
    pointer.down()
    pointer.goto(screenX, screenY - TICKSIZE)
    pointer.up()
    pointer.goto(screenX, screenY - LABELOFFSET)
    pointer.write(text, False, align = 'center')



# Draws the Y-axis ticks and labels on screen
def drawYAxisLabelTick(pointer, screenX, screenY, text):
    pointer.goto(screenX + TICKSIZE, screenY)
    pointer.down()
    pointer.goto(screenX - TICKSIZE, screenY)
    pointer.up()
    pointer.goto(screenX - LABELOFFSET, screenY)
    pointer.write(text, False, align = 'center')



# Draws the X-axis on screen
def drawXAxis(pointer, xorigin, yorigin, ratio):
    list = [-STEP, STEP]
    for step in list:
        screenX = xorigin
        screenY = yorigin
        pointer.up()
        pointer.goto(screenX, screenY)
        
        x = step
        condition = (XMIN <= x <= XMAX)
        while (condition):
            screenX, screenY = screenCoor(xorigin, yorigin, ratio, x, YORIGIN)
            pointer.down()
            pointer.goto(screenX, screenY)
            pointer.up()
            drawXAxisLabelTick(pointer, screenX, screenY, str(x))
            pointer.goto(screenX, screenY)
            pointer.down()
            x = x + step
            condition = (XMIN <= x <= XMAX)
    pointer.up()



# Draws the Y-axis on screen
def drawYAxis(pointer, xorigin, yorigin, ratio):
    list = [-STEP, STEP]
    for step in list:
        screenX = xorigin
        screenY = yorigin
        pointer.up()
        pointer.goto(screenX, screenY)

        y = step
        condition = (YMIN <= y <= YMAX)
        while (condition):
            screenX, screenY = screenCoor(xorigin, yorigin, ratio, XORIGIN, y)
            pointer.down()
            pointer.goto(screenX, screenY)
            pointer.up()
            drawYAxisLabelTick(pointer, screenX, screenY, str(y))
            pointer.goto(screenX, screenY)
            pointer.down()
            y = y + step
            condition = (YMIN <= y <= YMAX)
    pointer.up()



# Draws a continuous function
def drawExpr(pointer, xorigin, yorigin, ratio, expr):
    delta = 0.2
    x = XMIN
    while (x <= XMAX):
        y = eval(expr)
        if (YMIN <= y <= YMAX):
            screenX, screenY = screenCoor(xorigin, yorigin, ratio, x, y)
            pointer.goto(screenX, screenY)
            pointer.down()
        x += delta
    pointer.up()



def main():
    # Setup window
    pointer = setup()

    # Set (x,y) of origin to (400, 300) and set ratio to 30
    xorigin = 400
    yorigin = 300
    ratio = 30

    # Set color and draw axes
    pointer.color(AXISCOLOR)
    drawXAxis(pointer, xorigin, yorigin, ratio)
    drawYAxis(pointer, xorigin, yorigin, ratio)

    # Loop and draw expressions until empty string "" is entered
    # Change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xorigin, yorigin, ratio, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1

main()
