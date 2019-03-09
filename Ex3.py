"""
    Exercise 3:
    Tic-Tac-Toe
"""


def check_winner(game):
    """
    Find the winner of a tic-tac-toe game
    :param game: matrix representing tic-tac-toe board.
    :return: winning player of the game (1 or 2), 0 for draw.
    """
    n = len(game[0])  # length of a single row / col
    # check rows
    for row in game:
        if row[:-1] == row[1:]:
            return row[0]

    # check cols
    for i in range(n):
        first_val = game[0][i]
        win = True
        for row in game:
            if row[i] != first_val:
                win = False
                break
        if win:
            return first_val

    # check main diagonal
    first_val = game[0][0]
    win = True
    for i in range(n):
        if game[i][i] != first_val:
            win = False
            break
    if win:
        return first_val

    # check minor diagonal
    first_val = game[0][n - 1]
    win = True
    for i in range(n):
        if game[i][n - i - 1] != first_val:
            win = False
            break
    if win:
        return first_val
    return 0


def main():
    """
    Main program example.
    """
    game = [[1, 1, 0],
            [2, 2, 2],
            [2, 1, 1]]
    pw = check_winner(game)
    if pw == 0:
        print("Game drawn")
    else:
        print("Player", pw, "won")


if __name__ == '__main__':
    main()
