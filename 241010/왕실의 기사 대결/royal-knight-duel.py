def solve():
    l, n, q = list(map(int, input().split()))
    chess = []
    for _ in range(l):
        chess.append(list(map(int, input().split())))
    knights = []
    health = []
    for _ in range(n):
        r, c, h, w, k = list(map(int, input().split()))
        knights.append([r - 1, c - 1, h, w, k])
        health.append(k)
    maps = [[-1 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if chess[i][j] == 2:
                maps[i][j] = n

    for idx, (r, c, h, w, k) in enumerate(knights):
        for i in range(r, r + h):
            for j in range(c, c + w):
                maps[i][j] = idx

    def update_knigth_pos(x, d):
        if d == 0:
            r, c, h, w, k = knights[x]
            knights[x] = [r - 1, c, h, w, k]
        if d == 1:
            r, c, h, w, k = knights[x]
            knights[x] = [r, c + 1, h, w, k]
        if d == 2:
            r, c, h, w, k = knights[x]
            knights[x] = [r + 1, c, h, w, k]
        if d == 3:
            r, c, h, w, k = knights[x]
            knights[x] = [r, c - 1, h, w, k]

    def push(new_map, idx, d, pushed):
        r, c, h, w, k = knights[idx]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        dx, dy = directions[d]
        for i in range(r, r + h):
            for j in range(c, c + w):
                ex, ey = i + dx, j + dy
                if not (0 <= ex < l and 0 <= ey < l):
                    return False
                if new_map[ex][ey] == n:
                    return False
                if new_map[ex][ey] == idx:
                    continue
                if new_map[ex][ey] != -1:
                    is_pushed = push(new_map, new_map[ex][ey], d, pushed)
                    if is_pushed is False:
                        return False
        if d == 0:
            for i in range(r, r + h):
                for j in range(c, c + w):
                    ex, ey = i + dx, j + dy
                    new_map[ex][ey] = new_map[i][j]
                    new_map[i][j] = -1
        elif d == 1:
            for j in range(c + w - 1, c - 1, -1):
                for i in range(r, r + h):
                    ex, ey = i + dx, j + dy
                    new_map[ex][ey] = new_map[i][j]
                    new_map[i][j] = -1
        elif d == 2:
            for i in range(r + h - 1, r - 1, -1):
                for j in range(c, c + w):
                    ex, ey = i + dx, j + dy
                    new_map[ex][ey] = new_map[i][j]
                    new_map[i][j] = -1
        else:
            for j in range(c, c + w):
                for i in range(r, r + h):
                    ex, ey = i + dx, j + dy
                    new_map[ex][ey] = new_map[i][j]
                    new_map[i][j] = -1
        pushed[idx] = True
        return True

    def move(new_map, x, d):
        pushed = {}
        is_pushed = push(new_map, x, d, pushed)
        if is_pushed is False:
            return {}
        for key in pushed.keys():
            update_knigth_pos(key, d)
        return pushed

    def calculate_damage(pushed):
        for idx in pushed.keys():
            r, c, h, w, k = knights[idx]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    if chess[i][j] == 1:
                        health[idx] -= 1
            if health[idx] <= 0:
                for i in range(r, r + h):
                    for j in range(c, c + w):
                        maps[i][j] = -1

    total_damage = 0

    for _ in range(q):
        x, d = list(map(int, input().split()))
        x = x - 1
        if health[x] <= 0:
            continue
        new_map = []
        for line in maps:
            new_map.append(line[:])
        pushed = move(new_map, x, d)
        if len(pushed) == 0:
            continue
        maps = new_map
        pushed.pop(x)
        calculate_damage(pushed)

    for i in range(n):
        if health[i] <= 0:
            continue
        total_damage += knights[i][4] - health[i]
    print(total_damage)


solve()