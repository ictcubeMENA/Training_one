def validSolution(board):
    lst = [1,2,3,4,5,6,7,8,9]
    lst1 = []
    res = []
    for b in board:
        res.append(sorted(b) == lst)
    for i in range(9):
        for n in range(9):
            lst1.append(board[n][i])
        res.append(sorted(lst1) == lst)
        lst1 = []
    for n1 in range(0,9,3):
        for i1 in range(0,9):
            lst1.append(board[i1][n1:n1+3])
            if len(lst1) == 3:
                lst1 = [j for c in lst1 for j in c]
                res.append(sorted(lst1) == lst)
                lst1 = []
    return set(res) == {True}


def validSolutionB(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows

def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
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
    check = range(1,10)
    return sorted(lst) == check