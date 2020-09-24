from random import randint
from math import *
import turtle

number_of_turtles = 30
steps_of_time_number = 100
k = 1
d = {}


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.resizemode("user")
    unit.turtlesize(0.4,0.4)
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-300, 300), randint(-300, 300))
    unit.rt(randint(0, 360))
    x=str(unit)
    vx = str((randint(0, 3)))
    vy = str((randint(0, 3)))
    v0 = sqrt(float(vx) ** 2 + float(vy) ** 2)
    d.update({x : {'vx' : vx, 'vy': vy, 'v0' : v0}})


for i in range(steps_of_time_number):
    n = 1
    for unit in pool:
        if k<=len(pool):
            angle = unit.heading()
            for test in pool:
                if unit != test:
                    if unit.distance(test) < 10:
                        x1 = round(unit.xcor(), 5)
                        x2 = round(test.xcor(), 5)
                        y1 = round(unit.ycor(), 5)
                        y2 = round(test.ycor(), 5)
                        mod = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                        alpha = degrees(acos((y2 - y1)/mod))
                        beta = alpha = degrees(acos((x2 - x1)/mod))
                        if alpha > 90:
                            n += 1
                            alpha = 180 - alpha
                        if beta > 90:
                            n += 1
                        vx1 = float(d[str(unit)]['vx']) * cos(radians(alpha)) + float(d[str(unit)]['vy']) * cos(radians(90 - alpha)) * (-1) ** n
                        vx2 = float(d[str(test)]['vx']) * cos(radians(alpha)) + float(d[str(test)]['vy']) * cos(radians(90 - alpha)) * (-1) ** n
                        vy1 = float(d[str(unit)]['vx']) * sin(radians(alpha)) + float(d[str(unit)]['vy']) * cos(radians(90 - alpha)) * (-1) ** (n + 1)
                        vy2 = float(d[str(test)]['vx']) * cos(radians(alpha)) + float(d[str(test)]['vy']) * cos(radians(90 - alpha)) * (-1) ** (n + 1)
                        ux1 = vx2
                        ux2 = vx1
                        uy1 = vy1
                        uy2 = vy2
                        u01 = sqrt(vx1 ** 2 + vy1 ** 2)
                        u02 = sqrt(vx2 ** 2 + vy2 ** 2)
                        unit.setheading(unit.heading()-90)
                        test.setheading(test.heading()-90)
                        x = str(unit)
                        y = str(test)
                        d.update({x : {'vx' : str(ux1), 'vy': str(uy1), 'v0' : str(u01)}})
                        d.update({y : {'vx' : str(ux2), 'vy': str(uy2), 'v0' : str(u02)}})
            step = float(d[str(unit)]['v0'])
            if round(unit.xcor(), 5) >= 300 or round(unit.xcor(), 5) <= -300 or round(unit.ycor(), 5) >= 300 or round(unit.ycor(), 5) <= -300:
                    unit.setheading(unit.heading() - 270)
            unit.forward(step)
            k += 1
        else:
            k = 1
