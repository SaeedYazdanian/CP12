import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
x, y = 400, 300
x1, y1 = 100, 100
ObjectSize = 50
targetSize = 50
speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 0:
        y -= speed
    if keys[pygame.K_s] and y < 600 - ObjectSize:
        y += speed
    if keys[pygame.K_a] and x > 0:
        x -= speed
    if keys[pygame.K_d] and x < 800 - ObjectSize:
        x += speed

    player = pygame.Rect(x, y, ObjectSize, ObjectSize)
    target = pygame.Rect(x1, y1, targetSize, targetSize)
    if player.colliderect(target):
        print("Collision!")
        targetSize -= 5
        if targetSize <= 0:
            targetSize = 1
        x1 = random.randint(0,800 - targetSize)
        y1 = random.randint(0,600 - targetSize)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 0, 255), target)
    pygame.display.update()

pygame.quit()