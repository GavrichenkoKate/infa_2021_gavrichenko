import turtle 

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(4)

with open("C:/Users/elena/PycharmProjects/lab_progam/work 2 part 2/task3.txt", 'r') as input_file:
    lst = input_file.readlines()
    exec(''.join(lst))

turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
a = 50

one(a)
probel(a)
four(a)
probel(a)
one(a)
probel(a)
seven(a)
probel(a)
zero(a)
probel(a)
zero(a)