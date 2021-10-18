from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(1000):
    a = i / 50 * pi
    x = a * cos(a)
    y = a * sin(a)
    turtle.goto(x, y)