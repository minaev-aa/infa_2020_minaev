#изменять цвет домиков анимация, количества машин, цвет, форма колёс\окон. тучки двигаются по кругу и меняются цвета цвета

import pygame
from random import*

FPS = 60
run = True
clock = pygame.time.Clock()
width = 640
height = 360
amount = 100

class GameManager:
    def __init__(self, game_window, array):
        self.game_window = game_window
        self.array = array

    def redraw(self):
        self.game_window.fill((0, 0, 0))
        for star in self.array:
            star.set_new_position()

class House:
    def __init__(self, game_window, color):
        self.color = color
        self.game_window = game_window
        self.draw()

    def draw(self):
        pygame.draw.circle(self.game_window, (255, 0, 0),
                          [self.x, self.y], 3)


class Car:
    def __init__(self, game_window, start_x, start_y, color_corpus, type_wheel, increment):
        self.x = start_x
        self.y = start_y
        self.color1 = color_corpus[0]
        self.color2 = color_corpus[1]
        self.color3 = color_corpus[2]
        self.type = type_wheel
        self.game_window = game_window
        self.inc = increment
        self.draw()

    def draw(self):
        pygame.draw.polygon(self.game_window, (self.color1, self.color2, self.color3),  [(self.x + 250, self.y + 725), (self.x + 500 + self.inc, self.y + 725),
                                                                (self.x + 500, self.y + 675 + self.inc), (self.x + 430 + self.inc, self.y + 675),
                                                                (self.x + 430, self.y + 625 + self.inc), (self.x + 300 + self.inc, self.y + 625),
                                                                (self.x + 300, self.y + 675 + self.inc), (self.x + 250 + self.inc, self.y + 675)])
        pygame.draw.circle(self.game_window, (0, 0, 0), (self.x + 290 + self.inc, 725), 20 + self.inc)
        pygame.draw.circle(self.game_window, (0, 0, 0), (self.x + 450 + self.inc, 725), 20 + self.inc)
        pygame.draw.circle(self.game_window, (self.x + 255 + self.inc, 0, 0),
                          [self.x, self.y], 3)

    def set_new_position(self):
        self.x += 1
        self.y += 1
        self.draw()
pygame.init()
win = pygame.display.set_mode((width, height))

array = [Car(win, randint(0, width),
                        randint(0, height)) for i in range(amount)]

manager = GameManager(win, array)
pygame.draw.rect(win, (189, 183, 107, 255), (0,500,600,300) )
pygame.draw.rect(win, (127, 255, 212, 255), (0, 0,600,489) )
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    manager.redraw()
    pygame.display.flip()
pygame.quit()