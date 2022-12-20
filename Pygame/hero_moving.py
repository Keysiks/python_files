import pygame
import os
import sys

FPS = 50
map_x, map_y = map(int, input('Введите размер карты: ').split())
level_name = input("Введите имя файла с именем карты: ")
size = width, height = 50 * map_x, 50 * map_y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, event):
        res = load_level(level_name)
        res1 = res[(self.rect.x) // 50]
        res2 = res[(self.rect.x - 50) // 50]
        res3 = res[(self.rect.x + 50) // 50]

        if event.key == pygame.K_UP:
            if res1[(self.rect.y - 50) // 50] != "#":
                self.rect = self.rect.move((0, -50))
        elif event.key == pygame.K_DOWN:
            if res1[(self.rect.y + 50) // 50] != "#":
                self.rect = self.rect.move((0, 50))
        elif event.key == pygame.K_LEFT:
            if res2[self.rect.y // 50] != "#":
                self.rect = self.rect.move((-50, 0))
        elif event.key == pygame.K_RIGHT:
            if res3[self.rect.y // 50] != "#":
                self.rect = self.rect.move((50, 0))

    def cord(self):
        return self.rect.x, self.rect.y


player, level_x, level_y = generate_level(load_level(level_name))

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)

    running = True

    start_screen()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                    player_group.update(event)
        all_sprites.draw(screen)
        player_group.draw(screen)
        pygame.display.flip()
    pygame.quit()
