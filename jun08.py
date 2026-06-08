import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Starter")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)

GROUND_Y = 320

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 28)


def draw_text(text, x, y, color=BLACK, big=True):
    used_font = font if big else small_font
    img = used_font.render(text, True, color)
    screen.blit(img, (x, y))


def main_menu():
    while True:
        screen.fill(WHITE)

        draw_text("DINO JUMP", 310, 80)
        draw_text("1 - Play Easy Game", 280, 160, big=False)
        draw_text("2 - Play Hard Game", 280, 200, big=False)
        draw_text("3 - Credits", 280, 240, big=False)
        draw_text("ESC - Quit", 280, 280, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop("easy")
                elif event.key == pygame.K_2:
                    game_loop("hard")
                elif event.key == pygame.K_3:
                    credits()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


def credits():
    while True:
        screen.fill(WHITE)

        draw_text("Credits", 340, 100)
        draw_text("Created by Grade 12 Computer Programming Students", 180, 180, big=False)
        draw_text("Press BACKSPACE to return", 260, 260, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return


def game_loop(mode):
    dino_x = 100
    dino_y = GROUND_Y - 50
    dino_width = 40
    dino_height = 50

    velocity_y = 0
    gravity = 1
    jump_strength = -18
    on_ground = True

    obstacle_width = 30
    obstacle_height = 50
    obstacle_x = WIDTH
    obstacle_y = GROUND_Y - obstacle_height
    obstacle_speed = 6

    score = 0
    running = True
    game_over = False

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground and not game_over:
                    velocity_y = jump_strength
                    on_ground = False

                if event.key == pygame.K_r and game_over:
                    return game_loop(mode)

                if event.key == pygame.K_BACKSPACE:
                    return

        if not game_over:
            # Dino physics
            dino_y += velocity_y
            velocity_y += gravity

            if dino_y >= GROUND_Y - dino_height:
                dino_y = GROUND_Y - dino_height
                velocity_y = 0
                on_ground = True

            # Obstacle movement
            obstacle_x -= obstacle_speed

            if obstacle_x < -obstacle_width:
                obstacle_x = WIDTH + random.randint(100, 400)
                score += 1

            # Collision rectangles
            dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

            if dino_rect.colliderect(obstacle_rect):
                game_over = True

        # Draw ground
        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 3)

        # Draw dino
        pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))

        # Draw obstacle
        pygame.draw.rect(screen, GRAY, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        draw_text("Score: " + str(score), 20, 20, big=False)
        draw_text("Mode: " + mode, 20, 50, big=False)

        if game_over:
            draw_text("GAME OVER", 310, 140)
            draw_text("Press R to restart", 300, 200, big=False)
            draw_text("Press BACKSPACE for menu", 270, 240, big=False)

        pygame.display.update()


main_menu()