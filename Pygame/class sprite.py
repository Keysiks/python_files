class Mouse_cursor(pygame.sprite.Sprite):
    image = load_image("arrow.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Mouse_cursor.image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100

    def update(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]