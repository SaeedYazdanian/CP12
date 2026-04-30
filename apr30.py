import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont(None, 100)

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

current_player = "X"

def draw_board():
    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 5)

    for row in range(3):
        for col in range(3):
            if board[row][col] != "-":
                text = font.render(board[row][col], True, (0, 0, 0))
                screen.blit(text, (col * 200 + 70, row * 200 + 55))

def check_win(player):
    if board[0][0] == board[0][1] == board[0][2] == player:
        return True
    # TODO: Check rows
    # TODO: Check columns
    # TODO: Check diagonals
    return False

running = True
while running:
    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Player", current_player, "turn")

            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200

            # TODO: Fix this problem:
            # The player should NOT be allowed to play on a cell that is already taken.
            board[row][col] = current_player

            if check_win(current_player):
                print("Player", current_player, "wins!")
                running = False

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

    pygame.display.update()

pygame.quit()