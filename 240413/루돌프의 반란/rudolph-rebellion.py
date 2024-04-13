DEER = 0
n, m, p, c, d = map(int, input().split())
maps = [[-1 for i in range(n + 1)] for _ in range(n + 1)]
deer = list(map(int, input().split()))
maps[deer[0]][deer[1]] = DEER
santas = [[0, 999, 999]]
for i in range(p):
    santas.append(list(map(int, input().split())))

santas.sort(key=lambda x: x[0])
for i in range(1, len(santas)):
    maps[santas[i][1]][santas[i][2]] = santas[i][0]
scores = [0 for _ in range(p + 1)]
stunned = [-1 for _ in range(p + 1)]


def distance(deer, santa):
    return (deer[0] - santa[1]) ** 2 + (deer[1] - santa[2]) ** 2


def sort_santa_by_distance(deer, santas):
    copied = [[] for _ in range(len(santas))]
    for i in range(len(santas)):
        for j in range(3):
            copied[i].append(santas[i][j])
    copied.sort(key=lambda x: (distance(deer, x), -x[1], -x[2]))
    return copied


def move_to_nearest_santa(deer, santas):
    sorted_santas = sort_santa_by_distance(deer, santas)
    nearest_santa = sorted_santas[0]
    if deer[0] < nearest_santa[1]:
        dx = 1
    elif deer[0] > nearest_santa[1]:
        dx = -1
    else:
        dx = 0
    if deer[1] < nearest_santa[2]:
        dy = 1
    elif deer[1] > nearest_santa[2]:
        dy = -1
    else:
        dy = 0
    ex = deer[0] + dx
    ey = deer[1] + dy
    return ex, ey, dx, dy


def out_santa(santa):
    santas[santa[0]] = [santa[0], 999, 999]


def is_out(santa):
    if not (0 < santa[1] <= n and 0 < santa[2] <= n):
        return True
    return False


def deer_crash_santa(deer, dx, dy, turn):
    santa = [maps[deer[0] + dx][deer[1] + dy], deer[0] + dx, deer[1] + dy]
    maps[santa[1]][santa[2]] = -1
    santa_crashed(santa, dx, dy, turn, c)


def santa_crashed(santa, dx, dy, turn, score):
    santa_idx = santa[0]
    scores[santa_idx] += score
    stunned[santa_idx] = turn + 1
    santa_moved = [santa[0], santa[1] + score * dx, santa[2] + score * dy]
    interaction(santa_moved, dx, dy)


def interaction(santa, dx, dy):
    x, y, idx = santa[1], santa[2], santa[0]
    while idx != -1:
        if is_out([idx, x, y]):
            out_santa([idx, x, y])
            break
        tmp = maps[x][y]
        set_santa_pos(x, y, [idx, x, y])
        x = x + dx
        y = y + dy
        idx = tmp


def move_to_deer(deer, santa):
    santa_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    idx = -1
    min_dis = distance(deer, santa)
    for i in range(4):
        ex = santa[1] + santa_directions[i][0]
        ey = santa[2] + santa_directions[i][1]
        if not (0 < ex <= n and 0 < ey <= n):
            continue
        if maps[ex][ey] >= 1:
            continue
        if min_dis > distance(deer, [0, ex, ey]):
            idx = i
            min_dis = min(min_dis, distance(deer, [0, ex, ey]))
    if idx != -1:
        ex = santa[1] + santa_directions[idx][0]
        ey = santa[2] + santa_directions[idx][1]
        return ex, ey, santa_directions[idx][0], santa_directions[idx][1]
    else:
        return santa[1], santa[2], 0, 0


def set_deer_pos(ex, ey):
    global deer
    maps[deer[0]][deer[1]] = -1
    deer = [ex, ey]
    maps[ex][ey] = DEER


def move_deer(turn):
    ex, ey, dx, dy = move_to_nearest_santa(deer, santas)
    if maps[ex][ey] != -1:
        deer_crash_santa(deer, dx, dy, turn)
    set_deer_pos(ex, ey)


def move_santa(santa, turn):
    if is_out(santa) or is_stunned(santa[0], turn):
        return
    ex, ey, dx, dy = move_to_deer(deer, santa)
    if not is_moved(dx, dy):
        return
    maps[santa[1]][santa[2]] = -1
    if maps[ex][ey] == DEER:
        santa_crashed([santa[0], ex, ey], -dx, -dy, turn, d)
    else:
        set_santa_pos(ex, ey, santa)


def set_santa_pos(ex, ey, santa):
    santas[santa[0]] = [santa[0], ex, ey]
    maps[ex][ey] = santa[0]


def is_moved(dx, dy):
    return dx != 0 or dy != 0


def is_stunned(santa_idx, turn):
    return stunned[santa_idx] >= turn


for turn in range(m):
    move_deer(turn)
    for santa in santas:
        move_santa(santa, turn)

    for santa in santas:
        if is_out(santa):
            continue
        scores[santa[0]] += 1
for i in range(1,len(scores)):
    print(scores[i],end=" ")