ROWS = 6
COLS = 7

# a one line code to make the matrix
#board = [['-' for c in range(COLS)] for r in range(ROWS)]
board = []
for i in range(ROWS):
    row = []
    for j in range(COLS):
        row.append("-")
    board.append(row)

current_player = "X"


def print_board():
    for row in board:
        print(*row)
    print("0 1 2 3 4 5 6")


def drop_piece(col, player):
    # Start from the bottom row and go upward
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == "-":
            board[row][col] = player
            return True

    return False


def check_win(player):
    # TODO: Check horizontal win

    # TODO: Check vertical win

    # TODO: Check diagonal win

    return False


running = True

while running:
    print_board()
    print("Player", current_player, "turn")

    col = int(input("Choose a column 0-6: "))

    if col < 0 or col >= COLS:
        print("Invalid column!")
        continue

    success = drop_piece(col, current_player)

    if not success:
        print("That column is full!")
        continue

    if check_win(current_player):
        print_board()
        print("Player", current_player, "wins!")
        running = False
    else:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

