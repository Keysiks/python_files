import pygame


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, pos, direction, procreator=None, volume=0.5, group=None):
        super(SpaceShip, self).__init__(*group)
        self.pos = pos
        self.direction = pygame.math.Vector2(direction)
        self.procreator = procreator
        self.images = self.procreator.procreator.load_files("menu", "ship", resize=False)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.frames = 0
        self.real_frames = len(self.images) - 1
        self.volume = volume
        self.global_volume_multiplier = 1
        self.volume_multiplier = 0.0

        self.sound = pygame.mixer.Sound(self.procreator.procreator.get_full_path("sys", "ship_arrival_sound.mp3"))
        self.sound.set_volume(volume)

        self.mult = 1

    def set_pos(self, x, y):
        self.rect.topright = x, y

    def play_sound(self, arg):
        self.sound.play(arg)

    def set_volume(self, volume):
        self.global_volume_multiplier = volume

    def update(self):
        self.rect.center += self.direction
        self.frames += 1
        self.mult -= 0.001
        if self.frames // 4 > self.real_frames:
            self.frames = 0
        self.procreator.procreator.screen.blit(self.image, self.rect)
        if self.rect.bottom > self.procreator.procreator.screen_resulution[1]:
            self.volume_multiplier += 0.01
            self.sound.set_volume((self.volume * self.volume_multiplier) * self.global_volume_multiplier)

        if self.rect.bottom < 0:
            self.volume_multiplier -= 0.01
            self.sound.set_volume((self.volume * self.volume_multiplier) * self.global_volume_multiplier)

            if self.volume_multiplier <= 0:
                self.remove(self.groups()[0])
                self.sound.stop()
                self.volume_multiplier = 0
                self.sound.set_volume((self.volume * self.volume_multiplier) * self.global_volume_multiplier)