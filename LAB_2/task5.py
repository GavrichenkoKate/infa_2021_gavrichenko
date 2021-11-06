import turtle
turtle.shape('turtle')
n = 4

for i in range(n):
    turtle.forward(90)
    turtle.stamp()
    turtle.backward(90)
    turtle.left(360/n)
