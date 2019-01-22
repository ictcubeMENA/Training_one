import numpy as np


def done_or_not(board):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        x = sorted(board[i])
        if x != lst:
            return 'Try again!'

    w = [*zip(*board)]
    for i in range(9):
        x = sorted(w[i])
        if x != lst:
            return 'Try again!'

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            m = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            l = sorted(m)
            if l != lst:
                return 'Try again!'

    return 'Finished!'


import numpy as np


def done_or_not2(aboard):  # board[i][j]
    board = np.array(aboard)

    rows = [board[i, :] for i in range(9)]
    cols = [board[:, j] for j in range(9)]
    sqrs = [board[i:i + 3, j:j + 3].flatten() for i in [0, 3, 6] for j in [0, 3, 6]]

    for view in np.vstack((rows, cols, sqrs)):
        if len(np.unique(view)) != 9:
            return 'Try again!'

    return 'Finished!'
