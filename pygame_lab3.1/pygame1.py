#need pygame 2.0.0.dev12
import pygame,random
import os,sys,time
from pygame.draw import *


pygame.init()




FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill((255, 255, 255, 255))
'''
rect(screen, (189, 183, 107, 255), (0,500,600,300) )
rect(screen, (127, 255, 212, 255), (0, 0,600,489) )
pygame.draw.ellipse(screen, (24, 114, 98), [-50, 650 , 800,400])


rect(screen, (20, 20, 142), (20, 20,110, 500))
rect(screen, (45, 67, 12), (150, 45, 110, 480))
rect(screen, (167, 12, 142), (90, 100, 110, 470))
rect(screen, (17, 42, 112), (500, 10, 90, 540))
rect(screen, (255, 255, 255), (450, 110, 110, 480))


polygon(screen, (0, 0, 0, 255),  [(250, 725), (500, 725), (500, 675), (430, 675), (430, 625), (300, 625), (300, 675), (250, 675)])


circle(screen, (255, 0, 0, 255), (290, 725), 15)
circle(screen, (255, 0, 0, 255), (452, 725), 15)
rect(screen, (0, 255, 0, 0), (437, 710, 30, 30))
rect(screen, (0, 255, 0, 0), (275, 710, 30, 30), border_radius = 7)

rect(screen, (167, 12, 12), (320, 640, 35, 25))
rect(screen, (167, 12, 12), (375, 640, 45, 25))
surface = pygame.Surface((600,800), pygame.SRCALPHA)
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [70, 680 , 150,30])
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [60, 635 , 152, 32])
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [-70, 580 , 160,40])
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [60, 335 , 270,80])
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [150, 170 , 550,120])
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [-150, 50 , 600,110])
pygame.draw.ellipse(surface, (random.randint(0,255), random.randint(0,255), random.randint(0,255), 80), [190, -30 , 500,120])
screen.blit(surface, (0,0))




circle(screen, (255, 255, 0, 255) , (200, 200), 100)
circle(screen, (255, 0, 0, 255), (170, 170), 20)
circle(screen, (0, 0, 0, 255), (170, 170), 5)
polygon(screen, (0, 0, 0, 255),  [(160,130), (200,150), (190,160), (150,140)])
polygon(screen, (0, 0, 0, 255),  [(222,156), (260,143), (258,153), (220,166)])
'''
def smile(x,y,inc):
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