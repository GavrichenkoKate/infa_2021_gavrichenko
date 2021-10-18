import numpy as np
import turtle

turtle.shape ('turtle')

def polygon(n, R):
    turtle.left(90*(n+2)/n) 
    for i in range(n):
        turtle.forward(2*R*np.sin(np.pi/n))
        turtle.left(180-(180*(n-2))/n)
    turtle.right(90*(n+2)/n)
for i in range(10):
    polygon(i+3, 15*(i+1))
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()