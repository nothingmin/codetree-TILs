n, m, h, k = list(map(int, input().split()))
runners = []
for _ in range(m):
    x, y, d = list(map(int, input().split()))
    if d == 1:
        dx, dy = 0, 1
    else:
        dx, dy = 1, 0
    runners.append([x - 1, y - 1, dx, dy])
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
catcher = [n // 2, n // 2]
boards = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(h):
    x, y = list(map(int, input().split()))
    boards[x - 1][y - 1] = 1
catcher_route = []
nums = []
for i in range(1, n):
    nums.append(i)
    nums.append(i)
nums.append(n - 1)
idx = 0

for num in nums:
    for _ in range(num):
        catcher_route.append(directions[idx])
    idx = (idx + 1) % 4

nums = []
nums.append(n - 1)
for i in range(n - 1, 0, -1):
    nums.append(i)
    nums.append(i)

idx = 2
for num in nums:
    for _ in range(num):
        catcher_route.append(directions[idx])
    idx = (idx - 1) % 4


def distance(x, y):
    return abs(catcher[0] - x) + abs(catcher[1] - y)


def move_runners():
    tmp = []
    for x, y, dx, dy in runners:
        if distance(x, y) > 3:
            tmp.append([x, y, dx, dy])
            continue
        ex, ey = x + dx, y + dy
        if not (0 <= ex < n and 0 <= ey < n):
            dx = -dx
            dy = -dy
            ex, ey = x + dx, y + dy
        if not (ex == catcher[0] and ey == catcher[1]):
            tmp.append([ex, ey, dx, dy])
        else:
            tmp.append([x, y, dx, dy])
    return tmp


def move_catcher(turn):
    dx, dy = catcher_route[turn]
    x, y = catcher
    ex, ey = x + dx, y + dy
    return [ex, ey]


def catch_runners(turn):
    dx, dy = catcher_route[turn]
    a, b = catcher

    tmp = []
    catched = 0
    for idx, (x, y, _, _) in enumerate(runners):
        if boards[x][y] == 1:
            tmp.append(runners[idx])
            continue
        if (x == a and y == b) or (x == a + dx and y == b + dy) or (x == a + 2 * dx and y == b + 2 * dy):
            catched += 1
            continue
        tmp.append(runners[idx])
    return tmp, catched

result = 0
for turn in range(k):
    runners = move_runners()
    catcher = move_catcher(turn % len(catcher_route))
    runners,catched = catch_runners((turn + 1) % len(catcher_route))
    result += catched*(turn+1)
print(result)