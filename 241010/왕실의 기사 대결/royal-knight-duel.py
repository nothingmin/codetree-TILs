def solve():
    l, n, q = list(map(int, input().split()))
    chess = []
    for _ in range(l):
        chess.append(list(map(int, input().split())))
    knights = []
    for _ in range(n):
        r, c, h, w, k = list(map(int, input().split()))
        knights.append([r - 1, c - 1, h, w, k])
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
            knights[x] = [r - 1, c, h, w, k]
        if d == 3:
            r, c, h, w, k = knights[x]
            knights[x] = [r, c + 1, h, w, k]

    def push(new_map, r, c, count, d, pushed):
        if d == 0:
            for i in range(count):
                if not (0 <= r - 1 < l and 0 <= c + i < l):
                    return
                if new_map[r - 1][c + i] == n:
                    return
                if new_map[r - 1][c + i] != -1:
                    pushed.append(new_map[r - 1][c + i])
                    push(new_map, r - 1, c, count, d, pushed)
                    break
            for i in range(count):
                new_map[r - 1][c + i] = new_map[r][c + i]
                new_map[r][c + i] = -1
        elif d == 1:
            for i in range(count):
                if not (0 <= r + i < l and 0 <= c + 1 < l):
                    return
                if new_map[r + i][c + 1] == n:
                    return
                if new_map[r + i][c + 1] != -1:
                    pushed.append(new_map[r + i][c + 1])
                    push(new_map, r, c + 1, count, d, pushed)
                    break
            for i in range(count):
                new_map[r + i][c + 1] = new_map[r + i][c]
                new_map[r + i][c] = -1
        elif d == 2:
            for i in range(count):
                if not (0 <= r + 1 < l and 0 <= c + i < l):
                    return
                if new_map[r + 1][c + i] == n:
                    return
                if new_map[r + 1][c + i] != -1:
                    pushed.append(new_map[r + 1][c + i])
                    push(new_map, r + 1, c, count, d, pushed)
                    break
            for i in range(count):
                new_map[r + 1][c + i] = new_map[r][c + i]
                new_map[r][c + i] = -1
        else:
            for i in range(count):
                if not (0 <= r + i < l and 0 <= c - 1 < l):
                    return
                if new_map[r + i][c - 1] == n:
                    return
                if new_map[r + i][c - 1] != -1:
                    pushed.append(new_map[r + i][c - 1])
                    push(new_map, r, c - 1, count, d, pushed)
                    break
            for i in range(count):
                new_map[r + i][c - 1] = new_map[r + i][c]
                new_map[r + i][c] = -1

    def move(x, d):
        r, c, h, w, k = knights[x]
        new_map = []
        for line in maps:
            new_map.append(line[:])
        pushed = []
        if d == 0:
            push(new_map, r, c, w, d, pushed)
        elif d == 1:
            push(new_map, r, c, h, d, pushed)
        elif d == 2:
            push(new_map, r + h - 1, c, w, d, pushed)
        else:
            push(new_map, r, c + w - 1, h, d, pushed)

        return pushed

    def calculate_damage(pushed):
        damage = 0
        for idx in pushed:
            r, c, h, w, k = knights[idx]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    if chess[i][j] == 1:
                        k-=1
                        damage+=1
            knights[idx] = [r, c, h, w, k]
        return damage
    total_damage = 0
    for _ in range(q):
        x, d = list(map(int, input().split()))
        x = x - 1
        pushed = move(x, d)
        if len(pushed) == 0:
            continue
        update_knigth_pos(x, d)
        for idx in pushed:
            update_knigth_pos(idx, d)
        total_damage += calculate_damage(pushed)
    print(total_damage)


solve()