import pygame

from sprites.game_wall import Wall
from sprites.game_laptop import Laptop


class Map(pygame.sprite.Sprite):
    def __init__(self, path=None, procreator=None, group=None):
        super(Map, self).__init__(*group)
        self.path = path
        self.procreator = procreator
        self.group = group
        self.image = self.procreator.procreator.load_image(self.path, "textures", "field.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.95, self.image.get_height() * 0.95))
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0
        self.init()

    def init(self):
        # Wall((587.0, 184.0), (268.0, 101.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((574.0, 281.0), (13.0, 745.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((574.0, 1026.0), (66.0, 82.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((638.0, 1108.0), (817.0, 2.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((1452.0, 1025.0), (69.0, 85.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((1510.0, 286.0), (9.0, 740.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((581.0, 400.0), (277.0, 100.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((1236.0, 402.0), (277.0, 96.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((854.0, 400.0), (382.0, 2.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((799.0, 776.0), (72.0, 64.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((868.0, 839.0), (5.0, 109.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((696.0, 776.0), (103.0, 46.0), direction=-1, groups=(self.procreator.walls_group,))
        # Wall((695.0, 820.0), (0.0, 104.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((696.0, 820.0), (2.0, 0.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((693.0, 821.0), (5.0, 105.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((692.0, 920.0), (68.0, 69.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((759.0, 950.0), (112.0, 43.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((1254.0, 678.0), (73.0, 64.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((1254.0, 740.0), (0.0, 108.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((1251.0, 738.0), (4.0, 112.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((1251.0, 848.0), (111.0, 42.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((1431.0, 723.0), (1.0, 102.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((1365.0, 823.0), (67.0, 68.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((1325.0, 677.0), (105.0, 46.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((801.0, 593.0), (3.0, 63.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((800.0, 652.0), (41.0, 41.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((839.0, 668.0), (69.0, 25.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((905.0, 603.0), (1.0, 65.0), direction=1, groups=(self.procreator.walls_group,))
        Wall((803.0, 580.0), (59.0, 11.0), direction=-1, groups=(self.procreator.walls_group,))
        Wall((856.0, 579.0), (50.0, 28.0), direction=1, groups=(self.procreator.walls_group,))

        self.init_objects()

    def init_objects(self):
        Laptop((850, 580), procreator=self, group=(self.procreator.camera,))

    def update(self):
        self.procreator.procreator.blit(self.image, self.rect)