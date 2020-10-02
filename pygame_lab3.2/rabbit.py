import pygame

#специфицированные типы аргументов,  в какой-то функции исключения, декоратор
FPS = 60
run = True
clock = pygame.time.Clock()
width = 600
height = 800
amount = 1


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
        body_width = self.w // 2
        body_height = self.h // 2
        body_y = self.y + body_height // 2
        pygame.draw.ellipse(self.game_window, self.color, (self.x - body_width // 2, body_y - body_height // 2, body_width, body_height))


    def __draw_head(self):
        head_size = self.h // 8
        y_new = self.y - head_size // 2
        pygame.draw.circle(self.game_window, self.color, (self.x, y_new), head_size)

    def __draw_eye(self):
        eye_height = self.h // 24
        eye_y = self.y - self.h // 16 - eye_height // 2
        for eye_x in (self.x - self.h // 16, self.x + self.h // 16):
            pygame.draw.ellipse(self.game_window, (123,12,123), (eye_x - self.w // 16, eye_y - eye_height, self.w // 9, eye_height))

    def __draw_arm(self):
        eye_height = self.h // 4
        eye_y = self.y + 1.5 * eye_height
        for eye_x in (self.x - self.h // 9, self.x + self.h // 9):
            pygame.draw.ellipse(self.game_window, (13,12,123), (eye_x - self.w // 12, eye_y - eye_height, self.w // 6, eye_height))

    def __draw_ear(self):
        ear_height = self.h // 3
        ear_y = self.y - self.h // 2 + ear_height // 2
        for ear_x in (self.x - self.h // 16, self.x + self.h // 16):
            pygame.draw.ellipse(self.game_window, self.color, (ear_x - self.w // 16, ear_y - ear_height // 2, self.w // 8, ear_height))

    def __draw_mouth(self):
        eye_height = self.h // 24
        eye_y = self.y + self.h // 60
        eye_x = self.x - self.h // 18
        pygame.draw.ellipse(self.game_window, (123,12,123), (eye_x - self.w // 16, eye_y - eye_height, self.w // 3, eye_height))


    def __draw_leg(self):
        leg_height = self.h // 16
        leg_y = self.y + self.h // 2 - leg_height // 2
        for leg_x in (self.x - self.w // 4, self.x + self.w // 4):
            pygame.draw.ellipse(self.game_window, self.color, (leg_x - self.w // 8, leg_y - leg_height // 2, self.w // 4, leg_height))

    def draw_hare(self):
        self.__draw_ear()
        self.__draw_body()
        self.__draw_head()
        self.__draw_eye()
        self.__draw_leg()
        self.__draw_mouth()
        self.__draw_arm()

Rabbit(screen, 200, 200, 200, 400, (200, 200, 200)).draw_hare()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()