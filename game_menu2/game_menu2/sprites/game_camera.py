import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, procreator=None):
        super().__init__()
        self.procreator = procreator
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.ground_rect = (0, 0)

    def init(self):
        self.ground_rect = self.procreator.map.rect

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def update(self, player):
        self.center_target_camera(player)
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.procreator.map.image, ground_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            sprite.update(self.display_surface, sprite.rect.topleft - self.offset)
