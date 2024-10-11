n, m, santa_length, deer_power, santa_power = list(map(int, input().split()))
x, y = list(map(int, input().split()))
deer = [x - 1, y - 1]
santas = [[] for _ in range(santa_length)]
stuns = [0 for _ in range(santa_length)]
is_out = [False for _ in range(santa_length)]
maps = [[-1 for _ in range(n)] for _ in range(n)]
scores = [0 for _ in range(santa_length)]
DEER = santa_length
maps[deer[0]][deer[1]] = DEER
for _ in range(santa_length):
    p, x, y = list(map(int, input().split()))
    santas[p - 1] = [x - 1, y - 1]
    maps[x - 1][y - 1] = p - 1


def distance(x, y, a, b):
    return (x - a) ** 2 + (y - b) ** 2


def get_near_santa_idx():
    x, y = deer[0], deer[1]
    mini = 1e9
    idx = -1
    for i, santa in enumerate(santas):
        if is_out[i] is True:
            continue
        dist = distance(x, y, santa[0], santa[1])
        if mini > dist:
            mini = dist
            idx = i
        elif mini == dist:
            if santas[i][0] > santas[idx][0]:
                mini = dist
                idx = i
            elif santas[i][0] == santas[idx][0]:
                if santas[i][1] > santas[idx][1]:
                    mini = dist
                    idx = i
    return idx


def move_to_santa(idx):
    dx, dy = 0, 0
    x, y = deer
    a, b = santas[idx]
    if a > x:
        dx = 1
    elif a < x:
        dx = -1
    if b > y:
        dy = 1
    elif b < y:
        dy = -1
    return dx, dy


def deer_crash(dx, dy):
    global deer
    x, y = deer
    ex, ey = x + dx, y + dy
    if maps[ex][ey] >= 0:
        return True
    maps[x][y] = -1
    maps[ex][ey] = DEER
    deer = [ex, ey]
    return False


def push(idx, dx, dy):
    a, b = santas[idx]
    ex, ey = a + dx, b + dy
    if not (0 <= ex < n and 0 <= ey < n):
        is_out[idx] = True
        maps[a][b] = -1
        return
    if maps[ex][ey] >= 0:
        push(maps[ex][ey], dx, dy)
    if maps[ex][ey] == -1:
        santas[idx] = [ex, ey]
        maps[ex][ey] = idx
        maps[a][b] = -1
        return


def deer_crashed(idx, dx, dy):
    global deer
    a, b = santas[idx]
    x, y = deer
    ea, eb = a + dx * deer_power, b + dy * deer_power
    maps[a][b] = DEER
    maps[x][y] = -1
    deer = [a, b]
    scores[idx] += deer_power
    if not (0 <= ea < n and 0 <= eb < n):
        is_out[idx] = True
        return
    if maps[ea][eb] >= 0 and maps[ea][eb] != idx:  # 상호작용
        push(maps[ea][eb], dx, dy)
    maps[ea][eb] = idx
    santas[idx] = [ea, eb]
    stuns[idx] = 2


def move_to_deer(idx):
    a, b = santas[idx]
    x, y = deer
    da, db = 0, 0
    if a > x:
        da = -1
    elif a < x:
        da = 1
    if b < y:
        db = 1
    elif b > y:
        db = -1
    if da != 0 and db != 0:
        if not can_move(idx, da, 0):
            return 0, db
        elif not can_move(idx, 0, db):
            return da, 0

        dist1 = distance(x, y, a + da, b)
        dist2 = distance(x, y, a, b + db)
        if dist1 > dist2:
            return 0, db
        elif dist1 < dist2:
            return da, 0
        else:
            if da < 0:
                return da, 0
            elif db > 0:
                return 0, db
            elif da > 0:
                return da, 0
            else:
                return 0, db
    return da, db


def can_move(idx, da, db):
    a, b = santas[idx]
    ea, eb = a + da, b + db
    if not (0 <= ea < n and 0 <= eb < n):
        return False
    if santa_length > maps[ea][eb] >= 0:
        return False
    return True


def santa_crash(idx, dx, dy):
    a, b = santas[idx]
    ea, eb = a + dx, b + dy
    if maps[ea][eb] == DEER:
        return True
    santas[idx] = [ea, eb]
    maps[a][b] = -1
    maps[ea][eb] = idx
    return False


def santa_crashed(idx, dx, dy):
    a, b = santas[idx]
    ea, eb = a - dx * (santa_power - 1), b - dy * (santa_power - 1)
    maps[a][b] = -1
    scores[idx] += santa_power
    if not (0 <= ea < n and 0 <= eb < n):
        is_out[idx] = True
        return
    if maps[ea][eb] >= 0 and maps[ea][eb] != idx:  # 상호작용
        push(maps[ea][eb], -dx, -dy)

    maps[ea][eb] = idx
    santas[idx] = [ea, eb]
    stuns[idx] = 1


for _ in range(m):
    idx = get_near_santa_idx()
    if idx == -1:
        continue
    dx, dy = move_to_santa(idx)
    if deer_crash(dx, dy):
        deer_crashed(idx, dx, dy)
    for i in range(santa_length):
        if is_out[i]:
            continue
        if stuns[i] > 0:
            stuns[i] -= 1
            continue
        da, db = move_to_deer(i)
        if not can_move(i, da, db):
            continue
        if santa_crash(i, da, db) is True:
            santa_crashed(i, da, db)


    for i in range(santa_length):
        if is_out[i]:
            continue
        scores[i] += 1

print(" ".join(map(str, scores)))