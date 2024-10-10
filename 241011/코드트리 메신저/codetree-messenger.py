class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


class Heap:
    def __init__(self, nodes, auth):
        self.nodes = nodes
        self.auth = auth[:]
        self.alarm = [True] * (100000)


    def swap(self, a, b):
        al,ar,ap = self.nodes[a].left,self.nodes[a].right,self.nodes[a].parent
        bl,br,bp = self.nodes[b].left,self.nodes[b].right,self.nodes[b].parent
        self.nodes[a].parent = bp
        self.nodes[b].parent = ap
        if self.nodes[ap].left == a:
            self.nodes[ap].left = b
        else:
            self.nodes[ap].right = b
        if self.nodes[bp].left == b:
            self.nodes[bp].left = a
        else:
            self.nodes[bp].right = a


    def toggle_alarm(self, num):
        self.alarm[num] = not self.alarm[num]

    def set_auth(self, a, c):
        self.auth[a] = c

    def left(self, a):
        return self.nodes[a].left

    def right(self, a):
        return self.nodes[a].right

    def show(self, a):
        result = []
        self.recur(0,a,result)
        print(len(result)-1)

    def recur(self, depth, num, result):
        if self.alarm[num] is False:
            return
        if depth <= self.auth[num]:
            result.append(num)
        l = self.left(num)
        if l !=-1:
            self.recur(depth+1,l,result)
        r = self.right(num)
        if r !=-1:
            self.recur(depth+1,r,result)

n, q = list(map(int, input().split()))
first = list(map(int, input().split()))
parents = first[:n + 1]
parents[0] = 0
auth = first[n:]
auth[0] = 0
nodes = [Node() for _ in range(n + 1)]
nodes[0].parent = 0

for num, parent in enumerate(parents):
    if num == 0:
        continue
    nodes[num].parent = parent
    if nodes[parent].left == -1:
        nodes[parent].left = num
    else:
        nodes[parent].right = num

heap = Heap(nodes, auth)
for _ in range(q - 1):
    command = list(map(int, input().split()))
    if command[0] == 200:
        a = command[1]
        heap.toggle_alarm(a)
    elif command[0] == 300:
        heap.set_auth(command[1], command[2])
    elif command[0] == 400:
        heap.swap(command[1], command[2])
    elif command[0] == 500:
        heap.show(command[1])