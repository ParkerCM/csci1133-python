import turtle
import math

def orbit():
    degrees = 0
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0, -40)
    turtle.color('yellow')
    turtle.begin_fill()
    turtle.circle(40)
    turtle.end_fill()
    turtle.goto(150, 0)
    turtle.shape('circle')
    turtle.color('blue')
    turtle.showturtle()
    while degrees < ((2 * math.pi) * 3): # AKA while less than three rotations in radians
        x = math.cos(degrees)*150
        y = math.sin(degrees)*150
        turtle.goto(x, y)
        degrees += (math.pi/180) # Conversion to radians

def compound(start, target, rate):
    start = float(start)
    target = float(target)
    rate = float(rate)
    years = 0
    while start <= target:
        start = start * (1 + rate) # Yearly interest calculation
        years += 1
    return years

def perfect(num):
    num = int(num)
    start = 1
    total = 0
    while start < num:
        if num % start == 0: # % == 0 tells us it is a factor
            total += start
        start += 1
    if total == num:
        return True
    else:
        return False

def perfectList(upperLim):
    count = 1
    while count <= upperLim:
        x = perfect(count)
        if x is True:
            print(count)
        count += 1
