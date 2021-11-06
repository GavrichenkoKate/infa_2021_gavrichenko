from math import pi, sin, cos
import turtle

turtle.shape('turtle')
for i in range(2000):
    a = i / 50 * pi
    x = 2 * a * cos(a)
    y = 2 * a * sin(a)
    turtle.goto(x, y)