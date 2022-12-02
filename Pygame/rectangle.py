import pygame


def draw_rectangle(screen, width, height):
    pygame.draw.rect(screen, pygame.Color("red"), (1, 1, width - 2, height - 2), width=0)


if __name__ == '__main__':
    pygame.init()
    try:
        print("Enter coordinates:")
        width, height = map(int, input().split())
    except ValueError:
        print("error")
        exit()
    screen = pygame.display.set_mode((width, height))
    draw_rectangle(screen, width, height)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()