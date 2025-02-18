def show_gameboard(board):
    """
    Displays the current state of the game board.

    This function takes a 2D list representing the game board and
    displays it in a visually formatted way for the players. Rows of
    the board are delimited by horizontal lines, and cells within
    each row are separated by vertical bars.

    :param board: A 2D list where each sublist represents a row of
        the game board, and each element within the sublist is a
        string representing the state of a cell (e.g., "X", "O", or " ").
    :return: None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def game_won(board, player):
    """
    Determines whether the specified player has won the game on the given board.

    This function checks if the player has achieved a winning condition, i.e., having
    all their symbols in any row, column, or diagonal of a 3x3 game board.

    :param board: A 2-dimensional list representing the game board, where each element
        is the symbol of a player or an empty string if the cell is unoccupied. The
        board is assumed to be a 3x3 grid.
    :param player: A string representing the player's symbol whose victory is to be checked.
    :return: A boolean value indicating whether the specified player has won the game
        (True) or not (False).
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def board_full(b):
    """
    Checks whether the game board is full by verifying if there are no empty spaces
    remaining in any cell of the board.

    This function iterates through each cell in the 2D game board and determines
    if all cells are occupied (i.e., not containing empty spaces represented by
    " "). If all cells are occupied, the board is considered full.

    :param b: A 2D list representing the game board where rows and columns contain
              strings denoting the cell status (" " for empty, other values for
              occupied).
    :type b: list[list[str]]
    :return: True if the board is full (no empty spaces), False otherwise.
    :rtype: bool
    """
    return all(c != " " for r in b for c in r)


# noinspection PyBroadException
def app():
    gameboard = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    show_gameboard(gameboard)
    for turn in range(9):
        current_player = players[turn % 2]
        game_loop(current_player, gameboard)
        show_gameboard(gameboard)
        if game_won(gameboard, current_player):
            print(f"P {current_player} wins!")
            return
        if board_full(gameboard):
            print("Draw!")
            return
    print("Draw!")


def game_loop(current_player, gameboard):
    """
    Handles the main logic for the player's move in the game. The function ensures that
    the player selects a valid move on the provided gameboard by validating input and
    checking if the desired position is available. If the conditions are met, the player's
    symbol is placed on the gameboard at the specified coordinates.

    :raises ValueError: Raised if the input coordinates are not integers or fall outside the
        specified range (0-2).
    :raises IndexError: Raised if the input coordinates are outside the boundaries of the
        gameboard.

    :param current_player: The player making the current move, represented as a string,
        usually 'X' or 'O'.
    :type current_player: str

    :param gameboard: A 2D list representing the current state of the gameboard. Each element
        can either be a space (" ") if unoccupied or contain a player's symbol
        ('X'/'O'). Must be mutable and of size 3x3.
    :type gameboard: list[list[str]]

    :return: None
    """
    while 1:
        try:
            x_coord, y_coord = map(int, input(f"Player {current_player}, enter row col (between 0-2): ").split())
            if gameboard[x_coord][y_coord] == " ":
                gameboard[x_coord][y_coord] = current_player
                break
            else:
                print("Nope, that space is taken. Try again.")
        except:
            print("Invalid grid, enter integer between 0-2 pls.")


app()
