from collections import deque

k, m = list(map(int, input().split()))
maps = []

for _ in range(5):
    maps.append(list(map(int, input().split())))
nums = list(map(int, input().split()))


def rotate(i, j):
    tmp0, tmp1 = maps[i - 1][j - 1], maps[i][j - 1]
    maps[i - 1][j - 1], maps[i][j - 1] = maps[i + 1][j - 1], maps[i + 1][j]
    maps[i + 1][j - 1], maps[i + 1][j] = maps[i + 1][j + 1], maps[i][j + 1]
    maps[i + 1][j + 1], maps[i][j + 1] = maps[i - 1][j + 1], maps[i - 1][j]
    maps[i - 1][j + 1], maps[i - 1][j] = tmp0, tmp1


def calculate_value(maps):
    new_map = []
    for i in range(5):
        new_map.append(maps[i][:])
    dq = deque()
    visited = [[False for _ in range(5)] for _ in range(5)]
    value = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] is True:
                continue
            dq.append((i, j))
            visited[i][j] = True
            same = 0
            blanks= [(i,j)]
            while dq:
                x, y = dq.popleft()
                same += 1
                for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ex, ey = x + dx, y + dy
                    if not (0 <= ex < 5 and 0 <= ey < 5):
                        continue
                    if visited[ex][ey] is True:
                        continue
                    if maps[ex][ey] == maps[x][y]:
                        visited[ex][ey] = True
                        blanks.append((ex,ey))
                        dq.append((ex, ey))
            if same >= 3:
                for x,y in blanks:
                    new_map[x][y] = 0
                value += same
    return new_map, value


def get_maximal(value, l, j, i):
    tmp = [value, l, j, i]
    if maxi[0] > value:
        return maxi
    elif maxi[0] < value:
        return tmp
    if maxi[1] < l:
        return maxi
    elif maxi[1] > l:
        return tmp
    if maxi[2] < j:
        return maxi
    elif maxi[2] > j:
        return tmp
    if maxi[3] < k:
        return maxi
    elif maxi[3] > k:
        return tmp


def fill_blank(new_map):
    global idx
    for j in range(5):
        for i in reversed(range(5)):
            if new_map[i][j] == 0:
                new_map[i][j] = nums[idx]
                idx+=1

idx = 0
for _ in range(k):
    maxi = [-1, 999, 999, 999]
    result = 0
    for i in range(1,4):
        for j in range(1,4):
            for l in range(4):
                rotate(i,j)
                if l == 3:
                    continue
                new_map, value = calculate_value(maps)
                maxi = get_maximal(value, l, j, i)  # maxi =[value,l,j,i]
    if maxi[0] == 0:
        break
    l,j,i = maxi[1],maxi[2],maxi[3]
    for _ in range(l+1):
        rotate(i,j)
    new_map, value = calculate_value(maps)
    sumi = value
    while value !=0:
        fill_blank(new_map)
        new_map, value = calculate_value(new_map)
        sumi += value
    result += sumi
    maps= new_map
    print(result)