import pygame


class Charecter(pygame.sprite.Sprite):
    def __init__(self, pos, group=None, nick="Guest", color="fortegreen", procreator=None, speed=4):
        super().__init__(group)
        self.pos = pos
        self.group = group
        self.nick = nick
        self.color = color
        self.procreator = procreator
        self.speed = speed
        self.direction = [0, 0, 0, 0]
        # (100, 133)
        self.images = self.procreator.procreator.load_files("characters", "fortegreen", "animation", resize=(85, 113.05))
        self.images[0] = pygame.transform.scale(self.images[0], (self.images[0].get_width() * 0.85, self.images[0].get_height() * 0.85))
        self.max_frames = len(self.images)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.midtop = self.pos
        self.rotation = 1
        self.animation_pos = 0
        self.mask = pygame.mask.from_surface(self.image)

        self.nick_font = CharacterFont(self.nick, 'white', font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 20), bold=True, procreator=self)

    def animate(self):
        if self.rotation < 0:
            self.image = pygame.transform.flip(self.images[int(self.animation_pos / 4)], True, False)
        else:
            self.image = self.images[int(self.animation_pos / 4)]

    def move(self):
        if self.direction[1] > 0:
            #if not pygame.sprite.spritecollide(self, self.procreator.walls_group, False):
            #    self.rect = self.rect.move(0, -self.direction[1] * self.speed)
            self.rect.centery -= self.direction[1] * self.speed
            if self.procreator.procreator.collide_mask(self, self.procreator.walls_group):
                self.rect.centery += self.direction[1] * self.speed
        if self.direction[0] > 0:
            self.rect.centerx -= self.direction[0] * self.speed
            if self.procreator.procreator.collide_mask(self, self.procreator.walls_group):
                self.rect.centerx += self.direction[0] * self.speed
        if self.direction[2] > 0:
            self.rect.centerx += self.direction[2] * self.speed
            if self.procreator.procreator.collide_mask(self, self.procreator.walls_group):
                self.rect.centerx -= self.direction[2] * self.speed
        if self.direction[3] > 0:
            self.rect.centery += self.direction[3] * self.speed
            if self.procreator.procreator.collide_mask(self, self.procreator.walls_group):
                self.rect.centery -= self.direction[3] * self.speed

    def update(self, surface, offset):
        self.animation_pos += 1
        if sum(self.direction) == 0:
            self.animation_pos = 0
        elif self.animation_pos / 4 > self.max_frames - 1:
            self.animation_pos = 4
        self.animate()
        self.move()
        self.nick_font = CharacterFont(str(self.rect.midtop), 'white', font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 20),
                                       bold=True, procreator=self)
        self.nick_font.update(surface, offset)
        surface.blit(self.image, offset)


class CharacterFont:
    def __init__(self, text, color, font=None, bold=False, procreator=None):
        self.text = text
        self.color = color
        self.font = font
        self.font.set_bold(bold)
        self.procreator = procreator
        self.init()

    def init(self):
        self.font_render = self.font.render(self.text, True, self.color)
        self.offset = pygame.math.Vector2((self.procreator.rect.width - self.font_render.get_width()) // 2, -25)

    def update(self, surface, offset):
        surface.blit(self.font_render, self.offset + offset)