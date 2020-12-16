import pygame
class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255), (self.left + self.cell_size*i,
                                                           self.top + self.cell_size*j,
                                                           self.cell_size, self.cell_size), width=self.board[i][j])
    def get_cell(self,mouse_pos):
        x, y = mouse_pos
        for i in range(self.height):
            for j in range(self.width):
                if ((x > j*self.cell_size+self.top) and (x <= (j+1)*self.cell_size+self.top) and
                        (y > i*self.cell_size+self.left) and ((y <= (i + 1) * self.cell_size + self.left))):
                    r = i, j
                    return (r)
        return None

    def on_click(self, cell):
        x, y = cell
        self.board[y][x] = (self.board[y][x]+1) % 2
        for i in range(self.width):
            self.board[y][i] = (self.board[y][i] + 1) % 2
        for i in range(self.height):
            self.board[i][x] = (self.board[i][x]+1) % 2


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)



board = Board(8, 8)
pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
board.set_view(10, 10, 50)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()