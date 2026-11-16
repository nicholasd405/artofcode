import turtle

bob = turtle.Turtle()

def comet(distance, angle):
    for times in range(10):
        bob.width(times)
        bob.forward(distance)
        bob.left(angle)

def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

def polygon(distance, sides, c):
    bob.color(c)
    angle = 360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def spiral():
    for times in range(5):
        bob.width(times)
        bob.forward(20)
        bob.left(10)

def stair(distance, amount):
    for times in range(amount):
        bob.forward(distance)
        bob.left(90)
        bob.forward(distance)
        bob.right(90)
def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()


