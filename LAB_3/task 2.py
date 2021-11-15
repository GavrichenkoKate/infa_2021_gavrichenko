import numpy as np
import turtle 

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(4)

def one(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x,y+a)
    turtle.pendown()
    turtle.goto(x+a,y+2*a)
    turtle.goto(x+a,y)


def four(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x, y+2*a)    
    turtle.pendown()
    turtle.goto(x, y+a)
    turtle.goto(x+a, y+a)
    turtle.goto(x+a, y+2*a)
    turtle.goto(x+a, y)


def seven(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x, y+2*a)
    turtle.pendown()
    turtle.goto(x+a, y+2*a)
    turtle.goto(x, y+a)
    turtle.goto(x, y)
    turtle.penup()
    turtle.goto(x+a, y)
    turtle.pendown()

def zero(a):
    x, y = turtle.position()
    turtle.goto(x, y+2*a)    
    turtle.goto(x+a, y+2*a)  
    turtle.goto(x+a, y)
    turtle.goto(x, y)
    turtle.goto(x+a, y)

def probel(a):
    x, y = turtle.position()
    turtle.penup()
    turtle.goto(x+a, y)
    turtle.pendown()


turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
a = 50
one(a)
probel(a)
four(a)
probel(a)
one(a)
probel(a)
seven(a)
probel(a)
zero(a)
probel(a)
zero(a)
