from random import *
import turtle
turtle.shape('turtle')

turtle.color('red')
turtle.speed(50)

for i in range(300):
    turtle.forward(randint(0, 50))
    turtle.left(randint(0, 360))