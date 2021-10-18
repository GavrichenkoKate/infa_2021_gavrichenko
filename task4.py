import turtle

turtle.shape('turtle')
n = 10
for i in range(10):
    for i in range(4):
        turtle.left(90)
        turtle.forward(n)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    n += 20