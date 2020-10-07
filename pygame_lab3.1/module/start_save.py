from PIL import Image
import pygame

pygame.init()



def save(win, FPS, manager):
    '''
    Запуск картинки с сохранение gif
    :param win: главное окно display
    :param FPS: количество кадров в секунду
    :param manager: окно картинки с сохранение gif
    :return:
    '''
    w, h = win.get_size()
    run = True
    clock = pygame.time.Clock()
    frames = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frames[0].save('pygame_lab3.1\pic\gif.gif', format = 'GIF',
                                append_images = frames[1:],
                                save_all = True,
                                duration = 100, loop = 0)
                run = False
        manager.redraw()
        pygame.display.flip()
        img = pygame.image.tostring(win, "RGBA")
        new_frame = Image.frombytes("RGBA", (w, h), img)
        frames.append(new_frame)
    pygame.quit()


def running(win, FPS, manager):
    '''
    :param win: главное окно display
    :param FPS: количество кадров в секунду
    :param manager: конфигурация картинки
    :return: окно картинки без сохранения gif
    '''
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        manager.redraw()
        pygame.display.flip()
    pygame.quit()