import pygame
import time

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Шарики')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    running = True
    x_pos = 0
    v = 100
    clock = pygame.time.Clock()
    circle_pos = []
    fps = 120
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                circle_pos.append((x, y, True, True))
        screen.fill((0, 0, 0))
        for pos in circle_pos:
            pygame.draw.circle(screen, pygame.Color('white'), (pos[0], pos[1]), 10)
        for i in range(len(circle_pos)):
            if circle_pos[i][2]:
                x, y, t1, t2 = circle_pos[i]
                if (x - 10 - v / fps) > 0:
                    circle_pos[i] = x - v / fps, y, t1, t2
                else:
                    circle_pos[i] = x + v / fps, y, not (t1), t2
            else:
                x, y, t1, t2 = circle_pos[i]
                if (x + 10 - v / fps) < width:
                    circle_pos[i] = x + v / fps, y, t1, t2
                else:
                    circle_pos[i] = x - v / fps, y, not (t1), t2
            if circle_pos[i][3]:
                x, y, t1, t2 = circle_pos[i]
                if y - 10 - v / fps > 0:
                    circle_pos[i] = x, y - v / fps, t1, t2
                else:
                    circle_pos[i] = x, y - v / fps, t1, not (t2)
            else:
                x, y, t1, t2 = circle_pos[i]
                if y + 10 - v / fps < height:
                    circle_pos[i] = x, y + v / fps, t1, t2
                else:
                    circle_pos[i] = x, y - v / fps, t1, not (t2)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
