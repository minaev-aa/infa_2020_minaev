import pygame
from random import randint
import time
import math

FPS = 30
screen = pygame.display.set_mode((1500, 800))
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
    """
    Класс запуска и обновления экрана игры
    FUNCTIONS
    redraw(...):
        :param delta: очки из прошлогшо обнавления
        :return: обновление экрана
    score(...):
        :return: возврат счёта
    """

    def __init__(self, game_window, array_cloud, array_rect, box_input):
        """
        :param game_window: окно
        :param array_cloud: объекты круга
        :param array_rect: объекты прямоугольников
        :param box_input: объект ввода имени
        :return: запуск игры и обговление экрана
        """
        self.game_window = game_window
        self.array_rect = array_rect
        self.array_cloud = array_cloud
        self.box = box_input
        self.score = 0

    def redraw(self, delta):
        """
        :param delta: очки из прошлогшо обнавления
        :return: обновление экрана
        """
        self.game_window.fill((255, 255, 255))
        self.box.update()
        self.box.draw(self.game_window)
        self.array_rect.set_new_color_pos()
        self.array_cloud.set_new_color_pos()
        self.score = self.array_rect.score + self.array_cloud.score + delta
        if self.score < 0:
            self.score = 0
        draw_text(self.game_window,
                  'Счёт: ' + str(int(self.score)) + ' ' * 45 + 'Имя' + ' ' * 220 + str(
                          int(pygame.time.get_ticks() / 1000 - t)) + ' сек', 20,
                  750, 10)

    def score(self):
        """
        :return: возврат счёта
        """
        return int(self.score)


class InputBox:
    """
    Класс окна с возможностью ввода имени
    FUNCTIONS
    handle_event(...):
        :param event: действие
        :return: заимодействие с окном
    update(...):
        бновление окна после ввода
    draw(...):
        рисование окна и удлинение его в случае нихватки места
    """

    def __init__(self, screen, x, y, w, h, text=''):
        """
        :param screen: окно
        :param x: координата x
        :param y: координата y
        :param w: ширина
        :param h: длина
        :param text: имя
        :return: ввод имени
        """
        self.font = pygame.font.Font(None, 32)
        self.screen = screen
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color('lightskyblue3')
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        :param event: действие
        :return: заимодействие с окном
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pygame.Color('dodgerblue2') if self.active else pygame.Color('lightskyblue3')
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return (self.text)
                    # self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)


class Drawings:
    """
    Создание объектов врагов
    FUNCTIONS
    delete(...):
        :param n: номер элемента
        :return: удаление элемента
    """
    def __init__(self, game_window, count):
        """
        :param game_window: окно
        :param count: количество
        :return: информация об объекте
        """
        self.surface = pygame.Surface((1500, 800), pygame.SRCALPHA)
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
            self.x.append(randint(50, 1430))
            self.y.append(randint(50, 750))
            self.h.append(randint(10, 200))
            self.w.append(randint(10, 200))
            self.vx.append(randint(0, 20))
            self.vy.append(randint(0, 20))

    def delete(self, n):
        """
        :param n: номер элемента
        :return: удаление элемента
        """
        self.score += math.sqrt(abs((self.vx[n]) ^ 2 + (self.vy[n]) ^ 2))
        self.k -= 1
        self.x.pop(n - 1)
        self.y.pop(n - 1)
        self.h.pop(n - 1)
        self.w.pop(n - 1)
        self.vx.pop(n - 1)
        self.vy.pop(n - 1)
        self.color1.pop(n - 1)
        self.color2.pop(n - 1)
        self.color3.pop(n - 1)


class Circle(Drawings):
    """
    Создание круглых врагов
    FUNCTIONS
    __draw(...):
        :return: отрисовка
    set_new_color_pos(...):
        :return: движение
    """
    def __draw(self):
        """
        :return: отрисовка
        """
        self.sur = pygame.Surface((1500, 800), pygame.SRCALPHA)
        for p in range(self.k):
            pygame.draw.ellipse(self.sur, (self.color1[p], self.color2[p], self.color3[p], 30),
                                [self.x[p], self.y[p], self.h[p], self.w[p]])
        self.game_window.blit(self.sur, (0, 0))

    def set_new_color_pos(self):
        """
        :return: движение
        """
        for i in range(self.k):
            if self.x[i] < 1430 and self.x[i] > 30:
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


class Rect(Drawings):
    """
    Создание прямоугольных врагов
    FUNCTIONS
    __draw(...):
        :return: отрисовка
    set_new_color_pos(...):
        :return: движение
    """
    def __init__(self, game_window, count):
        """
        :param game_window: окно
        :param count: количество
        :return: информация об объекте
        """
        super().__init__(game_window, count)
        self.type = []
        for u in range(count):
            self.type.append(randint(0, 10))

    def __draw(self):
        """
        :return: отрисовка
        """
        self.sur = pygame.Surface((1500, 800), pygame.SRCALPHA)
        for p in range(self.k):
            pygame.draw.rect(self.sur, (self.color1[p], self.color2[p], self.color3[p], 30),
                             (self.x[p], self.y[p], self.h[p], self.w[p]), border_radius=self.type[p])
        self.game_window.blit(self.sur, (0, 0))

    def set_new_color_pos(self):
        """
        :return: движение
        """
        for i in range(self.k):
            if self.x[i] < 1430 and self.x[i] > 30:
                self.x[i] += self.vx[i]
            else:
                self.vx[i] *= -1
                self.x[i] += self.vx[i]
                if self.vx[i] >= 0:
                    self.vx[i] = randint(0, 20)
                if self.vx[i] < 0:
                    self.vx[i] = randint(-20, 0)
                if self.vy[i] >= 0:
                    self.vy[i] = randint(0, 20)
                if self.vy[i] < 0:
                    self.vy[i] = randint(-20, 0)
            if self.y[i] < 750 and self.y[i] > 50:
                self.y[i] += self.vy[i]
            else:
                self.vy[i] *= -1
                self.y[i] += self.vy[i]
                if self.vy[i] >= 0:
                    self.vy[i] = randint(0, 20)
                if self.vy[i] < 0:
                    self.vy[i] = randint(-20, 0)
                if self.vx[i] >= 0:
                    self.vx[i] = randint(0, 20)
                if self.vx[i] < 0:
                    self.vx[i] = randint(-20, 0)
            self.__draw()

pygame.display.update()
x = 0
t, start = 0, 0
score = 0
N = 10
M = 10
cloud = Circle(screen, N)
house = Rect(screen, M)
box = InputBox(screen, 100, 7, 140, 32)
manager = GameManager(screen, cloud, house, box)
paused = False
running = True
name = "None"

while running:
    tri = False
    clock.tick(FPS)
    for event in pygame.event.get():
        if box.handle_event(event) != None:
            name = box.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
        if event.type == pygame.QUIT:
            running = False
            with open("Leader.txt", "a") as file:
                file.write("Name: " + str(name) + " - Score:" + str(int(manager.score)) + " Time: "
                           + str(int(pygame.time.get_ticks() / 1000 - t)) + "\n")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(-1, cloud.k - 1):
                if pygame.mouse.get_pos()[0] > cloud.x[i] and pygame.mouse.get_pos()[0] < cloud.x[i] + cloud.h[i]:
                    if pygame.mouse.get_pos()[1] > cloud.y[i] and pygame.mouse.get_pos()[1] < cloud.y[i] + cloud.w[i]:
                        cloud.delete(i + 1)
                        x += 1
                        tri = True
                        break

            for i in range(-1, house.k - 1):
                if pygame.mouse.get_pos()[0] > house.x[i] and pygame.mouse.get_pos()[0] < house.x[i] + house.h[i]:
                    if pygame.mouse.get_pos()[1] > house.y[i] and pygame.mouse.get_pos()[1] < house.y[i] + house.w[i]:
                        house.delete(i + 1)
                        x += 1
                        tri = True
                        break
            if tri == False:
                score -= 2;
    if paused:
        if start == 0:
            start = time.monotonic()

    if not paused:
        if start != 0:
            result = time.monotonic() - start
            t += result
            start = 0
        manager.redraw(score)
        pygame.display.flip()
    if x == N + M:
        running = False
pygame.quit()
