def validSolution(board):
    temp = []
    for row in board:

        for i in range(1, 10):
            if i not in row:
                return False

    for column in range(0, 9):
        temp = []
        for row in board:
            temp.append(row[column])

        for i in range(1, 10):
            if i not in temp:
                return False

    j = 0
    while (j <= 2):
        temp = []
        for row in range(3 * j, 3 * j + 3):
            k = 0
            for column in range(3 * j, 3 * j + 3):
                temp.append(board[row][column])

        for i in range(1, 10):
            if temp.count(i) != 1:
                return False
        j += 1

    return True


correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def validSolution1(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return False

    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return False

    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i * 3:(i + 1) * 3]:
                region += line[j * 3:(j + 1) * 3]

            if sorted(region) != correct:
                return False

    # if everything correct
    return True
