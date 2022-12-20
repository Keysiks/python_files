import pygame
import os
import sys

all_sprites = pygame.sprite.Group()
size = width, height = 800, 400


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = height


mountain = Mountain()


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.delay(10)
    pygame.quit()