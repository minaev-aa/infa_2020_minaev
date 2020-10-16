import pygame
from random import randint
from os import path
import math

img_dir = path.join(path.dirname(__file__), 'pic')
FPS = 30
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Ball Game")


clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class GameManager:
    def __init__(self, game_window, array_cloud, array_house):
        self.game_window = game_window
        self.array1 = array_house
        self.array3 = array_cloud

    def redraw(self):
        self.game_window.fill((255, 255, 255))
        self.array1.set_new_color_pos()
        self.array3.set_new_color_pos()
        score = self.array1.score + self.array3.score
        draw_text(screen, str(int(score)), 20, 400, 10)

class Cloud:
    def __init__(self, game_window, count):
        self.surface = pygame.Surface((800, 800), pygame.SRCALPHA)
        self.x = []
        self.y = []
        self.h = []
        self.w = []
        self.vx = []
        self.vy = []
        self.k = count
        self.score = 0
        self.color1 = []
        self.color2 = []
        self.color3 = []
        self.game_window = game_window

        for u in range(count):
            self.color1.append(randint(2, 253))
            self.color2.append(randint(2, 253))
            self.color3.append(randint(2, 253))
            self.x.append(randint(50, 750))
            self.y.append(randint(50, 750))
            self.h.append(randint(10, 200))
            self.w.append(randint(10, 200))
            self.vx.append(randint(0, 20))
            self.vy.append(randint(0, 20))
        self.__draw()
    def delete(self, n):
        self.score += math.sqrt((self.vx[n])^2+(self.vy[n])^2) // 1
        self.k -= 1
        self.x.pop(n-1)
        self.y.pop(n-1)
        self.h.pop(n-1)
        self.w.pop(n-1)
        self.vx.pop(n-1)
        self.vy.pop(n-1)
        self.color1.pop(n-1)
        self.color2.pop(n-1)
        self.color3.pop(n-1)
    def __draw(self):
        self.sur = pygame.Surface((800,800), pygame.SRCALPHA)
        for p in range(self.k):
            pygame.draw.ellipse(self.sur, (self.color1[p],  self.color2[p], self.color3[p], 30),
                               [self.x[p], self.y[p], self.h[p], self.w[p]])
        self.game_window.blit(self.sur, (0,0))

    def set_new_color_pos(self):
        for i in range(self.k):
            if self.x[i] < 780 and self.x[i] > 30:
                self.x[i] += self.vx[i]
            else:
                self.vx[i] *= -1
                self.x[i] += self.vx[i]
            if self.y[i] < 750 and self.y[i] > 50:
                self.y[i] += self.vy[i]
            else:
                self.vy[i] *= -1
                self.y[i] += self.vy[i]
            self.__draw()
class Rect:
    def __init__(self, game_window, count):
        self.surface = pygame.Surface((800, 800), pygame.SRCALPHA)
        self.x = []
        self.y = []
        self.h = []
        self.w = []
        self.score = 0
        self.vx = []
        self.vy = []
        self.type = []
        self.k = count
        self.color1 = []
        self.color2 = []
        self.color3 = []
        self.game_window = game_window

        for u in range(count):
            self.color1.append(randint(2, 253))
            self.color2.append(randint(2, 253))
            self.color3.append(randint(2, 253))
            self.x.append(randint(50, 750))
            self.y.append(randint(50, 750))
            self.h.append(randint(10, 200))
            self.w.append(randint(10, 200))
            self.vx.append(randint(0, 20))
            self.vy.append(randint(0, 20))
            self.type.append(randint(0, 10))
        self.__draw()
    def delete(self, n):
        self.score += math.sqrt((self.vx[n])^2+(self.vy[n])^2) // 1
        self.k -= 1
        self.x.pop(n-1)
        self.y.pop(n-1)
        self.h.pop(n-1)
        self.w.pop(n-1)
        self.vx.pop(n-1)
        self.vy.pop(n-1)
        self.color1.pop(n-1)
        self.color2.pop(n-1)
        self.color3.pop(n-1)
    def __draw(self):
        self.sur = pygame.Surface((800,800), pygame.SRCALPHA)
        for p in range(self.k):
            pygame.draw.rect(self.sur, (self.color1[p],  self.color2[p], self.color3[p], 30),
                               (self.x[p], self.y[p], self.h[p], self.w[p]),  border_radius = self.type[p])
        self.game_window.blit(self.sur, (0,0))

    def set_new_color_pos(self):
        for i in range(self.k):
            if self.x[i] < 780 and self.x[i] > 30:
                self.x[i] += self.vx[i]
            else:
                self.vx[i] *= -1
                self.x[i] += self.vx[i]
            if self.y[i] < 750 and self.y[i] > 50:
                self.y[i] += self.vy[i]
            else:
                self.vy[i] *= -1
                self.y[i] += self.vy[i]
            self.__draw()
pygame.display.update()

cloud = Cloud(screen, 10)
house = Rect(screen, 10)
manager = GameManager(screen, cloud, house)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(-1, cloud.k-1):
                try:
                    if pygame.mouse.get_pos()[0] > cloud.x[i] and pygame.mouse.get_pos()[0] < cloud.x[i] + cloud.h[i]:
                        if pygame.mouse.get_pos()[1] > cloud.y[i] and  pygame.mouse.get_pos()[1] < cloud.y[i] + cloud.w[i]:
                            cloud.delete(i+1)
                except:
                    pass
            for i in range(-1, house.k-1):
                try:
                    if pygame.mouse.get_pos()[0] > house.x[i] and pygame.mouse.get_pos()[0] < house.x[i] + house.h[i]:
                        if pygame.mouse.get_pos()[1] > house.y[i] and  pygame.mouse.get_pos()[1] < house.y[i] + house.w[i]:
                            house.delete(i+1)
                except:
                    pass
    manager.redraw()

    pygame.display.flip()

pygame.quit()