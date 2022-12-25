import pygame


class RadioPass:
    def mouse_check(self, pos, clicked=False):
        pass


class Radio(pygame.sprite.Sprite, RadioPass):
    def __init__(self, pos, volume=0.4, procreator=None, group=None):
        super(Radio, self).__init__(group)
        self.pos = pos
        self.volume = volume
        self.procreator = procreator
        self.image = pygame.Surface((300, 60))
        self.rect = self.image.get_rect()
        self.rect.topright = self.pos
        self.radio_sound = None
        self.musics = list()
        self.load_music()
        self.music_now = 5
        self.initi()
        self.set_music()

    def load_music(self):
        for _ in self.procreator.procreator.get_files(self.procreator.procreator.get_full_path("music")):
            temp = self.procreator.procreator.get_full_path("music", _)
            temp1 = self.procreator.procreator.get_full_path("music_logos", _[::-1].split('.', 1)[1][::-1] + '.jpg')
            music_tuple = _[::-1].split('.', 1)[1][::-1].split('-', 1)
            if len(music_tuple) < 2:
                music_tuple = music_tuple[0], 'unknown author'
            if self.procreator.procreator.check_file_exists(temp1):
                self.musics.append((*music_tuple, pygame.mixer.Sound(temp), self.procreator.procreator.load_image(temp1, resize=(50, 50))))
            else:
                self.musics.append((*music_tuple, pygame.mixer.Sound(temp), None))

    def set_music(self):
        if self.radio_sound is not None:
            self.radio_sound[-2].stop()

        self.radio_sound = self.musics[self.music_now]
        self.music_logo.set_logo(self.radio_sound[-1])
        self.music_name.set_text(self.radio_sound[0], 'white')
        self.author_name.set_text(self.radio_sound[1], 'white')
        self.radio_sound[-2].set_volume(self.volume)
        self.radio_sound[-2].play(-1)

    def next_music(self):
        self.music_now += 1
        if self.music_now > len(self.musics) - 1:
            self.music_now = 0
        self.set_music()

    def prev_music(self):
        self.music_now -= 1
        if self.music_now < 0:
            self.music_now = len(self.musics) - 1
        self.set_music()

    def set_volume(self, volume):
        if self.radio_sound is not None:
            self.radio_sound[-2].set_volume(self.volume * volume)

    def initi(self):
        tmp = RadioButton((9, self.rect.centery), -1, procreator=self, group=self.groups()[0])
        RadioButton((self.rect.w - 33, self.rect.centery), 1, procreator=self, group=self.groups()[0])
        self.music_logo = RadioImage((tmp.rect.w + 18, self.rect.centery), procreator=self, group=self.groups()[0])
        self.music_name = RadioFont((self.music_logo.pos[0] + self.music_logo.rect.w + 9, self.rect.y + 14), 'SONG', 'white', bold=True, font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 14), procreator=self, group=self.groups()[0])
        self.author_name = RadioFont((self.music_logo.pos[0] + self.music_logo.rect.w + 9, self.rect.y + 30), 'author', 'white', bold=False, font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 14), procreator=self, group=self.groups()[0])

    def update(self):
        pygame.draw.rect(self.image, '#141414', pygame.Rect((0, 0), (300, 60)), border_radius=5)
        self.procreator.procreator.screen.blit(self.image, self.rect)


class RadioButton(pygame.sprite.Sprite, RadioPass):
    def __init__(self, pos, direction, procreator=None, group=None):
        super(RadioButton, self).__init__(group)
        self.pos = pos
        self.direction = direction
        self.procreator = procreator
        self.images = self.procreator.procreator.procreator.load_files("menu", "radio", "next" if self.direction > 0 else "previous", resize=False)
        self.image = self.images[1]
        self.rect = self.image.get_rect()
        self.rect.midleft = (self.procreator.rect.left + self.pos[0], self.pos[1])

    def mouse_check(self, pos, clicked=False):
        if self.rect.collidepoint(pos):
            self.image = self.images[0]
            if clicked is True:
                if self.direction > 0:
                    self.procreator.next_music()
                else:
                    self.procreator.prev_music()
        else:
            self.image = self.images[1]

    def update(self):
        self.procreator.procreator.procreator.screen.blit(self.image, self.rect)


class RadioImage(pygame.sprite.Sprite, RadioPass):
    def __init__(self, pos, procreator=None, group=None):
        super(RadioImage, self).__init__(group)
        self.pos = pos
        self.procreator = procreator
        self.default_image = procreator.procreator.procreator.load_image("sys", "unknown_music.jpg", resize=(self.procreator.rect.h - 10, self.procreator.rect.h - 10))
        self.image = self.default_image
        self.rect = self.image.get_rect()
        self.rect.midleft = (self.procreator.rect.left + self.pos[0], self.pos[1])

    def set_logo(self, logo):
        if logo is not None:
            self.image = logo
        else:
            self.image = self.default_image

    def update(self):
        self.procreator.procreator.procreator.screen.blit(self.image, self.rect)


class RadioFont(pygame.sprite.Sprite, RadioPass):
    def __init__(self, pos, text, color, bold=False, font=None, procreator=None, group=None):
        super(RadioFont, self).__init__(group)
        self.pos = pos
        self.procreator = procreator
        self.font = font
        self.font.set_bold(bold)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.procreator.rect.left + self.pos[0], self.pos[1])

    def set_text(self, text, color):
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.procreator.rect.left + self.pos[0], self.pos[1])

    def update(self):
        self.procreator.procreator.procreator.screen.blit(self.image, self.rect)