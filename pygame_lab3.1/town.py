#изменять цвет домиков - анимация. количества машин, цвет, форма колёс\окон -  в ручную. тучки двигаются и меняются цвета цвета - анимация
#ONLY
#pip install pygame==2.0.0.dev12

from random import randint
from sys import exit

from module import start_save
from pygame import draw, SRCALPHA, Surface, display

FPS = 60
width = 600
height = 800



class GameManager:
    def __init__(self, game_window, array_house, array_car, array_cloud):
        self.game_window = game_window
        self.array1 = array_house
        self.array2 = array_car
        self.array3 = array_cloud

    def redraw(self):
        self.game_window.fill((255, 255, 255))
        draw.rect(self.game_window, (189, 183, 107), (0, 500, 600, 300) )
        draw.rect(self.game_window, (127, 255, 212), (0, 0, 600, 489))
        draw.ellipse(self.game_window, (24, 114, 98), [-50, 650 , 800, 400])
        for car in self.array2:
            self.array1.set_new_color()
            self.array3.set_new_color_pos()
            car.draw()

class House:
    def __init__(self, game_window, count, color, x, y, h, w):
        self.color = color
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.k = count
        self.game_window = game_window
        self.n = [1] * count
        for i in range(count):
            self.n[i] = [1] * 3
        self.__draw()

    def __draw(self):
        for i in range(self.k):
            try:
                draw.rect(self.game_window, (self.color[i][0], self.color[i][1], self.color[i][2]),
                                (self.x[i], self.y[i],self.h[i], self.w[i]))
            except TypeError:
                print('Все аргуметы должны быть числами')
                exit()

    def set_new_color(self):
        for g in range(self.k):
            for o in range(3):
                if self.color[g][o] > 252 or self.color[g][o] < 4:
                    self.n[g][o] *= -1
                self.color[g][o] -= self.n[g][o]
                self.__draw()

class Car:
    def __init__(self, game_window, start_x, start_y, increment, color_corpus, type_window, type_wheel):
        self.x = start_x
        self.y = start_y
        self.color1 = color_corpus[0]
        self.color2 = color_corpus[1]
        self.color3 = color_corpus[2]
        self.type1 = type_window
        self.type2 = type_wheel
        self.game_window = game_window
        self.inc = increment
        self.draw()

    def draw(self):
        try:
            draw.polygon(self.game_window, (self.color1, self.color2, self.color3),
                              [(self.x + 250, self.y + 725),
                              ((self.x + 500) + self.inc, self.y + 725),
                              ((self.x + 500) + self.inc, (self.y + 675) - self.inc/5),
                              ((self.x + 425) + 0.7 * self.inc, ((self.y + 675) - self.inc/5)),
                              ((self.x + 425) + 0.7 * self.inc, (self.y + 625) - self.inc/2.5),
                              ((self.x + 300) + 0.2 * self.inc, (self.y + 625) - self.inc/2.5),
                              ((self.x + 300) + 0.2 * self.inc, (self.y + 675) - self.inc/5),
                               (self.x + 250 , (self.y + 675) - self.inc/5)])


            if self.type2 == 0:
                draw.circle(self.game_window, (0, 0, 0), (self.x + 300 + 0.2 * self.inc,  self.y + 725), 20 + self.inc/10)
                draw.circle(self.game_window, (0, 0, 0), (self.x + 450 + 0.8 * self.inc,  self.y + 725), 20 + self.inc/10)

            if self.type2 == 1:
                draw.rect(self.game_window, (0, 255, 0, 0), (self.x + 430 + 0.72 * self.inc,
                                 self.y + 705 - 0.08 * self.inc, 40 + self.inc * 0.16, 40 + self.inc * 0.16))
                draw.rect(self.game_window, (0, 255, 0, 0), (self.x + 280 + 0.12 * self.inc,
                                 self.y + 705 - 0.08 * self.inc, 40 + self.inc * 0.16, 40 + self.inc * 0.16))


            draw.rect(self.game_window, (117, 187, 253),
                             (self.x + 310 +  self.inc * 0.24, self.y + 635 - self.inc * 0.36,
                              45 + self.inc * 0.18, 40 + self.inc * 0.16), border_radius = self.type1)

            draw.rect(self.game_window, (117, 187, 253),
                             (self.x + 370 + self.inc * 0.48, self.y + 635 - self.inc * 0.36,
                              45 + self.inc * 0.18, 40 + self.inc * 0.16), border_radius = self.type1)
        except TypeError:
            print('Все аргуметы должны быть числами')
            exit()


class Cloud:
    def __init__(self, game_window, count, x, y, h, w):
        self.surface = Surface((600, 800), SRCALPHA)
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.k = count
        self.color1 = []
        self.color2 = []
        self.color3 = []
        self.game_window = game_window
        self.mac = [1] * count

        for u in range(count):
            self.color1.append(randint(2, 253))
            self.color2.append(randint(2, 253))
            self.color3.append(randint(2, 253))

        for i in range(count):
            self.mac[i] = [1] * 3
        self.__draw()

    def __draw(self):
        try:
            self.sur = Surface((600,800), SRCALPHA)
            for p in range(self.k):
                draw.ellipse(self.sur, (self.color1[p],  self.color2[p], self.color3[p], 30),
                                   [self.x[p], self.y[p], self.h[p], self.w[p]])
            self.game_window.blit(self.sur, (0,0))
        except TypeError:
                print('Все аргуметы должны быть числами')
                exit()

    def set_new_color_pos(self):
        for i in range(self.k):
            if self.color1[i] > 253 or self.color1[i] < 2:
                self.mac[i][0] *= -1
            if self.color2[i] > 253 or self.color2[i] < 2:
                self.mac[i][1] *= -1
            if self.color3[i] > 253 or self.color3[i] < 2:
                self.mac[i][2] *= -1
            self.color1[i] -= self.mac[i][0]
            self.color2[i] -= self.mac[i][1]
            self.color3[i] -= self.mac[i][2]
            try:
                if self.x[i] < 600:
                    self.x[i] += 1
                else:
                    self.x[i] = (-1) * self.h[i]
                    draw.ellipse(self.sur, (self.color1[i],  self.color2[i],
                                        self.color3[i], 80), [self.x[i], self.y[i], self.h[i], self.w[i]])
            except TypeError:
                print('Все аргуметы должны быть числами')
                exit()
            self.__draw()

win = display.set_mode((width, height))

array1 = House(win, 5, [[randint(2, 253), randint(2, 253), randint(2, 253)],
                        [randint(2, 253), randint(2, 253), randint(2, 253)],
                        [randint(2, 253), randint(2, 253), randint(2, 253)],
                        [randint(2, 253), randint(2, 253), randint(2, 253)],
                        [randint(2, 253), randint(2, 253), randint(0, 255)]],
                        [20, 150, 90, 500, 450], [20, 45, 100 ,10, 110], [110, 110, 110,  90, 110],
                        [500, 480, 470, 540, 480])


array2 = [Car(win, -120, -45, -150, [randint(0, 255), randint(0, 255), randint(0, 255)],
                                     randint(0, 10), randint(0, 1)),
          Car(win, 105,30, -100, [randint(0, 255), randint(0, 255), randint(0, 255)],
                                  randint(0, 10), randint(0, 1)),
          Car(win, -300, 30, -40, [randint(0, 255), randint(0,255), randint(0, 255)],
                                   randint(0, 10), randint(0, 1)),
          Car(win, -33, -130, -20, [randint(0, 255), randint(0, 255), randint(0, 255)],
                                    randint(0, 10), randint(0,1)),
          Car(win, -250, -140, -100, [randint(0, 255), randint(0, 255), randint(0, 255)],
                                      randint(0, 10), randint(0, 1))]
array3 = Cloud(win, 7, [70, 60, -70, 60, 150, -150, 190], [680, 635, 580, 335, 170, 50, -30],
                       [150, 152, 160, 270, 550, 600, 500], [30, 32, 40, 80, 120, 110, 120])

manager = GameManager(win, array1, array2, array3)

start_save.save(win, FPS, manager)