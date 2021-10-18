import numpy as np
import turtle 

turtle.shape('circle')
turtle.shapesize(0.5, 0.5)

x = -700
y = 0
Vx = 5
Vy = 20
ay = -1
dt = 0.1
Ky = 0.2
i = 0
turtle.goto(-400, 0)
while Vx > 0:
    turtle.goto(x, y)
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    if y <= 0:
        Vy = abs(Vy)*(1-Ky)
        i += 1
    if i == 7:
        break