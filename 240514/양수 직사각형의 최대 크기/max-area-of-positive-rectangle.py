n,m = map(int, input().split())
maps =[]
for _ in range(n):
    maps.append(list(map(int,input().split())))

result = -1
def sum_range(k,i,l,j):
    sumi = 0
    for a in range(k,k+i):
        for b in range(l, l+j):
            if maps[a][b] < 0:
                return -1

    return i*j


for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(n):
            for l in range(m):
                if k+i > n or l+j >m:
                    continue
                maxi  = sum_range(k,i,l,j)
                if result <= maxi:
                    result = maxi 
print(result)