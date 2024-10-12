n, m, k = list(map(int, input().split()))

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

attacked = [[0 for _ in range(m)] for _ in range(n)]


def get_weakest():
    mini = 1e9
    minis = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                continue
            if maps[i][j] < mini:
                mini = maps[i][j]
                minis = [[i, j]]
            elif maps[i][j] == mini:
                minis.append([i, j])
    maxi = -1
    maxis = []
    for i, j in minis:
        if attacked[i][j] > maxi:
            maxi = attacked[i][j]
            maxis = [[i, j]]
        elif attacked[i][j] == maxi:
            maxis.append([i, j])

    sumi = -1
    sumis = []
    for i, j in maxis:
        if i + j > sumi:
            sumi = i + j
            sumis = [[i, j]]
        elif i + j == sumi:
            sumis.append([i, j])

    def sort_by_column(a):
        return -a[1]

    sumis.sort(key=sort_by_column)
    if len(sumis) == 0:
        return [-1, -1]
    return sumis[0]


def get_strongest():
    maxi = -1
    maxis = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                continue
            if maps[i][j] > maxi:
                maxi = maps[i][j]
                maxis = [[i, j]]
            elif maps[i][j] == maxi:
                maxis.append([i, j])
    mini = 1e9
    minis = []
    for i, j in maxis:
        if attacked[i][j] < mini:
            mini = attacked[i][j]
            minis = [[i, j]]
        elif attacked[i][j] == mini:
            minis.append([i, j])
    sumi = 1e9
    sumis = []
    for i, j in minis:
        if i + j < sumi:
            sumi = i + j
            sumis = [[i, j]]
        elif i + j == sumi:
            sumis.append([i, j])

    def sort_by_column(a):
        return a[1]
    if len(sumis)==0:
        return [-1,-1]
    sumis.sort(key=sort_by_column)
    return sumis[0]


from collections import deque


def lazor(x, y, a, b):
    result = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[x][y] = True
    dq = deque()
    dq.append((0, x, y, []))
    mini = 1e9
    while dq:
        dist, c, d, routes = dq.popleft()
        if dist > mini:
            continue
        if dist <= mini and c == a and b == d:
            result.append(routes)
            mini = dist
            continue
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ex, ey = (c + dx) % n, (d + dy) % m
            if ex == 1 and ey == 2:
                pass
            if maps[ex][ey] == 0:
                continue
            if visited[ex][ey] == True:
                continue
            visited[ex][ey] = True
            tmp = []
            for line in routes:
                tmp.append(line[:])
            tmp.append([ex, ey])
            dq.append((dist + 1, ex, ey, tmp))
    if len(result) == 0:
        return []
    return result[0]


def cannon(x, y, a, b):
    route = []
    for da in [-1, 0, 1]:
        for db in [-1, 0, 1]:
            ea, eb = (a + da) % n, (b + db) % m
            if maps[ea][eb] == 0:
                continue
            if ea == x and eb == y:
                continue
            if ea == a and eb == b:
                continue
            route.append([ea, eb])
    route.append([a, b])
    return route


for l in range(k):
    x, y = get_weakest()
    if (x == -1 and y == -1) or maps[x][y] == 0:
        continue
    a, b = get_strongest()
    if a == -1 and b == -1 or maps[x][y] == 0:
        continue
    if x== a and b==y:
        continue
    maps[x][y] += n + m
    attacked[x][y] = l+1
    route = lazor(x, y, a, b)
    if len(route) == 0:
        route = cannon(x, y, a, b)
    route.pop()
    for c, d in route:
        maps[c][d] -= maps[x][y] // 2
        if maps[c][d] <= 0:
            maps[c][d] = 0
    maps[a][b] -= maps[x][y]
    if maps[a][b] <= 0:
        maps[a][b] = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                continue
            if i == a and j == b:
                continue
            if i == x and j == y:
                continue
            flag = False
            for c, d in route:
                if i == c and j == d:
                    flag = True
            if flag is True:
                continue
            maps[i][j] += 1
    for line in maps:
        print(line)
    print(" ")
q,w = get_strongest()
print(maps[q][w])