
import turtle
turtle.shape('turtle')
k = 5

def star(n):
    for i in range(n):
        turtle.forward(150)
        turtle.right(180 - 180/n)

star(k)