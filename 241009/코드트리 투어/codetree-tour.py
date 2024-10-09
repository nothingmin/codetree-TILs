q = int(input())

nodes = list(map(int, input().split()))
n, m = nodes[1], nodes[2]
graph = [[] for _ in range(n)]
costs = [[999 for _ in range(n)] for _ in range(n)]
for i in range(3, 3 + 3 * m, 3):
    u, v, w = nodes[i], nodes[i + 1], nodes[i + 2]
    if u == v:
        continue
    costs[u][v] = min(costs[u][v], w)
    costs[v][u] = min(costs[v][u], w)
for i in range(n):
    for j in range(n):
        if costs[i][j] != 999:
            graph[i].append([costs[i][j], j])
ids = {}
values = []
start = 0
from heapq import heappop, heappush


def calc_value(start, id, rev, dest):
    distances = [1e6] * n
    distances[start] = 0
    hq = []
    heappush(hq, [0, start])
    visited = [False]*n
    visited[start]= True

    while hq:
        dist, node = heappop(hq)
        if distances[node] < dist:
            continue
        for cost, nxt in graph[node]:
            if distances[nxt] > distances[node] + cost:
                distances[nxt] = distances[node] + cost
                heappush(hq, [distances[nxt], nxt])
    cost = distances[dest]
    if cost == 1e6:
        return [cost, id, dest]
    else:
        return [-rev+cost,id,dest]


for _ in range(q - 1):
    command = list(map(int, input().split()))
    if command[0] == 200:
        ids[command[1]] = command[1:]
        heappush(values, calc_value(start, command[1], command[2], command[3]))
    elif command[0] == 300:
        ids.pop(command[1],None)
    elif command[0] == 400:
        if len(values) == 0:
            print(-1)
            continue
        value, id, dest = heappop(values)
        while id not in ids.keys() and len(values) != 0:
            value, id, dest = heappop(values)
        if id not in ids.keys():
            print(-1)
        elif value >0 :
            print(-1)
            heappush(values, [value, id, dest])
        else:
            print(id)
            ids.pop(id,None)
    elif command[0] == 500:
        start = command[1]
        hq = []
        while values:
            value, id, dest = heappop(values)
            if id not in ids.keys():
                continue
            heappush(hq, calc_value(start, ids[id][0], ids[id][1], ids[id][2]))
        values = hq
    else:
        raise Error('wrong command')