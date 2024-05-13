n,m = map(int, input().split())
maps =[]
for _ in range(n):
    maps.append(list(map(int,input().split())))

result = -1
sum_max = 0
def sum_range(k,i,l,j):
    sumi = 0
    for a in range(k,k+i):
        for b in range(l, l+j):
            if maps[a][b] < 0:
                return 0, -1
            sumi += maps[a][b]
    return sumi, i*j


for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(n):
            for l in range(m):
                if k+i > n or l+j >m:
                    continue
                sumi, maxi = sum_range(k,i,l,j)
                if sum_max < sumi:
                    sum_max = sumi
                    result = maxi 
print(result)