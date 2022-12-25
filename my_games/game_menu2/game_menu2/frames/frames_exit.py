import pygame


class FrameExit(pygame.sprite.Sprite):
    def __init__(self, procreator=None, group=None):
        super().__init__(group)
        self.procreator = procreator
        self.image = pygame.Surface((400, 125))
        self.rect = self.image.get_rect()
        self.rect.center = (self.procreator.screen_rect.centerx, self.procreator.screen_rect.centery + 50)
        self.direction = 2
        self.alpha = 0.0

    def update(self):
        if self.rect.centery > self.procreator.screen_rect.centery:
            self.rect.centery -= self.direction
            self.alpha += 10.2
            self.image.set_alpha(round(self.alpha))
        pygame.draw.rect(self.image, 'white', (0, 0, 400, 125))
        self.procreator.screen.blit(self.image, self.rect)
