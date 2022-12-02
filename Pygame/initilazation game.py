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
        self.pixels_board = {}

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.left, self.left + self.width * self.cell_size, self.cell_size):
            for j in range(self.top, self.top + self.height * self.cell_size, self.cell_size):
                pygame.draw.rect(screen, (255, 255, 255), (i - 3, j - 3, self.cell_size, self.cell_size),
                                 width=3)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        down = self.top + self.cell_size * self.height
        right = self.left + self.cell_size * self.width
        if (x < self.left or x > right) or (y < self.top or y > down):
            return None
        return ((x - self.left) // 50 + 1, (y - self.top) // 50 + 1)


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
                print(board.get_cell(event.pos))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
