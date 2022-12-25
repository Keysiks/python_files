import pygame


class Laptop(pygame.sprite.Sprite):
    def __init__(self, pos, procreator=None, group=None):
        super(Laptop, self).__init__(*group)
        self.pos = pos
        self.procreator = procreator
        self.image = self.procreator.procreator.procreator.load_image("game/laptop/state.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, surface, offset):
        surface.blit(self.image, offset)