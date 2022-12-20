import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    n = 1
    try:
        n = int(input())
    except ValueError:
        print("error")
        exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        center = 150 - int(300 / (2 * n))
        size_ellipse = int(300/n)
        for i in range(n):
            pygame.draw.ellipse(screen, "white", (0, center, 300, size_ellipse), 1)
            center -= int(300/(2 * n))
            size_ellipse += int(300/n)
        center = 150 - int(300 / (2 * n))
        size_ellipse = int(300 / n)
        for i in range(n):
            pygame.draw.ellipse(screen, "white", (center, 0, size_ellipse, 300), 1)
            center -= int(300 / (2 * n))
            size_ellipse += int(300 / n)
        pygame.display.flip()
    pygame.quit()
