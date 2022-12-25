import pygame
import random


class RoomCode(pygame.sprite.Sprite):
    def __init__(self, pos, code, procreator=None, group=None):
        super(RoomCode, self).__init__(group)
        self.pos = pos
        self.code = code
        self.procreator = procreator
        self.can_play = False
        self.i = 0
        self.animation_done = False
        self.btn_animate_text = 'PLAY'
        self.init()

    def init(self):
        self.image = pygame.Surface((200, 50))
        self.image.set_colorkey((0, 0, 0))
        self.draw_rects('#262626', '#141414')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.pos
        self.room_code = RoomCodeFont(self.rect.center, self.code, font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 24), bold=True, color='white', procreator=self, group=self.groups()[0])

    def draw_rects(self, color1, color2):
        pygame.draw.rect(self.image, color1, pygame.Rect((0, 0), self.image.get_size()), border_radius=25)
        pygame.draw.rect(self.image, color2, pygame.Rect((0, 0), self.image.get_size()), 5, border_radius=25)

    def clicked(self):
        if self.can_play is False:
            self.draw_rects('#0B8E7E', '#0DAA97')
            self.can_play = True
        else:
            self.draw_rects('#262626', '#141414')
            self.room_code.init(self.code)
            self.animation_done = False
            self.can_play = False


    def update(self):
        #self.room_code.init(str(random.randint(0, 9999)))
        if self.can_play is True:
            if self.room_code.text != self.btn_animate_text:
                self.i = (self.i + 1) % 13
                if self.i > 11:
                    if not self.animation_done:
                        self.room_code.init(self.room_code.text[1::])
                        if len(self.room_code.text) < 1:
                            self.animation_done = True
                    else:
                        self.room_code.init(self.room_code.text + self.btn_animate_text[len(self.room_code.text)])


        self.procreator.procreator.screen.blit(self.image, self.rect)


class RoomCodeFont(pygame.sprite.Sprite):
    def __init__(self, pos, text, font=None, bold=False, color='white', procreator=None, group=None):
        super(RoomCodeFont, self).__init__(group)
        self.pos = pos
        self.text = text
        self.font = font
        self.font.set_bold(bold)
        self.color = color
        self.procreator = procreator
        self.init(self.text)

    def init(self, text):
        self.text = text
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def clicked(self):
        pass

    def update(self):
        self.procreator.procreator.procreator.screen.blit(self.image, self.rect)