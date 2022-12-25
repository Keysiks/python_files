import pygame
import random


class Dummy(pygame.sprite.Sprite):
    def __init__(self, pos, direction, procreator=None, group=None):
        super(Dummy, self).__init__(group)
        self.procreator = procreator
        self.orig_image = pygame.image.load("menu/charecters/fortegreen.png")
        self.i = random.randint(0, 360)
        self.direction = pygame.math.Vector2(direction)
        self.image = pygame.transform.rotate(self.orig_image, self.i)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.i += 1
        if self.i >= 720:
            self.i = 0
        self.image = pygame.transform.rotate(self.orig_image, self.i // 2)
        self.rect.center += self.direction
        self.procreator.procreator.screen.blit(self.image, self.rect)

        if self.rect.left > self.procreator.procreator.screen_resulution[0]:
            self.procreator.dummies_group.remove(self)
            self.procreator.spawn_dummies(count=1)
        elif self.rect.right < 0:
            self.procreator.dummies_group.remove(self)
            self.procreator.spawn_dummies(count=1)

        if self.rect.top > self.procreator.procreator.screen_resulution[1]:
            self.procreator.dummies_group.remove(self)
            self.procreator.spawn_dummies(count=1)
        elif self.rect.bottom < 0:
            self.procreator.dummies_group.remove(self)
            self.procreator.spawn_dummies(count=1)