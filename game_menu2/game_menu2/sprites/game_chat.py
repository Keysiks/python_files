import pygame


class Chat(pygame.sprite.Group):
    def __init__(self, procreator=None):
        super(Chat, self).__init__()
        self.procreator = procreator
        self.chat_showed = False
        self.init()

    def init(self):
        self.icon = ChatIcon((self.procreator.procreator.screen_resulution[0] - 20, 20), procreator=self, group=self)
        self.chat_rect = ChatRect(self.procreator.procreator.screen_rect.center, (
            self.procreator.procreator.screen_resulution[0],
            self.procreator.procreator.screen_resulution[1]),
                                  procreator=self, group=self)
        self.msg = ChatMessage((100, 100), 'pafaf', 'gwgsegag', 'gwgweg', 'ggege', procreator=self, group=self)

    def mouse_check(self, pos, clicked=False):
        for _ in self.sprites():
            _.mouse_check(pos, clicked)


class ChatIcon(pygame.sprite.Sprite):
    def __init__(self, pos, procreator=None, group=None):
        super(ChatIcon, self).__init__(group)
        self.pos = pos
        self.procreator = procreator
        self.init()

    def init(self):
        self.images = {'hide': self.procreator.procreator.procreator.load_files(
            self.procreator.procreator.procreator.get_full_path("game", "chat", "hide")),
            'show': self.procreator.procreator.procreator.load_files(
                self.procreator.procreator.procreator.get_full_path("game", "chat", "show"))}
        self.image = self.images['hide'][1]
        self.rect = self.image.get_rect()
        self.rect.topright = self.pos

    def mouse_check(self, pos, clicked=False):
        if self.rect.collidepoint(pos):
            if self.procreator.chat_showed:
                self.image = self.images['show'][0]
            else:
                self.image = self.image = self.images['hide'][0]
            if clicked:
                self.procreator.chat_showed = True if self.procreator.chat_showed is False else False
                self.image = self.images['show'][0]
        else:
            if self.procreator.chat_showed:
                self.image = self.images['show'][1]
            else:
                self.image = self.images['hide'][1]

    def update(self):
        self.procreator.procreator.procreator.screen.blit(self.image, self.rect)


class ChatRect(pygame.sprite.Sprite):
    def __init__(self, pos, size, procreator=None, group=None):
        super(ChatRect, self).__init__(group)
        self.pos = pos
        self.size = size
        self.procreator = procreator
        self.init()

    def init(self):
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, '#000000', self.rect, border_radius=15)
        self.image.set_alpha(127.5)
        self.rect.center = self.pos

    def mouse_check(self, pos, clicked=False):
        pass

    def update(self):
        if self.procreator.chat_showed is True:
            self.procreator.procreator.procreator.screen.blit(self.image, self.rect)


class ChatMessage(pygame.sprite.Sprite):
    def __init__(self, pos, text, author, logo, who, procreator=None, group=None):
        super(ChatMessage, self).__init__(group)
        self.pos = pos
        self.text = text.ljust(len(author), ' ')
        self.author = author
        self.logo = logo

        author_font = pygame.font.Font('fonts/Roboto-Medium.ttf', 24)
        author_font.set_bold(True)

        self.author_render = author_font.render(self.author, True, 'black')
        self.text_render = pygame.font.Font('fonts/Roboto-Medium.ttf', 24).render(self.text, True, 'white')

        self.image = pygame.Surface((self.text_render.get_width() + 100 + 3, self.text_render.get_height() + 69 + 3))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

        pygame.draw.rect(self.image, '#828282',
                         pygame.Rect((3, 3), (self.text_render.get_width() + 100, self.text_render.get_height() + 69)),
                         border_radius=5)
        pygame.draw.rect(self.image, '#D9D9D9',
                         pygame.Rect((0, 0), (self.text_render.get_width() + 100, self.text_render.get_height() + 69)),
                         border_radius=5)

        self.image.blit(self.author_render, (90, 22))
        self.image.blit(self.text_render, (90, 53))

        self.who = who
        self.procreator = procreator

    def mouse_check(self, pos, clicked):
        pass

    def update(self):
        if self.procreator.chat_showed is True:
            self.procreator.procreator.procreator.screen.blit(self.image, self.rect)
