

"""
1.  Write an algorithm that creates a chess board array with zeros and ones.
"""

def generate_chess_board():
    """
    This function creates a chessboard in the form of a two-dimensional array with zeros and ones.

    :return: board
    """

    board = []
    value = 0
    for _ in range(8):
        line = []
        for i in range(8):
            line.append(value)
            if i != 7:
                value = abs(value - 1)

        board.append(line)

    return board

def print_chess_board(board):
    """
    This function prints a chessboard in the terminal.

    :param board: two-dimensional array
    :return: None
    """
    vertical_number = 8
    indents = '  '
    for line in board:
        print(vertical_number, end='| ')
        for value in line:
            print(value, end=indents)
        vertical_number -= 1
        print('')

    print('   ', end='')
    start_character_ascii_value = 97
    for i in range(8):
        letter = chr(start_character_ascii_value+i)
        print(letter, end=indents)

if __name__ == '__main__':

    chess_board = generate_chess_board()
    print_chess_board(chess_board)
