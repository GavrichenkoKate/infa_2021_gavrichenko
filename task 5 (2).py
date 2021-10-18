from random import randint
import turtle

number_of_turtles = 15
steps_of_time_number = 300

pool = [turtle.Turtle(shape = 'circle') for i in range(number_of_turtles)]

for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-300, 300), randint(-300, 300))

dx = [randint(-2, 2) for i in range(number_of_turtles)]
dy = [randint(-2, 2) for i in range(number_of_turtles)]

for j in range(steps_of_time_number):
    for i in range(number_of_turtles):
        x, y = pool[i].position()
        if x >= 300 or x <= -300:
            dx[i] *= -1
        if y >= 300 or y <= -300:
            dy[i] *= -1
        x += dx[i]
        y += dy[i]
        pool[i].goto(x+dx[i], y+dy[i])
