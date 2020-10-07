import pygame
from PIL import Image




pygame.init()



def save(win, FPS, manager):
    w, h = win.get_size()
    run = True
    clock = pygame.time.Clock()
    frames = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                frames[0].save('pygame_lab3.1\pic\moving_ball.gif', format = 'GIF',
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