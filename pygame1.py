import pygame
import os,sys,time
from pygame.draw import *


pygame.init()




FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill((255, 255, 255, 255))
circle(screen, (255, 255, 0, 255) , (200, 200), 100)
rect(screen, (0, 0, 0, 255), (150,230,100,20) )
circle(screen, (255, 0, 0, 255), (170, 170), 20)
circle(screen, (0, 0, 0, 255), (170, 170), 5)
polygon(screen, (0, 0, 0, 255),  [(160,130), (200,150), (190,160), (150,140)])
circle(screen, (255, 0, 0, 255), (244, 173), 15)
circle(screen, (0, 0, 0, 255), (244, 173), 3)
polygon(screen, (0, 0, 0, 255),  [(222,156), (260,143), (258,153), (220,166)])


circle(screen, (255, 255, 0, 255) , (50, 300), 40)
rect(screen, (0, 0, 0, 255), (30, 310, 40, 8) )
circle(screen, (255, 0, 0, 255), (30, 284), 8)
circle(screen, (0, 0, 0, 255), (30, 284), 2)
polygon(screen, (0, 0, 0, 255),  [(30, 270), (42, 275), (39, 279), (28, 274)])
circle(screen, (255, 0, 0, 255), (60, 285), 6)
circle(screen, (0, 0, 0, 255), (60, 285), 1)
polygon(screen, (0, 0, 0, 255),  [(53, 278), (63, 272), (62, 276), (52, 282)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            print(x,y)
            os.system('cls')
            if (x in range(0,50)) and (y in range(0,50)):
                print('курсор в регионе')
                time.sleep(0.5)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()