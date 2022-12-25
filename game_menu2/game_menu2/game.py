import pygame

from sprites.game_camera import CameraGroup
from sprites.game_charecter import Charecter
from sprites.game_wall import Wall
from sprites.game_people_count import Counter
from sprites.game_room_code import RoomCode
from sprites.game_chat import Chat


class Game:
    def __init__(self, procreator=None, kwargs=None):
        self.procreator = procreator
        self.kwargs = kwargs
        self.simple_group = pygame.sprite.Group()
        self.camera = CameraGroup(procreator=self)
        self.walls_group = pygame.sprite.Group()
        self.init_map(self.kwargs.get('map', None))
        self.camera.init()
        self.last_button = False
        self.ui_group = pygame.sprite.Group()
        self.counter = Counter((20, 20), 1, procreator=self, group=self.ui_group)
        self.room_code = RoomCode((self.procreator.screen_rect.centerx, self.counter.rect.top - 10), '45SF3G', procreator=self, group=self.ui_group)
        self.chat = Chat(procreator=self)

        self.file = open("coords.txt", "a")

        self.player = Charecter((1040, 404), self.camera, color='fortegreen', nick="Zawh", procreator=self)

    def init_map(self, map):
        if map is None:
            self.procreator.return_error("error occured", "fk you")
        else:
            self.map = self.procreator.get_full_path("maps", map)
            if not self.procreator.check_file_exists(self.procreator.get_full_path(self.map, "map_core.py")):
                self.procreator.return_error("error occured", "fk you")
            else:
                exec(f"from maps.{map}.map_core import Map")
                exec(f"self.map = Map(path=self.map.__str__(), procreator=self, group=self.simple_group)")

    def recount_volume(self, volume):
        pass

    def render_frame(self):
        self.procreator.screen.fill("black")
        self.camera.update(self.player)
        self.ui_group.update()
        self.chat.update()

    def count_cords(self, c1, c2):
        c1 = list(c1)
        c2 = list(c2)
        return c1[0] + c2[0], c1[1] + c2[1]

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            """if self.last_button is False:
                self.last_button = self.count_cords(event.pos, self.camera.offset)
            else:
                coords = self.last_button, self.count_cords(event.pos, self.camera.offset)
                Wall((min(coords, key=lambda x: x[0])[0], min(coords, key=lambda x: x[1])[1]), (abs(coords[0][0] - coords[1][0]), abs(coords[0][1] - coords[1][1])), direction=1 if coords[0][0] < coords[1][0] else -1, groups=(self.camera, self.walls_group))
                self.file.write(f"Wall({(min(coords, key=lambda x: x[0])[0], min(coords, key=lambda x: x[1])[1])}, {(abs(coords[0][0] - coords[1][0]), abs(coords[0][1] - coords[1][1]))}, direction={1 if coords[0][0] < coords[1][0] else -1}, groups=(self.walls_group,))\n")
                self.last_button = False"""

            if event.button == pygame.BUTTON_LEFT:
                for _ in pygame.sprite.spritecollide(self.procreator.cursor, self.ui_group, False):
                    _.clicked()
                self.chat.mouse_check(event.pos, clicked=True)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.player.direction[1] = 1
            elif event.key == pygame.K_d:
                self.player.direction[2] = 1
                self.player.rotation = 1
            elif event.key == pygame.K_a:
                self.player.direction[0] = 1
                self.player.rotation = -1
            elif event.key == pygame.K_s:
                self.player.direction[3] = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.player.direction[1] = 0
            elif event.key == pygame.K_d:
                self.player.direction[2] = 0
            elif event.key == pygame.K_a:
                self.player.direction[0] = 0
            elif event.key == pygame.K_s:
                self.player.direction[3] = 0

        elif event.type == pygame.MOUSEMOTION:
            self.chat.mouse_check(event.pos)