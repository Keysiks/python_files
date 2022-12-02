import pygame


def draw_line(screen, width, height):
    pos_1 = (0, 0)
    pos_2 = (width, height)
    pos_3 = (width, 0)
    pos_4 = (0, height)
    pygame.draw.line(screen, pygame.Color(255, 255, 255), pos_1, pos_2, width=5)
    pygame.draw.line(screen, pygame.Color(255, 255, 255), pos_3, pos_4, width=5)


if __name__ == '__main__':
    pygame.init()
    print("Enter coordinates:")
    width, height = map(int, input().split())
    size = (width, height)
    screen = pygame.display.set_mode(size)
    draw_line(screen, width, height)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
