import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Clicker")

background = pygame.image.load("res\\background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

spaceship = pygame.image.load("res\\spaceship.png").convert_alpha()
spaceship = pygame.transform.scale(spaceship, (100, 100))



font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

circle_x = 400
circle_y = 300
circle_radius = 50
score = 0


def draw_circle(x, y, radius):
    #pygame.draw.circle(screen, (0, 120, 255), (x, y), radius)
    screen.blit(spaceship, (x - radius, y - radius))


def draw_score(points):
    text = font.render("Score: " + str(points), True, (255, 255, 255))
    screen.blit(text, (20, 20))


def is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, radius):
    dx = mouse_x - circle_x
    dy = mouse_y - circle_y
    return dx * dx + dy * dy <= radius * radius


def get_next_circle_position(x, y):
    new_x = x
    new_y = y
    return new_x, new_y


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, circle_radius):
                score = score + 1
                circle_x, circle_y = get_next_circle_position(circle_x, circle_y)

    #screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))
    draw_circle(circle_x, circle_y, circle_radius)
    draw_score(score)
    pygame.display.update()
    clock.tick(60)

pygame.quit()