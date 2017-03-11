import math
import turtle

def orbit():
    revolutions = 3*(2*math.pi)
    pdegrees = 0
    mdegrees = 0
    pc = 0
    mc = 0
    pcount = 1
    mcount = 1
    planetx = 0
    planety = 0

    moon = turtle.Turtle()
    planet = turtle.Turtle()
    sun = turtle.Turtle()

    sun.penup()
    sun.hideturtle()
    sun.goto(0, -40)
    sun.color('yellow')
    sun.begin_fill()
    sun.circle(40)
    sun.end_fill()

    planet.penup()
    planet.hideturtle()
    planet.goto(150, 0)
    planet.color('blue')
    planet.shape('circle')
    planet.showturtle()

    moon.penup()
    moon.hideturtle()
    moon.goto(230, 0)
    moon.color('green')
    moon.turtlesize(.5,.5,.5)
    moon.shape('circle')
    moon.showturtle()

    while pdegrees <= revolutions:
        while pc < pcount:
            while mc < mcount:
                moonx = (2*(math.cos(pdegrees) + (.5*math.cos(mdegrees)))) * 80 #Allows orbit around planet
                moony = (2*(math.sin(pdegrees) + (.5*math.sin(mdegrees)))) * 80
                moon.goto(moonx, moony)
                mdegrees += math.radians(5)
                mc += 1
            planetx = math.cos(pdegrees) * 150
            planety = math.sin(pdegrees) * 150
            planet.goto(planetx, planety)
            pdegrees += math.radians(2)
            pc += 1
        pc = 0
        mc = 0

def ptrip(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def findtriples():
    tryCount = 0
    a = 1
    b = 2
    c = 3
    while tryCount < 3:
        upperBound = int(input('Enter an upperbound > 10: '))
        if upperBound <= 10:
            print('Error! Must be > 10!')
            tryCount += 1
        else:
            break

    while c <= upperBound:
        b = 1
        while b <= upperBound:
            a = 1
            while a <= upperBound:
                if ptrip(a, b, c) is True:
                    check = a - b # Prevents duplicates. EX: (3,4,5), (4,3,5)
                    if check < 0:
                        print('(', a, b, c, ')')
                a += 1
            b += 1
        c += 1
