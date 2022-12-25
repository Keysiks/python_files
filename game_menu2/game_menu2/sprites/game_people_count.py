import pygame


class Counter(pygame.sprite.Sprite):
    def __init__(self, pos, players_now, procreator=None, group=None):
        super(Counter, self).__init__(group)
        self.pos = pos
        self.players_now = players_now
        self.procreator = procreator
        self.image = pygame.Surface((125, 50))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.procreator.procreator.screen_rect.centerx
        self.rect.bottom = self.procreator.procreator.screen_resulution[1] - 25
        self.init()

    def init(self):
        self.text = CounterFont((0, self.rect.h // 2), 1, 12, font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 24), bold=False, procreator=self, group=self.groups()[0])
        self.icon = CounterIcon((self.rect.w, self.rect.h // 2), procreator=self, group=self.groups()[0])

    def update(self):
        self.procreator.procreator.screen.blit(self.image, self.rect)


class CounterIcon(pygame.sprite.Sprite):
    def __init__(self, pos, procreator=None, group=None):
        super(CounterIcon, self).__init__(group)
        self.pos = pos
        self.procreator = procreator
        self.image = self.procreator.procreator.procreator.load_image(self.procreator.procreator.procreator.get_full_path("game", "counter", "state.svg"))
        self.rect = self.image.get_rect()
        self.rect.midright = self.pos

    def update(self):
        self.procreator.image.blit(self.image, self.rect)


class CounterFont(pygame.sprite.Sprite):
    def __init__(self, pos, players_now, max_players, font=None, bold=False, color='white', procreator=None, group=None):
        super(CounterFont, self).__init__(group)
        self.pos = pos
        self.players_now = players_now
        self.max_players = max_players
        self.font = font
        self.font.set_bold(bold)
        self.color = color
        self.procreator = procreator
        self.init()

    def init(self):
        self.image = self.font.render('{0} / {1}'.format(self.players_now, self.max_players), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.midleft = self.pos

    def update(self):
        self.procreator.image.blit(self.image, self.rect)