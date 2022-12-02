import pygame


def draw_board(screen, n, a):
    color, color_reverse = pygame.Color(0, 0, 0), pygame.Color(255, 255, 255)
    k = a
    for i in range(k):
        if a % 2 == 0:
            color, color_reverse = color_reverse, color
        for j in range(k):
            pygame.draw.rect(screen, color, (int(n / a) * (i), int(n / a) * (j), int(n / a), int(n / a)))
            color, color_reverse = color_reverse, color


if __name__ == '__main__':
    pygame.init()
    try:
        n, a = map(int, input().split())
    except ValueError:
        print("error")
        exit()
    size = (n, n)
    screen = pygame.display.set_mode(size)
    draw_board(screen, n, a)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()