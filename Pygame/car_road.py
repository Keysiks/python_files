import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100

    def update(self, speed_x):
        self.rect.x += speed_x


if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)

    sprites = pygame.sprite.Group()
    Car(sprites)

    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        sprites.update(50)
        sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()