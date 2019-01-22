import numpy as np


def validSolution(board):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        x = sorted(board[i])
        if x != lst:
            return False

    w = [*zip(*board)]
    for i in range(9):
        x = sorted(w[i])
        if x != lst:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            m = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            l = sorted(m)
            if l != lst:
                return False

    return True


def validSolution2(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows


def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
            if not check_one_to_nine(nums):
                return False
    return True


def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True


def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True


def check_one_to_nine(lst):
    check = range(1, 10)
    return sorted(lst) == check
