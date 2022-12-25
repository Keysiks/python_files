import os
import pygame
import sys
import pathlib
import ctypes
from sprites.menu_cursor import Cursor
from menu import GeneralMenu
from game import Game


class Core:
    def __init__(self):
        self.settings = {
            'fps_menu': 60,
            'fps_game': 120,
        }

        self.targets = {
            'general_menu': GeneralMenu,
            'game': Game,
        }

        self.custom_events = {
            'ship_passing': pygame.USEREVENT + 1,
        }

    def initialize(self):
        pygame.init()

    def convert_pos(self, x, y):
        return round(x * self.multipler[0]), round(y * self.multipler[1])

    def start_core(self):
        self.object_screen = pygame.display.Info()
        self.screen_resulution = (self.object_screen.current_w, self.object_screen.current_h)
        self.multipler = (self.screen_resulution[0] / 1440, self.screen_resulution[1] / 900)
        self.screen = pygame.display.set_mode(self.screen_resulution)
        self.screen_rect = self.screen.get_rect()
        self.cursor_group = pygame.sprite.Group()
        self.cursor = Cursor((18, 18), procreator=self, group=self.cursor_group)
        pygame.mouse.set_visible(False)
        self.frames_group = pygame.sprite.Group()
        self.fps_limiter = pygame.time.Clock()

    def return_error(self, tittle, text):
        ctypes.windll.user32.MessageBoxW(0, tittle, text, 0)
        self.close_game()

    def get_full_path(self, *args):
        return pathlib.Path(*args)

    def check_file_exists(self, arg):
        return os.path.exists(arg)

    def get_files(self, arg):
        return os.listdir(arg)

    def load_files(self, *args, resize=False):
        return [self.load_image(*args, _, resize=resize) for _ in self.get_files(self.get_full_path(*args))]

    def close_game(self):
        pygame.quit()
        sys.exit()

    def collide_mask(self, a, b):
        for _ in b.sprites():
            if pygame.sprite.collide_mask(a, _):
                return True
        return False

    def load_image(self, *args, resize=False):
        obj = pygame.image.load(self.get_full_path(*args))
        if resize is True:
            obj = pygame.transform.scale(obj, (
                round(obj.get_width() * self.multipler[0]), round(obj.get_height() * self.multipler[1])))
        elif type(resize) is tuple:
            obj = pygame.transform.scale(obj, (resize[0], resize[1]))
        return obj

    def initialize_main_cycle(self, target=None, kwargs=None):
        target = self.targets[target](procreator=self, kwargs=kwargs)
        if target is None:
            self.return_error("Critical Error", "Cant find target module")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    if len(self.cursor.groups()) == 0:
                        self.cursor.add(self.cursor_group)
                    self.cursor.set_pos(event.pos)
                elif event.type == pygame.WINDOWCLOSE:
                    self.close_game()
                elif event.type == pygame.WINDOWLEAVE:
                    self.global_volume = 0
                    target.recount_volume(self.global_volume)
                elif event.type == pygame.WINDOWENTER:
                    self.global_volume = 1
                    target.recount_volume(self.global_volume)

                target.events(event)
            target.render_frame()
            self.frames_group.update()
            self.cursor_group.update()
            pygame.display.update()
            self.fps_limiter.tick(self.settings['fps_game'])


core = Core()
core.initialize()
core.start_core()
core.initialize_main_cycle(target="game", kwargs={'map': 'awaiting_lobby'})
