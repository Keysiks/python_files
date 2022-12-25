import pygame
import random

from sprites.menu_dummy import Dummy
from sprites.menu_spaceship import SpaceShip
from sprites.menu_radio import Radio
from sprites.menu_menu import Menu
from sprites.menu_logo import Logo


class GeneralMenu:
    def __init__(self, procreator=None, kwargs=None):
        self.procreator = procreator
        self.background = self.procreator.load_image("menu", "bg.png", resize=True)
        self.group_with_volume = pygame.sprite.Group()
        self.dummies_group = pygame.sprite.Group()
        self.spaceship_group = pygame.sprite.Group()
        self.spaceship = SpaceShip((0, 0), (7, -7), procreator=self, group=self.group_with_volume)
        self.radio_group = pygame.sprite.Group()
        Radio(pos=(self.procreator.screen_resulution[0] - 20, 20), procreator=self, group=(self.radio_group, self.group_with_volume))
        self.menu = Menu((60, 400), (5, 15), procreator=self)
        self.menu.add_item("P L A Y", font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 48))
        self.menu.add_item("C H A R E C T E R S", font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 48))
        self.menu.add_item("S E T T I N G S", font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 48))
        self.menu.add_item("E X I T", font=pygame.font.Font('fonts/Inter-ExtraLight.ttf', 48), task="exit")
        self.absolutly_top = pygame.sprite.Group()
        Logo((50, 100), (519.0, 133.5), procreator=self, group=self.absolutly_top)
        self.spawn_dummies(count=5)

        pygame.time.set_timer(self.procreator.custom_events['ship_passing'], 30000)

    def spawn_dummies(self, count=0):
        for _ in range(count):
            direction = random.choices([-2, -1, 1, 2], k=2)
            Dummy((-80 if direction[0] > 0 else self.procreator.screen_resulution[0] + 80,
                   random.randint(0, self.procreator.screen_resulution[1])), direction, procreator=self, group=self.dummies_group)

    def event_ship_passing(self):
        self.spaceship.set_pos(-700, self.procreator.screen_resulution[1] + 700)
        self.spaceship.play_sound(-1)
        self.spaceship.add(self.spaceship_group)

    def recount_volume(self, volume):
        for _ in self.group_with_volume.sprites():
            _.set_volume(_.volume * volume)

    def render_frame(self):
        self.procreator.screen.blit(self.background, (0, 0))
        self.spaceship_group.update()
        self.dummies_group.update()
        self.radio_group.update()
        self.menu.update()
        self.absolutly_top.update()

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            for _ in self.radio_group.sprites():
                _.mouse_check(event.pos, clicked=False)
            self.menu.mouse_check(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for _ in self.radio_group.sprites():
                _.mouse_check(event.pos, clicked=True)
            self.menu.mouse_check(event.pos, clicked=True)
        elif event.type == self.procreator.custom_events['ship_passing']:
            self.event_ship_passing()