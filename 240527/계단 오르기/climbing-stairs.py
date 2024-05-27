n = int(input())

count = 0

def recur(current):
    global count 
    if current> n:
        return
    if current == n:
        count+=1
        return
    recur(current+2)
    recur(current+3)

recur(0)
print(count)