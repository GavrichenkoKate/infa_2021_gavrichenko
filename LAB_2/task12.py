import turtle

turtle.shape('turtle')

def circle(n):
    for i in range(100):
        turtle.forward(n)
        turtle.left(3.6)

def halfcircle(n):
    for i in range(50):
        turtle.right(3.6)
        turtle.forward(n)

turtle.color('black', 'yellow')
turtle.begin_fill()
circle(5)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(130)
turtle.left(90)
turtle.forward(40)
turtle.pendown()
turtle.color('black', 'green')
turtle.begin_fill()
circle(1)
turtle.end_fill()
turtle.penup()
turtle.right(180)
turtle.forward(80)
turtle.left(180)
turtle.pendown()
turtle.color('black', 'green')
turtle.begin_fill()
circle(1)
turtle.end_fill()
turtle.penup()
turtle.forward(40)
turtle.left(90)
turtle.forward(55)
turtle.pendown()
turtle.color('black')
turtle.width(4)
turtle.forward(20)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.color('red')
turtle.right(90)
turtle.pendown()
halfcircle(3)
