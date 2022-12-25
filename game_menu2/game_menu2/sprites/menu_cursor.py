import pygame


class Cursor(pygame.sprite.Sprite):
    def __init__(self, size, procreator=None, group=None):
        super(Cursor, self).__init__(group)
        self.size = size
        self.procreator = procreator
        self.images = self.procreator.load_files("sys", "cursor", resize=size)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.i = 0

    def set_pos(self, coord):
        self.rect.topleft = coord

    def set_cursor(self, index):
        self.image = self.images[index]

    def update(self):
        self.i += 1
        if self.i >= 600:
            self.i = 0
            self.remove(self.groups()[0])
        self.procreator.screen.blit(self.image, self.rect)
