import pygame


class Menu(pygame.sprite.Group):
    def __init__(self, pos, offset, procreator=None):
        super(Menu, self).__init__()
        self.pos = pos
        self.procreator = procreator
        self.min_offset, self.max_offset = self.offset = offset
        self.indicators = self.procreator.procreator.load_files("buttons", "rect")
        self.last_child_bottom = 0

    def add_item(self, text, font, bold=False, task=None):
        tmp = MenuItem((self.pos[0], self.pos[1] + self.last_child_bottom), text, font, bold=bold, task=task,
                       procreator=self, group=self)
        self.last_child_bottom += tmp.rect.h

    def mouse_check(self, pos, clicked=False):
        for _ in self.sprites():
            _.mouse_check(pos, clicked=clicked)


class MenuItem(pygame.sprite.Sprite):
    def __init__(self, pos, text, font, color=(255, 255, 255), bold=False, task=None, procreator=None, group=None):
        super(MenuItem, self).__init__(group)
        self.pos = pos
        self.text = text
        self.font = font
        self.color = color
        self.font.set_bold(bold)
        self.task = task
        self.procreator = procreator
        self.offset = self.procreator.min_offset
        self.direction = 0
        self.font_image = self.font.render(self.text, True, self.color)
        self.font_rect = self.font_image.get_rect()
        self.indicator = self.procreator.indicators[1]
        self.indicator_rect = self.indicator.get_rect()
        self.render_offset()

    def render_offset(self):
        self.image = pygame.Surface(
            (self.indicator_rect.w + self.offset + self.font_rect.w, max(self.font_rect.h, self.indicator_rect.h)))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.font_rect = self.font_image.get_rect()
        if self.font_rect.h > self.indicator_rect.h:
            self.indicator_rect.midleft = 0, self.font_rect.centery
        else:
            self.font_rect.mid = self.indicator_rect.centery
        self.font_rect.left = self.indicator_rect.w + self.offset

    def mouse_check(self, pos, clicked=False):
        if self.rect.collidepoint(pos):
            self.indicator = self.procreator.indicators[0]
            self.direction = 1
            if clicked is True:
                if self.task == "exit":
                    self.procreator.procreator.procreator.close_game()
        else:
            self.indicator = self.procreator.indicators[1]
            self.direction = 0

    def update(self):
        if self.direction > 0:
            if self.offset < self.procreator.max_offset:
                self.offset += 1
                self.render_offset()
        else:
            if self.offset > self.procreator.min_offset:
                self.offset -= 1
                self.render_offset()

        self.image.fill((0, 0, 0))
        self.image.blit(self.indicator, self.indicator_rect)
        self.image.blit(self.font_image, self.font_rect)
        self.procreator.procreator.procreator.screen.blit(self.image, self.rect)
