import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    fps = 30
    clock = pygame.time.Clock()
    screen2 = pygame.Surface(screen.get_size())
    pygame.draw.rect(screen2, pygame.Color('green'), (0, 0, 100, 100))
    x, y, w, h = 0, 0, 0, 0
    flag_motion = False  # режим рисования выключен
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag_motion = True
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                flag_motion = False
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] > x:
                    x += w - event.pos[0]
                else:
                    x -= w - event.pos[0]
                if event.pos[1] > y:
                    y += h - event.pos[1]
                else:
                    y -= h - event.pos[1]
                w, h = event.pos[0], event.pos[1]
        # рисуем на экране сохранённое на втором холсте
        screen.fill(pygame.Color('black'))
        if flag_motion:
            screen2.fill(pygame.Color('black'))
            pygame.draw.rect(screen2, pygame.Color('green'), (w, h, 100, 100))
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        pygame.display.flip()