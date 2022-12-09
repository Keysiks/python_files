import pygame
import os
import sys
import random


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Mouse_cursor(pygame.sprite.Sprite):
    image = load_image("arrow.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Mouse_cursor.image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100

    def update(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    pygame.mouse.set_visible(False)

    sprites = pygame.sprite.Group()
    Mouse_cursor(sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_focused() is True:
                if event.type == pygame.MOUSEMOTION:
                    screen.fill("black")
                    sprites.update(event.pos)
        sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()