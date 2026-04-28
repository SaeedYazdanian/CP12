board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
current_player = "X"
def print_board():
    for row in board:
        print(*row)
def check_win(player):
    if board[0][0] == board[0][1] == board[0][2] == player:
        return True
    # TODO: Check rows
    # TODO: Check columns
    # TODO: Check diagonals
    return False
running = True
while running:
    print_board()
    print("Player", current_player, "turn")
    row = int(input("Enter row 0, 1, or 2: "))
    col = int(input("Enter column 0, 1, or 2: "))
    # TODO: Fix this problem:
    # The player should NOT be allowed to play on a cell that is already taken.
    board[row][col] = current_player
    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        running = False
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"