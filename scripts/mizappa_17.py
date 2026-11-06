def new_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def show(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def place(board, row, col, mark):
    if board[row][col] == " ":
        board[row][col] = mark
        return True
    return False


if __name__ == "__main__":
    board = new_board()
    place(board, 0, 0, "X")
    place(board, 1, 1, "O")
    place(board, 0, 2, "X")
    show(board)
