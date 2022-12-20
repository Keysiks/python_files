import pygame

all_sprites = pygame.sprite.Group()


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("grey"), (pos[0], pos[1], 50, 10))
        self.rect = pygame.Rect(0, 0, 50, 10)


platform = []


class Square(pygame.sprite.Sprite):
    def __init__(self, pos, *platform):
        super().__init__(all_sprites)
        self.image = pygame.Surface((500, 500), pygame.SRCALPHA, 32)
        self.platform = list(platform)
        pygame.draw.rect(self.image, pygame.Color("blue"), (pos[0], pos[1], 20, 20))
        self.rect = pygame.Rect(20, 20, 20, 20)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, event=""):
        if not pygame.sprite.collide_mask(self, *self.platform):
            self.rect = self.rect.move(0, 1)
        if event != "":
            if event == pygame.K_LEFT:
                print("+")
                self.rect = self.rect.move((-10, 0))
            else:
                self.rect = self.rect.move((10, 0))


if __name__ == '__main__':
    event1 = ""
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                Square(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                platform.append(Platform(event.pos, platform))
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    event1 = event.key
        all_sprites.update(event1)
        event1 = ''
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.delay(20)

    pygame.quit()