import turtle

turtle.shape('turtle')
def circle(n):
    for i in range(200):
        turtle.forward(n)
        turtle.left(1.8)

for i in range(4):
    circle(2)
    turtle.left(180)
    circle(2)
    turtle.left(72)