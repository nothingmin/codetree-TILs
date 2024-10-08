from collections import deque
def solve():
    # 0,1,2 행에 있으면 map_out

    def check_map_out(maps):

        for i in range(3):
            tmp = max(maps[i])
            if tmp != 0:
                return True
        return False

    def clear_map(c, r):
        cleared_map = [[0 for _ in range(c)] for _ in range(r + 3)]
        return cleared_map

    def mark_golem(maps, x, y):
        maps[x][y] = 3
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ex = x + dx
            ey = y + dy
            maps[ex][ey] = 1
        return maps

    def clear_golem(maps, x, y):
        maps[x][y] = 0
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            ex = x + dx
            ey = y + dy
            maps[ex][ey] = 0
        return maps

    def init_golem(maps, c):
        return mark_golem(maps, 1, c)

    # 0이면 남쪽, 1이면 서쪽, 2면 동쪽, 3이면 못움직임
    def can_move(maps, x, y):
        for dx, dy in [[2, 0], [1, 1], [1, -1]]:
            ex = x + dx
            ey = y + dy
            if not (0 <= ex < R + 3 and 0 <= ey < C):
                break
            if maps[ex][ey] != 0:
                break
            if dx == 1 and dy == -1:
                return 0
        for dx, dy in [[0, -2], [-1, -1], [1, -1], [1, -2], [2, -1]]:
            ex = x + dx
            ey = y + dy
            if not (0 <= ex < R + 3 and 0 <= ey < C):
                break
            if maps[ex][ey] != 0:
                break
            if dx == 2 and dy == -1:
                return 1
        for dx, dy in [[0, 2], [-1, 1], [1, 1], [1, 2], [2, 1]]:
            ex = x + dx
            ey = y + dy
            if not (0 <= ex < R + 3 and 0 <= ey < C):
                break
            if maps[ex][ey] != 0:
                break
            if dx == 2 and dy == 1:
                return 2
        return 3

    # 0,1,2,3은 북, 동, 남, 서쪽
    def go_down(maps, x, y, d):
        ex, ey = x, y
        door = d
        direction = can_move(maps, ex, ey)
        while direction != 3:
            if direction == 0:
                ex = ex + 1
            elif direction == 1:
                ex = ex + 1
                ey = ey - 1
                door = (door - 1) % 4
            elif direction == 2:
                ex = ex + 1
                ey = ey + 1
                door = (door + 1) % 4
            direction = can_move(maps, ex, ey)
        clear_golem(maps, x, y)
        mark_golem(maps, ex, ey)
        if door == 0:
            maps[ex - 1][ey] = 2
        elif door == 1:
            maps[ex][ey + 1] = 2
        elif door == 2:
            maps[ex + 1][ey] = 2
        elif door == 3:
            maps[ex][ey - 1] = 2
        else:
            raise Exception("wrong direction")
        return maps, ex, ey

    def calculate_row(maps, x, y):
        visited = clear_map(C, R)
        result = x
        dq = deque()
        dq.append((x, y))
        while dq:
            ex, ey = dq.popleft()
            visited[ex][ey] = 1
            result = max(ex, result)
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                tmpx = ex + dx
                tmpy = ey + dy
                if not (0 <= tmpx < R + 3 and 0 <= tmpy < C):
                    break
                if visited[tmpx][tmpy] == 1:
                    continue
                if maps[ex][ey] == 1:
                    if maps[tmpx][tmpy] == 3:
                        dq.append((tmpx,tmpy))
                elif maps[ex][ey] == 2:
                    if maps[tmpx][tmpy] != 0:
                        dq.append((tmpx,tmpy))
                elif maps[ex][ey] == 3:
                    dq.append((tmpx,tmpy))

        return result - 2

    R, C, K = list(map(int, input().split()))
    maps = clear_map(C, R)
    sumi = 0
    for i in range(K):
        c, d = list(map(int, input().split()))
        c = c - 1  # n번째 열은 배열의 n-1번째
        maps, ex, ey = go_down(maps, 1, c, d)
        is_map_out = check_map_out(maps)
        if is_map_out:
            maps = clear_map(C, R)
            continue
        sumi += calculate_row(maps, ex, ey)
    print(sumi)


solve()