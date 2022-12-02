import pygame
import random


def draw_circle(r, screen, pos_x, pos_y):
    pygame.draw.circle(screen, "yellow", (pos_x, pos_y), r)


if __name__ == '__main__':
    pygame.init()
    size = width, height = random.randint(300, 800), random.randint(300, 800)
    screen = pygame.display.set_mode(size)
    v = 10  # пикселей в секунду
    fps = 60  # кадры в секунду
    clock = pygame.time.Clock()
    running = True
    r = 0
    pos_x, pos_y = 0, 0
    while running:
        screen.fill("dark blue")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = event.pos
                r = 0
        r += v * clock.tick() / 1000
        draw_circle(r, screen, pos_x, pos_y)
        pygame.display.flip()
    pygame.quit()
