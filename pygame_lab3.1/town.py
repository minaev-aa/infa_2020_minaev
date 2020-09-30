#изменять цвет домиков - анимация. количества машин, цвет, форма колёс\окон -  в ручную. тучки двигаются и меняются цвета цвета - анимация
#ONLY
#pip install pygame==2.0.0.dev12


import pygame
import random

FPS = 60
run = True
clock = pygame.time.Clock()
width = 600
height = 800
amount = 1

class GameManager:
    def __init__(self, game_window, array_house,array_car, array_cloud):
        self.game_window = game_window
        self.array1 = array_house
        self.array2 = array_car
        self.array3 = array_cloud

    def redraw(self):
        self.game_window.fill((255, 255, 255))
        pygame.draw.rect(self.game_window, (189, 183, 107), (0,500,600,300) )
        pygame.draw.rect(self.game_window, (127, 255, 212), (0, 0,600,489))
        pygame.draw.ellipse(self.game_window, (24, 114, 98), [-50, 650 , 800,400])
        for car in self.array2:
            self.array1.set_new_color()
            car.draw()
            self.array3.set_new_color_pos()

class House:
    def __init__(self, game_window, color):
        self.color = color
        self.game_window = game_window
        self.n = [1] *5
        for i in range(5):
            self.n[i] = [1] * 3
        self.draw()

    def draw(self):
        try:
            pygame.draw.rect(self.game_window, (self.color[0][0], self.color[0][1], self.color[0][2]), (20, 20,110, 500))
            pygame.draw.rect(self.game_window, (self.color[1][0], self.color[1][1], self.color[1][2]), (150, 45, 110, 480))
            pygame.draw.rect(self.game_window, (self.color[2][0], self.color[2][1], self.color[2][2]), (90, 100, 110, 470))
            pygame.draw.rect(self.game_window, (self.color[3][0], self.color[3][1], self.color[3][2]), (500, 10, 90, 540))
            pygame.draw.rect(self.game_window, (self.color[4][0], self.color[4][1], self.color[4][2]), (450, 110, 110, 480))
        except:
            print('Попробуйте снова')
    def set_new_color(self):
        for g in range(5):
            for o in range(3):
                if self.color[g][o] > 252 or self.color[g][o] < 4:
                    self.n[g][o] *= -1
                self.color[g][o] -= self.n[g][o]
                self.draw()
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
        pygame.draw.polygon(self.game_window, (self.color1, self.color2, self.color3),
                                                                [(self.x + 250, self.y + 725),
                                                                ((self.x + 500) + self.inc, self.y + 725),
                                                                ((self.x + 500) + self.inc, (self.y + 675) - self.inc/5),
                                                                ((self.x + 425) + 0.7 * self.inc, ((self.y + 675) - self.inc/5)),
                                                                ((self.x + 425) + 0.7 * self.inc, (self.y + 625) - self.inc/2.5),
                                                                ((self.x + 300) + 0.2 * self.inc, (self.y + 625) - self.inc/2.5),
                                                                ((self.x + 300) + 0.2 * self.inc, (self.y + 675) - self.inc/5),
                                                                (self.x + 250 , (self.y + 675) - self.inc/5)])


        if self.type2 == 0:
            pygame.draw.circle(self.game_window, (0, 0, 0), (self.x + 300 + 0.2 * self.inc,  self.y + 725), 20 + self.inc/10)
            pygame.draw.circle(self.game_window, (0, 0, 0), (self.x + 450 + 0.8 * self.inc,  self.y + 725), 20 + self.inc/10)
        if self.type2 == 1:
            pygame.draw.rect(self.game_window, (0, 255, 0, 0), (self.x + 430 + 0.72 * self.inc,
                                                                self.y + 705 - 0.08 * self.inc, 40 + self.inc * 0.16, 40 + self.inc * 0.16))
            pygame.draw.rect(self.game_window, (0, 255, 0, 0), (self.x + 280 + 0.12 * self.inc,
                                                                self.y + 705 - 0.08 * self.inc, 40 + self.inc * 0.16, 40 + self.inc * 0.16))
        pygame.draw.rect(self.game_window, (117, 187, 253),
                         (self.x + 310 +  self.inc * 0.24, self.y + 635 - self.inc * 0.36,
                          45 + self.inc * 0.18, 40 + self.inc * 0.16), border_radius = self.type1)
        pygame.draw.rect(self.game_window, (117, 187, 253),
                         (self.x + 370 + self.inc * 0.48, self.y + 635 - self.inc * 0.36,
                          45 + self.inc * 0.18, 40 + self.inc * 0.16), border_radius = self.type1)

class Cloud:
    def __init__(self, game_window):
        self.surface = pygame.Surface((600,800), pygame.SRCALPHA)
        self.x = [70,60,-70,60,150,-150,190]
        self.y = [680,635,580,335,170,50,-30]
        self.h = [150,152,160,270,550,600,500]
        self.w = [30,32,40,80,120,110,120]
        self.color1 = []
        self.color2 = []
        self.color3 = []
        for u in range(7):
            self.color1.append(random.randint(2,253))
            self.color2.append(random.randint(2,253))
            self.color3.append(random.randint(2,253))
        self.game_window = game_window
        self.m = [1] *7
        for i in range(7):
            self.m[i] = [1] * 3
        self.draw()

    def draw(self):
        self.surface = pygame.Surface((600,800), pygame.SRCALPHA)
        for p in range(7):
            pygame.draw.ellipse(self.surface, ( self.color1[p],  self.color2[p], self.color3[p], 30),
                                        [self.x[p], self.y[p], self.h[p], self.w[p]])
        self.game_window.blit(self.surface, (0,0))

    def set_new_color_pos(self):
        for i in range(7):
            if self.color1[i] > 253 or self.color1[i] < 2:
                self.m[i][0] *= -1
            if self.color2[i] > 253 or self.color2[i] < 2:
                self.m[i][1] *= -1
            if self.color3[i] > 253 or self.color3[i] < 2:
                self.m[i][2] *= -1
            self.color1[i] -= self.m[i][0]
            self.color2[i] -= self.m[i][1]
            self.color3[i] -= self.m[i][2]
            if self.x[i] < 600:
                self.x[i] += 1
            else:
                self.x[i] = (-1) * self.h[i]
                pygame.draw.ellipse(self.surface, (self.color1[i],  self.color2[i],
                                                   self.color3[i], 80), [self.x[i], self.y[i], self.h[i], self.w[i]])
            self.draw()

pygame.init()
win = pygame.display.set_mode((width, height))



array1 = House(win, [[random.randint(2,253), random.randint(2,253), random.randint(2,253)],
                    [random.randint(2,253), random.randint(2,253), random.randint(2,253)],
                    [random.randint(2,253), random.randint(2,253), random.randint(2,253)],
                    [random.randint(2,253), random.randint(2,253), random.randint(2,253)],
                    [random.randint(2,253), random.randint(2,253), random.randint(0,255)]])
array2 = [Car(win, -120, -45, -150, [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
                                    random.randint(0,10),random.randint(0,1)),
          Car(win, 105,30, -100, [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
                                    random.randint(0,10),random.randint(0,1)),
          Car(win, -300, 30, -40, [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
                                    random.randint(0,10),random.randint(0,1)),
          Car(win, 0,-140, 0, [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
                                    random.randint(0,10),random.randint(0,1)),
          Car(win, -250,-140, -100, [random.randint(0,255), random.randint(0,255), random.randint(0,255)],
                                    random.randint(0,10),random.randint(0,1))]
array3 = Cloud(win)


manager = GameManager(win, array1, array2, array3)
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    manager.redraw()
    pygame.display.flip()
pygame.quit()