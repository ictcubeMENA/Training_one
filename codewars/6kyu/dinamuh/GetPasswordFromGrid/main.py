dict = {'down': [1, 0], 'downT': [1, 0], 'left': [0, -1], 'leftT': [0, -1], 'right': [0, 1], 'rightT': [0, 1],
        'up': [-1, 0], 'upT': [-1, 0]}


def get_password(grid, directions):
    l = 0
    v = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'x':
                l = r
                v = c
                break
    res = ''
    for direction in directions:
        xr, xc = dict[direction]
        l += xr
        v += xc
        if direction.endswith('T'):
            res += grid[l][v]
    return res


MOVES = {"right": (0, 1), "down": (1, 0), "left": (0, -1), "up": (-1, 0)}


def get_password2(grid, dirs):
    x, y = next((x, y) for x, r in enumerate(grid) for y, c in enumerate(r) if c == 'x')
    pwd = []
    for d in dirs:
        dx, dy = MOVES[d.strip('T')]
        x, y = x + dx, y + dy
        if d.endswith('T'): pwd.append(grid[x][y])
    return ''.join(pwd)
