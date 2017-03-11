import turtle # Import module for turtle problem

def windchill(f, v):
    # Formula for computing windchill.
    # f == temp degrees, v == air velocity, t == windchill temp
    t = 35.74 + (0.6215 * f) - (35.75 * (v ** 0.16)) + (0.4275 * f * (v ** 0.16))
    return t # Return the windchill

def computeWC():
    f = int(input('Enter the temperature (F): ')) # User input for temp
    v = int(input('Enter the wind velocity (MPH): ')) # User input for velocity
    wc = str(windchill(f, v)) # Cacluate windchill and return it as a string
    print('The windchill is: ' + wc) # Print windchill value to console

def drawStar():
    l = turtle.numinput(" ", "Enter a length for each side:") # User side length
    # Functions for drawing the star
    turtle.left(36)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)
    turtle.forward(l)
    turtle.left(144)

computeWC()
drawStar()
