import turtle  as t

colors = ["red", "purple", "blue", "green", "orange", "yellow"]
pen = t.Pen()
t.bgcolor('black')
for x in range(360):

    pen.pencolor(colors[x%6])
    pen.width(x//100 + 1)
    pen.forward(x)
    pen.left(59)
