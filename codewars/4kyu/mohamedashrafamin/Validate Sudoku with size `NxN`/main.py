import math


class Sudoku(object):
    count = 0
    t = False
    data = None
    col = []
    tem = []
    tem1 = []
    mat = []

    def __init__(self, data):
        self.data = data
        self.count = 0
        self.t = False
        self.col = []
        self.tem = []
        self.tem1 = []
        self.mat = []
        for i in range(len(data)):
            for y in range(len(data[i])):
                try:
                    if data[i][y] <= 0 or data[i][y] > len(data[i]) or not str(data[i][y]).isdigit():
                        self.t = True
                        break
                    else:
                        self.tem.append(data[y][i])
                except:
                    self.t = True
                    break
            if self.t:
                break
            self.col.append(self.tem)
            self.tem = []
        if math.sqrt(len(self.data)) % 1 == 0 and len(data) > 1 and not self.t:
            x = int(math.sqrt(len(self.data)))
            for i in range(0, len(data), x):
                for j in range(len(data)):
                    self.tem1.append(data[j][i:i + x])
            for y in range(0, len(self.tem1), x):
                self.mat.append(sum(self.tem1[y:y+x], []))

    def is_valid(self):
        if math.sqrt(len(self.data)) % 1 == 0 and not self.t and len(self.data) > 1:
            for i in range(len(self.data)):
                if len(set(self.col[i])) != len(self.data[i]) or len(set(self.mat[i])) != len(self.data[i]):
                    return False
                else:
                    return True
        elif len(self.data) == 1 and not self.t:
            return True
        return False


