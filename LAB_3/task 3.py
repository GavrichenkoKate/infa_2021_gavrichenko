import turtle 

turtle.shape('turtle')
turtle.color('blue')
turtle.pensize(2)

with open("C:/Task1/homework/WORK_2(2) turtle/task3.txt", 'r') as input_file:
    lst = input_file.readlines()
    exec(''.join(lst))

turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
a = 30

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
two(a)
