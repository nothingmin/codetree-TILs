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

    def push(new_map, r, c, count, d, pushed):
        if d == 0:
            for i in range(count):
                if not (0 <= r - 1 < l and 0 <= c + i < l):
                    return -1
                if new_map[r - 1][c + i] == n:
                    return -1
                if new_map[r - 1][c + i] != -1:
                    is_moved = push(new_map, r - 1, c, count, d, pushed)
                    if is_moved == -1:
                        return -1
                    break
            for i in range(count):
                if new_map[r][c + i] == -1 or new_map[r][c + i] == n:
                    continue
                pushed[new_map[r][c + i]] = True
                new_map[r - 1][c + i] = new_map[r][c + i]
                new_map[r][c + i] = -1
        elif d == 1:
            for i in range(count):
                if not (0 <= r + i < l and 0 <= c + 1 < l):
                    return -1
                if new_map[r + i][c + 1] == n:
                    return -1
                if new_map[r + i][c + 1] != -1:
                    is_moved = push(new_map, r, c + 1, count, d, pushed)
                    if is_moved == -1:
                        return -1
                    break
            for i in range(count):
                if new_map[r + i][c] == -1 or new_map[r + i][c] == n:
                    continue
                pushed[new_map[r + i][c]] = True
                new_map[r + i][c + 1] = new_map[r + i][c]
                new_map[r + i][c] = -1
        elif d == 2:
            for i in range(count):
                if not (0 <= r + 1 < l and 0 <= c + i < l):
                    return -1
                if new_map[r + 1][c + i] == n:
                    return -1
                if new_map[r + 1][c + i] != -1:
                    is_moved = push(new_map, r + 1, c, count, d, pushed)
                    if is_moved == -1:
                        return -1
                    break
            for i in range(count):
                if new_map[r][c + i] == -1 or new_map[r][c + i] == n:
                    continue
                pushed[new_map[r][c + i]] = True
                new_map[r + 1][c + i] = new_map[r][c + i]
                new_map[r][c + i] = -1
        else:
            for i in range(count):
                if not (0 <= r + i < l and 0 <= c - 1 < l):
                    return -1
                if new_map[r + i][c - 1] == n:
                    return -1
                if new_map[r + i][c - 1] != -1:
                    is_moved = push(new_map, r, c - 1, count, d, pushed)
                    if is_moved == -1:
                        return -1
                    break
            for i in range(count):
                if new_map[r][c + i] == -1 or new_map[r + i][c] == n:
                    continue
                pushed[new_map[r + i][c]] = True
                new_map[r + i][c - 1] = new_map[r + i][c]
                new_map[r + i][c] = -1
        return 0

    def move(x, d):
        r, c, h, w, k = knights[x]
        pushed = {}
        if d == 0:
            push(maps, r, c, w, d, pushed)
        elif d == 1:
            push(maps, r, c, h, d, pushed)
        elif d == 2:
            push(maps, r + h - 1, c, w, d, pushed)
        else:
            push(maps, r, c + w - 1, h, d, pushed)
        for key in pushed.keys():
            update_knigth_pos(key, d)
        return pushed

    def calculate_damage(pushed):
        for idx in pushed.keys():
            r, c, h, w, k = knights[idx]
            for i in range(r, r + h):
                for j in range(c, c + w):
                    if chess[i][j] == 1:
                        health[idx]-=1

    total_damage = 0

    for _ in range(q):
        x, d = list(map(int, input().split()))
        x = x - 1

        pushed = move(x, d)

        if len(pushed) == 0:
            continue
 
        pushed.pop(x)
        calculate_damage(pushed)

    for i in range(n):
        if health[i] <=0:
            continue
        total_damage += knights[i][4]- health[i]
    print(total_damage)




solve()