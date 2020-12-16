import pygame

color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
if __name__ == '__main__':
    try:
        w, n = input().split(' ')
        w, n = int(w), int(n)
    except ValueError:
        print('Неправильный формат ввода')
        exit()
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    for i in range(n):
        pygame.draw.circle(screen, color[i % 3], (600 // 2, w * n), w * n - i * w)
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()