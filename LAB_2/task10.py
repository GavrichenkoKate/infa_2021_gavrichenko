import turtle

turtle.shape('turtle')
turtle.left(90)

def circle1(n):
    for i in range(100):
        turtle.forward(n)
        turtle.left(3.6)

def circle2(n):
    for i in range(100):
    
        turtle.forward(n)
        turtle.right(3.6)


turtle.right(90)
for i in range(5):
    circle1(i+2)
    circle2(i+2)

