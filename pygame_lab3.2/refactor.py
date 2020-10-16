import pygame


def girl(a, b, k, n):
    """
    :param a: сдвиг по x относительно нормального положения
    :param b: сдвиг по y относительно нормального положения
    :param k: перемещение по осям
    :param n: ореинтация девочки правая/левая
    :return: Рисунок девочки
    """
    s = 130 * k + a
    pygame.draw.polygon(screen, (210, 145, 188), ([s - 80, b], [s + 80, b], [s, b - 200]))
    pygame.draw.circle(screen, (224, 172, 105), (s, b - 200), r)
    pygame.draw.line(screen, (0, 0, 0), (s - 20, b), (s - 20, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s + 20, b + 80), (s + 40, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s - 40, b + 80), (s - 20, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s + 20, b), (s + 20, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s + 20 * pow(-1, n), b - 130), (s + 130 * pow(-1, n), b - 60))
    pygame.draw.line(screen, (0, 0, 0), (s - 20 * pow(-1, n), b - 130), (s - 80 * pow(-1, n), b - 90))
    pygame.draw.line(screen, (0, 0, 0), (s - 80 * pow(-1, n), b - 90), (s - 130 * pow(-1, n), b - 130))


def boy(a, b, k):
    """
    :param a: сдвиг по x относительно нормального положения
    :param b: сдвиг по y относительно нормального положения
    :param k: перемещение по осям
    :return: Рисунок мальчика
    """
    s = k * 130 + a
    pygame.draw.ellipse(screen, (178, 221, 255), pygame.Rect(s - 50, b - 200, 100, 200))
    pygame.draw.circle(screen, (204, 154, 108), (s, b - 210), r)
    pygame.draw.line(screen, (0, 0, 0), (s - 20, b - 15), (s - 20, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s + 20, b - 15), (s + 20, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s - 40, b + 80), (s - 20, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s + 20, b + 80), (s + 40, b + 80))
    pygame.draw.line(screen, (0, 0, 0), (s - 20, b - 130), (s - 130, b - 60))
    pygame.draw.line(screen, (0, 0, 0), (s + 20, b - 130), (s + 130, b - 60))


def ice(a, b):
    """
    :param a: сдвиг по x относительно нормального положения
    :param b: сдвиг по y относительно нормального положения
    :return: Рисунок мороженного
    """
    pygame.draw.polygon(screen, (201, 153, 126), ([a, b], [a + 40, b - 100], [a - 40, b - 100]))
    pygame.draw.circle(screen, (112, 213, 197), (a + 20, b - 110), r // 2)
    pygame.draw.circle(screen, (241, 206, 18), (a - 20, b - 110), r // 2)
    pygame.draw.circle(screen, (212, 104, 185), (a, b - 140), r // 2)


def love(a, b):
    """
    :param a: сдвиг по x относительно нормального положения
    :param b: сдвиг по y относительно нормального положения
    :return: Рисунок сердечка
    """
    pygame.draw.polygon(screen, (252, 180, 187), ([a, b], [a + 30, b - 60], [a - 30, b - 60]))
    pygame.draw.circle(screen, (252, 180, 187), (a - 15, b - 60), 15)
    pygame.draw.circle(screen, (252, 180, 187), (a + 15, b - 60), 15)


def fon(a, b):
    """
    :param a: Координата по x  относительно нормального положения
    :param b: Координата по y относительно нормального положения
    :return: Отображение фона
    """
    screen.fill((109, 193, 255))
    pygame.draw.line(screen, (0, 0, 0), (390 + a, -130 + b), (390 + a, -300 + b))
    pygame.draw.rect(screen, (186, 238, 145), (0, 600, 1200, 600))


def draw_now(a, b):
    """
    :param a: Координата по x  относительно нормального положения
    :param b: Координата по y относительно нормального положения
    :return: Построение конечного рисунка с несколькими людьми и мороженным
    """
    fon(a, b)
    girl(a, b, 4, 0)
    girl(a, b, 2, 1)
    boy(a, b, 6)
    boy(a, b, 0)
    ice(390 + a, -300 + b)
    ice(910 + a, -60 + b)
    love(-130 + a, -60 + b)
    pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((1200, 900))
done = False
r = 40
x = 200
y = 700

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    draw_now(x, y)
