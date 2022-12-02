import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color_slovar = {}
        for i in range(width):
            for j in range(height):
                self.color_slovar[(i, j)] = 2

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.left, self.left + self.width * self.cell_size, self.cell_size):
            for j in range(self.top, self.top + self.height * self.cell_size, self.cell_size):
                pygame.draw.rect(screen, (255, 255, 255), (i - 3, j - 3, self.cell_size, self.cell_size), width=1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        down = self.top + self.cell_size * self.height
        right = self.left + self.cell_size * self.width
        if (x < self.left or x > right) or (y < self.top or y > down):
            return None
        self.color_slovar[((x - self.left) // 50, (y - self.top) // 50)] += 1
        color_index = self.color_slovar[((x - self.left) // 50, (y - self.top) // 50)]
        return ((x - self.left) // 50 + 1, (y - self.top) // 50 + 1, color_index % 3)

    def on_click(self, pos, screen):
        if pos is None:
            return
        x, y, color = pos
        if color == 0: color = "black"
        elif color == 1: color = "red"
        else: color = "dark blue"
        x -= 1
        y -= 1
        pygame.draw.rect(screen, color, (self.left + self.cell_size * x - 3, self.top + self.cell_size * y - 3, self.cell_size, self.cell_size))

    def get_click(self, mouse_pos, screen):
        pos = self.get_cell(mouse_pos)
        self.on_click(pos, screen)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    width_board, height_board = 5, 5
    #width_board, height_board = int(input("Enter width of board: ")), int(input("Enter height of board: "))
    board = Board(width_board, height_board)
    board.set_view(10, 10, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos, screen)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
