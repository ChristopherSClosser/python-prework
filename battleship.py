# Battleship

# an import for random numbers
from random import randint

board = []

for x in range(5):
    board.append(["o"] * 5)


def print_board(board):
    for row in board:
        print " ".join(row)


print_board(board)
board_size = (len(board) - 1)


def random_row(board):
    return randint(0, board_size)


def random_col(board):
    return randint(0, len(board[0]) - 1)


# where the ship lives
ship_row = random_row(board)
ship_col = random_col(board)

turns = 4

for turn in range(turns):
    # four turns
    try:
        # validating a number was entered
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
    except ValueError:
        print "That wasn't a number!"
        # I believe continue forfeights the turn
        continue

    if turn == (turns - 1):
        print 'You lose and I sink you!'
        break

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break

    else:
        if guess_row not in range(board_size) or \
           guess_col not in range(board_size):
            # validates if on the board
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "x"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            # place an x where miss
            board[guess_row][guess_col] = "x"

        print 'Turn', turn + 1
        print_board(board)
