import pygame
import random
from pygame.draw import *

n = int(input())

pygame.init()
FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255, 255))

def smile(x , y, inc):
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (x + inc, y + inc), 62 + inc)
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (x + inc, y + inc), 60 + inc)
    rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (-30 + x + inc / 2,
                                                                                    20 + y + 1.3 * inc, 60 + inc, 10 + inc / 3) )
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (-20 + x + inc / 2, -20 + y + inc / 2), 10 + inc / 6)
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (0 + x + inc, 0 + y + inc), 1 + inc / 6)
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (-20 + x + inc / 2, -20 + y + inc / 2), 5 + inc / 12)
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (20 + x + inc * 1.5, -20 + y + inc / 2),
           random.randint(6,9) + inc / 10)
    circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)) , (20 + x + inc * 1.5, -20 + y + inc / 2),
           random.randint(2,4) + inc / 10)
    rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (-33 + x + inc / 4,                                                                               -32 + y + inc/3, 26 + inc/2, 5 + inc/6) )
    rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (10 + x + 1.37 * inc,
                                                                                    -29 + y + inc / 2.5, 20 + inc / 4, 4 + inc / 12) )

def draw_random(n):
    for i in range(n):
        smile(random.randint(0,400), random.randint(0,500), random.randint(0,100))

clock = pygame.time.Clock()
draw_random(n)
run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()