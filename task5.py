n = int(input())
import turtle
turtle.shape('turtle')

for i in range(n):
    turtle.forward(90)
    turtle.stamp()
    turtle.backward(90)
    turtle.left(360/n)