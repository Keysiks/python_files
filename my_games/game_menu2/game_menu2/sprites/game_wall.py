import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, width, direction=1, groups=None):
        super().__init__(*groups)
        self.direction = direction
        self.image = pygame.Surface(width)
        pygame.draw.line(self.image, 'red', *((0, 0), width) if direction > 0 else ((0, width[1]), (width[0], 0)), 5)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.image.set_colorkey((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, surface, offset):
        surface.blit(self.image, offset)