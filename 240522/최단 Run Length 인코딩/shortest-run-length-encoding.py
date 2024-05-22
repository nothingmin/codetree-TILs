A = input()
first = A[0]
i= len(A)-1

while A[i] == first:
    i-=1
    if i == 0:
        break
j=1
while A[j] == first:
    j+=1
    if j == len(A)-1:
        break
result = 4
if i>j:
    comp = A[j]
    while i>j:
        j+=1
        if comp != A[j]:
            comp = A[j]
            result+=2
print(result)