import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

x, y = 400, 300
ObjectSize = 20
speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, ObjectSize, ObjectSize))
    pygame.display.update()

pygame.quit()