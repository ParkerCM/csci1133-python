import turtle
import random

def mul(a, b):
    count = 0
    product = 0
    if a < b:
        limit = a
        num = b
    else:
        limit = b
        num = a
    while count < limit:
        product += num
        count += 1
    print(product)

def race():
    def distance():
        return random.randint(1, 15)
    def winner():
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(700, 200)
        if redTurtle.xcor() >= 1950:
            turtle.write('Red Wins', font=('Arial', 36))
        elif blueTurtle.xcor() >= 1950:
            turtle.write('Blue Wins', font=('Arial', 36))
        elif greenTurtle.xcor() >= 1950:
            turtle.write('Green Wins', font=('Arial', 36))

    turtle.setworldcoordinates(0, 0, 2000, 400)
    turtle.penup()
    turtle.hideturtle()

    redTurtle = turtle.Turtle()
    redTurtle.penup()
    redTurtle.hideturtle()
    redTurtle.goto(10, 100)
    redTurtle.shape('turtle')
    redTurtle.color('red')
    redTurtle.showturtle()

    blueTurtle = turtle.Turtle()
    blueTurtle.penup()
    blueTurtle.hideturtle()
    blueTurtle.goto(10, 200)
    blueTurtle.shape('turtle')
    blueTurtle.color('blue')
    blueTurtle.showturtle()

    greenTurtle = turtle.Turtle()
    greenTurtle.penup()
    greenTurtle.hideturtle()
    greenTurtle.goto(10, 300)
    greenTurtle.shape('turtle')
    greenTurtle.color('green')
    greenTurtle.showturtle()

    while redTurtle.xcor() < 1950 and blueTurtle.xcor() < 1950 and greenTurtle.xcor() < 1950:
        redTurtle.forward(distance())
        blueTurtle.forward(distance())
        greenTurtle.forward(distance())
        winner()

    turtle.exitonclick()

def checkerboard():
    def drawSquare():
        turtle.begin_fill()
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.end_fill()

    turtle.setworldcoordinates(0, 0, 800, 800)
    turtle.speed(0)
    turtle.bgcolor('red')
    turtle.hideturtle()
    turtle.penup()

    xnum = 0
    ynum = 0

    while ynum < 8:
        while xnum < 4:
            drawSquare()
            turtle.forward(200)
            xnum += 1
        if ynum % 2 == 0:
            turtle.left(90)
            turtle.forward(200)
            turtle.left(90)
        else:
            turtle.right(180)
        ynum += 1
        xnum = 0

    turtle.exitonclick()
