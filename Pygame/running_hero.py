import pygame
import os
import sys

#я сделал еще мод скорости перса, т.к мне показалось что 10 px слишком мало)
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Hero(pygame.sprite.Sprite):
    image = load_image("hero.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, pos):
        self.rect.x += pos[0]
        self.rect.y += pos[1]


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    speed = int(input("Введите скорость персонажа в пикселях:"))
    sprites = pygame.sprite.Group()
    Hero(sprites)

    running = True
    while running:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sprites.update((-speed, 0))
                elif event.key == pygame.K_RIGHT:
                    sprites.update((speed, 0))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    sprites.update((0, -speed))
                elif event.key == pygame.K_DOWN:
                    sprites.update((0, speed))
        sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()