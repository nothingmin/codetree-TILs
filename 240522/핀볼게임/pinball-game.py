n = int(input())
maps = []

#동서남북
directions = [[0,1],[0,-1],[1,0],[-1,0]] 

for _ in range(n):
    maps.append(list(map(int,input().split())))

def shoot(x,y,direction_index):
    time = 0
    while 0<=x<n and 0<=y<n:
        time+=1
        if maps[x][y] == 1:
            if direction_index == 0:
                direction_index = 3
            elif direction_index == 1:
                direction_index = 2
            elif direction_index == 2:
                direction_index = 1
            else:
                direction_index = 0
        elif maps[x][y] == 2:
            if direction_index == 0:
                direction_index = 2
            elif direction_index == 1:
                direction_index = 3
            elif direction_index == 2:
                direction_index = 0
            else:
                direction_index = 1
        dx,dy = directions[direction_index]
        x = x + dx
        y = y + dy
    return time

result = 0
# #동
for i in range(n):
    result = max(result,shoot(i,0,0))
# #서
for i in range(n):
    result = max(result,shoot(i,n-1,1))
# #남
for i in range(n):
    result = max(result,shoot(0,i,2))
# #북
for i in range(n):
    result = max(result,shoot(n-1,i,3))
print(result+1)