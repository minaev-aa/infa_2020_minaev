import pygame

#специфицированные типы аргументов,  в какой-то функции исключения, декоратор
FPS = 60
run = True
clock = pygame.time.Clock()
width = 600
height = 800
amount = 1

'''
    Функция рисует зайца на экране.
    surface - объект pygame.Surface
    x, y - координаты левого верхнего угла изображения
    width, height - ширина и высота изобажения
     color - цвет, заданный в формате, подходящем для pygame.Color
'''

screen = pygame.display.set_mode((400, 400))

class Rabbit:
    """Класс Rabbit используется для разбивки рисования кролика

    Attributes
    ----------
    surface : pygame.Surface
        Место рисование
    x, y : int
        координаты центра изображения
    width, height : int
        ширина и высота изобажения
    сolor : pygame.color
        цвет кролика

    Methods
    -------
    draw_hare()
        рисование
    """

    def __init__(self, surface, x, y, width, height, color):
        self.color = color
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.game_window = surface
    def __draw_body(self):
        __body_width = self.w // 2
        __body_height = self.h // 2
        __body_y = self.y + __body_height // 2
        pygame.draw.ellipse(self.game_window, self.color, (self.x - __body_width // 2, __body_y - __body_height // 2, __body_width, __body_height))


    def __draw_head(self):
        __head_size = self.h // 8
        __y_new = self.y - __head_size // 2
        pygame.draw.circle(self.game_window, self.color, (self.x, __y_new), __head_size)


    def __draw_ear(self):
        __ear_height = self.h // 3
        __ear_y = self.y - self.h // 2 + __ear_height // 2
        for __ear_x in (self.x - self.h // 16, self.x + self.h // 16):
            pygame.draw.ellipse(self.game_window, self.color, (__ear_x - self.w // 16, __ear_y - __ear_height // 2, self.w // 8, __ear_height))


    def __draw_leg(self):
        __leg_height = self.h // 16
        __leg_y = self.y + self.h // 2 - __leg_height // 2
        for __leg_x in (self.x - self.w // 4, self.x + self.w // 4):
            pygame.draw.ellipse(self.game_window, self.color, (__leg_x - self.w // 8, __leg_y - __leg_height // 2, self.w // 4, __leg_height))

    def draw_hare(self):
        self.__draw_body()
        self.__draw_head()
        self.__draw_ear()
        self.__draw_leg()

Rabbit(screen, 200, 200, 200, 400, (200, 200, 200)).draw_hare()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()