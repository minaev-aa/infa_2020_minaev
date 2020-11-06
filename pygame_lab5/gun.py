from random import randrange as rnd, choice
import tkinter as tk
import math
import time


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.delete = 0
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = None
        self.live = 30
    def create(self):
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
    def delet(self):
        if self.delete == 1:
            canv.delete(self.id)
            return 1
        else:
            return 0

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.vx > 750 or self.x + self.vx < 0:
            self.vx *= -1
        if self.y - self.vy > 495 or self.y - self.vy < 20:
            self.vy *= -1
        self.vy -= 1
        if self.y - self.vy > 496:
            self.vy = 0
        if abs(self.vy) == 0 and abs(self.vy) == 0:
            self.delete = 1
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.vx *= 0.985
        self.vy *= 0.99

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 > (self.r + obj.r) ** 2:
            return False
        else:
            return True
class ball_boom(ball):
    def __init__(self):
        super().__init__()

    def create(self):
        self.id = canv.create_rectangle(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)

    def hittestboom(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 + 10 > (self.r + obj.r) ** 2 :
            return False
        else:
            return True
class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = choice( [ball(), ball_boom()])
        new_ball.create()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.step = rnd(-10, 10)
        self.kx = 1
        self.ky = 1
        self.points = 0
        self.live = 1
        self.id = None

    def hit(self):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """
        Движение объекта
        """
        if self.x < 730 and self.x > 50:
            self.x += self.step * self.kx
        else:
            self.kx *= -1
            self.x += self.step * self.kx
        if self.y < 500 and self.y > 30:
            self.y += self.step * self.ky
        else:
            self.ky *= -1
            self.y += self.step * self.ky
        self.set_coords()


class krug(target):
    def __init__(self):
        super().__init__()
        self.new_target1()

    def new_target1(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 730)
        y = self.y = rnd(50, 500)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        self.id = canv.create_oval(0, 0, 0, 0)
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)


class rect(target):
    def __init__(self):
        super().__init__()
        self.new_target2()

    def new_target2(self):
    #     """ Инициализация новой цели. """
        x = self.x = rnd(600, 730)
        y = self.y = rnd(50, 500)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        self.id = canv.create_rectangle(0, 0, 0, 0)
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []
points = 0
point = canv.create_text(30, 30, text=int(points), font='28')


def new_game(X, Y, event=''):
    global screen1, balls, bullet, targets, points, Bind
    Bind = False
    bullet = 0
    balls = []
    targets = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    for i in range(X):
        targets.append(krug())
    for i in range(Y):
        targets.append(rect())
    for m in targets:
        m.live = 1
    while len(targets) != 0 or balls:
        for i in targets:
            i.move()
        for b in balls:
            b.move()
            for i in targets:
                if type(b) == type(ball_boom()):
                    if b.hittestboom(i) and i.live:
                        i.live = 0
                        i.hit()
                        targets.remove(i)
                        points += 1 / (X + Y)
                else:
                    if b.hittest(i) and i.live:
                        i.live = 0
                        i.hit()
                        targets.remove(i)
                        points += 1 / (X + Y)
            if len(targets) <= 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                canv.itemconfig(point, text=int(round(points)))
                b.vx *= 0.97
                b.vy *= 0.9
            if b.delet() == 1:
                balls.remove(b)
        canv.update()
        time.sleep(0.05)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    root.after(new_game(X, Y))


Y = 2
X = 2
new_game(X, Y)

tk.mainloop()
