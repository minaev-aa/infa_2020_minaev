from random import randint
import turtle


number_of_turtles = 25
steps_of_time_number = 100
step = 10
d = {}

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
i=0;
for unit in pool:
    i = i + 1
    unit.penup()
    unit.speed(100)
    unit.goto(randint(-300, 300), randint(-300, 300))
    unit.rt(randint(-180, 180))
    x=str(unit)
    d.update({x : {'orientation':'1','num': str(i)}})
k = 1
for i in range(steps_of_time_number):
    for unit in pool:
        if k<=len(pool):
            if round(unit.xcor(), 5)>=300 or round(unit.xcor(), 5)<=-300 or round(unit.ycor(), 5)>=300 or round(unit.ycor(), 5)<=-300:
                    d.update({str(unit) : {'orientation' : str(int(d[str(unit)]['orientation'])*(-1)), 'num' : str(i)}})
            if d[str(unit)]['orientation'] == '1':
                unit.forward(step)
            if d[str(unit)]['orientation'] == '-1':
                unit.forward(-1*step)
            k = k + 1
        else:
            k = 1
