import pygame

class Logo(pygame.sprite.Sprite):
    def __init__(self, pos, size, procreator=None, group=None):
        super(Logo, self).__init__(group)
        self.pos = pos
        self.procreator = procreator
        self.image = self.procreator.procreator.load_image("menu", "logo.png", resize=size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.procreator.procreator.screen.blit(self.image, self.rect)