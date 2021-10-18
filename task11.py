import turtle

turtle.shape('turtle')
def halfcircle(n):
    for i in range(50):
        turtle.right(3.6)
        turtle.forward(n)

turtle.left(90)
for i in range(3):
        halfcircle(4)
        halfcircle(1)
