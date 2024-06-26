n = int(input())
maps = []

for _ in range(n):
    maps.append(list(map(int,input().split())))

def explode(arr,x,y):
    num = arr[x][y]
    arr[x][y] = 0
    for direction in [[0,1],[1,0],[0,-1],[-1,0]]:
        dx, dy = direction
        for i in range(1,num):
            ex = i*dx
            ey = i*dy
            if not(0<=x+ex<n and 0<=y+ey<n):
                continue
            arr[x+ex][y+ey] = 0
    return arr

def fall(arr):
    for i in reversed(range(n)):
        for j in range(n):
            arr[i][j]
            tmp = i
            while tmp+1 <n:
                if arr[tmp+1][j] == 0:
                    arr[tmp+1][j]= arr[tmp][j]
                    arr[tmp][j] = 0
                    tmp+=1
                else:
                    break
    return arr


def count(arr):
    count = 0
    for i in range(n):
        for j in range(n):
            for direction in [[1,0],[0,1]]:
                dx ,dy =direction
                if arr[i][j] == 0:
                    continue
                if not(0<=i+dx<n and 0<=j+dy<n):
                    continue
                if arr[i][j] == arr[i+dx][j+dy]:
                    count+=1
    return count
result = 0
for i in range(n):
    for j in range(n):
        arr = [row[:] for row in maps]
        result = max(result,count(fall(explode(arr,i,j))))
print(result)