from collections import deque
A = input()
x = deque()
for a in A:
    x.append(a)
first = x.popleft()
count = 1
while x[-1] == first:
    x.pop()
    count+=1
while x[0] == first:
    x.popleft()
    count+=1
result = 0
if count >= 10:
    result+=3
else:
    result+=2

if len(x)>0:
    last = ''
    while len(x)!=0:
        node = x.pop()
        if last == node:
            pass
        else:
            last = node
            result+=2

print(result)